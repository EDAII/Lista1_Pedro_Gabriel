from random import randint
def numbers_gen():
    number_list = []
    while(len(number_list) < 105):
        n = randint(0, 100000)
        if not n in number_list:
            number_list.append(n)
    number_list.sort()
    return number_list
def choose_number(number_list):
    n = randint(0, 105)
    print(number_list[n])
    return number_list[n]