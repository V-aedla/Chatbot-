"""
Traditional Student Support Chatbot
A rule-based chatbot using keyword matching and predefined responses.
No LLM, external API, or machine-learning model is used.
"""

import re


BOT_NAME = "CampusHelper"


RESPONSES = {
    "greeting": "Hello! I'm CampusHelper, a simple student-support chatbot. How can I help?",
    "hours": "The student support office is open Monday to Friday, 9:00 a.m. to 5:00 p.m. Confirm current hours with your institution.",
    "registration": "For course registration, sign in to your student portal, review available courses, and contact the registrar if you see a hold.",
    "library": "For library help, check the library catalogue, borrowing rules, and research databases through your institution's library website.",
    "fees": "For tuition or fee questions, review your student account statement and contact the finance office about balances or payment plans.",
    "study": "Try breaking your work into short sessions, setting a specific goal, and reviewing notes using practice questions.",
    "thanks": "You're welcome! Let me know if you have another question.",
    "goodbye": "Goodbye! Good luck with your studies."
}


KEYWORDS = {
    "greeting": {"hello", "hi", "hey", "good morning", "good afternoon"},
    "hours": {"hours", "open", "opening", "office time", "working hours"},
    "registration": {"register", "registration", "course", "enroll", "enrol", "classes"},
    "library": {"library", "book", "books", "research", "catalogue", "catalog"},
    "fees": {"fee", "fees", "tuition", "payment", "balance", "invoice"},
    "study": {"study", "studying", "exam", "revision", "assignment", "learning"},
    "thanks": {"thanks", "thank you", "thank"},
    "goodbye": {"bye", "goodbye", "exit", "quit"}
}



CAPABILITIES = [
    "greetings and farewells",
    "basic office-hours information",
    "course registration guidance",
    "library and research guidance",
    "tuition and fee guidance",
    "basic study tips"
]


def normalize(text):
    """Lowercase input and remove punctuation while preserving spaces."""
    return re.sub(r"[^a-z0-9\s]", " ", text.lower()).strip()

def get_response(user_text):
    """Return a predefined response based on the first matching keyword category."""
    cleaned = normalize(user_text)
    if not cleaned:
        return "I didn't receive a question. Please type a few words, such as 'registration' or 'library'."

    if cleaned in {"help", "what can you do", "capabilities", "menu"}:
        return "I can help with: " + "; ".join(CAPABILITIES) + "."

    # Match whole words/phrases to reduce accidental partial matches.
    for category, terms in KEYWORDS.items():
        for term in sorted(terms, key=len, reverse=True):
            if re.search(r"\b" + re.escape(term) + r"\b", cleaned):
                return RESPONSES[category]

    return ("I'm not sure how to answer that. Try asking about registration, "
           "library, fees, office hours, or study tips, or type 'help'.")


def main():
    print(f"{BOT_NAME}: Hello! Type 'help' to see what I can do, or 'quit' to end.")
    while True:
        try:
            user_text = input("You: ")
        except (EOFError, KeyboardInterrupt):
            print(f"\n{BOT_NAME}: Session ended. Goodbye!")
            break
        response = get_response(user_text)
        print(f"{BOT_NAME}: {response}")
        if normalize(user_text) in {"bye", "goodbye", "exit", "quit"}:
            break


if __name__ == "__main__":
    main()
