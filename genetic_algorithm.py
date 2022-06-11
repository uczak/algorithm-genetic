#import os
from random import randint

# print('foi')

NUMBER_OF_ENTRIES = 8
MAX_VALUE = -1  # maximun value
MAX_RUNS = 10  # number maximun of executin
CUT_NUMBER = NUMBER_OF_ENTRIES/2  # numero de corte para gerar nova populacao
# class Rules:

#     def __init__(self):
#         pass


class objects(object):
    def __init__(self, point_x, point_y, chromosome, fun, weighting=0):
        self.__point_x = point_x
        self.__point_y = point_y
        self.__chromosome = chromosome
        self.__fun = fun
        self.__weighting = weighting

    def print_not_weighting(self):
        return "%s %s %s %s" % (self.__point_x, self.__point_y, self.__chromosome, self.__fun)

    def print_yes_weighting(self):
        return "%s %s %s %s %s" % (self.__point_x, self.__point_y, self.__chromosome, self.__fun, self.__weighting)

    def get_point_x(self):
        return self.__point_x

    def get_point_y(self):
        return self.__point_y

    def get_chromosome(self):
        return self.__chromosome

    def get_fun(self):
        return self.__fun

    def get_weighting(self):
        return self.__weighting

    def set_weighting(self, weighting):
        self.__weighting = weighting


def convert_integer_to_binary(integer):
    return bin(integer)[2:]


def function(point_x, point_y):
    return 2 - ((point_x-2)**2) - ((point_y-3)**2)


def __stap_two():
    print('\n passo 2')
    stap_two = []
    for var in range(NUMBER_OF_ENTRIES):
        obj = []
        obj.append(str(var))
        obj.append(convert_integer_to_binary(var).rjust(3, '0'))
        stap_two.append(obj)
    print('Decimal | Binario')
    for obj in stap_two:
        print(obj)


def __stap_three():
    points_history = ''
    stap_three = []
    while len(stap_three) < 10:
        obj = []
        point_x = randint(0, NUMBER_OF_ENTRIES - 1)
        point_y = randint(0, NUMBER_OF_ENTRIES - 1)

        point = ' | ' + str(point_x) + ';' + str(point_y)
        if point in points_history:
            continue

        points_history += point
        obj.append(point_x)
        obj.append(point_y)
        obj.append(convert_integer_to_binary(point_x).rjust(
            3, '0') + convert_integer_to_binary(point_y).rjust(3, '0'))
        stap_three.append(obj)

    print('\n passo 3')
    print('X | Y | Cromossomo')
    for obj in stap_three:
        print(obj)
    return stap_three


def __stap_four(object_of_table):
    stap_four = []
    for obj_stap_three in object_of_table:
        obj_stap_three.append(function(obj_stap_three[0], obj_stap_three[1]))
        obj = objects(obj_stap_three[0], obj_stap_three[1],
                      obj_stap_three[2], obj_stap_three[3])
        stap_four.append(obj)

    print('\n passo 4')
    print('X | Y | Cromossomo | f(x,y)')
    for obj in stap_four:
        print(obj.print_not_weighting())
    return stap_four


def __stap_five(stap_four):
    stap_five = sorted(stap_four, key=objects.get_fun, reverse=True)
    print('\n passo 5')
    for obj in stap_five:
        print(obj.print_not_weighting())
    return stap_five


def __stap_six(stap_five):
    stap_six = stap_five[0:int(CUT_NUMBER)]
    print('\n passo 6')
    for obj in stap_six:
        print(obj.print_not_weighting())
    return stap_six


def __add_weighting(stap_six):
    number = 0
    new_object_of_table = []
    while number < CUT_NUMBER:
        # set attribute set_weighting from object with number of weighting
        stap_six[number].set_weighting(int(CUT_NUMBER - number))
        new_object_of_table.append(stap_six[number])
        number = number + 1
    print('\n passo 7')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for obj in new_object_of_table:
        print(obj.print_yes_weighting())
    return new_object_of_table


def __stap_seven(stap_six):
    new_object_of_table = __add_weighting(stap_six)
    number = CUT_NUMBER
    while number >= 0:
        new_object_of_table.append
        number = number - 1


def sort_number_of_chromosomes():
    number = randint(1, 6)
    print('quantidade de cromossomos que seram utilizados para mutação: ', number)
    direction = randint(0, 1)
    if direction == 1:
        print('começando a mutação de tras para a frente')
    else:
        print('começando a mutação da frente para tras')


# stapTwo
__stap_two()
# stapThree
stap_three = __stap_three()
object_of_table = stap_three
#runs = 0
# while MAX_VALUE < 2 or runs == MAX_RUNS:
# stapFour
stap_four = __stap_four(object_of_table)
# stapFive
stap_five = __stap_five(stap_four)
# stapSix
stap_six = __stap_six(stap_five)
# add weighting in objects
# __add_weighting(stap_six)
# stapSeven
stap_seven = __stap_seven(stap_six)
# sort number of chromosomes for mutation
sort_number_of_chromosomes()
#MAX_VALUE = int(stap_six[0].get_fun())

# print(MAX_VALUE)
