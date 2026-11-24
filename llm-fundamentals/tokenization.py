import re

def count_tokens(text):
    # Simple token approximation, not an actual LLM tokenizer
    tokens = re.findall(r"\w+|[^\w\s]", text)
    return tokens

text = "Large Language Models are changing the world of AI!"

tokens = count_tokens(text)

print("Original Text:")
print(text)

print("\nTokens:")
print(tokens)

print("\nTotal Token Count:", len(tokens))
