while True:
    N1 = float(input('Enter the first number: '))
    N2 = float(input('Enter the second number: '))
    opr = input("Enter the operator(+,-,*,**,/,%,Enter 'Exit' or 'Quit' to stop): ")

    if opr=='Exit'or opr=='Quit':
      print()
      print('Thank you for using this calculator')
      break
    if opr=='+':
      print(f'The sum of {N1} and {N2} is: {N1+N2}')
    elif opr=='-':
      print(f'The difference of {N1} and {N2} is: {N1-N2}')
    elif opr=='*':
      print(f'The multiplication of {N1} and {N2} is: {N1*N2}')
    elif opr=='/':
      if N2==0:
        print('Cannot divide by zero')
      else:
        print(f'The division of {N1} and {N2} is: {N1/N2}')
    elif opr=='%':
      if N2==0:
        print('Cannot divide by zero')
      else:
        print(f'The remainder of {N1} and {N2} is: {N1%N2}')
    elif opr=='**':
      print(f'{N1} raised to the power of {N2} is: {N1**N2}')
    else:
      print('Invalid operator, please enter a valid operator')
