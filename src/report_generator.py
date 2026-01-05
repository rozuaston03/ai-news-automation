from datetime import datetime

class ReportGenerator:
    @staticmethod
    def generate_markdown(articles):
        date_str = datetime.now().strftime('%Y-%m-%d')
        report = f"# AI Daily News Report - {date_str}\n\n"
        report += "Prepared by Antigravity Production Agent.\n\n"
        report += "---\n\n"

        for article in articles:
            report += f"## {article['title']}\n"
            report += f"**Source:** {article['source']} | **Date:** {article['published']}\n\n"
            report += f"{article['summary']}\n\n"
            report += f"[Read more here]({article['link']})\n\n"
            report += "---\n\n"
            
        return report

    @staticmethod
    def generate_telegram_summary(articles):
        date_str = datetime.now().strftime('%Y-%m-%d')
        text = f"ðŸ¤– *AI Daily News Brief ({date_str})*\n\n"
        
        for article in articles[:5]: # Send top 5 for brevity
            text += f"â€¢ *{article['title']}*\n"
            text += f"[{article['source']}]({article['link']})\n\n"
            
        text += "Full report available in logs/repos."
        return text
