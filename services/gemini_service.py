from dotenv import load_dotenv
import os
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

import time

def ask_gemini(prompt):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )

            return response.text

        except Exception as e:

            print(f"Attempt {attempt+1} failed")

            if attempt < 2:
                time.sleep(5)

            else:
                return f"Error: {str(e)}"

if __name__ == "__main__":

    answer = ask_gemini(
        "What is HPI in hemodynamic monitoring?"
    )

    print(answer)