#a=str(input("give the string:"))
with open('C:\\Users\\99003727\\Documents\\GitHub\\python-module-shiva\\pythonminiproject.txt', 'r') as infile:
    lines = infile.readlines()
    #print(lines)
    '''for line in lines:
        if 'Software' in line:
            print(line)'''
#a=str(input("give the input:"))
with open('C:\\Users\\99003727\\Documents\\GitHub\\python-module-shiva\\miniproject_1.txt', 'w') as file_output:
    count=0
    words=[]
    word_index=[]
    before_words=[]
    after_words=[]
    for x in lines: #accesing the elements in lines
        for word in x.split(): # accesing the word in line
            if 'software'.upper() in word.upper():
                   count+=1                                #checking the word in line and increasing the count
           #if word.isalpha():
            word.split("[\\s@&.? $+-]+") #splitting the word which has special characters
            words.append(word.upper())
           
    for i in range(len(words)):                     # getting the range of the repeated input in words list
        if 'software'.upper() in words[i].upper():
            word_index.append(i)              

    file_output.write(str(count))
    #file_output.write(str(words))
    #file_output.write(str(word_index))
    file_output.write(str(len(word_index)))
    for i in word_index:                            #getting the previous and after input by accessing range
        before_words.append(words[i-1])
        after_words.append(words[i+1])
    file_output.write(str(before_words))
    file_output.write(str(after_words))
    
