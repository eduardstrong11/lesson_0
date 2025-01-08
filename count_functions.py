calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())
def is_contains(string, list_to_search):
    count_calls()
    if string.upper in list_to_search.upper: # return string.upper() in [s.upper() for s in list_to_search]
        return True #НЕ СОВСЕМ понятно как указать наличие строки в списке!
    else:
        return False
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)

#print(string_info('Eduard'))
#print(is_contains('Eduard','Eduard'))
