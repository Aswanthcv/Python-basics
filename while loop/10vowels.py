# Write a program that counts the number of vowels in a given string using a while loop

text=input("Enter a text: ")
vowels="AEIOUaeiou"
count=0
i=0
while i<len(text):
    if text[i] in vowels:
        count+=1
    i=i+1    
print("Vowels in the text : ",count)        
