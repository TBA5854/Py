import pickle
with open('prac.dat','rb') as f:
    try:
        while True:
            i=pickle.load(f)
            print(i)
            if i['rno']=='2':
                print("hi")
    except Exception as e:
        print(e)
        pass