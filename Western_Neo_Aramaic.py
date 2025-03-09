import random

# Dictionary with English to Aramaic translations
english_to_aramaic = {
    "sun": "5im5a",
    "village": "Blöta",
    "mother": "emma/imma",
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
    "brother": "Höna",
    "son": "EBRA",
    "greeting": "Shloma/Slöma",
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
    "alot": "bahar",
    "how old are you": "Kam shne it lakh?",
    "I love you": "Rakhimna lakh"
}

# Random responses for common phrases
# I also had to use common letters to not disturb the loop
random_responses = {
    "how are you/Ex ḉub(m)/ḉiba(f)": [
        "Ana nkayyes(m)/nkayyeesa, tudi/todi. (I'm fine, thank you!)",
        "Ana nkayyes/nkayyeesa W enta/k? (I'm good! How about you?)",
        "Ana nkayyes/nkayyeesa! tudi/todi! (I'm well! Thanks!)"
    ],
    "hello": [
        "Shloma/Slöma! (Hello!)",
        "Shloma/Slöma!, Ex ḉub(m)/ḉiba(f) (Hello! How are you?)",
        "Shloma/Slöma u safra brixa/ibrix 'sofrax(m)/ibrix 'sofriš(f)! (Hello and good morning!)"
    ],
    "good morning": [
        "Safra brixa/ibrix 'sofrax(m)/'sofriš(f)! (Good morning!)",
        "Safra brixa/ibrix 'sofrax(m)/'sofriš(f), ex ḉub? (Good morning! How are you?)"
    ],
    "good night": [
        "Leyla ibrex! (Good night!)",
        "Leyla ibrex, Slöma/shloma loxun! (Good night, peace be with you!)"
    ],
    "thank you": [
        "tudi/todi! (Thank you!)",
        "tudi/todi saggi! (Many thanks!)",
        "tudi/todi, Aloha mberakhlakh! (Thank you, God bless you!)"
    ],
    "yes": [
        "Eyn! (Yes!)",
        "Eyn, tabʕan! (Yes, of course!)"
    ],
    "no": [
        "Laa! (No!)",
        "Laa, bahar! (No, not really!)"
    ],
    "do you speak aramaic/ḉyoda' aromai": [
        "Eyn, ana bḥakki Arāmōy/aromai!(Yes, I speak Aramaic!)",
        "Ana bḥakki arāmōy/aromai, bass lā ktīr mnaḥ! (I speak Aramaic, but not very well!)"
    ],
    "what is your name/ Mo ušmax/ušmiš": [
        "Mo usmax/usmis (What is your name?)",
        "Shmi/Usmi [your name]! (My name is [your name]!)"
    ],
    "where are you from/Minna Haḉ/Haš": [
        "Ana mn Blöta. (I am from the village.)",
        "Ana mn Almänya. (I am from Germany.)",
        "Minna Haḉ (Where are you from?)"
    ],
    "i don't understand": [
        "La masmak. (I don't understand.)",
        "La masmak, mitbayel bashmey? (I don’t understand, can you repeat?)"
    ],
    "how old are you": [
        "Kaṁ šne ʕandak/ʕandek? (How old are you?)",
        "Ana ʕandi [age] šne. (I am [age] years old.)"
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
