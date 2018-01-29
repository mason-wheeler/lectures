import string
def get_personal_data() -> dict:
    '''
    :return: Returns a dictionary of personal information.
    '''
    personal_data = {"name": "Mason", "a_role": "student"}
    return personal_data


def main() -> int:
    default_dict = dict()
    print(default_dict)
    initailized_dict = dict([('name', 'Mason'), ('a_role', 'joker')])
    print(initailized_dict)
    simple_int_dict = dict(name='Mason', a_role='student')
    print(simple_int_dict)
    simple_int_dict['a_role'] = 'joker'
    print(simple_int_dict)
    my_comprehension = {x: x**2 for x in range(5)}
    print(my_comprehension)

    print(string.punctuation)
    s = "a little lamb, it's fleece".translate({ord(i): None for i in string.punctuation})
    s = s.split()
    print(s)
    return 0


if __name__ == '__main__':
    main()
