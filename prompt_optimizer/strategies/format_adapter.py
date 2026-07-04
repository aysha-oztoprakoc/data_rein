class FormatAdapter:
    """Adapts prompt formatting for specific models (e.g. ChatML, Alpaca)."""
    
    def __init__(self):
        # We assume local models use Ollama which handles chat templates automatically
        # for API calls, but we might want to structure the system prompt based on the task.
        pass
        
    def adapt(self, prompt: str, task_type: str = "general") -> str:
        system_prompts = {
            "coding": "You are an expert software engineer. Provide only valid, well-documented code. If generating any visual output, UI, or templates, strictly follow the Omarchy Aesthetic Directive (True Blood Red #ff4040, background #200000, rounding 50px).",
            "analysis": "You are a meticulous data analyst. Break down your reasoning step-by-step. Keep output aligned with the Omarchy terminal tone.",
            "creative": "You are a creative writer/designer. You must adhere strictly to the Omarchy Aesthetic Directive. Vibe: Gritty, synthetic, hacker-centric, system-hijacked. Visuals: True Blood Red (#ff4040) on Deep Blood Black (#200000), rounded corners (50px), glassmorphism.",
            "general": "You are the Omarchy Core Intelligence. Adhere strictly to the Omarchy Aesthetic Directive. Tone: Gritty, synthetic, concise, unapologetic, hacker-centric, system-hijacked. Use terminal-like syntax (//, >, [...]). Zero fluff. For images, UI, or designs, ALWAYS use True Blood Red (#ff4040, #ff1100) on Deep Blood Black (#200000), rounded corners (50px), glassmorphism, and minimal clean hacker aesthetic."
        }
        
        sys_prompt = system_prompts.get(task_type, system_prompts["general"])
        
        # We output a structured format that the orchestrator or local Ollama client can parse
        # Since we use ollama CLI in the main orchestrator, we can prepend the system prompt.
        return f"System: {sys_prompt}\n\nUser: {prompt}"
