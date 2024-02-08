import numpy as np
from numpy.linalg import matrix_power
import random


matrice = np.array([[0.7 , 0.2 , 0.1],[0.5 , 0.3 , 0.2],[0.4 , 0.3 , 0.3]])
valeurs = ["E","N","P"]


def calcul(Etat_initial, nb_jour):


    matrice_puissance = matrix_power(matrice, nb_jour)

    if Etat_initial == "E":
        initial = np.array([1,0,0])
    elif Etat_initial == "N":
        initial = np.array([0,1,0])
    elif Etat_initial == "P":
        initial = np.array([0,0,1])
    else :
        print("l'etat initial invalide")



    res = np.dot(initial,matrice_puissance)

    return res

print(calcul("E",2))


def simulation(nb_jour):
    passage=[] 
    probabilité = []

    resultat = np.random.choice(valeurs, p=ponderations)

    for i in range(nb_jour):


