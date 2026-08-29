# This program performs different string operations on a full name.

name = input("Enter your full name: ")

clean_name = name.strip()

print("Uppercase:", clean_name.upper())
print("Lowercase:", clean_name.lower())
print("Title Case:", clean_name.title())
print("Reversed:", clean_name[::-1])
print("Length:", len(clean_name))