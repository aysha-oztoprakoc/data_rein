import os
import pathlib
import sys

# Ensure extraction_pipeline can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

try:
    from extraction_pipeline.extractors.text_extractors import PDFExtractor
except ImportError:
    print("[ERROR] Could not import PDFExtractor.")
    sys.exit(1)

def main():
    training_data_dir = pathlib.Path(os.path.expanduser("~/data_rein/training_data/text"))
    vault_dest_dir = pathlib.Path(os.path.expanduser("~/data_rein/data-oby/TrainingData"))
    
    vault_dest_dir.mkdir(parents=True, exist_ok=True)
    
    extractor = PDFExtractor()
    
    pdfs = list(training_data_dir.glob("*.pdf"))
    if not pdfs:
        print("No PDFs found in training_data/text/")
        return
        
    print(f"Starting extraction for {len(pdfs)} PDFs...")
    
    success_count = 0
    error_count = 0
    
    for pdf in pdfs:
        print(f"Extracting: {pdf.name}")
        try:
            result = extractor.extract(str(pdf), str(vault_dest_dir))
            if result.get("status") == "success":
                success_count += 1
            else:
                error_count += 1
                print(f"Failed to extract {pdf.name}: {result.get('error')}")
        except Exception as e:
            error_count += 1
            print(f"Exception extracting {pdf.name}: {e}")
            
    print(f"Extraction Pipeline Complete. Success: {success_count}, Errors: {error_count}")
    
    # Also update SHARED_CONTEXT.md to reflect this ingestion
    shared_context = pathlib.Path(os.path.expanduser("~/data_rein/knowledge_base/SHARED_CONTEXT.md"))
    if shared_context.exists():
        with open(shared_context, "a", encoding="utf-8") as f:
            f.write(f"\n\n## RAG Ingestion Update\n")
            f.write(f"- {success_count} academic PDFs extracted and appended to the Vault for RAG intelligence.\n")

if __name__ == "__main__":
    main()
