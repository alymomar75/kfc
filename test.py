import streamlit as st

# Configuration de la page
st.set_page_config(page_title="KFC Sénégal - Menu", layout="wide", page_icon="🍗")

# --- STYLE CSS ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Oswald:wght@700&family=Roboto:wght@400;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Roboto', sans-serif;
    }
    h1, h2, h3 {
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
    }
    .main {
        background-color: #ffffff;
    }
    .price-tag {
        color: #e4002b;
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 0px;
    }
    .product-name {
        font-size: 18px;
        font-weight: bold;
        margin-top: 10px;
    }
    .stButton>button {
        background-color: #e4002b;
        color: white;
        border-radius: 0px;
        font-weight: bold;
        border: none;
        width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
col_logo, col_title = st.columns([1, 4])
with col_logo:
    st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=100)
with col_title:
    st.title("MENU KFC - SEDIMA SÉNÉGAL")

st.divider()

# --- DONNÉES DU MENU (Lien images officiels) ---
menu = {
    "A-LA-CARTE": [
        {"nom": "2 Pieces Original Recipe", "prix": 2200, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/2-pc-chicken-box.png"},
        {"nom": "1 Piece Original Recipe", "prix": 1500, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/1-pc-chicken.png"},
        {"nom": "Purée de Pommes de Terre", "prix": 1000, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/individual-mashed-potatoes-gravy.png"},
        {"nom": "Mini Pain", "prix": 750, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/individual-butter-bread.png"}
    ],
    "BURGERS": [
        {"nom": "Colonel Burger (Repas)", "prix": 4500, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/kentucky-flatbread-sandwich.png"},
        {"nom": "Zinger Burger (Repas)", "prix": 4500, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/zinger-sandwich.png"}
    ],
    "WINGS ÉPICÉS": [
        {"nom": "8 pc Wings", "prix": 3500, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/8-hot-wings.png"},
        {"nom": "4 pc Wings", "prix": 2000, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/4-hot-wings.png"}
    ]
}

# --- AFFICHAGE EN COLONNES (Style Menu Board) ---
col1, col2 = st.columns(2)

# Colonne de Gauche : A-LA-CARTE
with col1:
    st.header("🍗 A-LA-CARTE")
    for item in menu["A-LA-CARTE"]:
        c_img, c_txt = st.columns([1, 1.5])
        with c_img:
            st.image(item["img"], use_container_width=True)
        with c_txt:
            st.markdown(f"<p class='product-name'>{item['nom']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='price-tag'>{item['prix']} <small>CFA</small></p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item['nom'])

# Colonne de Droite : BURGERS & WINGS
with col2:
    st.header("🍔 BURGERS")
    for item in menu["BURGERS"]:
        c_img, c_txt = st.columns([1, 1.5])
        with c_img:
            st.image(item["img"], use_container_width=True)
        with c_txt:
            st.markdown(f"<p class='product-name'>{item['nom']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='price-tag'>{item['prix']} <small>CFA</small></p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item['nom'])
            
    st.header("🌶️ WINGS ÉPICÉS")
    for item in menu["WINGS ÉPICÉS"]:
        c_img, c_txt = st.columns([1, 1.5])
        with c_img:
            st.image(item["img"], use_container_width=True)
        with c_txt:
            st.markdown(f"<p class='product-name'>{item['nom']}</p>", unsafe_allow_html=True)
            st.markdown(f"<p class='price-tag'>{item['prix']} <small>CFA</small></p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item['nom'])
