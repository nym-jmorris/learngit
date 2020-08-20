
"""
let's try a game of pico fomi zilch

We'll need:
[x] to generate a number
[x] Prompt for a guess
[x] test that it's suitable
[x] evaluate the guess against the number
[x] solicit guesses until matched

play again?


"""


from random import randrange

'''
a = randrange(0,10)
b = randrange(0,10)
c = randrange(0,10)
'''

digits = 3

# def getDigits():
#     entry = input('How many digits? [2,3,4]')
#     try: 
#         digits = int(entry)
#         if digits > 0 and digits < 5:
#             return digits,True
#         elif digits > 4:
#             print('That''s too many digits, hombre. Please try again.')
#             return 0, False
#         else: 
#             print('Postive integers only, amigo. Please try again.')
#             return 0, False
#     except ValueError:
#         print('Please enter an integer between 1 and 4.')
#         return 0, False




#this is not escaped in a function. Enter an integer...
digits = int(input('How many digits? [2,3,4]'))

d = randrange(0,10**digits)

#d =123

rounds = 0

guessGood = False


def getGuess():
    x = input('Enter your guess: ')
    return x

def isNumber(guess):
    gNumber = False
    try: 
        val = int(guess)
        if val < 0 or val > 10**digits:
            print('Please enter a positive integer less than {}.\n'.format(str(10**digits)))
            return gNumber
        else:
            gNumber= True
            return gNumber
    except ValueError:
        print('Please enter a positive integer less than {}.\n'.format(str(10**digits)))
        return gNumber


def formatGuess(guess):
    gformat = '{:>0'+str(digits)+'}'
    if guess != gformat.format(guess):
        print('Reformatting...')
    guess = gformat.format(guess)
    return guess

def pfz(x):
    if x == 'Pico':  z=1
    if x == 'Fomi':  z=2
    if x == 'Zilch': z=3
    return z

gNumber = False

guessCorrect = False

def evalGuess(guess):
    response =[]
    guessCorrect = False
    dstr = str(d)
    for i in range(0,digits):
        if dstr[i] == guess[i]:
            response.append('Pico')
        elif guess.find(dstr[i]) >-1:
            response.append('Fomi')
        else: 
            response.append('Zilch')
    print(sorted(response, key = pfz))
    if guess == str(d):
        print('You win!')
        guessCorrect = True
    return guessCorrect

while not guessCorrect:
    gNumber = False
    while not gNumber:
        guess = getGuess()
        gNumber = isNumber(guess)
        if gNumber: 
            guess = formatGuess(guess)
    guessCorrect = evalGuess(guess)
    rounds +=1
    if guessCorrect == True:
        print('It took you {} rounds.'.format(rounds))
    

