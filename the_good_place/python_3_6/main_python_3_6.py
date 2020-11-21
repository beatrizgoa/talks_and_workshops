import time


def new_dataclasses():
    import math

    class Circumference:
        def __init__(self, radius=2, diameter=None):
            self.radius = radius
            self.diameter = diameter
            self.area = None

        def __repr__(self):
            return f'Radius: {self.radius}. Diameter: {self.diameter}'

        def calculate_diameter(self):
            self.diameter = self.radius * 2

        def calculate_area(self):
            self.area = math.pi*math.sqrt(self.radius)

    circumference = Circumference(radius=3)
    circumference.calculate_diameter()
    print(circumference.diameter)
    circumference.__repr__()
    circumference.calculate_area()


def breakpoint_use():
    pass


def positional_only_arguments():
    # print(help(float))  # the same as python 3.9

    pass


def easy_debugging():
    # 3.8
    animal = 'cat'
    print(f'Hello, im a animal={animal}')
    print(f'Hello, im a animal={animal :>20}')


def assignment_expressions():
    for item in range(10):
        a = item+3
        if a > 10:
            print(f'{a} is bigger than 10')

    #####
    data = [25, 8, 4, 9, 3, 5, 9]
    results = [x/sum(data)*100
               for x in data if x/sum(data)*100 >= 10]
    print(results)

    ######
    from math import pi
    radius = 3.
    diameter = radius*2
    print(f"The radius of a cincunference is {radius},"
          f" its diameter is {diameter} "
          f"and gives a circumference {pi * diameter}")


def remove_prefix_suffix():
    def remove_prefix(prefix: str, str_list: list):
        return [item[len(prefix):]
                if item.startswith(prefix) else item
                for item in str_list]

    def remove_suffix(suffix: str, str_list: list):
        return [item[:-len(suffix)] if item.endswith(suffix) else item
                for item in str_list]


    str_list = ['Hola Juan', 'Lucia que tal', 'Hola Pepa', 'Pedro que tal']
    print(remove_prefix(prefix='Hola ', str_list=str_list))
    print(remove_suffix(suffix=' que tal', str_list=str_list))


def type_hints():
    def a_random_function(list_a: list = None, dict_b: dict = None):
        return list_a, dict_b

    a_random_list: list = []
    a_random_dict: dict = {}

    a_random_list.append('hello')
    a_random_list.append(1)
    a_random_dict['hello'] = 1

    a_random_function()


def updating_merging_dictionaries():
    """
    How to update and union dictionaries
    """

    def merge_dictionaries(dict_list: list) -> dict:
        if len(dict_list) == 1:
            return dict_list[0]

        a = dict_list[0]
        for item in dict_list[1:]:
            a = {**a, **item}

        return a

    def update_dictionaries(dict_list: list) -> dict:
        if len(dict_list) == 1:
            return dict_list[0]

        a = dict_list[0]
        for item in dict_list[1:]:
            a.update(item)

        return a

    t = time.time()

    dict_1 = {'a': 1, 'b': 2}
    dict_2 = {'c': 3, 'd': 5, 'e': 6}
    dict_3 = {'a': 3, 'd': 5, 'e': 6}

    # merge
    print(merge_dictionaries([dict_1, dict_2]))  # {'a': 1, 'b': 2, 'c': 3, 'd': 5, 'e': 6}
    print(merge_dictionaries([dict_2, dict_1]))  # {'c': 3, 'd': 5, 'e': 6, 'a': 1, 'b': 2}

    print(merge_dictionaries([dict_1, dict_3]))  # {'a': 3, 'b': 2, 'd': 5, 'e': 6}
    print(merge_dictionaries([dict_3, dict_1]))  # {'a': 1, 'd': 5, 'e': 6, 'b': 2}

    # update dictionary
    print(update_dictionaries([dict_1, dict_3]))
    print(time.time()-t)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    new_dataclasses()
    # positional_only_arguments()
    # easy_debugging()
    # assignment_expressions()
    # remove_prefix_suffix()
    # type_hints()
    # updating_merging_dictionaries()

    print('hola')

