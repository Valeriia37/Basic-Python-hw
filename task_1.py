# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот
# день выходным.
while True:
    try:
        a = int(input('Input number of the week from 1 to 7: '))
        if a < 1 or a > 7:
            raise TypeError
    except ValueError:
        print('it is not a number.')
        continue
    except TypeError:
        print('number is out of the range.')
        continue
    break
if a > 5:
    print(f'{a} -> выходной день')
else:
    print(f'{a} -> будний день')