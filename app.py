import streamlit as st
import random

st.set_page_config(layout="centered")

# CONFIG
TOTAL_STEPS = 10  # pasos hasta el altar

AMIGAS = [
    {"nombre": "Rut", "img": "img/rut.png", "msg": "😏 Sin mí no hay boda"},
    {"nombre": "Marta", "img": "img/marta.png", "msg": "🔥 Drama máximo"},
    {"nombre": "Lorena", "img": "img/lorena.png", "msg": "💅 Outfit urgente"},
    {"nombre": "Leslie", "img": "img/leslie.png", "msg": "🍷 He abierto vino..."},
    {"nombre": "Julia", "img": "img/julia.png", "msg": "📞 Llámame YA"},
    {"nombre": "Andrea", "img": "img/andrea.png", "msg": "🚗 Estoy perdida"},
]

# INIT
if "step" not in st.session_state:
    st.session_state.step = 0

if "correct_door" not in st.session_state:
    st.session_state.correct_door = random.randint(0, 2)

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "win" not in st.session_state:
    st.session_state.win = False

if "amiga_evento" not in st.session_state:
    st.session_state.amiga_evento = None


def reiniciar():
    st.session_state.step = 0
    st.session_state.correct_door = random.randint(0, 2)
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.amiga_evento = None


def elegir_puerta(idx):
    if idx == st.session_state.correct_door:
        st.session_state.step += 1

        if st.session_state.step >= TOTAL_STEPS:
            st.session_state.win = True
        else:
            st.session_state.correct_door = random.randint(0, 2)
    else:
        st.session_state.game_over = True
        st.session_state.amiga_evento = random.choice(AMIGAS)


# UI
st.title("💍 NO ABRAS LA PUERTA EQUIVOCADA")

# PROGRESO
progreso = st.session_state.step / TOTAL_STEPS
st.progress(progreso)

st.markdown(f"### 🏃‍♀️ Progreso: {st.session_state.step}/{TOTAL_STEPS}")

# NOVIA
st.image("img/yasmina.png", width=120)

st.markdown("## 🚪 Elige una puerta")

col1, col2, col3 = st.columns(3)

for i, col in enumerate([col1, col2, col3]):
    with col:
        if st.button(f"🚪 Puerta {i+1}", use_container_width=True):
            if not st.session_state.game_over and not st.session_state.win:
                elegir_puerta(i)
                st.rerun()


# GAME OVER
if st.session_state.game_over:
    amiga = st.session_state.amiga_evento

    st.markdown("---")
    st.error(f"💥 TE HAS ENCONTRADO CON {amiga['nombre'].upper()}")

    st.image(amiga["img"], width=150)
    st.markdown(f"### {amiga['msg']}")

    if st.button("💔 Intentar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()


# WIN
if st.session_state.win:
    st.markdown("---")
    st.success("💒 ¡HAS LLEGADO AL ALTAR SIN SER INTERCEPTADA!")

    if st.button("🔁 Jugar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()
