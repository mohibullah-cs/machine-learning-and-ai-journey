def check_ai_response(response, verified_facts):
    response_lower = response.lower()

    print("AI RESPONSE CHECK")
    print("-----------------")
    print("Response:", response)

    found = False

    for fact in verified_facts:
        if fact.lower() in response_lower:
            print("\nVerified information found:", fact)
            found = True

    if not found:
        print("\nNo matching verified facts found.")

        print("Warning: This response needs fact-checking.")

# Example AI response
ai_response = "Python was created by Guido van Rossum."

# Example verified information
verified_facts = [
    "Python was created by Guido van Rossum."
]

check_ai_response(ai_response, verified_facts)
