def func(x):
     return x.upper()

x = " "
while (x):
    x = input("Enter Word: ")
    if (x is None):
        break
    else:
         print(func(x))
