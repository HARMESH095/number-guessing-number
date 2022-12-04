import random
import time

print('HELLO BUDDY!!! MY NAME IS TIM WHAT IS YOUR NAME ?')
myName = input(":: ")
print(".")
time.sleep(0.8)
print(".")
time.sleep(0.8)
while True:
    h = input( myName.upper() + ", WOULD YOU LIKE TO PLAY A GAME\n(YES/NO)\n::")
    print(".")
    time.sleep(0.8)
    print(".")
    time.sleep(0.8)
    if h == "yes" or h=="YES":
        print("SELECT A LEVEL TO ENTER INTO THE GAME ! "+ myName.upper()+" .")
        print(":> TYPE 'E' FOR EASY LEVEL\n:> TYPE 'M' FOR MEDIUM LEVEL\n:> TYPE 'H' FOR HARD LEVEL")
        user = input("::")
        print(".")
        time.sleep(0.8)
        print(".")
        time.sleep(0.8)
        if user == "e" or user=="E":
            range = int(input("UP TO WHICH NUMBER CAN I THINK OF:: "))
            number = random.randint(1, range)
            guessesTaken = 0
            while guessesTaken < 10:
                print(".")
                time.sleep(0.8)
                print(".")
                time.sleep(0.8)
                guess = int(input("GUESS THE NUMBER::"))
                guessesTaken = guessesTaken + 1

                if str(guessesTaken) == "3":
                    if 0 < number <= (20 / 100) * range:
                        time.sleep(1)
                        print(".")
                        print("HINT ::: guessed number is between")
                        print((0, number + 3))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)
                    elif (20 / 100) * range < number <= (80 / 100) * range:
                        time.sleep(1)
                        print(".")
                        print("HINT ::: guessed number is between")
                        print((number - 5), "and", (number + 6))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)
                    elif (80 / 100) * range < number < range:
                        time.sleep(1)
                        print(".")
                        print("HINT ::: guessed number is between")
                        print((number - 6), "and", (range))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)

                if guess < number:
                    print('Your guess is too low, try higher...')

                elif guess > number:
                    print('Your guess is too high, try lower...')

                elif guess == number:
                    guessesTaken = str(guessesTaken)
                    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
                    print(".")
                    time.sleep(0.8)
                    print(".")
                    time.sleep(0.8)
                    break
        elif user == "m" or user=="M":

            range = int(input("UP TO WHICH NUMBER CAN I THINK OF:: "))
            number = random.randint(1, range)
            guessesTaken = 0
            while guessesTaken < 10:
                print(".")
                time.sleep(0.8)
                print(".")
                time.sleep(0.8)
                guess = int(input("GUESS THE NUMBER::"))
                guessesTaken = guessesTaken + 1

                if str(guessesTaken) == "5":
                    if 0 < number <= (20 / 100) * range:
                        time.sleep(1)
                        print(".")
                        print("guessed number is between")
                        print((0, number + 14))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)
                    elif (20 / 100) * range < number <= (80 / 100) * range:
                        time.sleep(1)
                        print(".")
                        print("guessed number is between")
                        print((number - 13), "and", (number + 17))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)
                    elif (80 / 100) * range < number < range:
                        time.sleep(1)
                        print(".")
                        print("guessed number is between")
                        print((number - 9), "and", (range))
                        print(".")
                        time.sleep(0.8)
                        print(".")
                        time.sleep(0.8)

                if guess < number:
                    print('Your guess is too low, try higher...')

                elif guess > number:
                    print('Your guess is too high, try lower...')

                elif guess == number:
                    guessesTaken = str(guessesTaken)
                    print(
                        'Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
                    print(".")
                    time.sleep(0.8)
                    print(".")
                    time.sleep(0.8)
                    break
        elif user == "h" or user=="H":
            range = int(input("UP TO WHICH NUMBER CAN I THINK OF:: "))
            number = random.randint(1, range)
            guessesTaken = 0
            while guessesTaken < 10:
                print(".")
                time.sleep(0.8)
                print(".")
                time.sleep(0.8)
                guess = int(input("GUESS THE NUMBER::"))
                guessesTaken = guessesTaken + 1
                if guess < number:
                    print('Your guess is too low, try higher...')
                elif guess > number:
                    print('Your guess is too high.')
                elif guess == number:
                    guessesTaken = str(guessesTaken)
                    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')
                    print(".")
                    time.sleep(1)
                    print("THANK YOU FOR PLAYING")
                    time.sleep(0.8)
                    print(".")
                    time.sleep(0.8)
                    break
        else:
            print("may be you typed wrong try again...")
            print(".")
            time.sleep(1)
            print(".")
            time.sleep(1)
    else:
        print(":)")
        break




