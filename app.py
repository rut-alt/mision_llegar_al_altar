import streamlit as st
import os
import urllib.parse

st.set_page_config(layout="centered")

# ========================
# CONFIG
# ========================
TOTAL_STEPS = 6

AMIGAS = {
    "rut": {
        "img": "img/rut.png",
        "telefono": "34663413206",
        "historia": "Te vas a México en horas. Todo es impulsivo y sin control.",
    },
    "marta": {
        "img": "img/marta.png",
        "telefono": "34655068171",
        "historia": "Acabas metida en un caos con gatos que no termina nunca.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "telefono": "34676097913",
        "historia": "Cambias completamente tu look y pierdes la noción del tiempo.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "telefono": "34688422600",
        "historia": "Una copa lleva a otra y el plan cambia por completo.",
    },
    "julia": {
        "img": "img/julia.png",
        "telefono": "34615853540",
        "historia": "Una conversación se alarga más de lo esperado.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "telefono": "34635288588",
        "historia": "Te pierdes ayudando a Andrea y todo cambia.",
    },
}

# ========================
# ESTILO
# ========================
st.markdown("""
<style>
body {background-color: #0f0f0f;}
.block {
    background: #1c1c1c;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
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

def reiniciar():
    st.session_state.pantalla = "juego"
    st.session_state.step = 0
    st.session_state.evento = None
    st.session_state.valoracion = None
    st.session_state.desvios = []

def obtener_evento(step):
    eventos = [
        {"texto": "Empieza el día.", "ok": "Seguir", "bad": "Revisar algo"},
        {"texto": "Algo interrumpe.", "ok": "Continuar", "bad": "Pararte"},
        {"texto": "Dudas un momento.", "ok": "Seguir", "bad": "Consultar"},
        {"texto": "Recibes algo.", "ok": "Ignorar", "bad": "Responder"},
        {"texto": "Te cruzas con alguien.", "ok": "Seguir", "bad": "Pararte"},
        {"texto": "Último momento.", "ok": "Continuar", "bad": "Desviarte"},
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

# ========================
# UI
# ========================
st.markdown('<div class="title">Misión: llegar al altar</div>', unsafe_allow_html=True)

# INICIO
if st.session_state.pantalla == "inicio":

    st.markdown('<div class="block text">', unsafe_allow_html=True)
    st.markdown("""
    Tendrás que tomar decisiones sin saber qué pasará.

    Si te desvías, tendrás otra historia.

    Envía captura a cada amiga diciendo si te habría gustado esa vida.

    Luego intenta llegar al final.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Empezar"):
        st.session_state.pantalla = "juego"
        st.rerun()

# JUEGO
elif st.session_state.pantalla == "juego":

    progreso = max(0.0, min(1.0, st.session_state.step / TOTAL_STEPS))
    st.progress(progreso)

    evento = obtener_evento(st.session_state.step)

    st.markdown(f'<div class="block text">{evento["texto"]}</div>', unsafe_allow_html=True)

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

    st.markdown(f'Has elegido a <span class="pink">{amiga_key.upper()}</span>', unsafe_allow_html=True)

    mostrar_imagen(amiga["img"])
    st.markdown(amiga["historia"])

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí"):
            st.session_state.valoracion = "Sí"

    with col2:
        if st.button("No"):
            st.session_state.valoracion = "No"

    if st.session_state.valoracion:
        texto = f"Me he ido contigo y {st.session_state.valoracion.lower()} me habría gustado esta vida"
        url = f"https://wa.me/{amiga['telefono']}?text=" + urllib.parse.quote(texto)

        st.markdown(f"[Enviar por WhatsApp]({url})")

        if st.button("Seguir jugando"):
            st.session_state.pantalla = "juego"
            st.session_state.step += 1
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# WIN
elif st.session_state.pantalla == "win":

    st.balloons()

    tipo = ranking()

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    st.markdown(f"Has llegado al altar\n\nTipo de novia: **{tipo}**")

    if st.button("Jugar otra vez"):
        reiniciar()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
