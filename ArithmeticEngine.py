# CMPT 120 - Lab #6
# Timothy Schindler
# 13-12-2018
###

def showIntro():
    print("Welcome to the Arithmetic Engine!")
    print("=================================\n")
    print("Valid commands are 'add', 'mult', 'sub', 'div', and 'quit'.\n"

def showOutro():
          print("\nThank you for using the Arithmetic Engine…")
          print("\nPlease come back again soon!")

def doLoop():
          while True:
          num1 = int(input("Enter the first  number: "))
          num2 = int(input("Enter the second number: "))
          cmd = input("What computation do you want to perform? ").lower().strip()

          if num2 == 0:
              print("You cant divide by 0")
          elif cmd == "add":
              result = num1 + num2
          elif cmd == "sub":
              result = num1 – num2
          elif cmd == "mult":
              result = num1 * num2
          elif cmd == "div":
              result = num1 // num2
          elif cmd == "quit":
              break
          else
              print(cmd, "is not a valid command.")
          
          print("The result is " + str(result) + ".\n")


def main():
    showIntro()
    doLoop()
    showOutro()
          
main()
    
            
