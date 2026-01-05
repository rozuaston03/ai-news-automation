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
        Analyze the following AI news article. 
        1. Summarize it in exactly 3 concise bullet points.
        2. Assign a 'Relevance Score' from 1-10 (10 being most impactful).
        
        Title: {title}
        Content: {content}
        
        Output format:
        Summary:
        - [Point 1]
        - [Point 2]
        - [Point 3]
        Relevance Score: [X]/10
        """
        
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a senior AI research analyst. You specialize in identifying high-impact innovation."
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
            response = completion.choices[0].message.content.strip()
            
            # Simple extraction of score
            score = 5
            if "Relevance Score:" in response:
                try:
                    score_str = response.split("Relevance Score:")[1].split("/")[0].strip()
                    score = int(score_str)
                except:
                    pass
            
            return response, score
        except Exception as e:
            logger.error(f"Groq API Error: {e}")
            return f"Summarization failed: {e}", 0
