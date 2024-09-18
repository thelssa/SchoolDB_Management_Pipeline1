
-- Création de la base de données
CREATE DATABASE Ecole;

-- Utiliser la base de données Ecole
\c Ecole;

-- Création de la table 'eleves'
CREATE TABLE eleves (
    student_id SERIAL PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INTEGER NOT NULL,
    telephone VARCHAR(15) UNIQUE NOT NULL,
    email VARCHAR(100) UNIQUE,
    annee_obtention INTEGER,
    numero_classe INTEGER NOT NULL
);

-- Créer la table 'enseignants'
CREATE TABLE enseignants (
    teacher_id SERIAL PRIMARY KEY,
    prenom VARCHAR(50) NOT NULL,
    nom VARCHAR(50) NOT NULL,
    numero_salle INTEGER NOT NULL,
    departement VARCHAR(100) NOT NULL,
    annee_obtention INTEGER,
    email VARCHAR(100) UNIQUE NOT NULL,
    telephone VARCHAR(15) UNIQUE NOT NULL,
    numero_classe INTEGER NOT NULL
);

-- Insertion d'un élève
INSERT INTO eleves (prenom, nom, numero_salle, telephone, email, annee_obtention, numero_classe)
VALUES ('Mark', 'Watney', 101, '777-555-1234', NULL, 2035, 5);

-- Insertion d'un enseignant
INSERT INTO enseignants (prenom, nom, numero_salle, departement, annee_obtention, email, telephone, numero_classe)
VALUES ('Jonas', 'Salk', 102, 'Biologie', 1955, 'jsalk@school.org', '777-555-4321', 5);
