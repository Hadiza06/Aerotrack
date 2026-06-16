# ✈️ AeroTrack — Dashboard KPI Production Aéronautique

## Objectif
Simuler le suivi d'une chaîne de production aéronautique 
via un dashboard Power BI interactif.

## Stack
- Python (pandas, random) — génération des données
- Power BI Desktop — visualisation
- DAX — calcul des mesures

## KPI suivis
- Quantité produite
- Taux de défaut (%)
- Temps moyen de fabrication (min)
- Backlog commandes

## Structure
AeroTrack/
├── generate_data.py  # Script de génération des données
├── export.xlsx       # Dataset généré
└── AeroTrack.pbix    # Dashboard Power BI
