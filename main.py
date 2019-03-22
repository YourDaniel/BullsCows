from random import randint
numbers = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))


def check_for_bulls(g):
    bulls = []
    for i in range(len(numbers)):
        if numbers[i] == g[i]:
            bulls.append(numbers[i])
        else:
            bulls.append(-1)
    return bulls


def check_for_cows(g, b):
    no_cow_index = []
    cow_index = []
    for i in range(len(b)):
        if b[i] == numbers[i]:
            no_cow_index.append(i)
        else:
            cow_index.append(i)
    cows_number = 0
    for i in cow_index:
        for j in cow_index:
            if g[i] == numbers[j] and i != j and not(i in no_cow_index):
                cows_number += 1
                no_cow_index.append(i)
    return cows_number


def count_bulls(b):
    s = 0
    for i in b:
        if i != -1:
            s += 1
    return s


tries = 0
print('Guess the 4 numbers!')
while True:
    tries += 1
    while True:
        guess = [int(i) for i in input().split()]
        if len(guess) != 4:
            print('Enter 4 numbers')
        else:
            break
    bulls = check_for_bulls(guess)
    cows = check_for_cows(guess, bulls)
    print('Bulls: {}. Cows: {}.'.format(count_bulls(bulls), cows))
    if count_bulls(bulls) == 4:
        print('You win! Tries: {}'.format(tries))
        print('Numbers: {}'.format(numbers))
        break
