a=str(input("give the string:"))
with open('C:\\Users\\99003727\\Documents\\GitHub\\python-module-shiva\\pythonminiproject.txt', 'r') as infile:
    for ch in ['\\n','`','*','_','{','}','[',']','(',')','>','#','+','-','.','!','$','\'','@',str([0-9]),'(',')',',','<']:
        if ch in infile:
            infile=infile.replace(ch,"")
    lines = infile.readlines()
    
with open('C:\\Users\\99003727\\Documents\\GitHub\\python-module-shiva\\miniproject_1.txt', 'w') as file_output:
    

    count=0
    words=[]
    word_index=[]
    before_words=[]
    after_words=[]
    for x in lines: #accesing the elements in lines
        for word in x.split(): # accesing the word in line
            if a.upper() in word.upper():
                   count+=1                                #checking the word in line and increasing the count
           #if word.isalpha():
            word.split("[\\s@&.? ()$+-]+") #splitting the word which has special characters
            words.append(word.upper())
           
    for i in range(len(words)):                     # getting the range of the repeated input in words list
        if a.upper() in words[i].upper():
            word_index.append(i)              

    file_output.write("count of the given word:\n"+str(count))
    file_output.write(str(words))
    #file_output.write(str(word_index))
    #file_output.write(str(len(word_index)))
    for i in word_index:                            #getting the previous and after input by accessing range
        before_words.append(words[i-1])
        after_words.append(words[i+1])
    file_output.write("\nbeforewords:\n"+str(before_words))
    file_output.write("\nafterwords:\n"+str(after_words))
    file_output.write("\ncount of before words:\n"+str(len(before_words)))
    file_output.write("\ncount of after words:\n"+str(len(after_words)))

    
    
