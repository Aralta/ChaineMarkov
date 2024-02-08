# ChaineMarkov

Imaginez un système de météo composé de trois états possibles : "Ensoleillé" (E), "Nuageux" (N), et "Pluvieux" (P). La transition entre ces états se fait selon les probabilités suivantes :
- S'il fait "Ensoleillé", il y a 70% de chance que le lendemain soit également "Ensoleillé", 20% de chance que ce soit "Nuageux", et 10% de chance que ce soit "Pluvieux".
- S'il fait "Nuageux", il y a 50% de chance que le lendemain soit "Ensoleillé", 30% de chance que ce soit "Nuageux", et 20% de chance que ce soit "Pluvieux".
- S'il fait "Pluvieux", il y a 40% de chance que le lendemain soit "Ensoleillé", 30% de chance que ce soit "Nuageux", et 30% de chance que ce soit "Pluvieux".

- Utilisez Python pour effectuer les calculs suivants :
- État Initial: Supposons que le système commence par être "Ensoleillé". Calculez la probabilité qu'il fasse "Ensoleillé", "Nuageux", et "Pluvieux" après 2 jours.
- Évolution Temporelle: Écrivez une fonction Python qui simule l'évolution du système pour n jours, en commençant par un état initial donné. Utilisez cette fonction pour simuler l'évolution du système pendant 5 jours, en partant de l'état "Nuageux".
- Probabilité Stationnaire: Calculez la probabilité stationnaire du système en utilisant la méthode de puissance itérative.
N'hésitez pas à utiliser des fonctions et des bibliothèques Python (par exemple, NumPy) pour faciliter les calculs.
Conseil: Utilisez une matrice de transition pour représenter les probabilités de transition entre les états. Utilisez la multiplication matricielle pour calculer les probabilités d'états après plusieurs jours.
