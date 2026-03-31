import streamlit as st

# Configuration de la page
st.set_page_config(page_title="KFC Sénégal - Smart Menu", layout="wide", page_icon="🍗")

# --- STYLE CSS POUR LE CONTRASTE ET LE LOOK KFC ---
# On force le mode clair, le fond blanc, et le texte noir/rouge pour un contraste maximum
st.markdown("""
    <style>
    /* Forcer le fond blanc sur toute l'application */
    .stApp {
        background-color: #ffffff !important;
        color: #000000 !important;
    }
    
    /* Style des titres KFC (Rouge sur Blanc) */
    h1, h2, h3 {
        color: #e4002b !important;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
        margin-bottom: 15px;
    }

    /* Cartes produits : fond blanc, bordure rouge douce */
    .product-card {
        background-color: #ffffff;
        border: 1px solid #eeeeee;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        transition: 0.3s;
    }
    
    .product-card:hover {
        box-shadow: 0 10px 20px rgba(228, 0, 43, 0.1);
        border-color: #e4002b;
    }

    /* Nom du produit : Noir profond pour la lisibilité */
    .item-name {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.3rem;
        margin-top: 15px;
        margin-bottom: 5px;
    }
    
    /* Prix : Rouge KFC bien visible */
    .item-price {
        color: #e4002b !important;
        font-size: 1.5rem;
        font-weight: 900;
        margin-bottom: 15px;
    }

    /* Bouton "Ajouter" Rouge KFC */
    div.stButton > button:first-child {
        background-color: #e4002b;
        color: white;
        border: none;
        width: 100%;
        border-radius: 8px;
        font-weight: bold;
        padding: 10px;
    }
    
    /* Section Boissons : Texte noir sur fond blanc */
    .drink-text {
        color: #000000 !important;
        font-size: 1.1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE AVEC LOGO ---
st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=120)
st.title("🔴 MENU KFC SEDIMA")
st.markdown("### LE GOÛT ORIGINAL EST ICI, AU SÉNÉGAL !")
st.divider()

# --- DONNÉES DU MENU (Vos liens officiels + Noms corrigés) ---
# J'ai remis les bons noms en face des bonnes images selon votre photo.
menu_items = [
    {
        "titre": "A LA CARTE", # Correspond à l'image du poulet seul
        "img": "https://kfcsenegal.sn/storage/48/categorie-photo-14-08-2023vVRNN1692022970.png",
        "prix": "1500 F"
    },
    {
        "titre": "NOS WINGS", # Correspond à l'image des ailes épicées
        "img": "https://kfcsenegal.sn/storage/49/categorie-photo-14-08-20238CZyR1692024550.jpg",
        "prix": "3500 F"
    },
    {
        "titre": "NOS BURGERS", # Correspond à l'image du Zinger/Colonel
        "img": "https://kfcsenegal.sn/storage/50/categorie-photo-14-08-2023Gm0UZ1692023013.jpg",
        "prix": "3000 F"
    },
    {
        "titre": "NOS BOISSONS & ACCOMP.", # Correspond à l'image des frites/boissons
        "img": "https://kfcsenegal.sn/storage/25/categorie-photo-14-08-2023yJlhj1692022268.jpg",
        "prix": "800 F"
    }
]

# --- AFFICHAGE EN GRILLE (2 colonnes pour mobile-first) ---
col1, col2 = st.columns(2, gap="medium")

for i, item in enumerate(menu_items):
    current_col = col1 if i % 2 == 0 else col2
    with current_col:
        st.markdown(f"""
            <div class="product-card">
                <img src="{item['img']}" style="width:100%; border-radius:10px;">
                <div class="item-name">{item['titre']}</div>
                <div class="item-price">{item['prix']} <small>CFA</small></div>
            </div>
        """, unsafe_allow_html=True)
        # Bouton factice pour la démo
        if st.button(f"COMMANDER {item['titre']}", key=f"btn_{i}"):
            st.success(f"Ajout de {item['titre']} au panier !")

# --- SECTION BOISSONS DÉTAILLÉE (Avec vos nouveaux liens) ---
st.divider()
st.header("🥤 NOS BOISSONS FRAÎCHES")

col_b1, col_b2, col_b3 = st.columns(3)

# Boisson 1 : 7Up (Votre nouveau lien)
with col_b1:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://www.edenpizza.fr/wp-content/uploads/2019/11/7up-33cl.png" style="height:150px; object-fit: contain;">
            <div class="item-name">7UP / SEVEN</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)
    if not st.image("https://www.edenpizza.fr/wp-content/uploads/2019/11/7up-33cl.png", width=1): # Hack pour tester le chargement
        st.caption("7Up 33cl")

# Boisson 2 : Coca-Cola (Votre nouveau lien)
with col_b2:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://www.23pizzastreet.com/web/cache/images/product/6d1696bee7835dd96f75f90fc20b01bf-gfgdf-368.png" style="height:150px; object-fit: contain;">
            <div class="item-name">COCA-COLA</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)
    if not st.image("https://www.23pizzastreet.com/web/cache/images/product/6d1696bee7835dd96f75f90fc20b01bf-gfgdf-368.png", width=1):
        st.caption("Coca-Cola 33cl")

# Boisson 3 : Autre/Eau (Par défaut)
with col_b3:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://www.sn.coca-cola.com/content/dam/journey/sn/fr/brands/coca-cola/coca-cola-original-250ml.png" style="height:150px; object-fit: contain; filter: grayscale(100%);">
            <div class="item-name">AUTRES BOISSONS</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)
    st.caption("Pepsi, Eau, Fanta...")

# --- BARRE LATÉRALE (SIDEBAR) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=60)
    st.header("🛒 MON PANIER")
    st.write("Votre panier est vide pour le moment.")
    st.divider()
    st.warning("📶 Pas de connexion ?")
    st.write("Les prix affichés ici sont garantis en caisse du restaurant SEDIMA.")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("<p style='text-align: center; color: #666;'>KFC Sénégal © 2026 - SEDIMA Group. Déployé sur Streamlit Cloud.</p>", unsafe_allow_html=True)
