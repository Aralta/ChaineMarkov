import numpy as np
from numpy.linalg import matrix_power
import random


matrice = np.array([[0.7 , 0.2 , 0.1],[0.5 , 0.3 , 0.2],[0.4 , 0.3 , 0.3]])


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

    actuel = "N"
    passage.append(actuel)
    probabilité.append(1)

    for i in range(nb_jour):
        actuel = passage[i]
        if actuel=="E":
            valeurs = ["E","N","P"]
            proba = matrice[0]
            suivant = np.random.choice(valeurs, p=matrice[0])
            passage.append(suivant)
            if suivant=="E":
                probabilité.append(proba[0])
            elif suivant=="N":
                probabilité.append(proba[1])
            elif suivant=="P":
                probabilité.append(proba[2])

            

        elif actuel=="N":
            valeurs = ["E","N","P"]
            proba = matrice[1]
            suivant = np.random.choice(valeurs, p=proba)
            passage.append(suivant)
            if suivant=="E":
                probabilité.append(proba[0])
            elif suivant=="N":
                probabilité.append(proba[1])
            elif suivant=="P":
                probabilité.append(proba[2])

        elif actuel=="P":
            valeurs = ["E","N","P"]
            proba = matrice[2]
            suivant = np.random.choice(valeurs, p=proba)
            passage.append(suivant)
            if suivant=="E":
                probabilité.append(proba[0])
            elif suivant=="N":
                probabilité.append(proba[1])
            elif suivant=="P":
                probabilité.append(proba[2])

    return passage,probabilité

print(simulation(3))
