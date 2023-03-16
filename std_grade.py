#!/usr/bin/pytho
grade = 0

print('Welcome to osfoce mini quiz')

playing = input ('Did you wanna play? ')

if playing.lower() != "yes":
    quit()
else:
    print('Thats wonderful lets go!!')    

Q1 = input('\nWhat does CPU stands for?\n')  
if Q1.lower() == "central processing unit":
    print('Correct!!')
    grade += 1
else:
    grade = grade

Q2 = input('\nWhat is GPU \n')  
if Q2.lower() == "graphical processing unit":
    print('Correct!!')
    grade += 1
else:
    grade = grade

Q3 = input('\nwhats 2 + 5?\n a 9 \n b 7 \n')  
if Q3 == "b":
    print('Correct!!')
    grade += 1
else:
    grade = grade

Q4 = input('\nIs Elon Must the CEO of Tesla\n a yes \n b no \n')  
if Q4 == "a":
    print('Correct!!')
    grade += 1
else:
    grade = grade

print(f'your grade is {grade}/4')
print(f'you got {(grade / 4) * 100}%')