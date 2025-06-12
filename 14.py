import random
words=["cat","mats","Tharini"]
word=random.choice(words)
attempts=6
guessed=["_"]*len(word)
word=word.lower()

while attempts>0 and "_" in guessed:
    print(" ".join(guessed))
    guess=input("guess a letter:").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
    else:
        attempts-=1
        print(f"Wrong guess{attempts}left")
if "_" not in guessed:
    print("congrats")
else:
    print(f"game over the correct word is{word} ")
    