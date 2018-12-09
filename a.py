path='d:\\cd.txt'
try:
    with open(path,'r+') as f:
        for each_line in f:
            print(f)
except OSError as reason:
    print(reason)

