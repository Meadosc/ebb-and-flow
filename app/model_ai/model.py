from dotenv import load_dotenv
load_dotenv()

import groq


class AIModel():
    @classmethod
    def get_summary(cls, book_title):
        client = groq.Client()
        prompt = f"Summarize {book_title} as a plot summary."
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role":"user", "content":prompt}],
            temperature=0.7,
        )

        return response.choices[0].message.content.strip()

