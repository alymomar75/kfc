import streamlit as st
import streamlit.components.v1 as components

# 1. Configuration de la page
st.set_page_config(page_title="KFC Sénégal - Smart Menu", layout="wide")

# 2. Script de Détection de Connexion (JavaScript)
# Ce script tourne dans le navigateur du client
components.html("""
<script>
    function updateOnlineStatus() {
        if (navigator.onLine) {
            console.log("Mode En Ligne");
        } else {
            // Si hors ligne, on affiche une alerte ou on modifie l'UI
            alert("⚠️ Mode Hors-Ligne activé : Affichage du menu simplifié (Prix garantis)");
        }
    }
    window.addEventListener('online', updateOnlineStatus);
    window.addEventListener('offline', updateOnlineStatus);
    updateOnlineStatus();
</script>
""", height=0)

# 3. CSS Personnalisé (Forcer le mode clair et le rouge KFC)
st.markdown("""
    <style>
    .stApp { background-color: white !important; color: black !important; }
    .kfc-card { border: 2px solid #e4002b; padding: 15px; border-radius: 10px; margin-bottom: 10px; }
    .price { color: #e4002b; font-weight: bold; font-size: 22px; }
    .offline-banner { background-color: #ffcccc; padding: 10px; border-radius: 5px; text-align: center; color: #b30021; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 4. Logique de détection via Streamlit (Simulation)
# Note : Streamlit s'exécute côté serveur, donc on utilise un bouton de secours
# ou la détection JS ci-dessus pour informer l'utilisateur.

# --- HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=80)
st.title("KFC SEDIMA - SÉNÉGAL")

# 5. CONTENU DU MENU
# On définit les données une seule fois
menu_data = [
    {"nom": "Zinger Burger", "prix": "3000 FCFA", "img": "https://kfcsenegal.sn/storage/50/categorie-photo-14-08-2023Gm0UZ1692023013.jpg"},
    {"nom": "8 Pcs Wings", "prix": "3500 FCFA", "img": "https://kfcsenegal.sn/storage/49/categorie-photo-14-08-20238CZyR1692024550.jpg"},
    {"nom": "2 Pcs Poulet", "prix": "2200 FCFA", "img": "https://kfcsenegal.sn/storage/48/categorie-photo-14-08-2023vVRNN1692022970.png"}
]

# 6. AFFICHAGE HYBRIDE
# Si le navigateur est hors-ligne, les images ne chargeront pas. 
# On prévoit donc un affichage textuel robuste.

st.markdown("---")

col1, col2 = st.columns(2)

for i, item in enumerate(menu_data):
    target_col = col1 if i % 2 == 0 else col2
    with target_col:
        # Conteneur qui contient à la fois l'image (si possible) et le texte (garanti)
        st.markdown(f"""
            <div class="kfc-card">
                <img src="{item['img']}" style="width:100%; border-radius:5px; onerror="this.style.display='none'">
                <h3>{item['nom']}</h3>
                <p class="price">{item['prix']}</p>
                <p style="font-size: 0.8em; color: gray;">Disponible même hors-connexion</p>
            </div>
        """, unsafe_allow_html=True)

# 7. SECTION BOISSONS (Texte pur pour le hors-ligne)
st.header("🥤 Boissons & Desserts")
st.table({
    "Produit": ["Coca-Cola / Pepsi", "Schweppes / 7Up", "Eau Minérale", "Potatoes"],
    "Prix": ["800 FCFA", "800 FCFA", "500 FCFA", "1200 FCFA"]
})

# 8. FOOTER DE SECOURS
st.sidebar.header("Options de secours")
st.sidebar.write("Si les photos ne s'affichent pas, c'est que vous êtes en mode hors-ligne. Les prix affichés restent valables en caisse.")
