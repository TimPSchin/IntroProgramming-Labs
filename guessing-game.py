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
        if guess[0] == "q":
            break 
        elif guess == answer:
            print("\nCongratulations, you guessed correctly!")
            yORn = input("Do you like that animal? y or n")
            if yORn == "y":
                print("Awesome")
            else:
                print("Damn, you suck")
            return
        else:
              print("I am sorry, thats not it, try again")
    print("\nDamn, you suck")

main()
