import json
with open("dict.json","r") as file:
    data=json.load(file)
while True:
    word=input("\n Enter the word").strip()
    if not word:
        break
    if word in data:
        print(data[word])
    else:
        suggestions=[key for key in data if key.lower()==word.lower()]
        if suggestions:
            correct_word=suggestions[0]
            choice=input(f" did u mean{correct_word} if yes give Y else N").strip().lower()
            if choice=="y":
                print(data[correct_word])
            else:
                print("the word is not real")
        else:
            print("doesnt exixt yaar")
    print("Press enter to exit")
                