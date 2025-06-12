import random
words=["Tharini","Giri","loves"]
word=random.choice(words).lower()
guessed=["_"]*len(word)
attempts=6
while attempts>0 and "_" in guessed:
    print(" ".join(guessed))
    guess=input("Guess a word:").lower()
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guessed[i] = guess
    else:
        attempts-=1
        print(f"Wrong guess {attempts}left")
if "_" not in guessed:
    print("congrats")
else:
    print(f"the correct word is {word}")
        
          