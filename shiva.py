# class userinput:
#     def __init__(self,number,input_string):
#         self.number = number
#         self.input_string = input_string
#     def usernumber(self):
#         return self.number
#     def userstring(self):
#         return self.input_string
number = int(input("How many words: "))
for userinputcount in range(int(number)):
    input_string = str(input("give the string:"))
    # path = 'C:\\Users\\99003727\\Documents\\GitHub\\python-module-shiva\\'
    with open('test.txt', 'r') as infile:
        lines = infile.readlines()
    with open(input_string+'.txt', 'w') as file_output:
        count = 0
        words = []
        word_index = []
        before_words = []
        after_words = []
        for x in lines:  # accesing the word in line
            for word in x.split():   # accesing the elements in lines
                if input_string.upper() in word.upper():
                    count += 1  # checking the word and increasing the count
                word.split("[\\s@&.? ()$+-]+")  # splitting the word
                words.append(word.upper())
        for i in range(len(words)):  # getting the range of the repeated input
                if input_string.upper() in words[i].upper():
                    word_index.append(i)
        file_output.write("The word being find is: "+input_string)
        file_output.write("\ncount of the given word:\n"+str(count))
        for i in word_index:    # getting the previous and after input
            before_words.append(words[i-1])
            after_words.append(words[i+1])
        file_output.write("\nbeforewords:\n"+str(before_words))
        file_output.write("\nafterwords:\n"+str(after_words))
        file_output.write("\ncount of before words:\n"+str(len(before_words)))
        file_output.write("\ncount of after words:\n"+str(len(after_words)))