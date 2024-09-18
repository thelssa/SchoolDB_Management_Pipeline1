---
title: "Projet de Gestion des Élèves et Enseignants avec PostgreSQL et Python"
author:
  - Thelma LUM
date: "18/09/2024"
---

## Description du projet

Ce projet a pour objectif de créer une base de données pour gérer les élèves et enseignants d'une école, puis d'extraire, manipuler, et analyser les données à l'aide de Python. Le projet est divisé en deux grandes étapes :

1. **Création de la base de données** : Un fichier SQL est utilisé pour créer la base de données `Ecole`, ainsi que deux tables (`eleves` et `enseignants`) avec des données d'exemple.
2. **Extraction et analyse des données** : Un script Python est utilisé pour extraire les données des tables, associer les élèves à leurs enseignants selon le numéro de classe, et compter combien d'élèves chaque enseignant a sous sa responsabilité.

## Fichiers inclus

- `bd_ecole.sql` : Fichier SQL contenant les instructions pour créer la base de données, les tables, et insérer les données initiales (15 élèves et 6 enseignants).
- `data_automation.py` : Script Python permettant de se connecter à la base de données, d'extraire et d'analyser les données (association élèves-enseignants et comptage des élèves par enseignant).

## Prérequis

Avant de démarrer, assurez-vous d'avoir installé :

- **PostgreSQL** (Version 12 ou supérieure) pour gérer la base de données.
- **Python 3** et la bibliothèque **psycopg2** pour interagir avec PostgreSQL via Python. Pour installer `psycopg2`, exécutez la commande suivante :

  ```bash
  pip install psycopg2
  ```

## Étapes d'exécution

### 1. Créer la base de données et les tables

1. Ouvrez une invite de commande ou un terminal.
2. Assurez-vous que PostgreSQL est installé et que le service est en cours d'exécution.
3. Exécutez le fichier SQL pour créer la base de données et insérer les données d'exemple :

   ```bash
   psql -U postgres -f bd_ecole.sql
   ```

   Cette commande crée :
   - La base de données `ecole`.
   - Les tables `eleves` et `enseignants`.
   - Insère 15 élèves et 6 enseignants dans les tables respectives.

### 2. Exécuter le script Python pour l'extraction et l'analyse

1. Assurez-vous que les informations de connexion (nom d'utilisateur, mot de passe, port) dans le fichier `automate_pipeline.py` correspondent à votre configuration PostgreSQL.
2. Exécutez le script Python pour extraire et analyser les données :

   ```bash
   python data_automation.py
   ```

   Ce script :
   - Se connecte à la base de données `ecole`.
   - Extrait les données des tables `eleves` et `enseignants`.
   - Associe les élèves à leurs enseignants selon le numéro de classe.
   - Affiche combien d'élèves chaque enseignant a sous sa responsabilité.

### 3. Résultats

Le script Python affichera dans la console :
- Une liste d'élèves associée à leurs enseignants respectifs.
- Le nombre d'élèves pour chaque enseignant.

## Structure de la base de données

### Table `eleves`

| Colonne          | Type         | Description                           |
|------------------|--------------|---------------------------------------|
| `student_id`     | `SERIAL`     | Identifiant unique (clé primaire)     |
| `prenom`         | `VARCHAR(50)`| Prénom de l'élève                     |
| `nom`            | `VARCHAR(50)`| Nom de l'élève                        |
| `numero_salle`   | `INTEGER`    | Numéro de salle de l'élève            |
| `telephone`      | `VARCHAR(15)`| Numéro de téléphone de l'élève        |
| `email`          | `VARCHAR(100)`| Email de l'élève                      |
| `annee_obtention`| `INTEGER`    | Année d'obtention de diplôme          |
| `numero_classe`  | `INTEGER`    | Numéro de la classe de l'élève        |

### Table `enseignants`

| Colonne          | Type         | Description                           |
|------------------|--------------|---------------------------------------|
| `teacher_id`     | `SERIAL`     | Identifiant unique (clé primaire)     |
| `prenom`         | `VARCHAR(50)`| Prénom de l'enseignant                |
| `nom`            | `VARCHAR(50)`| Nom de l'enseignant                   |
| `numero_salle`   | `INTEGER`    | Numéro de salle de l'enseignant       |
| `departement`    | `VARCHAR(100)`| Département de l'enseignant           |
| `annee_obtention`| `INTEGER`    | Année d'obtention du diplôme          |
| `email`          | `VARCHAR(100)`| Email de l'enseignant                 |
| `telephone`      | `VARCHAR(15)`| Numéro de téléphone de l'enseignant   |
| `numero_classe`  | `INTEGER`    | Numéro de la classe de l'enseignant   |

## Personnalisation

Vous pouvez personnaliser le projet en modifiant :
- Les données insérées dans les tables (dans le fichier `bd_ecole.sql`).
- Le traitement des données dans le script Python (par exemple, ajouter des filtres ou des analyses supplémentaires).

## Dépendances

- **PostgreSQL** pour la gestion de la base de données.
- **Python** avec la bibliothèque **psycopg2** pour l'interaction avec la base de données.

