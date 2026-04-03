import streamlit as st

# Configuration de la page
st.set_page_config(page_title="KFC Sénégal - Aurora Menu", layout="wide", page_icon="🍗")

# --- STYLE CSS (ARRIÈRE-PLAN ANIMÉ & CONTRASTE) ---
st.markdown("""
    <style>
    /* 1. L'animation de l'arrière-plan "Liquide/Aurora" */
    @keyframes aurora {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    /* Appliquer l'arrière-plan animé à toute l'application */
    .stApp {
        /* Dégradé de base : Blanc, Rouge très clair (KFC), Rose pâle */
        background: linear-gradient(-45deg, #ffffff, #fff0f1, #ffdde0, #ffffff);
        background-size: 400% 400%;
        /* Animation fluide qui tourne toutes les 10 secondes pour ne pas fatiguer les yeux */
        animation: aurora 10s ease infinite;
        color: #000000 !important;
    }
    
    /* 2. Style des Titres KFC */
    h1, h2, h3 {
        color: #e4002b !important;
        font-family: 'Arial Black', sans-serif;
        text-transform: uppercase;
        text-shadow: 1px 1px 2px rgba(255,255,255,0.8); /* Légère ombre pour décoller du fond mouvant */
    }

    /* 3. Cartes produits : Un peu plus opaques pour bien se détacher du fond */
    .product-card {
        background-color: rgba(255, 255, 255, 0.95); /* Blanc presque opaque */
        border: 1px solid #f0f0f0;
        padding: 20px;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 25px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.1); /* Ombre plus forte pour l'effet de relief */
        transition: 0.3s;
    }
    
    .product-card:hover {
        transform: translateY(-5px); /* Petit saut au survol */
        box-shadow: 0 12px 24px rgba(228, 0, 43, 0.2);
    }
    
    /* 4. Texte et Prix */
    .item-name {
        color: #000000 !important;
        font-weight: bold;
        font-size: 1.2rem;
        margin-top: 10px;
    }
    
    .item-price {
        color: #e4002b !important;
        font-size: 1.4rem;
        font-weight: 800;
    }

    /* 5. Boutons de commande */
    div.stButton > button:first-child {
        background-color: #e4002b;
        color: white;
        border-radius: 8px;
        border: none;
        width: 100%;
        font-weight: bold;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    div.stButton > button:first-child:hover {
        background-color: #b30021;
    }

    /* Ajustement de la sidebar pour qu'elle reste lisible */
    [data-testid="stSidebar"] {
        background-color: rgba(255, 255, 255, 0.9) !important;
    }
    </style>
    """, unsafe_allow_html=True)

# --- EN-TÊTE ---
# J'ai ajouté une colonne vide pour centrer légèrement le logo sur grand écran
col_space, col_logo, col_title = st.columns([1, 2, 8])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=120)
with col_title:
    st.title("KFC SEDIMA - SÉNÉGAL")
    st.markdown("##### Menu Digital Interactif")
st.divider()

# --- SECTION PRINCIPALE (PLATS) ---
col1, col2 = st.columns(2)

categories = [
    {
        "nom": "WINGS + MENU", 
        "prix": "À partir de 3000 F", 
        "img": "https://kfcsenegal.sn/storage/50/categorie-photo-14-08-2023Gm0UZ1692023013.jpg"
    },
    {
        "nom": "NOS WINGS", 
        "prix": "À partir de 3500 F", 
        "img": "https://kfcsenegal.sn/storage/49/categorie-photo-14-08-20238CZyR1692024550.jpg"
    },
    {
        "nom": "NOS BURGERS", 
        "prix": "À partir de 1500 F", 
        "img": "https://kfcsenegal.sn/storage/48/categorie-photo-14-08-2023vVRNN1692022970.png"
    },
    {
        "nom": "ACCOMPAGNEMENTS", 
        "prix": "À partir de 1000 F", 
        "img": "https://kfcsenegal.sn/storage/25/categorie-photo-14-08-2023yJlhj1692022268.jpg"
    }
]

for i, item in enumerate(categories):
    with (col1 if i % 2 == 0 else col2):
        st.markdown(f"""
            <div class="product-card">
                <img src="{item['img']}" style="width:100%; border-radius:10px;">
                <div class="item-name">{item['nom']}</div>
                <div class="item-price">{item['prix']}</div>
            </div>
        """, unsafe_allow_html=True)
        st.button(f"Voir les détails {item['nom']}", key=f"cat_{i}")

# --- SECTION BOISSONS (AVEC VOS LIENS SPÉCIFIQUES) ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.header("🥤 NOS BOISSONS FRAÎCHES")

b_col1, b_col2, b_col3 = st.columns(3)

# 1. 7UP
with b_col1:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://www.edenpizza.fr/wp-content/uploads/2019/11/7up-33cl.png" style="height:180px; object-fit: contain;">
            <div class="item-name">7UP / SEVEN</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)

# 2. COCA-COLA
with b_col2:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://www.23pizzastreet.com/web/cache/images/product/6d1696bee7835dd96f75f90fc20b01bf-gfgdf-368.png" style="height:180px; object-fit: contain;">
            <div class="item-name">COCA-COLA</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)

# 3. AUTRES (PRESSEA)
with b_col3:
    st.markdown(f"""
        <div class="product-card">
            <img src="https://cdn.prod.website-files.com/66d72c4d3a8971a008db2846/66d72c4d3a8971a008db2945_Pressea-hero%20(1).png" style="height:180px; object-fit: contain;">
            <div class="item-name">PRESSEA / EAU</div>
            <div class="item-price">800 F</div>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (PANIER) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=60)
    st.markdown("### 🛒 Mon Panier")
    st.write("Votre panier est vide.")
    st.divider()
    st.caption("Faites glisser pour commander")

# --- FOOTER ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.divider()
st.markdown("<p style='text-align: center; color: #666; font-size: 0.9rem;'>ceci n'es qu'à but académique dans le cadre de ma formation est sera supprimé ! en aucun cas cest a but commercial ni lucratif ! je ne suis pas kfc © 2026 - Distribué via Streamlit Cloud.</p>", unsafe_allow_html=True)
