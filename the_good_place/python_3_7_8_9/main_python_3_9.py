import time


def new_dataclasses():
    # 3.7
    import math
    from dataclasses import dataclass

    @dataclass(init=True, repr=True, eq=True,
               order=False, unsafe_hash=False, frozen=False)
    class Circumference:
        radius: int
        diameter: float = None
        area: float = None

        def calculate_diameter(self):
            self.diameter = self.radius * 2

        def calculate_area(self):
            self.area = math.pi*math.sqrt(self.radius)

    circumference = Circumference(3)
    circumference.calculate_diameter()
    print(circumference.diameter)
    print(circumference.__repr__())
    circumference.calculate_area()

    from dataclasses import asdict

    print(asdict(circumference))



def breakpoint_use():
    # 3.7
    pass

def positional_only_arguments():
    # 3.8
    # print(help(float))

    def double(x):
        return x*2

    double(x=3)
    double(3)
    # works in both ways

    # after / only positional arguments
    def double_2(x, /):
        return x*2

    double_2(3)
    # double_2(x=3)  # this does not works

    def sum_values(value1, /, value2):
        return value1+value2

    sum_values(5,1)  # this works
    sum_values(4, value2=7)  # this works

    # sum_values(value1=2, value2=7)  # this does not work


    # keyword-only arguments already exists from python 3 and its using *
    def subtract_value(value_1, *, value_2):
        return value_1-value_2

    # subtract_value(1,2)  # this does not works
    subtract_value(value_1=1, value_2=2)  # this works
    subtract_value(1, value_2=2)  # this works

    # using both
    def multiply_three_values(value_1, /, value_2, *, value_3):
        ...
        return value_1*value_2*value_3

    multiply_three_values(3, value_2=5, value_3=2)
    multiply_three_values(3, 5, value_3=2)


    pass


def easy_debugging():
    # 3.8
    animal = 'cat'
    print(f'Hello, im a {animal}')
    print(f'Hello, im a {animal=}')
    print(f'Hello, im a {animal= :>20}')
    print(f'Hello, im a {animal.upper()=}')


def assignment_expressions():
    # 3.8
    for item in range(10):
        if (a := item+3) > 10:
            print(f'{a} is bigger than 10')

    # BE CAREFUL! here "a" is a bool, brackets are needed!
    for item in range(10):
        if a := item+3 > 10:
            print(f'{a} is bigger than 10')

    ######

    data = [25, 8, 4, 9, 3, 5, 9]
    results = [percentage for x in data 
               if (percentage := x/sum(data)*100) >= 10]
    print(results)

    # here, bool values will be appended, because the bracket is incorrect at the end
    results = [percentage for x in data if (percentage := x/sum(data)*100 >= 10)]


    ######
    from math import pi
    print(f"The radius of a circumference is {(radius:=3)}, its diameter is "
          f"{(diameter := radius*2)} and gives a circumference {pi * diameter}")
    # without brackets, for example, in radius:=3 we would obtain an error like:
    # NameError: name 'radius' is not defined

    print(results)


def remove_prefix_suffix():
    # python 3.9
    def remove_prefix(prefix: str, str_list: list[str]):
        return [item.removeprefix(prefix) for item in str_list]

    def remove_suffix(suffix: str, str_list: list[str]):
        return [item.removesuffix(suffix) for item in str_list]


    str_list = ['Hola Juan', 'Lucia que tal', 'Hola Pepa', 'Pedro que tal']
    print(remove_prefix(prefix='Hola ', str_list=str_list))
    print(remove_suffix(suffix=' que tal', str_list=str_list))


def a_random_function():
    # python 3.9
    def a_random_function(list_a: list[int] = None, dict_b: dict[str, int] = None):
        return list_a, dict_b

    a_random_function(list_a=['hello', 'my_friend'])
    a_random_function(list_a=[1, 2, 3])

    a_random_function(list_a=[1, 2, 3], dict_b={'hello': 1})
    a_random_function(list_a=[1, 2, 3], dict_b={'hello': 'my_friend'})
    
    a = list[int]
    a.append('hola')

    a_random_list: list[int] = []
    a_random_dict: dict[str: int] = {}

    a_random_list.append('hello')
    a_random_list.append(1)
    a_random_dict['hello'] = 1
    
    
    def shopping_function(things_to_buy, supermarket, product_codes):
        # do a lot of complicated things
        money = 0
        return money

    def shopping_function(things_to_buy: dict, supermarket: str, product_codes: list) -> float:
        # do a lot of complicated things
        money: float = 0.
        return money

    shopping_function(things_to_buy={'eggs': 12, 'milk': 6, 'tomatoes': 6},
                      supermarket='euromarket',
                      product_codes=[123456, 654321, 135642])

    def shopping_function(things_to_buy: dict[str, int], supermarket: str, product_codes: list[int]) -> float:
        # do a lot of complicated things
        money: float = 0.
        return money
    
    
    shopping_function(things_to_buy={'eggs': 'ten', 'milk': 'six', 'tomatoes': 'six'},
                      supermarket='euromarket',
                      product_codes=[123456, 654321, 135642])


def updating_merging_dictionaries():
    """
    How to update and union dictionaries
    """

    def merge_dictionaries(dict_list: list[dict]) -> dict:
        if len(dict_list) == 1:
            return dict_list[0]

        a = dict_list[0]
        for item in dict_list[1:]:
            a = a | item

        return a

    def update_dictionaries(dict_list: list[dict]) -> dict:
        if len(dict_list) == 1:
            return dict_list[0]

        a = dict_list[0]
        for item in dict_list[1:]:
             a |= item

        return a

    t = time.time()

    dict_1 = {'a': 1, 'b': 2}
    dict_2 = {'c': 3, 'd': 5, 'e': 6}
    dict_3 = {'a': 3, 'd': 5, 'e': 6}

    # merge operator: |

    print(merge_dictionaries([dict_1, dict_2]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}
    print(merge_dictionaries([dict_2, dict_1]))  # {'c': 3, 'd': 5, 'e': 6, 'a': 1, 'b': 2}

    print(merge_dictionaries([dict_1, dict_3]))  # {'a': 3, 'b': 2, 'd': 5, 'e': 6}
    print(merge_dictionaries([dict_3, dict_1]))  # {'a': 1, 'd': 5, 'e': 6, 'b': 2}

    # update dictionary performs the merge in-place: |=
    print(update_dictionaries([dict_1, dict_3]))  # {'a': 3, 'b': 2, 'd': 5, 'e': 6}
    print(time.time()-t)


def simonSays(f):
    def run ():
        print('Simon says')
        f()
    return run

@simonSays
def hello():
    print("hola")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_dataclasses()
    # positional_only_arguments()
    # easy_debugging()
    # assignment_expressions()
    # remove_prefix_suffix()
    # type_hints
    # updating_merging_dictionaries()

    print('hola')


    def shopping_function(things_to_buy: dict[str, int], supermarket: str,
                          product_codes: list[int]) -> float:
        # do a lot of complicated things
        money: float = 0.
        return money


    shopping_function(
        things_to_buy={'eggs': 'ten', 'milk': 'six', 'tomatoes': 'six'},
        supermarket='euromarket',
        product_codes=[123456, 654321, 135642])

