def a():
    x=10
    y=1
    while True:
        try:
            x-=1
            y+=1
            z=y/x
            print(x)
            print(y)
            print(z)
        except:
            print("catch error, reset x")
            x=10

a()

