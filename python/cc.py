try:
   with open("a.txt","rb") as f:
       content=f.read().decode("utf-8")
except Exception as ret:
    print(ret)

print(eval(content)["aa"])
print(eval(content)["bb"])
