from random import choice
from string import ascii_lowercase as letters

list_of_domains = ['yaexample.com','goexample.com','example.com']

quotes = [  'My vision is augmented.',
            'Bravery is not a function of firepower.',
            'Im not big into books.',
            'When due process fails us, we really do live in a world of terror.']

def generate_name(length_of_name):
    return ''.join(choice(letters) for i in range(length_of_name))

def get_domain(list_of_domains):
    return choice(list_of_domains)

def get_quotes(list_of_quotes):
    return choice(list_of_quotes)

def generate_records(length_of_name, list_of_domains, total_records, list_of_quotes):
    with open("data.txt", "w") as to_write:
        for num in range(total_records):
            key = generate_name(length_of_name)+"@"+get_domain(list_of_domains)
            value = get_quotes(quotes)
            to_write.write(key + ":" + value + "\n")
        to_write.write("mashrur@example.com:Don't let me leave Murph\n")
        to_write.write("evgeny@example.com:All I do is win win win no matter what!\n")

generate_records(10, list_of_domains, 100000, quotes)