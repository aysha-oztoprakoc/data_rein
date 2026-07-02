class FormatAdapter:
    """Adapts prompt formatting for specific models (e.g. ChatML, Alpaca)."""
    
    def __init__(self):
        # We assume local models use Ollama which handles chat templates automatically
        # for API calls, but we might want to structure the system prompt based on the task.
        pass
        
    def adapt(self, prompt: str, task_type: str = "general") -> str:
        system_prompts = {
            "coding": "You are an expert software engineer. Provide only valid, well-documented code.",
            "analysis": "You are a meticulous data analyst. Break down your reasoning step-by-step.",
            "creative": "You are a creative writer. Use evocative language and maintain a consistent tone.",
            "general": "You are a helpful AI assistant."
        }
        
        sys_prompt = system_prompts.get(task_type, system_prompts["general"])
        
        # We output a structured format that the orchestrator or local Ollama client can parse
        # Since we use ollama CLI in the main orchestrator, we can prepend the system prompt.
        return f"System: {sys_prompt}\n\nUser: {prompt}"
