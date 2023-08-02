import random

def get_random_quote():
    quotes = [
        "The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela",
        "The way to get started is to quit talking and begin doing. - Walt Disney",
        "Life is what happens when you're busy making other plans. - John Lennon",
        "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt",
        "Tell me and I forget. Teach me and I remember. Involve me and I learn. - Benjamin Franklin",
        "The only limit to our realization of tomorrow will be our doubts of today. - Franklin D. Roosevelt",
        "It is during our darkest moments that we must focus to see the light. - Aristotle",
        "Life is a succession of lessons which must be lived to be understood. - Helen Keller",
        "You will face many defeats in life, but never let yourself be defeated. - Maya Angelou",
        "The only way to do great work is to love what you do. - Steve Jobs"
    ]
    return random.choice(quotes)

if __name__ == "__main__":
    print(get_random_quote())