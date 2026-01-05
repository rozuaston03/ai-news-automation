import logging
from groq import Groq
from src.config import Config

logger = logging.getLogger(__name__)

class Summarizer:
    def __init__(self):
        if not Config.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY not set in environment.")
        self.client = Groq(api_key=Config.GROQ_API_KEY)
        self.model = Config.GROQ_MODEL

    def summarize(self, title, content):
        prompt = f"""
        Summarize the following AI news article in 3 concise bullet points.
        Focus on the innovation, the motivation, and the real-world impact.
        
        Title: {title}
        Content: {content}
        
        Summary:
        """
        
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior AI research analyst. Provide high-density, professional summaries."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=Config.TEMPERATURE,
                max_tokens=Config.MAX_TOKENS,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            logger.error(f"Groq API Error: {e}")
            return f"Summarization failed: {e}"
