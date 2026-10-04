import datetime

# Sentiment keyword lists
POSITIVE_WORDS = [
    "good", "great", "awesome", "fantastic", "happy", "love",
    "excellent", "nice", "wonderful", "amazing", "cool"
]

NEGATIVE_WORDS = [
    "bad", "terrible", "awful", "sad", "hate", "horrible",
    "disappointing", "worst", "angry", "upset"
]

# Data storage
conversation_history = []  # list of dicts: {"text": ..., "sentiment": ...}
sentiment_counts = {"positive": 0, "negative": 0, "neutral": 0}


def analyze_sentiment(text):
    """Return 'positive', 'negative', or 'neutral' based on simple keyword matching."""
    lower_text = text.lower()
    score = 0

    for word in POSITIVE_WORDS:
        if word in lower_text:
            score += 1

    for word in NEGATIVE_WORDS:
        if word in lower_text:
            score -= 1

    if score > 0:
        return "positive"
    elif score < 0:
        return "negative"
    else:
        return "neutral"


def record_message(text, sentiment):
    """Store message and update counts."""
    conversation_history.append({"text": text, "sentiment": sentiment})
    sentiment_counts[sentiment] += 1


def show_stats():
    """Print sentiment statistics."""
    total = len(conversation_history)
    print("\n--- Sentiment Statistics ---")
    print(f"Total messages: {total}")
    print(f"Positive: {sentiment_counts['positive']}")
    print(f"Negative: {sentiment_counts['negative']}")
    print(f"Neutral:  {sentiment_counts['neutral']}")
    print("----------------------------\n")


def show_history():
    """Print conversation history."""
    if not conversation_history:
        print("\nNo conversation history yet.\n")
        return

    print("\n--- Conversation History ---")
    for i, entry in enumerate(conversation_history, start=1):
        print(f"{i}. [{entry['sentiment'].upper()}] {entry['text']}")
    print("----------------------------\n")


def reset_data():
    """Clear history and reset counts."""
    conversation_history.clear()
    sentiment_counts["positive"] = 0
    sentiment_counts["negative"] = 0
    sentiment_counts["neutral"] = 0
    print("\nAll data has been reset.\n")


def final_report():
    """Generate and print a final sentiment report."""
    total = len(conversation_history)
    print("\n===== FINAL SENTIMENT REPORT =====")
    print(f"Generated at: {datetime.datetime.now()}")
    print(f"Total messages: {total}")
    print(f"Positive messages: {sentiment_counts['positive']}")
    print(f"Negative messages: {sentiment_counts['negative']}")
    print(f"Neutral messages:  {sentiment_counts['neutral']}")

    if total > 0:
        # Simple overall mood
        if sentiment_counts["positive"] > sentiment_counts["negative"]:
            overall = "Overall mood: POSITIVE"
        elif sentiment_counts["negative"] > sentiment_counts["positive"]:
            overall = "Overall mood: NEGATIVE"
        else:
            overall = "Overall mood: NEUTRAL / MIXED"
        print(overall)
    else:
        print("No messages were analyzed.")

    print("==================================\n")


def print_help():
    """Show available commands."""
    print("\nCommands:")
    print("  /stats   - show sentiment statistics")
    print("  /history - show conversation history")
    print("  /reset   - reset all data")
    print("  /help    - show this help message")
    print("  /exit    - exit and show final report\n")


def main():
    print("Welcome to Sentiment Spy!")
    print("Type a message and I will analyze its sentiment.")
    print("Use commands like /stats, /history, /reset, /help, /exit.\n")

    while True:
        user_input = input("You: ").strip()

        if not user_input:
            continue

        # Handle commands
        if user_input.startswith("/"):
            if user_input == "/stats":
                show_stats()
            elif user_input == "/history":
                show_history()
            elif user_input == "/reset":
                reset_data()
            elif user_input == "/help":
                print_help()
            elif user_input == "/exit":
                final_report()
                print("Goodbye, agent!")
                break
            else:
                print("Unknown command. Type /help for options.\n")
            continue

        # Normal message: analyze sentiment
        sentiment = analyze_sentiment(user_input)
        record_message(user_input, sentiment)

        print(f"Sentiment Spy: That sounds {sentiment}.\n")


if __name__ == "__main__":
    main()