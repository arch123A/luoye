import re
line = "Cats are smarter than dogs"
# s= re.search( r'(.*) are (.*?) .*', line, re.M|re.I)
a="GET /asasas HTTP/1.1"
s=re.search(r'[^/]+(/[^ ]+?) ',a)
print(s.group())
print(s.groupdict())
print(s.group(1))
# print(s.group(2))
print(s.groups())