import pandas as pd
import random


start_date = '2024-01-01'
end_date = '2026-12-31'
num_dates = 500

random_dates = pd.date_range(start=start_date, end=end_date, freq='D').to_series().sample(num_dates)
print(random_dates)


sites = ["Bordeaux", "Tarnos", "Gennevilliers"]
composants = ["Nacelle", "Aube de turbine", "Harnais électrique"]
statuts = ["En cours", "Livré", "En retard"]

# Sélection aléatoire d'un élément
site_choisi = random.choices(sites, k=500)

composants_choisis= random.choices(composants, k=500)

status_choisis= random.choices(statuts, k=500)

quantite_produite = [random.randint(10, 50) for _ in range(500)]

quantite_defectueuse = [random.randint(0, 2) for _ in range(500)]

# Exemple de DataFrame
data = {
    "Site": site_choisi,
    "Composant": composants_choisis,
    "Statut": status_choisis,
    "Quantité produite": quantite_produite,
    "Quantité défectueuse": quantite_defectueuse,
    "Date": random_dates,
    "Temps fabrication": [random.randint(60, 4320) for _ in range(500)]
}


df = pd.DataFrame(data)

try:
  
    df.to_excel("export.xlsx", index=False)

    print("Export réussi : fichier 'export.xlsx' créé.")
except PermissionError:
    print("Erreur : le fichier est peut-être déjà ouvert. Fermez-le et réessayez.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")
