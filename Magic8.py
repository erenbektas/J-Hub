def magic8():

    while True:

        def main():   #the function to turn back to main.py
            from BackHome import back
            back()

        ###############################################################################################################################################
        help = """
        Someone asked for help?!
        The Magic 8-Ball is a plastic sphere, made to look like an oversized eight-ball, that is used for fortune-telling or seeking advice. 
        It was invented in 1946 by Albert C. Carter and Abe Bookman and is currently manufactured by Mattel.
        The user asks a yes–no question to the ball, then turns it over to reveal an answer in a window on the ball. 

        NOTE: You can go back to main menu by entering \"main/exit/home\"!
        """
        ###############################################################################################################################################
        exit = "main", "exit", "home", "back"
        ###############################################################################################################################################

        import random

        answers = [
        "It is certain.",
        " It is decidedly so.",
        "Without a doubt.",
        "Yes definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful."
        ]

        answer_index = random.randint(0, len(answers) - 1)

        question = input("================================\nPlease ask your question, or enter \"help\" for more information: ")

        sepr = "================================"
        txt = "\n\n Magic 8-Ball says:"
        res = print(sepr, txt, answers[answer_index], "\n")

        if question == "help":
            return help
        elif question in exit:
            main()
        else:
            result = res