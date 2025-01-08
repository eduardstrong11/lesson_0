import re

string = 'bobbyhadz.com'

match = re.search(r'\.com$', string)
print(match)

