import streamlit as st

# Configuration de la page pour forcer le mode clair
st.set_page_config(page_title="KFC Sénégal Menu", layout="wide")

# --- CSS POUR LE CONTRASTE ET LE STYLE ---
st.markdown("""
    <style>
    /* Forcer le fond de page en gris très clair pour faire ressortir les cartes */
    .stApp {
        background-color: #f8f9fa !important;
    }
    
    /* Cartes produits : fond blanc pur, texte noir pour un contraste 100% */
    .product-card {
        background-color: #ffffff;
        border: 2px solid #e4002b;
        padding: 15px;
        border-radius: 12px;
        text-align: center;
        margin-bottom: 20px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    .item-name {
        color: #000000 !important; /* Noir pur */
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: 10px;
    }
    
    .item-price {
        color: #e4002b !important; /* Rouge KFC */
        font-size: 1.4rem;
        font-weight: 900;
    }

    /* Style spécifique pour la section Boissons */
    .drink-section {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 15px;
        border-top: 5px solid #e4002b;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ENTÊTE ---
st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=100)
st.title("🔴 MENU KFC SEDIMA")

# --- SECTION 1 : LES PLATS (VOS LIENS) ---
st.header("🍗 NOS CATÉGORIES")
col1, col2 = st.columns(2)

categories = [
    {"n": "BURGERS", "p": "3000 F", "img": "https://kfcsenegal.sn/storage/50/categorie-photo-14-08-2023Gm0UZ1692023013.jpg"},
    {"n": "WINGS", "p": "3500 F", "img": "https://kfcsenegal.sn/storage/49/categorie-photo-14-08-20238CZyR1692024550.jpg"},
    {"n": "POULET", "p": "1500 F", "img": "https://kfcsenegal.sn/storage/48/categorie-photo-14-08-2023vVRNN1692022970.png"},
    {"n": "FRITES & ACCOMP.", "p": "1000 F", "img": "https://kfcsenegal.sn/storage/25/categorie-photo-14-08-2023yJlhj1692022268.jpg"}
]

for i, cat in enumerate(categories):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="product-card">
                <img src="{cat['img']}" style="width:100%; border-radius:8px;">
                <div class="item-name">{cat['n']}</div>
                <div class="item-price">{cat['p']}</div>
            </div>
        """, unsafe_allow_html=True)

# --- SECTION 2 : LES BOISSONS (AVEC PHOTOS) ---
st.markdown("---")
st.header("🥤 BOISSONS FRAÎCHES")

# Liens d'images directs pour les boissons
boissons = [
    {"n": "COCA-COLA", "p": "800 F", "img": "https://www.sn.coca-cola.com/content/dam/journey/sn/fr/brands/coca-cola/coca-cola-original-250ml.png"},
    {"n": "PEPSI", "p": "800 F", "img": "https://atlas-content-cdn.pixelsquid.com/stock-images/pepsi-soda-can-0mE0E67-600.jpg"},
    {"n": "7UP / SEVEN", "p": "800 F", "img": "https://www.7up.com/images/products/7up-can.png"}
]

b_col1, b_col2, b_col3 = st.columns(3)
cols = [b_col1, b_col2, b_col3]

for i, b in enumerate(boissons):
    with cols[i]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{b['img']}" style="height:150px; object-fit: contain;">
                <div class="item-name">{b['n']}</div>
                <div class="item-price">{b['p']}</div>
            </div>
        """, unsafe_allow_html=True)

# --- SOLUTION POUR LE "HORS-LIGNE" ---
st.sidebar.title("ℹ️ INFOS PRATIQUES")
st.sidebar.error("**PAS DE CONNEXION ?**")
st.sidebar.write("""
Si vous n'avez pas internet, demandez le **code Wi-Fi** du restaurant ou téléchargez le menu une fois pour toutes :
""")
st.sidebar.button("Télécharger le Menu PDF")
