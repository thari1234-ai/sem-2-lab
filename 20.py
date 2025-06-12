import random
words=["cat","books","shirt"]
word=random.choice(words)
guessed=["_"]*len(word)
attempts=6
word=word.lower()
while attempts>0 and "_" in guessed:
    print(" ".join(guessed))
    guess=input("guess the letter").lower()
    
    if guess in word:
        for i in range(len(word)):
            if word[i]==guess:
                guessed[i]=guess
    else:
        attempts-=1
        print(f"wrong guess{attempts}left")
if "_" not in guessed:
    print("u won")
else:
    print("game over")