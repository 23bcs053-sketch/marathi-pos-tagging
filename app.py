import streamlit as st
import sqlite3
import stanza
import pandas as pd
import os

# =========================
# FIX: Safe Stanza Folder (NO PERMISSION ERROR)
# =========================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_DIR = os.path.join(BASE_DIR, "stanza_models")
os.makedirs(MODEL_DIR, exist_ok=True)

os.environ["STANZA_RESOURCES_DIR"] = MODEL_DIR

# =========================
# LOAD MODELS (FAST - CACHE)
# =========================
@st.cache_resource
def load_models():
    nlp_mr = stanza.Pipeline("mr", processors="tokenize,pos", verbose=False)
    nlp_en = stanza.Pipeline("en", processors="tokenize,pos", verbose=False)
    return nlp_mr, nlp_en

nlp_mr, nlp_en = load_models()

# =========================
# DATABASE
# =========================
conn = sqlite3.connect(os.path.join(BASE_DIR, "users.db"), check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE,
    password TEXT
)
""")
conn.commit()

# =========================
# SESSION
# =========================
if "page" not in st.session_state:
    st.session_state.page = "home"
if "login" not in st.session_state:
    st.session_state.login = False
if "user" not in st.session_state:
    st.session_state.user = ""

# =========================
# UI STYLE
# =========================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.8)),
    url("https://images.unsplash.com/photo-1603791440384-56cd371ee9a7");
    background-size: cover;
    color: white;
}
.block-container {
    background: rgba(0,0,0,0.6);
    padding: 2rem;
    border-radius: 15px;
}
.stButton button {
    background: linear-gradient(to right,#00c6ff,#0072ff);
    border-radius: 10px;
    color:white;
}
</style>
""", unsafe_allow_html=True)

# =========================
# HOME
# =========================
def home():
    st.title("📝 Marathi POS Tagger")
    if st.button("🔐 Login"):
        st.session_state.page = "login"
    if st.button("📝 Signup"):
        st.session_state.page = "signup"

# =========================
# LOGIN
# =========================
def login():
    st.subheader("Login")

    u = st.text_input("Username")
    p = st.text_input("Password", type="password")

    if st.button("Login"):
        res = cursor.execute(
            "SELECT * FROM users WHERE username=? AND password=?",
            (u, p)
        ).fetchone()

        if res:
            st.session_state.login = True
            st.session_state.user = u
            st.session_state.page = "app"
        else:
            st.error("Wrong credentials")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# =========================
# SIGNUP
# =========================
def signup():
    st.subheader("Signup")

    u = st.text_input("New Username")
    p = st.text_input("New Password", type="password")

    if st.button("Create Account"):
        try:
            cursor.execute("INSERT INTO users VALUES (NULL, ?, ?)", (u, p))
            conn.commit()
            st.success("Account created")
            st.session_state.page = "login"
        except:
            st.error("Username already exists")

    if st.button("⬅ Back"):
        st.session_state.page = "home"

# =========================
# APP
# =========================
def app():
    st.write(f"👤 Welcome {st.session_state.user}")

    text = st.text_area("Enter Marathi / English text")

    if st.button("🚀 POS Tag"):
        if text.strip() == "":
            st.warning("Enter text")
        else:
            # Language detect
            lang = "mr" if any('\u0900' <= c <= '\u097F' for c in text) else "en"

            doc = nlp_mr(text) if lang == "mr" else nlp_en(text)

            data = []
            for sent in doc.sentences:
                for word in sent.words:
                    data.append([word.text, word.upos, word.xpos])

            df = pd.DataFrame(data, columns=["Word", "POS", "Detail"])
            st.dataframe(df)

    st.markdown("---")
    if st.button("🚪 Logout"):
        st.session_state.login = False
        st.session_state.page = "home"

# =========================
# ROUTER
# =========================
if st.session_state.page == "home":
    home()
elif st.session_state.page == "login":
    login()
elif st.session_state.page == "signup":
    signup()
elif st.session_state.page == "app" and st.session_state.login:
    app()
else:
    st.session_state.page = "home"
