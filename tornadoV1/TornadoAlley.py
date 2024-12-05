import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

# Titre de l'application
st.title("Calcul des coûts des vacances dans Tornado Alley")

# Entrées utilisateur dans la barre latérale
st.sidebar.header("Paramètres des coûts")
billet = st.sidebar.number_input("Prix du billet par personne (en €)", value=600, min_value=0)
location = st.sidebar.number_input("Prix location voiture par jour (en $)", value=40, min_value=0)
essence = st.sidebar.number_input("Prix essence par jour (en $)", value=50, min_value=0)
nourriture = st.sidebar.number_input("Prix de la nourriture par jour et par personne (en $)", value=20, min_value=0)
hotel = st.sidebar.number_input("Prix de la chambre d'hôtel par jour (en $)", value=50, min_value=0)
jours = st.sidebar.slider("Nombre de jours", min_value=1, max_value=42, value=28)
personnes = st.sidebar.slider("Nombre de personnes", min_value=1, max_value=5, value=3)
conversion = st.sidebar.number_input("Taux de conversion USD vers EUR", value=0.95, min_value=0.01)  # Changement ici

# Calculs nécessaires
location_euro = location / conversion
essence_euro = essence / conversion
nourriture_euro = nourriture / conversion
hotel_euro = hotel / conversion

cout_partage = (location_euro + essence_euro + hotel_euro) / personnes
jours_array = np.arange(1, jours + 1)
cout_total = billet + (cout_partage + nourriture_euro) * jours_array

# Affichage des résultats
st.write(
    f"Coût total des vacances par personne : **{round(cout_total[-1], 2)} €** "
    f"(si **{personnes}** personne(s) présente(s) durant **{jours}** jour(s))."
)

# Affichage du graphique
st.subheader("Graphique des coûts des vacances")
plt.figure(figsize=(10, 5))
plt.plot(jours_array, cout_total, marker='o', color='blue', linewidth=2)
plt.title(
    f"Coût des vacances par personne en fonction du nombre de jours\n"
    f"pour {personnes} personne(s)", fontsize=16
)
plt.xlabel("Nombre de jours", fontsize=12)
plt.ylabel("Coût total (en euros)", fontsize=12)
plt.ylim(0, max(cout_total) * 1.1)  # Ajuster l'échelle en fonction du coût maximum
plt.grid(True)
st.pyplot(plt)
