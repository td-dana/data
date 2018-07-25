import json

survey = ["What is your name?", "What is your favorite programming language?"]

keys = ["name", "language"]

list_of_answers = []

done = "No"

while done == "No":
    answers = {}

    for x in range(len(survey)):
        response = input(survey[x]+" ")
        answers[keys[x]] = response

    list_of_answers.append(answers)
    done = input("Hey are you done? Yes or No?")

#Open file with all past results and apppend them to current listen

f = open("file.json", "r")
oldData = json.load(f)
list_of_answers.extend(oldData)
f.close()

f = open("file.json", "w")
f.write('\n')
index = 0

for j in list_of_answers:
    if (index, len(list_of_answers)-1):
        json.dump(j,f)
        f.write('\n')
    else:
        json.dump(j,f)
        f.write('\n')
    index += 1

    f.write(']')
    f.close()
