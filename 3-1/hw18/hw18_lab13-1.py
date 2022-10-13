def tower(n, source, destination, auxilliary):
    if n==1:
        print("Move disk 1 form source", source, "to destination", destination)
        return 
    tower(n-1, source, auxilliary, destination)
    print("move disk", n, "from source", source, "to destination", destination)
    tower(n-1,auxilliary, destination, source)

n=4
tower(n,'A','B','C')
