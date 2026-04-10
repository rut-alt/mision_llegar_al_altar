import streamlit as st
import random
import time

# CONFIG
NUM_CASILLAS = 14

AMIGAS = [
    {"nombre": "Marta", "mensaje": "🚨 ¡NO TE CASES!", "img": "img/leslie.png.png"},
    {"nombre": "Lorena", "mensaje": "💅 Outfit urgente", "img": "img/lorena.png.png"},
    {"nombre": "Leslie", "mensaje": "🍷 Vino abierto", "img": "img/leslie.png.png"},
    {"nombre": "Julia", "mensaje": "📞 Drama YA", "img": "img/lorena.png.png"},
    {"nombre": "Andrea", "mensaje": "🚗 Estoy perdida", "img": "img/leslie.png.png"},
    {"nombre": "Rut", "mensaje": "😏 Sin mí no hay boda", "img": "leslie.png.png"},
]

# INIT
if "init" not in st.session_state:
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(2, NUM_CASILLAS-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1
    st.session_state.init = True

def reiniciar():
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(2, NUM_CASILLAS-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1

def tirar_dado():
    for _ in range(5):
        st.session_state.dado = random.randint(1, 3)
        time.sleep(0.1)

    paso = st.session_state.dado
    st.session_state.pos_yasmina += paso

    nuevas = []
    for pos in st.session_state.pos_amigas:
        mov = random.choice([-1, 0, 1])
        nuevas.append(max(1, min(NUM_CASILLAS-1, pos + mov)))

    st.session_state.pos_amigas = nuevas

    for i, pos in enumerate(nuevas):
        if pos == st.session_state.pos_yasmina:
            st.session_state.game_over = True
            st.session_state.evento = AMIGAS[i]
            return

    if st.session_state.pos_yasmina >= NUM_CASILLAS:
        st.session_state.win = True


# UI
st.set_page_config(page_title="Boda Yasmina 💍", layout="centered")

st.markdown("<h2 style='text-align:center;'>💍 MISIÓN: LLEGAR AL ALTAR</h2>", unsafe_allow_html=True)
st.markdown(f"<h4 style='text-align:center;'>🎲 Dado: {st.session_state.dado}</h4>", unsafe_allow_html=True)

# TABLERO VERTICAL (MÓVIL)
for i in range(NUM_CASILLAS + 1):

    st.markdown(
        "<div style='border:2px solid #ddd; border-radius:12px; padding:12px; margin:6px 0; text-align:center;'>",
        unsafe_allow_html=True
    )

    # ALTAR
    if i == NUM_CASILLAS:
        st.markdown("💒 ALTAR")

    # YASMINA
    if i == st.session_state.pos_yasmina:
        st.image("img/yasmina.png.png", width=80)

    # AMIGAS
    for idx, amiga in enumerate(AMIGAS):
        if i == st.session_state.pos_amigas[idx]:
            st.image(amiga["img"], width=70)

    st.markdown(f"<b>Casilla {i}</b>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# BOTÓN GRANDE (MÓVIL)
if not st.session_state.game_over and not st.session_state.win:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🎲 TIRAR DADO", use_container_width=True):
        tirar_dado()


# GAME OVER
if st.session_state.game_over:
    amiga = st.session_state.evento

    st.error(f"💥 {amiga['nombre']}: {amiga['mensaje']}")
    st.image(amiga["img"], width=250)

    if st.button("💔 REINTENTAR", use_container_width=True):
        reiniciar()


# WIN
if st.session_state.win:
    st.balloons()
    st.success("💒 ¡SE HA CASADO!")

    st.image("img/yasmina.png.png", width=250)

    if st.button("🔁 OTRA VEZ", use_container_width=True):
        reiniciar()
