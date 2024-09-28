import schedule
import time
import random

# List of motivational quotes
quotes = [
    "Believe you can and you're halfway there. - Theodore Roosevelt",
    "Your limitation—it's only your imagination.",
    "Push yourself, because no one else is going to do it for you.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Success doesn’t just find you. You have to go out and get it.",
    "The harder you work for something, the greater you’ll feel when you achieve it.",
    "Dream bigger. Do bigger.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "Wake up with determination. Go to bed with satisfaction."
]

def send_quote():
    quote = random.choice(quotes)
    print(f"Motivational Quote: {quote}")

# Schedule the job every 24 hours
schedule.every(24).hours.do(send_quote)

# Run the scheduler
if __name__ == "__main__":
    print("Starting the motivational quote generator...")
    send_quote()  # Send an initial quote immediately
    while True:
        schedule.run_pending()
        time.sleep(1)
