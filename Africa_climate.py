import pandas as pd
import matplotlib.pyplot as plt
          # Étape 1 : Charger l'ensemble de données
df = pd.read_csv('Africa_climate_change.csv')
   # Convertir la colonne DATE au format datetime en incluant l'heure
df['DATE'] = pd.to_datetime(df['DATE'], format='%Y%m%d %H%M%S')
   # Vérifier que la conversion a réussi
print(df['DATE'].head())
          # Étape 2 : Nettoyer les données
print(df.describe())
print(df.isnull().sum())
   # Remplir les valeurs manquantes par la moyenne de chaque colonne
df['PRCP'] = df['PRCP'].fillna(df['PRCP'].mean())
df['TAVG'] = df['TAVG'].fillna(df['TAVG'].mean())
df['TMAX'] = df['TMAX'].fillna(df['TMAX'].mean())
df['TMIN'] = df['TMIN'].fillna(df['TMIN'].mean())
   # Sauvegarder les données nettoyées
df.to_csv('Clean_Africa_climate_change.csv')
          # Étape 3 : Tracer un graphique linéaire pour la Tunisie et le Cameroun
   # Filtrer les données pour la Tunisie et le Cameroun
tunisia = df[df['COUNTRY'] == 'Tunisia']
cameroon = df[df['COUNTRY'] == 'Cameroon']
   # Calculer les moyennes quotidiennes des températures
tunisia_mean = tunisia.groupby('DATE')['TAVG'].mean()
cameroon_mean = cameroon.groupby('DATE')['TAVG'].mean()
   # Tracer le graphique linéaire
plt.figure(figsize=(10, 5))
plt.plot(tunisia_mean, label='Tunisia')
plt.plot(cameroon_mean, label='Cameroon')
plt.title('Fluctuations Moyennes de la Température (1980-2023)')
plt.xlabel('Année')
plt.ylabel('Température Moyenne')
plt.legend()
plt.show()
          # Étape 4 : Zoomer sur les années 1980 à 2005
   # Filtrer les données entre 1980 et 2005
tunisia_zoom = tunisia[(tunisia['DATE'] >= '1980-01-01') & (tunisia['DATE'] <= '2005-12-31')]
cameroon_zoom = cameroon[(cameroon['DATE'] >= '1980-01-01') & (cameroon['DATE'] <= '2005-12-31')]

tunisia_mean_zoom = tunisia_zoom.groupby('DATE')['TAVG'].mean()
cameroon_mean_zoom = cameroon_zoom.groupby('DATE')['TAVG'].mean()
   # Tracer le graphique linéaire avec zoom
plt.figure(figsize=(10, 5))
plt.plot(tunisia_mean_zoom, label='Tunisia')
plt.plot(cameroon_mean_zoom, label='Cameroon')
plt.title('Fluctuations Moyennes de la Température (1980-2005)')
plt.xlabel('Année')
plt.ylabel('Température Moyenne')
plt.legend()
plt.show()
          # Étape 5 : Créer des histogrammes pour le Sénégal
   # Filtrer les données pour le Sénégal
senegal = df[df['COUNTRY'] == 'Senegal']
   # Séparer les données en deux périodes
senegal_1980_2000 = senegal[(senegal['DATE'] >= '1980-01-01') & (senegal['DATE'] <= '2000-12-31')]
senegal_2000_2023 = senegal[(senegal['DATE'] >= '2000-01-01') & (senegal['DATE'] <= '2023-12-31')]
   # Créer des histogrammes
plt.figure(figsize=(10, 5))
plt.hist(senegal_1980_2000['TAVG'], bins=20, alpha=0.5, label='1980-2000')
plt.hist(senegal_2000_2023['TAVG'], bins=20, alpha=0.5, label='2000-2023')
plt.title('Distribution de la Température au Sénégal')
plt.xlabel('Température')
plt.ylabel('Fréquence')
plt.legend()
plt.show()
           # Étape 6 : Sélectionner le meilleur graphique
   # Calculer la température moyenne par pays
average_temp_by_country = df.groupby('COUNTRY')['TAVG'].mean()
   # Tracer un graphique à barres
plt.figure(figsize=(10, 5))
average_temp_by_country.plot(kind='bar')
plt.title('Température Moyenne par Pays')
plt.xlabel('Pays')
plt.legend()
plt.show()