import random

def Willy():
    list_a1 = []
    for a1 in range(38):
        list_a1.append(a1+1)

    print("First Area:")
    k=1
    for i in range(38):
        random.shuffle(list_a1)
        if i+1 >= 33:             
            print("第{}個號碼: {}".format(k,list_a1.pop()))
            k=k+1

    list_a2 = []
    for a2 in range(8):
        list_a2.append(a2+1)

    for i in range(8):
        random.shuffle(list_a2)
        if i+1==8:
            print("Second Area: {}".format(list_a2.pop()))

def Big():
    list_a1 = []
    for a1 in range(49):
        list_a1.append(a1+1)

    print("Random Result:")
    for i in range(6):
        random.shuffle(list_a1)
        print("第{}個號碼: {}".format(i+1,list_a1.pop()))

def Five39():
    list_a1 = []
    for a1 in range(39):
        list_a1.append(a1+1)

    print("Random Result:")
    for i in range(5):
        random.shuffle(list_a1)
        print("第{}個號碼: {}".format(i+1,list_a1.pop()))            

print("Willy input 1, Big input 2, 539 input 3 !!")
x = input()

if x=="1":
    Willy()
elif x=="2":
    Big()
elif x=="3":
    Five39()

