# Create an array of keys for each survey question
#hint: all keys must be unique
survey = ["What is your name?","What is your horoscope?","What is your lucky number?","What is your favorite ice cream flavor?","What is your favorite food?"]
key = ["key1", "key2", "key3", "key4", "key5"]

# Create an array of keys for each survey question
#hint: all keys must be unique

#Use a for loop to go through the questions in your survey
#Ex: if your survey has 4 questions, go through it the right number of times

#Inside the for loop, prompt user for response to each question.
#set their answers equal to the response
for i in range(len(survey)):
    key[i] = input(survey[i])

print (key[0])

#their answers are the "values"
answers = {
    "name": key[0],
    "horoscope": key[1],
    "lucky number": key[2],
    "favorite ice cream flavor": key[3],
    "favorite food": key[4]
}

#print the answers
print (answers)
