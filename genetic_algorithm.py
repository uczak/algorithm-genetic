#import os
from random import randint
#from time import time
import time

# print('foi')

NUMBER_OF_ENTRIES = 8
NUMBER_EXPECTED = 2 
#MAX_VALUE = -1  # maximun value
MAX_RUNS = 6  # number maximun of executin
CUT_NUMBER = NUMBER_OF_ENTRIES/2  # numero de corte para gerar nova populacao
# class Rules:

#     def __init__(self):
#         pass


class objects(object):
    def __init__(self, point_x=0, point_y=0, chromosome=0, fun=0, weighting=0):
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

    def set_chromosome(self, chromosome):
        self.__chromosome = chromosome

    def get_fun(self):
        return self.__fun

    def set_fun(self, fun):
        self.__fun = fun

    def get_weighting(self):
        return self.__weighting

    def set_weighting(self, weighting):
        self.__weighting = weighting
    
    def convert_chromosome(self):
        point_x =  str(self.__chromosome[0:3])
        point_y =  str(self.__chromosome[3:5])
        self.__point_x = int(point_x, 2)
        self.__point_y = int(point_y, 2)


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

def sort_number_of_chromosomes():
    amount = 2#randint(1, 5)
    print('quantidade de cromossomos que seram utilizados para mutação: ', amount)
    direction = 1#randint(0, 1)
    if direction == 1:
        print('começando a mutação de tras para a frente')
    else:
        print('começando a mutação da frente para tras')
    return amount, direction


def replicate_population(individual,  amount, direction):
    replicate_population =[]
    replicate_population.append(individual) # salvando o pai na nova lista
    chromosome = str(individual.get_chromosome())
    chromosome_changed = ''
    chromosome_unchanged = chromosome
    new_chromosome = chromosome
    if direction == 0:
        chromosome_changed = chromosome[0:amount]
        chromosome_unchanged = chromosome[amount:len(chromosome)]
        new_chromosome = chromosome_convert(chromosome_changed) + chromosome_unchanged 
    else: #if direction == 1:
        chromosome_changed = chromosome[(len(chromosome) - amount):len(chromosome)]
        chromosome_unchanged = chromosome[0:(len(chromosome) - amount)]
        new_chromosome = chromosome_unchanged + chromosome_convert(chromosome_changed)

    #print('chromosome_changed', chromosome_changed)
    #print('chromosome_unchanged', chromosome_unchanged)
    #print('new_chromosome', new_chromosome)
    
    iteration = 0
    while iteration < individual.get_weighting() - 1:
        if direction == 0:
            new_chromosome = chromosome_convert(chromosome_changed) + chromosome_unchanged 
        else:
            new_chromosome = chromosome_unchanged + chromosome_convert(chromosome_changed)
        #for pop in amount_individual:
        replicate_population.append(objects(chromosome=new_chromosome))
        iteration+=1
    ##print('test')
    #print(replicate_population.print_yes_weighting())
    return replicate_population

def chromosome_convert(chromosome):
    returned = ''
    for chr in chromosome:
        #time.sleep(1.5)
        # num = randint(0, 100)
        # if num % 2 == 0:
        #     returned = returned + '0'
        # else:
        #     returned = returned + '1'
        returned = returned + str(randint(0, 1))
        #print(chr)
        # if chr =='0':
        #     returned = returned + '1'
        # else:
        #     returned = returned + '0'
    return returned

def create_new_population(object_with_weighting, amount, direction):
    children = []
    for individual in object_with_weighting:
        children = children + replicate_population(individual, amount, direction)
    return children

def __stap_seven(stap_six):
    #number = CUT_NUMBER
    object_with_weighting = __add_weighting(stap_six)
    amount, direction = sort_number_of_chromosomes()
    new_population = create_new_population(object_with_weighting, amount, direction) 
    
    print('\n passo 7')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in new_population:
        print(ff.print_yes_weighting())
    # while number >= 0:
    #     new_object_of_table.append
    #     number = number - 1
    return new_population



def __stap_nine(stap_seven, account_runs):

    if not (account_runs - 1) % 5 == 0:
        return

    individual_position = []
    while True:

        num = str(randint(0, 9))
        if num not in individual_position:
            individual_position.append(num)
            if len(individual_position) == 5:
                break

    # for ff in individual_position:
    #     print(ff)

    for position in individual_position:
        individual = stap_seven[int(position)]
        chromosome = individual.get_chromosome()
        num = randint(0, 5)
        #print('chromosome', int(position) + 1 , 'gene',num +1)
        #print('num',num)
        chromosome_changed_pre = chromosome[0:num]
        chromosome_changed_pos = chromosome[num + 1:len(chromosome)]
        chromosome_unchanged = chromosome[num]
        if chromosome_unchanged == '1':
            chromosome_unchanged = '0'
        else:
            chromosome_unchanged = '1'
        #print('chromosome_changed_pre', chromosome_changed_pre , 'chromosome_unchanged',chromosome_unchanged, 'chromosome_changed_pos',chromosome_changed_pos)
        
        individual.set_chromosome(chromosome_changed_pre + chromosome_unchanged + chromosome_changed_pos)

    print('\n passo 9')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in stap_seven:
        print(ff.print_yes_weighting())


def __stap_ten(stap_seven):
    for individual in stap_seven:
        individual.convert_chromosome()

    print('\n passo 10')
    print('X | Y | Cromossomo | f(x,y) | Ponderação')
    for ff in stap_seven:
        print(ff.print_yes_weighting())

def __stap_eleven(stap_seven):
    for individual in stap_seven:
        individual.set_fun(function(individual.get_point_x(), individual.get_point_y()))
    
    stap_eleven = sorted(stap_seven, key=objects.get_fun, reverse=True)
    for ff in stap_eleven:
        ff.set_weighting(0)

    print('\n passo 11')
    print('X | Y | Cromossomo | f(x,y)')
    for ff in stap_eleven:
        print(ff.print_not_weighting())
    return stap_eleven

# stapTwo
__stap_two()
# stapThree
stap_three = __stap_three()
 # stapFour
stap_four = __stap_four(stap_three)

account_runs = 0
function_value = 0

while account_runs < MAX_RUNS:
    account_runs = account_runs + 1
   
    # stapFive
    stap_five = __stap_five(stap_four)
    # stapSix
    stap_six = __stap_six(stap_five)
    # stapSeven
    stap_seven = __stap_seven(stap_six)
    # stap_nine
    __stap_nine(stap_seven, account_runs)
    # stap_ten
    stap_ten = __stap_ten(stap_seven)
    # stap_eleven
    stap_eleven = __stap_eleven(stap_seven)

    function_value = stap_eleven[0].get_fun()
    if function_value == NUMBER_EXPECTED:
        break

print('finalizado com ', account_runs, ' épocas e valor da função encontrado ', function_value)

