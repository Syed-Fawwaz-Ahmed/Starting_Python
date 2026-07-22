import time
Time=int(input('Enter the time in seconds: '))
for X in range(Time,-1,-1):
    time.sleep(1)
    Seconds=X%60
    Minutes=int(X/60) % 60
    Hours=int(X/3600)
    print(f'{Hours:02}:{Minutes:02}:{Seconds:02}')
