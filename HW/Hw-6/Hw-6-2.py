# Task - I
text = "Python claims to strive for a simpler, less-cluttered syntax and grammar, while" \
" giving developers a choice in their coding methodology. Python lacks do while loops, " \
"which Rossum considered harmful. In contrast to Perl's motto \"there is more than one way to do it\", Python advocates " \
"an approach where \"there should be one – and preferably only one – obvious way to do it\". In practice, however, Python provides many ways to " \
"achieve a given goal. There are at least three ways to format a string literal, with no certainty as to which one a programmer should use." \
"Alex Martelli is a Fellow at the Python Software Foundation and Python book author; he wrote that \"To describe something as 'clever' is not considered a compliment in the Python culture."

# The comment is also a part of homework
#with open("data.txt", "w") as file:
#    file.write(text)
#    file.close()

with open("data.txt", "r") as file:
    content = file.read()
    file.close()

content = content.replace("Python", "Java")

with open("data.txt", "w") as file:
    file.write(content)
    file.close()

print("Done I")

# Task - II
with open("data.txt", "r") as file:
    content = file.read()
    file.close()

content = content.lower()
alphabet = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'e' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0 ,'x' : 0, 'y' : 0, 'z' : 0}
for letter in alphabet:
    alphabet[letter] = content.count(letter)

lines = []
for letter in alphabet:
    lines.append(f"{letter}: {alphabet[letter]}\n")

with open("charCount.txt", "w") as file:
    file.writelines(lines)
    file.close()

# Task - III
oldLines = []
newLines = []
differences = ["Differences:\n"]

with open("oldVersion.txt", "r") as file:
    oldLines = file.readlines()
    file.close()

with open("newVersion.txt", "r") as file:
    newLines = file.readlines()
    file.close()

for line in newLines:
    if not oldLines.__contains__(line):
        differences.append(f"  > {line}")

with open("differences.txt", "w") as file:
    file.writelines(differences)
    file.close()

# Task - IV
words = []
text = ""

with open("words.txt", "r") as file:
    words = file.read().splitlines()
    file.close()

print(words)

with open("source.txt", "r") as file:
    text = file.read()
    file.close()

for word in words:
    text = text.replace(word, "***")

with open("censored.txt", "w") as file:
    file.write(text)

