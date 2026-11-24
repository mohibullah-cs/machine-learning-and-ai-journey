import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in .env file")

# Connect to Groq API
client = OpenAI(
    api_key=api_key,
    base_url="https://api.groq.com/openai/v1"
)

# Model configuration
MODEL = os.getenv("GROQ_MODEL", "openai/gpt-oss-20b")

# System prompt
system_prompt = """
You are a helpful AI assistant.
Explain technical topics in simple English.
Give practical examples whenever possible.
"""

# User prompt
user_prompt = input("Ask MOBA AI something: ")

try:
    # Send request to AI
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.7
    )

    # Display response
    ai_response = response.choices[0].message.content

    print("\nMOBA AI Response:")
    print(ai_response)

except Exception as error:
    print("\nAPI Error:", error)
