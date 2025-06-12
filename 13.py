import json
with open("dict.json","r")as file:
    data=json.load(file)
while True:
    word=input("Enter the word").strip()
    if not word:
        break
    if word in data:
        print(data[word])
    else:
        suggestions=[key for key in data if key.islower()==word.islower()]
        if suggestions:
            correct_word=suggestions[0]
            choice=input(f"did u mean {correct_word} if yes give Y else give N").strip().lower()
            if choice=="y":
                print(data[correct_word])
            else:
                print("The word is not found")
        else:
            print("The word is not exist")
    print("Press enter to exit")
            