import streamlit as st

# Configuration
st.set_page_config(page_title="KFC Sénégal - Menu", layout="wide")

# --- CSS Personnalisé ---
st.markdown("""
    <style>
    .product-card {
        border: 1px solid #eee;
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        background-color: #f9f9f9;
    }
    .price {
        color: #e4002b;
        font-weight: bold;
        font-size: 20px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- DONNÉES DU MENU (Avec les bonnes images) ---
# Note : Remplacez les liens URL par "images/votre_image.jpg" une fois vos fichiers uploadés
menu_data = {
    "A-LA-CARTE": [
        {"nom": "2 Pieces Original Recipe", "prix": 2200, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V022.jpg"},
        {"nom": "Purée de Pommes de Terre", "prix": 1000, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V003.jpg"},
        {"nom": "Mini Pain", "prix": 750, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V005.jpg"}
    ],
    "BURGERS": [
        {"nom": "Colonel Burger", "prix": 3000, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V036.jpg"},
        {"nom": "Zinger Burger", "prix": 3000, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V008.jpg"}
    ],
    "WINGS ÉPICÉS": [
        {"nom": "8 pc Ailes de Poulet", "prix": 3500, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V017.jpg"},
        {"nom": "4 pc Ailes de Poulet", "prix": 2000, "img": "https://orderserv-kfc-assets.yum.com/101327/images/Items/Large/L-V017.jpg"}
    ]
}

# --- AFFICHAGE ---
st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=80)
st.title("Menu KFC SEDIMA")

# Création des colonnes pour le menu (2 colonnes comme sur votre photo)
col_left, col_right = st.columns(2)

with col_left:
    st.header("🍗 A-LA-CARTE")
    for item in menu_data["A-LA-CARTE"]:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(item["img"], use_container_width=True)
        with c2:
            st.subheader(item["nom"])
            st.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item["nom"])

with col_right:
    st.header("🍔 BURGERS")
    for item in menu_data["BURGERS"]:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(item["img"], use_container_width=True)
        with c2:
            st.subheader(item["nom"])
            st.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item["nom"])
            
    st.header("🌶️ WINGS")
    for item in menu_data["WINGS ÉPICÉS"]:
        c1, c2 = st.columns([1, 2])
        with c1:
            st.image(item["img"], use_container_width=True)
        with c2:
            st.subheader(item["nom"])
            st.markdown(f"<p class='price'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
            st.button("Ajouter", key=item["nom"])
