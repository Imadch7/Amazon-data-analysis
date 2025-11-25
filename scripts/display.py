import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="whitegrid") 

class DataVisualizer:
    
    def __init__(self, filepath):
        self.filepath = filepath
        
    def load_data(self):
        try:
            df = pd.read_csv(self.filepath) 
            return df
        except FileNotFoundError:
            print(f"File not found: {self.filepath}")
            return None

    def visualize_rating_distribution(self, df):
        """Visualise la distribution des notes (rating)."""
        if df is None or 'rating' not in df.columns:
            print("Colonne 'rating' manquante ou données non chargées.")
            return
            
        plt.figure(figsize=(10, 6))
        sns.histplot(df['rating'].dropna(), bins=20, kde=True, color='skyblue')
        plt.title('1. Distribution des notes de produits (KDE)', fontsize=16)
        plt.xlabel('Note (Rating)', fontsize=12)
        plt.ylabel('Fréquence', fontsize=12)
        plt.show()

    def visualize_price_relationship(self, df):
        """Visualise la densité de la relation entre le prix réel et le prix remisé."""
        if df is None or 'actual_price' not in df.columns or 'discounted_price' not in df.columns:
            print("Colonnes de prix manquantes ou données non chargées.")
            return

        plt.figure(figsize=(10, 8))
        plt.hexbin(df['actual_price'], df['discounted_price'], 
                    gridsize=50, cmap='inferno', mincnt=1)
        plt.colorbar(label='Densité des produits')
        plt.title('2. Relation entre prix réel et prix remisé (Hexbin)', fontsize=16)
        plt.xlabel('Prix réel (Actual Price)', fontsize=12)
        plt.ylabel('Prix remisé (Discounted Price)', fontsize=12)
        plt.show()

    def visualize_top_products_by_count(self, df, top_n=15):
        """Visualise les top produits les plus vendus."""
        if df is None or 'product_name' not in df.columns or 'rating_count' not in df.columns:
            print("Colonnes 'product_name' ou 'rating_count' manquantes ou données non chargées.")
            return

        top_products = df.groupby('product_name')['rating_count'].sum().nlargest(top_n)

        plt.figure(figsize=(12, 8))
        sns.barplot(x=top_products.values, y=top_products.index, palette='crest')
        plt.title(f'3. Top {top_n} produits les plus notés/populaires', fontsize=16)
        plt.xlabel('Nombre Total de Notes (Rating Count)', fontsize=12)
        plt.ylabel('Nom du Produit', fontsize=12)
        plt.show()

if __name__ == "__main__":
    visualizer = DataVisualizer('cleaned_amazon_data.csv') 
    data = visualizer.load_data()
    if data is not None:
        #visualizer.visualize_rating_distribution(data)
        visualizer.visualize_price_relationship(data)
        #visualizer.visualize_top_products_by_count(data)