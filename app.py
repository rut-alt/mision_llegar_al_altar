import streamlit as st
import random
import time

# CONFIG
NUM_CASILLAS = 14

AMIGAS = [
    {"nombre": "Marta", "mensaje": "🚨 ¡NO TE CASES! ¡Los gatos llevan 3 días mirándome raro!", "img": "img/marta.png"},
    {"nombre": "Lorena", "mensaje": "💅 Tía necesito outfit urgente, ¡esto es más importante que tu boda!", "img": "img/lorena.png"},
    {"nombre": "Leslie", "mensaje": "🍷 He abierto vino… no puedes dejarme sola con esto", "img": "img/leslie.png"},
    {"nombre": "Julia", "mensaje": "📞 Drama máximo. Llámame YA o me caso yo antes", "img": "img/julia.png"},
    {"nombre": "Andrea", "mensaje": "🚗 Estoy perdida… otra vez… ven a rescatarme 😭", "img": "img/andrea.png"},
    {"nombre": "Rut", "mensaje": "😏 Sabes que sin mí no hay boda que valga", "img": "img/rut.png"},
]

# INIT STATE
if "init" not in st.session_state:
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(2, NUM_CASILLAS-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1
    st.session_state.init = True

# RESET
def reiniciar():
    st.session_state.pos_yasmina = 0
    st.session_state.pos_amigas = [random.randint(2, NUM_CASILLAS-2) for _ in AMIGAS]
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.dado = 1

# TURNO
def tirar_dado():
    # mini animación del dado
    for _ in range(5):
        st.session_state.dado = random.randint(1, 3)
        time.sleep(0.1)

    paso = st.session_state.dado
    st.session_state.pos_yasmina += paso

    # mover amigas
    nuevas = []
    for pos in st.session_state.pos_amigas:
        mov = random.choice([-1, 0, 1])
        nuevas.append(max(1, min(NUM_CASILLAS-1, pos + mov)))

    st.session_state.pos_amigas = nuevas

    # comprobar choque
    for i, pos in enumerate(nuevas):
        if pos == st.session_state.pos_yasmina:
            st.session_state.game_over = True
            st.session_state.evento = AMIGAS[i]
            return

    # comprobar victoria
    if st.session_state.pos_yasmina >= NUM_CASILLAS:
        st.session_state.win = True


# UI
st.set_page_config(page_title="Boda Yasmina 💍", layout="centered")

st.title("💍 MISIÓN: LLEGAR AL ALTAR")

# 🎵 música
st.audio("audio/boda.mp3", loop=True)

# 🎲 dado visual
st.markdown(f"## 🎲 Dado: {st.session_state.dado}")

# TABLERO
cols = st.columns(NUM_CASILLAS + 1)

for i in range(NUM_CASILLAS + 1):
    with cols[i]:

        # ALTAR
        if i == NUM_CASILLAS:
            st.image("img/altar.png", width=70)

        # YASMINA
        if i == st.session_state.pos_yasmina:
            st.image("img/yasmina.png", width=70)

        # AMIGAS (cada una con su cara)
        for idx, amiga in enumerate(AMIGAS):
            if i == st.session_state.pos_amigas[idx]:
                st.image(amiga["img"], width=50)

# BOTÓN
if not st.session_state.game_over and not st.session_state.win:
    if st.button("🎲 Tirar dado"):
        tirar_dado()

# 💥 EVENTO (pantalla grande)
if st.session_state.game_over:
    amiga = st.session_state.evento

    st.markdown("## 💥 TE HAN PILLADO")
    st.image(amiga["img"], width=300)
    st.error(f"{amiga['nombre']} dice: {amiga['mensaje']}")

    if st.button("💔 Volver a empezar"):
        reiniciar()

# 🎉 VICTORIA
if st.session_state.win:
    st.balloons()
    st.success("💒 ¡YASMINA HA CONSEGUIDO CASARSE!")

    st.image("img/yasmina.png", width=200)

    if st.button("🔁 Otra vez"):
        reiniciar()
