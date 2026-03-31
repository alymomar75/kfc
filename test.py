import streamlit as st

# Configuration de la page style "Menu Board"
st.set_page_config(page_title="KFC Digital Menu", layout="wide")

# --- CSS PERSONNALISÉ (ROUGE KFC) ---
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    h1, h2, h3 { color: #e4002b; font-family: 'Arial Black', sans-serif; text-transform: uppercase; }
    .price { color: #e4002b; font-weight: bold; font-size: 20px; margin-top: -10px; }
    .item-card { border: 1px solid #eee; padding: 10px; border-radius: 15px; margin-bottom: 20px; background: #fff; box-shadow: 2px 2px 5px rgba(0,0,0,0.05); }
    </style>
    """, unsafe_allow_html=True)

st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=80)
st.title("Menu KFC - Commande Express")

# --- BASE DE DONNÉES DU MENU (Liens Internet) ---
menu = {
    "POULET & WINGS": [
        {"nom": "KFC Hot Wings (8pcs)", "prix": 3500, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/8-hot-wings.png"},
        {"nom": "2 Pièces Poulet Original", "prix": 2200, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/2-pc-chicken-box.png"}
    ],
    "ACCOMPAGNEMENTS & FROMAGE": [
        {"nom": "Frites au Fromage", "prix": 1800, "img": "https://images.ctfassets.net/wt71v9imv975/5vR5v8X9v0QG6uO8S8k8u8/7b69c4c7b8d8b1c4e1b8e8b1c4e1b8e8/Cheese_Fries.png"},
        {"nom": "Potatoes Croustillantes", "prix": 1200, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/individual-fries.png"}
    ],
    "BOISSONS FRAÎCHES": [
        {"nom": "Pepsi / Coca-Cola (50cl)", "prix": 800, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/pepsi.png"},
        {"nom": "7Up / Schweppes", "prix": 800, "img": "https://pwa-api.kfc.ca/api/cms/v1/assets/kfc-canada/storage/products/hero/7-up.png"}
    ]
}

# --- AFFICHAGE DYNAMIQUE ---
col1, col2 = st.columns(2)

# Colonne de Gauche : Poulet et Accompagnements
with col1:
    st.header("🍗 Le Poulet")
    for item in menu["POULET & WINGS"]:
        with st.container():
            c1, c2 = st.columns([1, 2])
            c1.image(item["img"], use_container_width=True)
            c2.subheader(item["nom"])
            c2.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            c2.button("Ajouter au panier", key=item["nom"])

    st.header("🍟 Accompagnements")
    for item in menu["ACCOMPAGNEMENTS & FROMAGE"]:
        with st.container():
            c1, c2 = st.columns([1, 2])
            c1.image(item["img"], use_container_width=True)
            c2.subheader(item["nom"])
            c2.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            c2.button("Ajouter au panier", key=item["nom"])

# Colonne de Droite : Boissons et Panier
with col2:
    st.header("🥤 Boissons")
    for item in menu["BOISSONS FRAÎCHES"]:
        with st.container():
            c1, c2 = st.columns([1, 2])
            c1.image(item["img"], use_container_width=True)
            c2.subheader(item["nom"])
            c2.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            c2.button("Ajouter au panier", key=item["nom"])

    st.divider()
    st.sidebar.title("🛒 Votre Commande")
    st.sidebar.info("Sélectionnez vos produits pour voir le récapitulatif ici.")
