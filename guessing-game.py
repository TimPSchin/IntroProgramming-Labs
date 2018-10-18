def main():
    print("PYTHON GUESSING GAME")
    print(gameLoop())
        
answer = "monkey"
x = 0
def gameLoop():
    global x
    print("I am thinking of an animal.")
    while x < 10:
        guess = input("\nGuess what animal it is?").lower().strip()
        x += 1
        if guess == "quit":
            break 
        elif guess == answer:
              return "\nCongratulations, you guessed correctly!"
        else:
              print("I am sorry, thats not it, try again")
    print("\nDamn you suck")

main()
