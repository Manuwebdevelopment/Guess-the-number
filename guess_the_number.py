import random
import time
secret_number = random.randint(1,100)
print("I'm thinking of a number between 1 and 100....")
time.sleep(5)
#print(f"Shhhh I'm helping you... {secret_number}")
for guess_taken in range(1,8):
    print('Take a guess')
    guess = int(input())

    if guess > secret_number:
        print('Your guess is too high')
    elif guess < secret_number:
        print('Your guess is too low')
    else:
        break
if guess == secret_number:
    print("Good job! You guessed my number in " + str(guess_taken) + " guesses")
else:
    print("Nope. The number I was thinking was" + str(secret_number))