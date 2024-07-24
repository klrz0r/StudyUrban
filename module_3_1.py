import random

calls = 0
def caunt_calls():
    global calls
    calls += 1

def string_info (string: str):
    caunt_calls()
    length = len(string)
    up = string.upper()
    down = string.lower()
    return (length, up, down)


def is_contains (string: str, list_to_search: list):
    caunt_calls()
    string = string.lower()
    for a in list_to_search:
        b = a.lower()
        if string == b:
           return True
    return False
a = random.randint(1,9)
for i in range(a):
    print(string_info('Capybara'))
    print(string_info('Armageddon'))
    print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
    print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls, a)