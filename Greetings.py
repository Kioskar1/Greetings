import time

name = input('Enter your name :')
gender = input('Male or Female :')

h = time.strftime('%H')
h = int(h)

if h < 12 and h > 4:
    greeting = 'Good Morning'

elif h >= 12 and h <= 16:
    greeting = 'Good Evening'

elif h > 16 and h <=20 :
    greeting = 'Good Afternoon'

else :
    greeting = 'Good Night'

gender = gender.lower()

match gender :
    case 'male' :
        print(f'{greeting} {name} sir, nice to meet you!')
    case 'female' :
        print(f'{greeting} {name} mam, nice to meet you!')
    case _ :
        raise ValueError('Invalid input')