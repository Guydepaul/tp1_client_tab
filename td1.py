import sqlite3

# Création d'une connexion à la base de données SQLite
conn = sqlite3.connect('salaires.db')
cur = conn.cursor()
# Création d'une table pour stocker les données des utilisateurs
conn.execute('''CREATE TABLE IF NOT EXISTS utilisateurs
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nom TEXT,
                salaire REAL)''')

# Demande le nom et le salaire de l'utilisateur
nom = input("Entrez votre nom : ")
salaire = float(input("Entrez votre salaire : "))

# Insère les données de l'utilisateur dans la table
conn.execute("INSERT INTO utilisateurs (nom, salaire) VALUES (?, ?)", (nom, salaire))
conn.commit()

# Demande à l'utilisateur s'il souhaite voir le tableau de salaires triés
reponse = input("Voulez-vous voir un tableau de salaires triés du plus grand au plus petit ? (oui/non) ")

# Si l'utilisateur répond "oui", affiche le tableau de salaires triés
if reponse.lower() == "oui":
    # Récupère les salaires depuis la base de données
    resultats = conn.execute("SELECT nom, salaire FROM utilisateurs ORDER BY salaire DESC")

    # Affiche le tableau de salaires triés
    print("Tableau de salaires triés du plus grand au plus petit :")
    for row in resultats:
        print(f"NOM : {row[0]}, SALAIRE : {row[1]}")
        print("________________________________")
else:
    # Affiche un message de remerciement si l'utilisateur répond "non"
    print("Merci !")

# Ferme la connexion à la base de données
conn.close()
