b = True
while b :
    a = input("Entrer un nombre  ")
    try:
        a = int(a)
    except ValueError:
        print("la valeur entrée n est pas un nombre")
    else :
        b = False

print(a)

