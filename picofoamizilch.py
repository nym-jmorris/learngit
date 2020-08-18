
"""
let's try a game of pico fomi zilch

We'll need:
[x] to generate a number
[x] Prompt for a guess
[ ] test that it's suitable
[ ] evaluate the guess against the number
[ ] solicit guesses until matched

play again?


"""


from random import randrange

a = randrange(0,10)
b = randrange(0,10)
c = randrange(0,10)

a = 1
b = 2 
c = 3 

rounds = 1

testStatus = False

def getGuess():
    x = input('Enter your guess: ')
    return x

def evalGuess(guess):

    try: 
        val = int(guess)
        if val < 0 or  val > 999:
            print('Please enter a three digit positive integer.\n')
            evalStatus = False
        else: evalStatus = True

    except ValueError:
        print("Please enter a three digit positive integer.\n")
        evalStatus = False
    
    return evalStatus

def padGuess(guess):
    if int(guess)<10:
        guess = '00' + guess
    if int(guess)<100:
        guess = '0' + guess
    return guess

def testGuess(guess):
    testStatus = False

    if int(guess[0])== a:
        print('Pico')
    if int(guess[1])== b:
        print('Pico')
    if int(guess[2])== c:
        print('Pico')

#FOMI is the idea of the wrong spot.
# if we match a pico, we don't get a FOMI

    if int(guess[0])== b or int(guess[0])== c:
        if int(guess[0]) != a:
            print('Fomi')
    if int(guess[1])== a or int(guess[1])== c:
        if int(guess[1]) != b:
            print('Fomi')
    if int(guess[2])== a or int(guess[2])== b:
        if int(guess[2]) != c:
            print('Fomi')

    '''if (int(guess[0])== b or int(guess[0])== c) and  int(guess[0]) != a :
        print('Fomi')
    if (int(guess[1])== a or int(guess[1])== c) and  int(guess[1]) != b :
        print('Fomi')
    if (int(guess[2])== a or int(guess[2])== b) and  int(guess[2]) != c :
        print('Fomi')'''

    if int(guess[0]) != a and int(guess[0]) != b and int(guess[0]) != c:
        print('Zilch')
    if int(guess[1]) != a and int(guess[1]) != b and int(guess[1]) != c:
        print('Zilch') 
    if int(guess[2]) != a and int(guess[2]) != b and int(guess[2]) != c:
        print('Zilch')

    if guess == str(a)+str(b)+str(c):
        print('You win!')
        testStatus = True

    return testStatus

while not testStatus:
    testStatus = testGuess(getGuess())
    rounds +=1

print('And it only took you {} rounds!'.format(rounds-1))