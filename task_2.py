# Напиисать программу проверки пятизначное число на палиндромом.

while True:
    try:
        n = int(input('Input a number from 10000 to 99999: '))
        if n < 10000 or n > 99999:
            raise TypeError
    except ValueError:
        print('It is not a number')
        continue
    except TypeError:
        print('Number is out of the range.')
        continue
    break

# 1st decision
# m = 0
# num = n
# for i in range(4, -1, -1):
#     m = m + n % 10 * 10 ** i
#     n = n//10

# 2nd decision
# num = str(n)
# m = ''
# for s in reversed(num):
#     m = m + s


# 3rd decision
num = list(str(n))
m = list(reversed(num))

if m == num:
    print('Введенное число - палиндром ')
else:
    print('Введенное число - не палиндром ')

