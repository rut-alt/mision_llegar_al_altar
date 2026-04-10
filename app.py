import streamlit as st
import random
import time

# CONFIG
FILAS = 4
COLUMNAS = 4
TOTAL = FILAS * COLUMNAS

AMIGAS = [
    {"nombre": "Marta", "mensaje": "🚨 ¡NO TE CASES!", "img": "img/leslie.png.png"},
    {"nombre": "Lorena", "mensaje": "💅 Outfit urgente", "img": "img/lorena.png.png"},
    {"nombre": "Leslie", "mensaje": "🍷 Vino abierto", "img": "img/leslie.png.png"},
    {"nombre": "Julia", "mensaje": "📞 Drama YA", "img": "img/lorena.png.png"},
    {"nombre": "Andrea", "mensaje": "🚗 Estoy perdida", "img": "img/leslie.png.png"},
    {"nombre": "Rut", "mensaje": "😏 Sin mí no hay boda", "img": "img/leslie.png.png"},
]

# INIT
if "init" not in st.session_state:
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(1, TOTAL-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1
    st.session_state.init = True

def reiniciar():
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(1, TOTAL-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1

def tirar_dado():
    for _ in range(5):
        st.session_state.dado = random.randint(1, 3)
        time.sleep(0.1)

    # mover yasmina
    st.session_state.pos_yasmina += st.session_state.dado

    # mover amigas RANDOM 1 paso
    nuevas = []
    for pos in st.session_state.pos_amigas:
        mov = random.choice([-1, 1])
        nuevas.append(max(0, min(TOTAL-1, pos + mov)))

    st.session_state.pos_amigas = nuevas

    # choque
    for i, pos in enumerate(nuevas):
        if pos == st.session_state.pos_yasmina:
            st.session_state.game_over = True
            st.session_state.evento = AMIGAS[i]
            return

    # victoria
    if st.session_state.pos_yasmina >= TOTAL-1:
        st.session_state.win = True


# UI
st.set_page_config(page_title="Boda 💍", layout="centered")

st.title("💍 MISIÓN: LLEGAR AL ALTAR")
st.markdown(f"🎲 Dado: **{st.session_state.dado}**")

# GRID
for fila in range(FILAS):
    cols = st.columns(COLUMNAS)

    for col in range(COLUMNAS):
        idx = fila * COLUMNAS + col

        with cols[col]:
            st.markdown(
                "<div style='border:2px solid #ccc; border-radius:10px; padding:10px; text-align:center;'>",
                unsafe_allow_html=True
            )

            # ALTAR
            if idx == TOTAL-1:
                st.markdown("💒")

            # YASMINA
            if idx == st.session_state.pos_yasmina:
                try:
                    st.image("img/yasmina.png", width=60)
                except:
                    st.markdown("👰")

            # AMIGAS
            for i, amiga in enumerate(AMIGAS):
                if idx == st.session_state.pos_amigas[i]:
                    try:
                        st.image(amiga["img"], width=50)
                    except:
                        st.markdown("👯‍♀️")

            st.markdown(f"<small>{idx}</small>", unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)


# BOTÓN
if not st.session_state.game_over and not st.session_state.win:
    if st.button("🎲 Tirar dado", use_container_width=True):
        tirar_dado()

# GAME OVER
if st.session_state.game_over:
    amiga = st.session_state.evento

    st.error(f"💥 {amiga['nombre']}: {amiga['mensaje']}")
    try:
        st.image(amiga["img"], width=200)
    except:
        st.markdown("💀")

    if st.button("💔 Reintentar", use_container_width=True):
        reiniciar()

# WIN
if st.session_state.win:
    st.balloons()
    st.success("💒 ¡SE HA CASADO!")

    if st.button("🔁 Otra vez", use_container_width=True):
        reiniciar()
