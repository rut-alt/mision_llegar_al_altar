import streamlit as st
import random
import os

st.set_page_config(layout="centered")

# CONFIG
TOTAL_STEPS = 5

AMIGAS = {
    "rut": {"img": "img/rut.png", "msg": "😏 Sin mí no hay boda"},
    "marta": {"img": "img/marta.png", "msg": "🔥 Drama máximo"},
    "lorena": {"img": "img/lorena.png", "msg": "💅 Outfit urgente"},
    "leslie": {"img": "img/leslie.png", "msg": "🍷 He abierto vino..."},
    "julia": {"img": "img/julia.png", "msg": "📞 Llámame YA"},
    "andrea": {"img": "img/andrea.png", "msg": "🚗 Estoy perdida"},
}

# FUNCION IMAGEN SEGURA
def mostrar_imagen(ruta, width=150):
    if os.path.exists(ruta):
        st.image(ruta, width=width)

# INIT
if "step" not in st.session_state:
    st.session_state.step = 0

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "win" not in st.session_state:
    st.session_state.win = False

if "evento" not in st.session_state:
    st.session_state.evento = None


def reiniciar():
    st.session_state.step = 0
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None


# HISTORIA (aquí está la magia 🔥)
def obtener_evento(step):
    eventos = [
        {
            "texto": "⏰ Yasmina se despierta tarde el día de su boda...",
            "opciones": [
                {"texto": "☕ Tomar café rápido", "resultado": "ok"},
                {"texto": "📱 Mirar el móvil", "resultado": "rut"},
            ],
        },
        {
            "texto": "🚪 Suena el teléfono… es alguien insistiendo",
            "opciones": [
                {"texto": "❌ Ignorar llamada", "resultado": "ok"},
                {"texto": "📞 Contestar", "resultado": "julia"},
            ],
        },
        {
            "texto": "👗 Duda con el vestido...",
            "opciones": [
                {"texto": "👗 Elegir el que ya tenía", "resultado": "ok"},
                {"texto": "💅 Pedir opinión", "resultado": "lorena"},
            ],
        },
        {
            "texto": "🚗 Camino al altar...",
            "opciones": [
                {"texto": "🚀 Ir directa", "resultado": "ok"},
                {"texto": "📍 Parar a ayudar", "resultado": "andrea"},
            ],
        },
        {
            "texto": "🍷 Aparece una tentación final...",
            "opciones": [
                {"texto": "💒 Seguir al altar", "resultado": "ok"},
                {"texto": "🍷 Tomar una copa", "resultado": "leslie"},
            ],
        },
    ]

    return eventos[step]


def elegir(opcion):
    if opcion == "ok":
        st.session_state.step += 1

        if st.session_state.step >= TOTAL_STEPS:
            st.session_state.win = True
    else:
        st.session_state.game_over = True
        st.session_state.evento = opcion


# UI
st.title("💍 ELIGE TU DESTINO")

# PROGRESO
progreso = st.session_state.step / TOTAL_STEPS
st.progress(progreso)
st.markdown(f"### 🏃‍♀️ Progreso: {st.session_state.step}/{TOTAL_STEPS}")

# NOVIA
mostrar_imagen("img/yasmina.png", 120)

# GAME
if not st.session_state.game_over and not st.session_state.win:
    evento = obtener_evento(st.session_state.step)

    st.markdown(f"## {evento['texto']}")

    for opcion in evento["opciones"]:
        if st.button(opcion["texto"], use_container_width=True):
            elegir(opcion["resultado"])
            st.rerun()


# GAME OVER
if st.session_state.game_over:
    amiga = AMIGAS[st.session_state.evento]

    st.markdown("---")
    st.error("💥 TE HAN LIADO... NO LLEGAS AL ALTAR")

    mostrar_imagen(amiga["img"])
    st.markdown(f"### {amiga['msg']}")

    if st.button("💔 Intentar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()


# WIN
if st.session_state.win:
    st.markdown("---")
    st.success("💒 ¡HAS LLEGADO AL ALTAR SIN DISTRACCIONES!")

    if st.button("🔁 Jugar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()
