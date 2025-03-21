import random
"""""

__author__  = "Jesper Collste"
__version__ = "1.0"
__email__   = "Jesper.Collste@elev.ga.ntig.se"

"""

words = [ #Lista med ord, alla samma längd för att det ska bli rättvist
    "banana", "circle", "button", "action", "people", "guitar", "market", "singer", 
    "driven", "travel", "laptop", "teacher", "garden", "summer", "orange", "frozen", 
    "nighty", "bottle", "circle", "rescue", "flames", "clouds", "bright", "friend", 
    "winter", "steady", "puzzle", "remote", "gather", "crisis", "mighty"
]

def choose_random_word(word_list):
    return random.choice(word_list)

def display_word(word, guessed_letters): #Visar upp ordet som _ tills du gissar en bokstav så byts _ ut mot bokstaven ifall den var rätt
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def guess_letter(word, guessed_letters): #Funktion för att gissa en bokstav
    guess = input("Gissa på en bokstav: ").lower()
    if len(guess) != 1 or not guess.isalpha():
        print("Snälla skriv EN bokstav.")
        return False
    if guess in guessed_letters:
        print("Knäppjök, du har redan gissat den bokstaven, försök igen!")
        return False
    guessed_letters.add(guess)
    return guess in word

def guess_whole_word(word): #Funktion för att gissa hela ordet
    guess = input("Modigt! Gissa hela ordet: ").lower()
    return guess == word

def sort_by_attempts(player):
    return player[1]  #Returnerar antalet gissningar för sortering

def save_to_leaderboard(name, attempts):  
    leaderboard = []  

    #Läs in leaderboard-filen  
    try:  
        with open("leaderboard.txt", "r") as file:  
            for line in file:  
                parts = line.strip().split(": ")  
                if len(parts) == 2:  
                    player_name = parts[0]  
                    try:  
                        player_attempts = int(parts[1].split()[0])  
                        leaderboard.append((player_name, player_attempts))  
                    except ValueError:  
                        continue  #Hoppa över rader som inte följer formatet  

    except FileNotFoundError:  
        pass  #Om filen inte finns skapas den automatskt

   
    leaderboard.append((name, attempts))  #lägger till spelaren i leaderboarden.

   
    leaderboard.sort(key=sort_by_attempts)  #Sorterar listan baserat på antal gissningar

      
    with open("leaderboard.txt", "w") as file:   #Öppnar text filen med write permissions och skriver in spelaren
        for player_name, player_attempts in leaderboard:  
            file.write(f"{player_name}: {player_attempts} gissningar\n")  

    print("Ditt resultat har sparats och leaderboarden har uppdaterats!")  


def play_hangman():  #Huvudkod
    while True:  #Loop för att låta spelaren spela igen
        word = choose_random_word(words)
        guessed_letters = set()
        incorrect_guesses = 0
        max_attempts = 10
        total_guesses = 0

        print("\nHänga gubbe dags!")
        while incorrect_guesses < max_attempts:
            print("\n" + display_word(word, guessed_letters))
            print(f"Fel!: {incorrect_guesses}/{max_attempts}")

            choice = input("Skriv 1 för att gissa en bokstav eller tryck 2 för att gissa hela ordet: ")  # Ger spelaren valet att gissa en bokstav eller hela ordet
            if choice == '1':
                if not guess_letter(word, guessed_letters):
                    incorrect_guesses += 1
                total_guesses += 1
            elif choice == '2':
                if guess_whole_word(word):
                    print(f"Grattis! Du gissade rätt ord. Ordet var: {word}")
                    break
                else:
                    print("Fel!")
                    incorrect_guesses += 1
                total_guesses += 1
            else:
                print("Fel input, skriv 1 eller 2")

            if set(word) <= guessed_letters:
                print(f"Grattis! Du gissade rätt ord. Ordet var: {word}")
                break

        print(f"Du klarade det på {total_guesses} gissningar.")
        save_name = input("Vill du spara ditt resultat på leaderboarden? (ja/nej): ").lower()
        if save_name == "ja":
            name = input("Skriv ditt namn: ")
            save_to_leaderboard(name, total_guesses)
            print("Ditt resultat har sparats!")
        else:
            print("Resultatet sparades inte.")

        #Fråga om spelaren vill spela igen
        play_again = input("\nVill du spela igen? (ja/nej): ").lower()
        if play_again != "ja":
            print("Tack för att du spelade! Hejdå! 👋")
            break  #Avslutar loopen och spelet

play_hangman()  #Startar spelet
