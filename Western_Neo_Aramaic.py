import random

# Dictionary with English to Aramaic translations
english_to_aramaic = {
    "sun": "5im5a",
    "village": "Blöta",
    "mother": "emma",
    "father": "abba",
    "god": "Aloha",
    "bone": "Germa",
    "wall": "xotla",
    "rice": "ruzya",
    "path": "Tarba",
    "foot": "Regra",
    "boy": "Psöna",
    "boy (plural)": "bisinö",
    "honey": "deb5a",
    "hello": "Shloma/Slöma",
    "peace": "Shloma/Slöma",
    "good morning": "Safra brixa",
    "good night": "Laila brixa",
    "how are you": "Ek it?",
    "I am fine": "Ana brixa",
    "thank you": "Tawdi",
    "please": "Baqasha",
    "yes": "Eyn",
    "no": "Laa",
    "sleep": "idmex",
    "take": "i5kal",
    "pass": "Imrek",
    "come": "töle",
    "sit": "k'öle",
    "man": "gabröna",
    "name": "e5ma",
    "hand": "ida",
    "write": "xöteb",
    "high": "Calya",
    "big": "rabb",
    "go": "allex",
    "open": "iftali",
    "friend": "RFI&A",
    "right": "a iöles",
    "why": "Caya",
    "two": "it ar",
    "stone": "Xéfa",
    "day": "yöma",
    "house": "payta",
    "brother": "Köna",
    "son": "EBRA",
    "greeting": "Slöma",
    "good": "Atyab",
    "better": "awrab",
    "bad": "xöla",
    "life": "hyy",
    "to die": "amet",
    "bring": "ay!",
    "stand up": "a&am",
    "eat": "xöla",
    "work": "éapp-",
    "war": "barba",
    "land": "ara",
    "bread": "lahma",
    "water": "Möya",
    "money": "kaspa",
    "market": "souqa",
    "morning": "safra",
    "night": "laila",
    "king": "malka",
    "queen": "malkta",
    "do you speak aramaic": "Titray Aramit?",
    "what is your name": "Shmakh man?",
    "where are you from": "Mnin it?",
    "I don't understand": "La masmak",
    "how old are you": "Kam shne it lakh?",
    "I love you": "Rakhimna lakh"
}

# Random responses for common phrases
# I also had to use common letters to not disturb the loop
random_responses = {
    "how are you": [
        "Ek it? Ana brixa. (I'm fine, thank you!)",
        "Ana brixa! Ek it lakh? (I'm good! How about you?)",
        "Brixa! Tawdi! (I'm well! Thanks!)"
    ],
    "hello": [
        "Slöma! (Hello!)",
        "Slöma! Ek it? (Hello! How are you?)",
        "Slöma u safra brixa! (Hello and good morning!)"
    ],
    "good morning": [
        "Safra brixa! (Good morning!)",
        "Safra brixa, Ek it? (Good morning! How are you?)"
    ],
    "good night": [
        "Laila brixa! (Good night!)",
        "Laila brixa, Slöma/shloma! (Good night, peace be with you!)"
    ],
    "thank you": [
        "Tawdi! (Thank you!)",
        "Tawdi saggi! (Many thanks!)",
        "Tawdi, Aloha mberakh! (Thank you, God bless you!)"
    ],
    "yes": [
        "Eyn! (Yes!)",
        "Eyn, besey! (Yes, of course!)"
    ],
    "no": [
        "Laa! (No!)",
        "Laa, lo yit! (No, not really!)"
    ],
    "do you speak aramaic": [
        "Eyn, titray Aramit! (Yes, I speak Aramaic!)",
        "Titray Aramit, bass la mitmar basim! (I speak Aramaic, but not very well!)"
    ],
    "what is your name": [
        "Shmakh man? (What is your name?)",
        "Shmi/Usmi [your name]! (My name is [your name]!)"
    ],
    "where are you from": [
        "Ana mn Blöta. (I am from the village.)",
        "Ana mn Almänya. (I am from Germany.)",
        "Mnin it? (Where are you from?)"
    ],
    "i don't understand": [
        "La masmak. (I don't understand.)",
        "La masmak, mitbayel bashmey? (I don’t understand, can you repeat?)"
    ],
    "how old are you": [
        "Kam shne it lakh? (How old are you?)",
        "Ana [age] shne. (I am [age] years old.)"
    ],
    "i love you": [
        "Rakhimna lakh! (I love you!)",
        "Ana rakhim lakh! (I love you!)"
    ]
}

def translate_to_aramaic():
    print("Enter an English phrase to translate to Aramaic (type 'exit' to quit):")
    while True:
        english_phrase = input("> ").strip().lower()
        if english_phrase == "exit":
            print("Goodbye I hope you had fun learning aramaic😊!")
            break
        
        # Check if phrase exists in the dictionary
        aramaic_translation = english_to_aramaic.get(english_phrase, None)
        
        # If it's a common phrase, respond with a random answer + translation
        if english_phrase in random_responses:
            response = random.choice(random_responses[english_phrase])
            print(f"{response}")
        elif aramaic_translation:
            print(f"Aramaic: {aramaic_translation}")
        else:
            print("Translation not found.")

if __name__ == "__main__":
    translate_to_aramaic()
