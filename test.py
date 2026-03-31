import streamlit as st

# Configuration de la page
st.set_page_config(page_title="KFC Clone - Sénégal", layout="wide", page_icon="🍗")

# --- STYLE CSS POUR LE LOOK KFC ---
st.markdown("""
    <style>
    .main {
        background-color: #ffffff;
    }
    .stButton>button {
        width: 100%;
        background-color: #e4002b;
        color: white;
        border-radius: 5px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #b30021;
        color: white;
    }
    h1, h2, h3 {
        color: #e4002b;
        font-family: 'Arial Black', sans-serif;
    }
    .price-tag {
        font-weight: bold;
        font-size: 1.2rem;
        color: #333;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.image("https://upload.wikimedia.org/wikipedia/sco/b/bf/KFC_logo.svg", width=100)
st.title("Aly test QR code KFC SEDIMA - Commande en ligne")
st.write("Faites-vous plaisir avec le goût original au Sénégal !")

# --- PANIER (Session State) ---
if 'cart' not in st.session_state:
    st.session_state.cart = []

# --- MENU DATA ---
menu_items = {
    "A-LA-CARTE": [
        {"nom": "2 Pieces Original Recipe", "prix": 2200, "img": "https://placehold.co/400x300?text=2+Pieces+Chicken"},
        {"nom": "1 Piece Original Recipe", "prix": 1500, "img": "https://placehold.co/400x300?text=1+Piece+Chicken"},
        {"nom": "Purée de Pommes de Terre", "prix": 1000, "img": "https://placehold.co/400x300?text=Puree"},
    ],
    "BURGERS": [
        {"nom": "Colonel Burger (Repas)", "prix": 4500, "img": "https://placehold.co/400x300?text=Colonel+Burger"},
        {"nom": "Zinger Burger (Repas)", "prix": 4500, "img": "https://placehold.co/400x300?text=Zinger+Burger"},
    ],
    "WINGS ÉPICÉS": [
        {"nom": "8 pc Ailes de Poulet", "prix": 3500, "img": "https://placehold.co/400x300?text=8+Wings"},
        {"nom": "4 pc Ailes de Poulet", "prix": 2000, "img": "https://placehold.co/400x300?text=4+Wings"},
    ]
}

# --- AFFICHAGE DU MENU ---
tabs = st.tabs(list(menu_items.keys()))

for i, category in enumerate(menu_items):
    with tabs[i]:
        cols = st.columns(3)
        for idx, item in enumerate(menu_items[category]):
            with cols[idx % 3]:
                st.image(item["img"], use_container_width=True)
                st.subheader(item["nom"])
                st.markdown(f"<p class='price-tag'>{item['prix']} FCFA</p>", unsafe_allow_html=True)
                if st.button(f"Ajouter", key=f"{category}_{idx}"):
                    st.session_state.cart.append(item)
                    st.toast(f"{item['nom']} ajouté au panier !")

# --- SIDEBAR : RÉSUMÉ DE LA COMMANDE ---
st.sidebar.header("🛒 Votre Panier")
total = 0
if not st.session_state.cart:
    st.sidebar.write("Votre panier est vide.")
else:
    for i, cart_item in enumerate(st.session_state.cart):
        st.sidebar.write(f"**{cart_item['nom']}** - {cart_item['prix']} FCFA")
        total += cart_item['prix']
    
    st.sidebar.divider()
    st.sidebar.subheader(f"Total: {total} FCFA")
    
    if st.sidebar.button("Vider le panier"):
        st.session_state.cart = []
        st.rerun()

    if st.sidebar.button("🚀 Commander maintenant"):
        st.sidebar.success("Commande envoyée en cuisine !")
        st.balloons()
