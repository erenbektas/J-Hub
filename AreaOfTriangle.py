def area():

    while True:

        def main():   #the function to turn back to main.py
            from BackHome import back
            back()

###############################################################################################################################################
        help = """
        Someone said help?!
        So, what you need to do is writing lengths of each sides of the triangle. Don\'t forget to separate them with space.
        Let\'s say our triangle has sides with following lenghts: 8 cm, 15 cm, 17 cm.
        In this case, the input should be \"8 15 17\", without the quotation marks (\")! You can also use decimals!
        NOTE: You can go back to main menu by entering \"main/exit/home\"!
        """
###############################################################################################################################################
        errormsg = """
        Looks like something isn't right. Let me explain the system.
        So, what you need to do is writing lengths of each sides of the triangle. Don\'t forget to separate them with space.
        Let\'s say our triangle has sides with following lenghts: 8 cm, 15 cm, 17 cm.
        In this case, the input should be \"8 15 17\", without the quotation marks (\")! You can also use decimals!
        NOTE: You can go back to main menu by entering \"main/exit/home/back\"!
        """
###############################################################################################################################################
        exit = "main", "exit", "home", "back"
###############################################################################################################################################

        lengths = input("================================\nPlease enter the lengths of the sides of the triangle by separating them with spaces. Enter \"help\" for more information:" )
        ls_ln = lengths.split(" ")

        if lengths == "help":
            return help
        elif lengths in exit:
            main()
        else:
            try:
                a = float(ls_ln[0])
                b = float(ls_ln[1])
                c = float(ls_ln[2])
                s = float((a + b + c) / 2)
                if a > 0 and b > 0 and c > 0:
                    txt = "The area of the triangle with the lines you entered is: "
                    result = str((s * (s - a) * (s - b) * (s - c)) ** 0.5)
                    return txt + result
            except ValueError:
                return errormsg