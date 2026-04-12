import streamlit as st
import os
import urllib.parse
import base64
import glob
import re
import time

st.set_page_config(layout="centered")

# ========================
# CONFIG
# ========================
TOTAL_STEPS = 6

AMIGAS = {
    "rut": {
        "img": "img/rut.png",
        "telefono": "34663413206",
        "historia": "Te vas a México en horas. Ha encontrado vuelos por menos de 300€ y ha cogido uno para cada una. Todo es impulsivo.",
    },
    "marta": {
        "img": "img/marta.png",
        "telefono": "34655068171",
        "historia": "Te quedas con Marta y acabas siendo mamá de gatos.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "telefono": "34676097913",
        "historia": "Das vueltas eternas en Atocha intentando encontrar a Lorena.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "telefono": "34688422600",
        "historia": "Un matcha se convierte en copas y nunca llegas a la boda.",
    },
    "julia": {
        "img": "img/julia.png",
        "telefono": "34615853540",
        "historia": "La llamada de Julia no termina nunca.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "telefono": "346635288588",
        "historia": "Andrea duda del vestido y acabas dudando tú también.",
    },
}

# ========================
# ESTILO
# ========================
st.markdown("""
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

body {background-color: #0f0f0f;}

.block {
    background: #1c1c1c;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    text-align:center;
}

.title {font-size: 28px; font-weight: bold; color: white;}
.text {color: #d1d1d1; font-size: 17px;}
.pink {color: #ff4da6; font-weight: bold;}
</style>
""", unsafe_allow_html=True)

# ========================
# FUNCIONES
# ========================
def mostrar_imagen(ruta, width=150):
    if os.path.exists(ruta):
        st.image(ruta, width=width)

def autoplay_audio(file_path):
    try:
        if os.path.exists(file_path):
            with open(file_path, "rb") as f:
                data = f.read()
                b64 = base64.b64encode(data).decode()

            st.markdown(f"""
            <audio autoplay loop>
            <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
            </audio>
            """, unsafe_allow_html=True)
    except:
        pass

def carrusel_fotos():

    with st.spinner("Recopilando momentos..."):
        fotos = glob.glob("img/foto*.png")

        def ordenar(f):
            return int(re.findall(r'\d+', f)[0])

        fotos = sorted(fotos, key=ordenar)
        time.sleep(1.5)

    if "foto_idx" not in st.session_state:
        st.session_state.foto_idx = 0

    if fotos:
        st.image(fotos[st.session_state.foto_idx], use_column_width=True)

        col1, col2 = st.columns(2)

        with col1:
            if st.button("⬅️"):
                st.session_state.foto_idx = (st.session_state.foto_idx - 1) % len(fotos)

        with col2:
            if st.button("➡️"):
                st.session_state.foto_idx = (st.session_state.foto_idx + 1) % len(fotos)
    else:
        st.warning("No hay fotos")

def reiniciar():
    st.session_state.pantalla = "juego"
    st.session_state.step = 0
    st.session_state.evento = None
    st.session_state.valoracion = None
    st.session_state.desvios = []
    st.session_state.confetti = False
    st.session_state.foto_idx = 0

def obtener_evento(step):
    eventos = [
        {"texto": "Empieza el día.", "ok": "Seguir", "bad": "Mirar el móvil"},
        {"texto": "Marta necesita ayuda con los gatos.", "ok": "No ir", "bad": "Ir"},
        {"texto": "Lorena necesita que la recojas.", "ok": "Que coja Uber", "bad": "Ir"},
        {"texto": "Ves a alguien en una cafetería.", "ok": "Ignorar", "bad": "Entrar"},
        {"texto": "Julia te llama.", "ok": "No coger", "bad": "Coger"},
        {"texto": "Andrea duda del vestido.", "ok": "Pasar", "bad": "Ayudar"},
    ]
    return eventos[step]

def elegir(resultado, amiga=None):
    if resultado == "ok":
        st.session_state.step += 1
        if st.session_state.step >= TOTAL_STEPS:
            st.session_state.pantalla = "win"
    else:
        st.session_state.evento = amiga
        st.session_state.desvios.append(amiga)
        st.session_state.pantalla = "game_over"

def ranking():
    n = len(st.session_state.desvios)
    if n == 0:
        return "Novia imparable"
    elif n <= 2:
        return "Novia con dudas"
    elif n <= 4:
        return "Novia influenciable"
    else:
        return "Novia del caos"

# ========================
# INIT
# ========================
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "step" not in st.session_state:
    st.session_state.step = 0

if "evento" not in st.session_state:
    st.session_state.evento = None

if "valoracion" not in st.session_state:
    st.session_state.valoracion = None

if "desvios" not in st.session_state:
    st.session_state.desvios = []

if "confetti" not in st.session_state:
    st.session_state.confetti = False

if "foto_idx" not in st.session_state:
    st.session_state.foto_idx = 0

# ========================
# UI
# ========================
st.markdown('<div class="title">Misión: llegar al altar</div>', unsafe_allow_html=True)

# INICIO
if st.session_state.pantalla == "inicio":

    st.markdown('<div class="block text">', unsafe_allow_html=True)
    st.markdown("""
    Toma decisiones sin saber qué pasará.

    Si te desvías, vivirás otra vida.

    Luego intenta llegar al altar.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Empezar"):
        st.session_state.pantalla = "juego"
        st.rerun()

# JUEGO
elif st.session_state.pantalla == "juego":

    progreso = st.session_state.step / TOTAL_STEPS
    st.progress(progreso)

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    mostrar_imagen("img/yasmina.png", 150)

    evento = obtener_evento(st.session_state.step)
    st.markdown(evento["texto"])

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button(evento["ok"], use_container_width=True):
        elegir("ok")
        st.rerun()

    if st.button(evento["bad"], use_container_width=True):
        amiga = list(AMIGAS.keys())[st.session_state.step]
        elegir("bad", amiga)
        st.rerun()

# GAME OVER
elif st.session_state.pantalla == "game_over":

    amiga_key = st.session_state.evento
    amiga = AMIGAS[amiga_key]

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    st.markdown(f'<span class="pink">{amiga_key.upper()}</span>', unsafe_allow_html=True)

    mostrar_imagen(amiga["img"])
    st.markdown(amiga["historia"])

    if st.button("Seguir"):
        st.session_state.pantalla = "juego"
        st.session_state.step += 1
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# WIN
elif st.session_state.pantalla == "win":

    if not st.session_state.confetti:
        st.balloons()
        st.session_state.confetti = True

    st.markdown('<div class="block text">Has llegado al altar.</div>', unsafe_allow_html=True)

    autoplay_audio("audio/musica.mp3")

    carrusel_fotos()

    if st.button("Jugar otra vez"):
        reiniciar()
        st.rerun()
