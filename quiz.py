print("Welcome to my computer quiz!")
print()
print('The rules of the quiz are as follows:')
print('1. +4 for every correct answer.')
print('2. -1 for every incorrect answer.')
print('3. 0 if you skip the question.')
print('ALL THE BEST!!')
score = 0
print()
Q1=input('What is the full form of CPU?(enter "Skip" to skip this question): ')
if Q1.lower() =='skip':
        print('You skipped this question')
        print('The correct answer was Central Processing Unit')
        print()
elif Q1.lower() == 'central processing unit':
         print('That is the correct answer!')
         score= score + 4
         print()
else:
        print('That is the incorrect answer')
        print('The correct answer was Central Processing Unit')
        score = score - 1
        print()

Q2=input('Which memory holds data temporarily during processing?(enter "Skip" to skip this question): ')
if Q2.lower() == 'skip':
        print('You skipped this question')
        print('The correct answer was Random Access Memory')
        print()
elif Q2.lower() == 'ram' or Q2.lower() == 'random access memory':
        print('That is the correct answer!')
        score = score + 4
        print()
else:
        print('That is the incorrect answer')
        print('The correct answer was Random Access Memory')
        score = score - 1
        print()

Q3=input('What is the full form of ROM?(enter "Skip" to skip this question): ')
if Q3.lower() == 'skip':
        print('You skipped this question')
        print('The correct answer was Read Only Memory')
        print()
elif Q3.lower() == 'read only memory':
        print('That is the correct answer!')
        score = score + 4
        print()
else:
        print('That is the incorrect answer')
        print('The correct answer was Read Only Memory')
        score = score - 1
        print()

Q4=input('Name the main circuit board inside a computer(enter "Skip" to skip this question): ')
if Q4.lower() == 'skip':
        print('You skipped this question')
        print('The correct answer was Motherboard')
        print()
elif Q4.lower() == 'motherboard':
        print('That is the correct answer!')
        score = score + 4
        print()
else:
        print('That is the incorrect answer')
        print('The correct answer was Motherboard')
        score = score - 1
        print()

Q5=input('Which storage device uses flash memory and has no moving parts?(enter "Skip" to skip this question): ')
if Q5.lower() == 'skip':
    print('You skipped this question')
    print('The correct answer was Solid State Drive')
    print()
elif Q5.lower() == 'ssd' or Q5.lower() == 'solid state drive':
    print('That is the correct answer!')
    score=score + 4
    print()
else:
    print('That is the incorrect answer')
    print('The correct answer was Solid State Drive')
    score = score - 1

print()
print('Thank you for taking my quiz')
print(f'Your final score is {score}/20')
print()

if score<=0:
    print('Dont take it personally bro but I think you should go back to 1st grade.')
elif score<=7:
    print('pretty bad bro you just go humbled by a grade 3 level quiz.')
elif score<=14:
    print('My man that is pretty good.')
else:
    print('YOU ARE THE GOAT!!!')
