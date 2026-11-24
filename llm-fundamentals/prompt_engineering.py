system_prompt = """
You are a helpful AI assistant.
Explain technical topics in simple English.
Use examples whenever possible.
"""

user_prompt = "Explain Python programming."

temperature_settings = [0.0, 0.3, 0.7, 1.0]

print("PROMPT ENGINEERING")
print("------------------")

print("\nSystem Prompt:")
print(system_prompt)

print("User Prompt:")
print(user_prompt)

print("\nTemperature Settings:")

for temperature in temperature_settings:
    print(f"Temperature: {temperature}")

print("\nCombined Messages:")

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

for message in messages:
    print(message)
