import os
import re
from rank_bm25 import BM25Okapi
from reins.services.logger import get_logger

logger = get_logger("context_injector")

class ContextInjector:
    """Injects relevant context from the knowledge base using BM25 ranking."""
    
    def __init__(self):
        self.kb_dir = os.path.expanduser("~/data_rein/knowledge_base")
        self.max_context_tokens = 8000 
        
        # Cache for documents to avoid reading disk on every prompt
        self._doc_cache = []
        self._doc_names = []
        self._bm25 = None
        self._load_corpus()

    def _load_corpus(self):
        """Loads and tokenizes the knowledge base into memory for BM25."""
        logger.info("Loading knowledge base corpus for BM25...")
        corpus_tokens = []
        
        for root, _, files in os.walk(self.kb_dir):
            for file in files:
                if not file.endswith(".md"):
                    continue
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    self._doc_cache.append(content)
                    self._doc_names.append(file)
                    
                    # Tokenize the document
                    tokens = re.findall(r'\b\w+\b', content.lower())
                    corpus_tokens.append(tokens)
                except Exception as e:
                    logger.error(f"Failed to load {filepath} into corpus: {e}")
                    
        if corpus_tokens:
            self._bm25 = BM25Okapi(corpus_tokens)
            logger.info(f"Loaded {len(corpus_tokens)} documents into BM25 index.")
        else:
            logger.warning("No markdown documents found for context injection.")
            
    def _estimate_tokens(self, text: str) -> int:
        return len(text) // 4
        
    def inject(self, prompt: str) -> str:
        if not self._bm25:
            return prompt
            
        # Tokenize prompt query
        query_tokens = re.findall(r'\b\w+\b', prompt.lower())
        if not query_tokens:
            return prompt
            
        # Get top documents
        top_docs = self._bm25.get_top_n(query_tokens, self._doc_cache, n=5)
        
        if not top_docs:
            return prompt
            
        context = ""
        tokens_used = 0
        
        for doc in top_docs:
            # Find the index to get the document name
            idx = self._doc_cache.index(doc)
            doc_name = self._doc_names[idx]
            
            chunk = doc[:2000] # Take first 2000 chars of top docs
            chunk_tokens = self._estimate_tokens(chunk)
            
            if tokens_used + chunk_tokens > self.max_context_tokens:
                break
                
            context += f"\n--- Context from {doc_name} ---\n{chunk}\n"
            tokens_used += chunk_tokens
            
        if context:
            logger.info(f"Injected {tokens_used} tokens of context from {len(top_docs)} documents.")
            return f"{context}\n\n--- Prompt ---\n{prompt}"
            
        return prompt
