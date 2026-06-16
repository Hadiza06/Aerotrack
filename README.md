# AeroTrack

## Dashboard KPI pour la production aéronautique

---

## Présentation

AeroTrack est un projet de simulation de suivi de production dans le secteur aéronautique.  
Il permet de générer des données réalistes et de les analyser via un dashboard interactif développé sous Power BI.

L’objectif est de reproduire un environnement industriel afin de suivre la performance d’une chaîne de production et d’identifier les axes d’amélioration grâce aux KPI.

---

## Objectif du projet

**Simuler une chaîne de production aéronautique et analyser ses performances via des indicateurs clés de performance (KPI).**

---

## Stack technique

- Python (pandas, random) : génération des données simulées  
- Power BI Desktop : création du dashboard interactif  
- DAX : calcul des mesures et KPI  

---

## KPI suivis

- Quantité produite  
- Taux de défaut (%)  
- Temps moyen de fabrication  
- Backlog des commandes  

---

## Structure du projet

```text
AeroTrack/
│
├── generate_data.py      # Génération des données
├── export.xlsx           # Dataset produit
├── AeroTrack.pbix        # Dashboard Power BI
└── README.md             # Documentation

## Utilisation

1. Installer les dépendances :
pip install pandas openpyxl

2. Générer les données :
python generate_data.py

3. Étapes dans Power BI :
Ouvrir le fichier : export.xlsx
Charger les données dans Power BI Desktop
Explorer le dashboard