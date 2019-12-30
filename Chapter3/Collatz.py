def collatz(number):
    if number % 2 == 0:
        print(number // 2)
        return number // 2
    else:
        result = 3 * number + 1
        print(result)
        return result


n = input('Enter number: ')
try:
    while n != 1:
        n = collatz(int(n))
except ValueError:
    print('That isn\'t a number, silly')