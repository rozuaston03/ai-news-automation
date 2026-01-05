import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

class Summarizer:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables.")
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.3-70b-versatile"

    def summarize(self, title, content):
        prompt = f"""
        Summarize the following AI news article in 2-3 concise bullet points.
        Focus on the "why it matters" and the core innovation/news.
        
        Title: {title}
        Content: {content}
        
        Summary:
        """
        
        try:
            completion = self.client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "You are a professional AI news curator. Provide concise, impactful summaries."
                    },
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=self.model,
                temperature=0.5,
                max_tokens=256,
            )
            return completion.choices[0].message.content.strip()
        except Exception as e:
            return f"Error during summarization: {e}"

if __name__ == "__main__":
    summarizer = Summarizer()
    print(summarizer.summarize("Test Article", "OpenAI has released a new model that can reason about complex math problems using a chain-of-thought process similar to human experts."))
