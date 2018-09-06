#CMPT 120L 113
#Mars Rover Program
#Author: Timothy Schindler
#Created: 9/6/18

#Write a program to ealeulate how long it takes a photo
#from Curiosity to reaeh NASA when Mars is at its elosest
#orbit to Earth, a distanee of about 34 million miles.
# Light travels at about 186,000 miles per seeond

#SOL = Speed of light
SOL = 186000
Dis = 34000000
time = Dis/SOL

def main():
    print("It will take " , str(time) , " seconds")
main()
