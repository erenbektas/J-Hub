def hang():

    def main():   #the function to turn back to main.py
        from BackHome import back
        back()

    def again():
        again = input("Would you like to try again? (y/n)")
        if again == "y":
            hang()
        else:
            main()

    import random
    from poorguy import poorguy


    source = open("words.txt", "r")
    wordtext = source.read()
    wordlist = wordtext.split("\n")

    rolldice = random.randint(0, len(wordlist) - 1)

    word = wordlist[rolldice]

    wordmap = list(enumerate(word))
        
    hint_list = []
    for i in range(len(word)):
        hint_list.append("_")

    win = "Congratulations! You saved that poor guy! You saved the poor guy :\')"
    fail = "Sorry, you failed. The word was: " + word

    def game():

        wrong_guess = []
        right_ones = []
        
        while True:

            hint = "         Hint: " + " ".join(hint_list) + " (The word has " + str(len(word)) + " letters.)"
            mistakes = "Wrong Guesses: " + ", ".join(wrong_guess)
            mistake_count = len(wrong_guess)
            print(poorguy[mistake_count].format(hint, mistakes))

            if mistake_count > 5:
                print(fail)
                again()

            letters = []
            count = 1
            for n in word:
                letters.append(n)

            debug = 0
            while debug:
                print(word)
                print(letters)
                break

            pos = []
            right_guess = []

            if len(right_ones) == len(letters):
                print(win)
                again()

            guess_raw = input("Please enter your guess: ")
            guess = guess_raw.lower()

            if len(guess) == 1:
                if guess in letters:
                    for n in wordmap:
                        if n[1] == guess:
                            pos.append(n[0])
                            right_guess.append(n[1])
                            right_ones.append(n[1])
                            for n in pos:
                                index = pos.index(n)
                                hint_list[n] = right_guess[index]        
                else:
                    wrong_guess.append(guess)
                    continue
            else:
                if guess == word:
                    print(win)
                    again()
                else:
                    wrong_guess.append(guess)
                    continue
    game()