import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Use the lighter model to reduce quota hits
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

class GPTHandler:
    @staticmethod
    def parse_task(user_input):
        prompt = f"""
        Convert the following task description into JSON with:
        - title
        - due_date (if any)
        - priority (low/medium/high)
        - steps (2-4 steps)

        Task: {user_input}
        """
        try:
            response = model.generate_content([prompt])
            return json.loads(response.text)
        except Exception as e:
            print("⚠️ GPT Error during task parsing:", e)
            # Fallback structure to keep your app running
            return {
                "title": user_input,
                "priority": "medium",
                "due_date": "N/A",
                "steps": []
            }

    @staticmethod
    def get_motivation():
        prompt = "Give a short motivational message for someone who just completed a task."
        try:
            response = model.generate_content([prompt])
            return response.text.strip()
        except Exception as e:
            print("⚠️ GPT Error during motivation generation:", e)
            return "You did it! Keep crushing your goals. 💪"
