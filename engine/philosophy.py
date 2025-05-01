import random

# Filosofi dan kutipan untuk pilihan tertentu
def get_philosophical_quote(choice_type):
    quotes = {
        'good': [
            "“The good you do today may be forgotten tomorrow, but the kindness you showed will never be.” – Unknown",
            "“The right thing is not always the popular thing, but it's always the most rewarding.” – Unknown"
        ],
        'bad': [
            "“He who commits injustice is ever made more wretched than he who suffers it.” – Plato",
            "“It is not enough to be good; one must also act well.” – Aristotle"
        ]
    }
    return random.choice(quotes.get(choice_type, []))
