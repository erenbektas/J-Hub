from AreaOfTriangle import area
from Magic8 import magic8

###############################################################################################################################################
intro = """
================================
Welcome to J-Hub!\n
Here is where you can find all my extremely unnecessary tools which are created by me while studying Python.
I\'ll be listing these tools/projects below in an alphabetical order and keep the list up-to-date if I add some new ones.
Don\'t be shy!
"""
###############################################################################################################################################
value_error = """
!!! - Please enter numbers. i.e. \"1\" for the first tool/project in the list, without the quotation marks (\"). - !!!"""

index_error = """
!!! - Please select a valid item from the list. - !!!"""
###############################################################################################################################################

list = "1- Calculate the Area of a Triangle", "2- Magic 8-Ball"

funcs = [area, magic8,] #list of imported functions to be called by "print(funcs[int(direct_to) - 1]())"

def home():   #The function which will provdide the options

    print(intro)

    list_txt = "\n".join(list)   #Will list all the tools in a vertical order
    print(list_txt)

    def select():

        direct_to = input("================================\nPlease enter the number of the tool/project you want to use: ")

        while True:
            try:
                print(funcs[int(direct_to) - 1]())
            except ValueError:
                print("-----------------------------------------------------")
                print(list_txt)
                print(value_error)
                select()
            except IndexError:
                print("-----------------------------------------------------")
                print(list_txt)
                print(index_error)
                select()
    select()
            

home()