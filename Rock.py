def rockps():

    def main():   #the function to turn back to main.py
        from BackHome import back
        back()

    import random

    intro = "\nWelcome challenger!\nDo you think you can win against a computer on a rock paper scissors game?\nLet's find out! But first, please let me give you an introduction.\nEach round, you will enter your selection between \"rock\", \"paper\" and \"scissors\". Or you can just enter their initials!\nRight after you press the \"enter\" key, computer will also show its hand and the winner will get 1 point.\nThe one who gets 3 points wins.\nNOTE: You can go back to main menu by entering \"main/exit/home\"!\n"

    print(intro)    

    name = input("What\'s your name?: ")
    namelen = len(name)
    doubleline_counter = "═" * int(namelen)
    line_counter = "─" * int(namelen)

    exit = "main", "exit", "home", "back"

    score = """
    ╔═══{}══════════════════════╗
    ║ ╓─{}─────┬──────────────╖ ║
    ╟─╢ {} | {} │ {} | Computer ╟─╢
    ║ ╙─{}─────┴──────────────╜ ║
    ╚═══{}══════════════════════╝"""

    # Rock wins against scissors
    # Scissors win against paper
    # Paper wins against rock
    
    
    def game():

        def again():
            again = input("Would you like to try again? (y/n)")
            if again == "y":
                game()
            else:
                main()

        player_score = 0
        computer_score = 0
        while True:

            comp_index = random.randint(0, 2)
            bag = "Rock", "Paper", "Scissors"
            
            # 0 - Rock
            # 1 - Paper
            # 2 - Scissors

            rock = "rock", "r", "ro", "roc", "rck"
            paper = "paper", "p", "pap", "papr", "pper"
            sci = "scissors", "s", "scis", "scissor", "scisor", "scisors", "sci"

            if max(computer_score, player_score) < 3:

                user_hand = input("Please enter your choice between \"rock\", \"paper\" and \"scissors\": ").lower()

                if user_hand in exit:
                    main()
                else:

                    if comp_index == 0:     # ROCK

                        print("======================================")
                        print("The computer shows", bag[comp_index],)
                        if user_hand in rock:
                            print("Your choice was \"Rock.\"")
                            print("Draw! No point.")
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in paper:
                            print("Your choice was \"Paper.\"")
                            print("Congrats! You got 1 point.")
                            player_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in sci:
                            print("Your choice was \"Scissors.\"")
                            print("You were unlucky. Computer gets 1 point!")
                            computer_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue

                        else:
                            print("Your input is not recognized. Please choice between \"rock\", \"paper\" and \"scissors\", you can also enter the initial.")


                    elif comp_index == 1:     # PAPER

                        print("======================================")
                        print("The computer shows", bag[comp_index],)
                        if user_hand in rock:
                            print("Your choice was \"Rock.\"")
                            print("You were unlucky. Computer gets 1 point!")
                            computer_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in paper:
                            print("Your choice was \"Paper.\"")
                            print("Draw! No point.")
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in sci:
                            print("Your choice was \"Scissors.\"")
                            print("Congrats! You got 1 point.")
                            player_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue

                        else:
                            print("Your input is not recognized. Please choice between \"rock\", \"paper\" and \"scissors\", you can also enter the initial.")


                    else:     # SCISSORS    

                        print("======================================")
                        print("The computer shows", bag[comp_index],)
                        if user_hand in rock:
                            print("Your choice was \"Rock.\"")
                            print("Congrats! You got 1 point.")
                            player_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in paper:
                            print("Your choice was \"Paper.\"")
                            print("You were unlucky. Computer gets 1 point!")
                            computer_score += 1
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue
                        elif user_hand in sci:
                            print("Your choice was \"Scissors.\"")
                            print("Draw! No point.")
                            print(score.format(doubleline_counter, line_counter, name, player_score, computer_score, line_counter, doubleline_counter))
                            continue

                        else:
                            print("Your input is not recognized. Please choice between \"rock\", \"paper\" and \"scissors\", you can also enter the initial.")
                
            else:
                if computer_score == 3:
                    print("Game over. Computer wins. 🤖")
                else:
                    print("You win! Congrats. 😼")
                again()
        
    game()