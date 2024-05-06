#Description de la fonction:
        #Calcule le factoriel d'un nombre donné en utilisant la récursivité.
        
    #Paramètres:
        #n (int): Le nombre entier pour lequel le factoriel doit être calculé.
        
    #Retours:
        #int: Le factoriel du nombre n.
#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

f = factorial(int(sys.argv[1]))
print(f)
