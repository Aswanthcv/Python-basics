#Write a program that uses a for loop to count the number of vowels in a given string.
word=(input("Enter a word: "))
vowels="AEIOUaeiou"
vowels_count=0
for i in word:
    if i in vowels:
        vowels_count+=1
print("Vowels in", word," is",vowels_count)        