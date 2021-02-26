class userinput:
    def __init__(self, number):
        self.number = number

    def usernumber(self):
        return self.number

    def main(self):
        while int(self.number) > 0:
            self.number = int(self.number)-1
            input_string = str(input("give the string:"))
            with open('test.txt', 'r') as infile:
                lines = infile.readlines()
                # creating a list with lines as elements
            with open(input_string+'.txt', 'w') as file_output:
                count = 0
                words = []
                word_index = []
                before_words = []
                after_words = []
                for x in lines:  # accesing the word in line
                    for word in x.split():  # accesing the elements in lines
                        if input_string.upper() in word.upper():
                            count += 1
                        word.split("[\\s@&.? ()$+-]+")  # splitting the word
                        words.append(word.upper())
#  appendingthe element of line by using upper function to word list
                        # get the range of the repeat input
                for i in range(len(words)):
                        if input_string.upper() in words[i].upper():
                            word_index.append(i)
                file_output.write("The word being find is: "+input_string)
                file_output.write("\ncount of the given word:\n"+str(count))
                for i in word_index:    # getting the previous and after input
                    before_words.append(words[i-1])
                    after_words.append(words[i+1])
                file_output.write("\nbeforewords:\n"+str(before_words))
                file_output.write("\nafterwords:\n"+str(after_words))
                file_output.write("\ncnt bef words:\n"+str(len(before_words)))
                file_output.write("\ncount aft words:\n"+str(len(after_words)))