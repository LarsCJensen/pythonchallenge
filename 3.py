import re

with open("3_data.txt", "r") as f:
    chars = f.read()

regex = "[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+"
matches = re.findall(regex, chars)
if matches:
    print("".join(matches))
else:
    print("No match")
