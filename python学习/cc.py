import re
line = "Cats are smarter than dogs"
s= re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
print(s.group())
print(s.groupdict())
print(s.group(1))
print(s.group(2))
print(s.groups())