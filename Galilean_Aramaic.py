import random

# Dictionary for English to Galilean Aramaic translation and transliteration
translations = {
    'hello': ('Shəlam(Shlam)', 'שְׁלָמָא'),
    'peace': ('Shəlam', 'שְׁלָמָא'),
    'city': ('Kərak/Karka', 'קְרַק'),
    'teacher': ('Rabbi', 'רַבִּי'),
    'lord': ('Marya/Moryo', 'מָרְיָא'),
    'god': ('Elaha/Alaha', 'אֱלָהָא'),
    'father': ('Abba', 'אַבָּא'),
    'mother': ('Imma', 'אִמָּא'),
    'brother': ('Akh', 'אָחָא'),
    'love': ('Rakhma', 'רַחְמָא'),
    'thank you': ('Yishar', 'תָּוְדִי'),
    'please': ('(b-Bau)', 'בָּקָשָׁא'),
    'good': ('Tab', 'טַב'),
    'bad': ('Bisha', 'בִּישָׁא'),
    'yes': ('Eyn', 'אֵין'),
    'no': ('Laa', 'לָא'),
    'man': ('Gabar/gobra/gabra', 'גַּבְרָא'),
    'woman': ('iṭṭa/etā', 'אִטָּא'),
    'child/son': ('ber/bar/bara', 'בַּר/בֵּר'),
    'child/daughter':('bəra, barta, berta', 'בֶּרְתָּא'),
    'king': ('Malka/Məlek', 'מַלְכָּא'),
    'queen': ('malktəṭā/malakuta', 'מַלְכְּתָּא'),
    'holy': ('qaddish/qaddisha', 'קָדִישָׁא'),
    'life': ('Hayye', 'חַיֵּי'),
    'death': ('Mota', 'מוּתָא'),
    'water': ('mayin/mayim/mayya', 'מַיָּא'),
    'bread': ('Pittā', 'פִּתָּא'),
    'world': ('Alma', 'עָלְמָא'),
    'light': ('Bəraq/Barqa', 'נוּהְרָא'),
    'darkness': ('ḥāšok/ḥăšokā', 'חָשׁוּךְ'),
    'heaven': ('Shəmayya', 'שְׁמַיָּא'),
    'jesus':('Yešuaᶜ/Yeshua', 'יֵשׁוּעַ'),
    'where are you from': ('Min ayka at?', 'מִן אֵיכָּא אַתְּ?'),
    'do you speak aramaic': ('Metaret am Aramit?', 'מְתַּרֵּת אַם אַרָמִית?'),
    'what are you up to': ('Mah at abeyd(M)/abdah(f)', '{עַבְדָּה}מָה אַת עַבֵּיד?'),
}

# Random responses for common phrases
random_responses = {
    "how are you": [
        "Mah lak? Ana tab. (How are you? I am good.)",
        "Ana tab! Yishar! (I'm good! Thank you!)",
        "Bisha la. Shalamlak! (Not bad. Peace to you!)"
    ],
    "hello": [
        "Shalam! (Hello!)",
        "Shalamlak/lek(f)! (Peace be upon you!)"
    ],
    "thank you": [
        "Yishar! (Thank you!)",
        "Tebu lak/lek saggin! (Many thanks!)",
        "Yishar, Elaha nibarekhlakh! (Thank you, God bless you!)"
    ],
    "yes": [
        "Eyn! (Yes!)",
        "Eyn, tab! (Yes, good!)"
    ],
    "no": [
        "Laa! (No!)",
        "Laa, lo yit! (No, not really!)"
    ],
    "do you speak aramaic": [
        "Eyn, metaret am Aramit! (Yes, I speak Aramaic!)",
        "Metaret am Aramit, bass la tab saggin! (I speak Aramaic, but not very well!)"
    ],
    "where are you from": [
        "Ana min Galil! (I am from Galilee!)",
        "Min ayka at? (Where are you from?)"
    ],
    "what are you up to": [
        "Mah at abeyd(M)/abdah(f) (What are you up to)"
    ]
}

def translate_to_aramaic():
    print("Enter an English word or phrase to translate to Galilean Aramaic (type 'exit' to quit):")
    while True:
        english_phrase = input("> ").strip().lower()  # Convert input to lowercase
        if english_phrase == "exit":
            print("Goodbye I hoped you enjoyed learning Galilean Aramaic😊!")
            break
        
        # Check if phrase exists in the dictionary
        if english_phrase in translations:
            aramaic_word, aramaic_script = translations[english_phrase]
            print(f"Aramaic: {aramaic_word} ({aramaic_script})")
        
        # If it's a common phrase, respond with a random answer + translation
        elif english_phrase in random_responses:
            response = random.choice(random_responses[english_phrase])
            print(f"{response}")
        
        else:
            print("Translation not found.")

if __name__ == "__main__":
    translate_to_aramaic()
