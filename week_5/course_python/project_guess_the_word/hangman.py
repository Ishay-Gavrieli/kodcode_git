import random

GAME_WORDS = ["apple", "orange", "banana"]

def show_menu(secret_word: list, count_attempts: int):
    print("wellcome to a guess game")
    print("you need to enter a letter that appear in the word or guess the word")
    print(f"the lenght of the word is {len(secret_word)}")
    print(f"you have {count_attempts} times to try")

def get_status(attempts: int, chosed: list, hidden_word: list):
    print(f"you have {attempts} times to try")
    
    print("the letters that you already chosed: ", end="")
    for i in range(len(chosed)):
        if i == len(chosed) - 1:
            print(chosed[i])
        else:
            print(chosed[i], end=", ")
            
    print("hidden word: ", end="")
    for letter in hidden_word:
        print(letter, end=" ")
    print()

def get_word() -> list[str]:
    word = random.choice(GAME_WORDS)
    return list(word)

def get_valid_guess(already_guess: list):
    while True:
        user_guess = input("please enter your guess:").lower()
        if user_guess.isalpha() and len(user_guess) == 1:
            if user_guess in already_guess:
                print("You already guessed that letter.")
                continue
            return user_guess
        print("you can only type one letter please try again")
        continue

def update_hidden_word(user_guess, secret_word, hidden_word):
    found = False
    for i, v in enumerate(secret_word):
        if v == user_guess:
            hidden_word[i] = user_guess
            found = True
    return found

def main():
    count_attempts = 10
    secret_word = get_word()
    hidden_word = ["_"] * len(secret_word)
    already_guess = []
    
    show_menu(secret_word, count_attempts)
    
    while count_attempts > 0 and "_" in hidden_word:
        user_guess = get_valid_guess(already_guess)
        already_guess.append(user_guess)
        if update_hidden_word(user_guess, secret_word, hidden_word):
            print("good guess")
        else:
            print("wrong guess try again")
            count_attempts -= 1
            
        get_status(count_attempts, already_guess, hidden_word)
        
    if "_" not in hidden_word:
        print("congradulations you won")
    else:
        print("your attempts are over")
        print("The word was: ", end="")
        for letter in secret_word:
            print(letter, end="")
        print()

if __name__ == "__main__":
    main()
