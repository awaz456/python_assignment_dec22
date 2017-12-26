def dic(n):

    i = 1
    dictionary = {}

    while(i<n+1):
        dictionary.update(
            {
                i : i**2
            }
        )
        i=i+1
        print (dictionary)

        n=int (input ("Enter value:"))

        dic(n)


