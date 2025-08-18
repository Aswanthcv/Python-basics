# Write a program that takes a list of strings as input and returns a set containing
# the lengths of those strings.
word=input("Enter strings: ").split()

length={len(s) for s in word}
print(length)