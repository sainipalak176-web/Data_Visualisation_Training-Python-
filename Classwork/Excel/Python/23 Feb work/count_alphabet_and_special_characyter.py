sentence = input("enter a sentence:")
#to count the number of alphabets
count=0
for x in sentence:
    #to check x is alphabet or not
    if(x.isalpha()):
        count=count+1
print("the tota alphabets are:",count)
count = 0
#to count special character in character
for x in sentence:
    if(x.isalnum()):
        continue
    else:
        count=count+1        
print("the total special characters are:",count)

#output
#enter a sentence: Hello@123 World!
#the tota alphabets are: 10
#the total special characters are: 3