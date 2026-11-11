#VERSION 2!
first = input("Enter your first name: ")
last = input("Enter your last name: ")
section = input("Enter your section: ")
subj = input("Enter your favorite subject: ")

first = "".join(first.split())
last = "".join(last.split())

code = first+" "+last
code = code.upper()

section = section.upper()

subj = subj.capitalize()

length = len(code)

print()
print("Formatted Output:")
print("Name:", first, last)
print("Name code:", code)
print("Section:", section)
print("Favorite subject:", subj)
print("Character Count:", length)
