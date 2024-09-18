#Thelma LUM

import psycopg2

def connect_to_db():
    """Connexion à la base de données PostgreSQL"""
    return psycopg2.connect(
        dbname="ecole", 
        user="postgres", 
        password="1994", 
        host="localhost", 
        port="5433"
    )

def extract_data(cur):
    """Extraction des données des tables"""
    # Extraire les élèves
    cur.execute("SELECT * FROM eleves;")
    eleves = cur.fetchall()

    # Extraire les enseignants
    cur.execute("SELECT * FROM enseignants;")
    enseignants = cur.fetchall()

    return eleves, enseignants

def associate_students_teachers(eleves, enseignants):
    """Associer chaque élève à son enseignant"""
    print("\nAssociations élèves-enseignants :")
    for eleve in eleves:
        for enseignant in enseignants:
            if eleve[7] == enseignant[8]:  # Comparer le numero_classe
                print(f"Élève: {eleve[1]} {eleve[2]} -> Enseignant: {enseignant[1]} {enseignant[2]}")

def count_students_per_teacher(eleves, enseignants):
    """Compter le nombre d'élèves par enseignant"""
    eleves_par_enseignant = {enseignant[1] + " " + enseignant[2]: 0 for enseignant in enseignants}

    for eleve in eleves:
        for enseignant in enseignants:
            if eleve[7] == enseignant[8]:  # Si les numéros de classe correspondent
                eleves_par_enseignant[enseignant[1] + " " + enseignant[2]] += 1

    print("\nNombre d'élèves par enseignant :")
    for enseignant, count in eleves_par_enseignant.items():
        print(f"{enseignant} : {count} élève(s)")

def main():
    # Connexion à la base de données
    conn = connect_to_db()
    cur = conn.cursor()

    # Extraire les données
    eleves, enseignants = extract_data(cur)

    # Associer les élèves aux enseignants
    associate_students_teachers(eleves, enseignants)

    # Compter les élèves par enseignant
    count_students_per_teacher(eleves, enseignants)

    # Fermer la connexion
    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
