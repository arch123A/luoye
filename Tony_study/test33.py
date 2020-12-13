import pickle
import os

file_list=os.path.join("d:\\","test","namelist.pkl")
try:

    pf=open(file_list,'rb')
    ml=pickle.load(pf)
    print(ml)
    pf.close()
except:
    print("error!!")
ls2=list(range(1,41))
zt=dict(zip(ls2,ml))
print(zt)