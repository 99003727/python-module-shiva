#a=str(input("give the string:"))
with open('C:\\Users\\shiva\\OneDrive\\Documents\\GitHub\\python-module-shiva\\pythonminiproject.txt', 'r') as infile:
    lines = infile.readlines()
    #print(lines)
    '''for line in lines:
        if 'Software' in line:
            print(line)'''
#a=str(input("give the input:"))
with open('C:\\Users\\shiva\\OneDrive\\Documents\\GitHub\\python-module-shiva\\miniproject_1.txt', 'w') as file_output:
    count=0
    words=[]
    word_index=[]
    for x in lines:
        for word in x.split():
           if word.isalpha():
               words.append(word.upper())
           if 'software'.upper() in word.upper():
               count+=1
    for i in range(len(words)):
        if words[i].upper() == 'software'.upper():
            word_index.append(i)

    file_output.write(str(count))
    file_output.write(str(words))
    file_output.write(str(word_index))
    file_output.write(str(len(word_index)))
    
