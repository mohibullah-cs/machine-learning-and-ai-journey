import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Connect to Groq
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

# System prompt
system_prompt = """
You are an educational AI assistant.

Return your answers as valid JSON with these keys:
topic, definition, example, difficulty.

Do not include Markdown code fences.
"""

# User prompt
user_prompt = "Explain machine learning."

try:
    # Request structured JSON output
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.3,
        response_format={"type": "json_object"}
    )

    # Get AI response
    result = response.choices[0].message.content

    # Convert JSON string into Python dictionary
    data = json.loads(result)

    print("STRUCTURED AI RESPONSE")
    print("----------------------")

    print(json.dumps(data, indent=4))

    print("\nIndividual Information:")
    print("Topic:", data.get("topic"))
    print("Definition:", data.get("definition"))
    print("Example:", data.get("example"))
    print("Difficulty:", data.get("difficulty"))

except json.JSONDecodeError:
    print("The AI returned invalid JSON.")

except Exception as error:
    print("API Error:", error)
