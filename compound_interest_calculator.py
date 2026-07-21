P=int(input('Enter the principle amount: '))
R=float(input('Enter the rate of interest: '))
T=int(input('Enter the time period: '))

while P<=0:
    print('The principle amount cannot be zero or negative')
    P=int(input('Enter a valid principle amount: '))
while R<=0:
    print('The rate of interest cannot be zero or negative')
    R=float(input('Enter a valid rate of interest: '))
while T<=0:
    print('The time period cannot be zero or negative')
    T=int(input('Enter a valid time period: '))

print(f'Your total bank balance after compound interest is {round(P*(1+R/100)**T, 2)}')
