import random
max_range = input('Enter the range of your number: ')

if max_range.isdigit():
    max_range = int(max_range)
    if max_range <= 0:
        print('Please enter a number greater than 0 next time')
        quit()
else:
    print('Please enter a number')
    quit()

random_number = random.randrange(0, max_range)
guess_count = 0

while True:
    guess_count += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please enter a number')
        continue
    if user_guess == random_number:
        print('You got it right')
        break
    elif user_guess < random_number:
            print('you are below the number Try again!')
    else:
            print('you are above the number Try again!')

print(f'\nIt took you',guess_count,'guess to get it right ')