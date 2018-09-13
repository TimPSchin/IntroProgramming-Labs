#CMPT 120L 113
#Madlibs
#Author: Timothy Schindler
#Created: 9/6/18

def promptForWords():
    global obj, verb, adj, place
    obj = input('Enter an object: ')
    verb = input('Enter a verb: ')
    adj = input('Enter a adjective: ')
    place = input('Enter a place: ')

def makeAndPrintSentence():
    print("Take your " + adj + " " + obj + " and" + " " + verb + " it at the " + place)

def main():
    promptForWords()
    makeAndPrintSentence()


main()
