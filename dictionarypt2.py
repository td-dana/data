survey = ["What is your name?","What is your horoscope?","What is your lucky number?","What is your favorite ice cream flavor?","What is your favorite food?"]
key = ["key1", "key2", "key3", "key4", "key5"]

for i in range(len(survey)):
    key[i] = input(survey[i])

answers = {
    "name": key[0],
    "horoscope": key[1],
    "lucky number": key[2],
    "favorite ice cream flavor": key[3],
    "favorite food": key[4]
}

answerKey = ["key1", "key2", "key3", "key4", "key5"]

results = {
    "name": answerKey[0],
    "horoscope": answerKey[1],
    "lucky number": answerKey[2],
    "favorite ice cream flavor": answerKey[3],
    "favorite food": answerKey[4]
}


y = "true"
while y:
    ans = input("Would you like to take the survey again?")

    if ans.lower() == "no":
        print("Sure, we will show you your answers!")
        print (answers)
        break
    else:
        print("Sure, we will provide you the survey again!")
        for i in range(len(survey)):
            answerKey[i] = input(survey[i])
        print ( answers, results)
        continue
