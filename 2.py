import string

with open("2_data.txt", "r") as f:
    chars = f.read()
letters = ""
for char in chars:
    if char in string.ascii_lowercase:
        letters = letters + char
print(letters)
