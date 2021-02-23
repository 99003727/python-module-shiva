a=str(input("give the string:"))
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
    for x in lines:
        for word in x.split():
           if word.isalpha():
               words.append(word)
           if a.casefold() in word.casefold():
               count+=1 

    file_output.write(str(count))
    file_output.write(str(words))
    
