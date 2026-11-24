CONTEXT_WINDOW = 4096

conversation = [
    "Hello, how are you?",
    "Explain machine learning.",
    "What is deep learning?",
    "Give me a Python example."
]

def estimate_tokens(text):
    return len(text.split())

used_tokens = sum(
    estimate_tokens(message) for message in conversation
)

remaining_tokens = CONTEXT_WINDOW - used_tokens

print("LLM Context Window")
print("------------------")

print("Maximum Tokens:", CONTEXT_WINDOW)
print("Used Tokens:", used_tokens)
print("Remaining Tokens:", remaining_tokens)

if remaining_tokens > 0:
    print("\nThere is still space in the context window.")
else:
    print("\nContext window limit reached!")
