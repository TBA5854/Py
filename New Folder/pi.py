import pickle
with open('prac.dat','ab') as f:
    q={}
    rno=input('enter value')
    name=input('enter value')
    m1=input('enter value')
    m2=input('enter value')
    m3=input('enter value')
    q["rno"]=rno
    q["name"]=name
    q['m1']=m1
    q['m2']=m2
    q['m3']=m3
    pickle.dump(q,f)