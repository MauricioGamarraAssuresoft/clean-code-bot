def proc(n, t, d):
    # n es el nombre, t es el total, d es si tiene descuento
    if d == True:
        res = t * 0.90
    else:
        res = t
    
    # Add tax
    f = res * 1.15
    
    # Print and save
    print("Loading...")
    print("Client: " + n)
    print("Final: " + str(f))
    
    file = open("data.txt", "w")
    file.write("User: " + n + " Total: " + str(f))
    file.close()
    
    return f

v = proc("Juan Perez", 100, True)
