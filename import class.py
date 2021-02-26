from shiva import*


class Inheriting(userinput):   # inheriting the userinput class
    def __init__(self):
        print("Pls provide valid inputs!!!")
        userinput.__init__(self, str(input("give the number:")))
obj1 = Inheriting()  # creating the obj for Inherited class
obj1.main()  # calling the main function
