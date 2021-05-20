import json
import requests

# import statements
dictionary = {}
letters = "abcdefghijklmnopqrstuvwxyz"
result = ""
dlc = requests.get("https://raw.githubusercontent.com/mical385/english_words/main/words.txt")
# download the words from my repo
dlc = str(dlc.text)
f = open("words.txt", "w+")
temp = dlc.replace("\n", "")  # removes the newlines that I don't need
dlc = temp
f.write(dlc)
f.close()
temp = 0
with open('words.txt', 'r') as f:
    for line in f:
        temp = line.replace("\n", "")
        line = temp
        temp = 0
        for i in range(0, 26):  # loop through all the alphabets
            for j in range(0, len(line)):  # checks every letters
                if letters[i] == line[j]:
                    temp += 1
            result += str(temp)

            temp = 0
        dictionary[line] = result
        result = ""

with open("words_dictionary.json", "w") as f:
    json.dump(dictionary, f, indent=4)
