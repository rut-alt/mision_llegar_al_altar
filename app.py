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
        "historia": "Te vas a México con Rut en cuestión de horas. Todo es impulsivo, caótico y emocionante. No hay plan, pero sí libertad absoluta.",
    },
    "marta": {
        "img": "img/marta.png",
        "historia": "Te quedas ayudando a Marta con los gatos. El día se convierte en una sucesión de imprevistos y el tiempo desaparece.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "historia": "Terminas cambiando completamente tu look. Entre decisiones y dudas, el tiempo se te escapa.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "historia": "Una copa lleva a otra. El ambiente cambia y el día toma un rumbo totalmente distinto.",
    },
    "julia": {
        "img": "img/julia.png",
        "historia": "La conversación se alarga más de lo esperado. Cuando te das cuenta, ya has tomado otra dirección.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "historia": "Decides ayudar a Andrea. Acabas dando vueltas sin rumbo y alejándote de todo lo planeado.",
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

def obtener_evento(step):
    eventos = [
        {
            "texto": "Empieza el día.",
            "opciones": [
                {"texto": "Seguir con lo previsto", "resultado": "ok"},
                {"texto": "Revisar algo rápido", "resultado": "rut"},
            ],
        },
        {
            "texto": "Algo interrumpe tu camino.",
            "opciones": [
                {"texto": "Continuar", "resultado": "ok"},
                {"texto": "Pararte un momento", "resultado": "julia"},
            ],
        },
        {
            "texto": "Dudas por un instante.",
            "opciones": [
                {"texto": "Seguir adelante", "resultado": "ok"},
                {"texto": "Consultar", "resultado": "lorena"},
            ],
        },
        {
            "texto": "Recibes algo inesperado.",
            "opciones": [
                {"texto": "Ignorarlo", "resultado": "ok"},
                {"texto": "Responder", "resultado": "leslie"},
            ],
        },
        {
            "texto": "Te cruzas con alguien conocido.",
            "opciones": [
                {"texto": "Seguir", "resultado": "ok"},
                {"texto": "Pararte", "resultado": "marta"},
            ],
        },
        {
            "texto": "Último momento antes del final.",
            "opciones": [
                {"texto": "Continuar", "resultado": "ok"},
                {"texto": "Desviarte un momento", "resultado": "andrea"},
            ],
        },
    ]
    return eventos[step]

def elegir(resultado):
    if resultado == "ok":
        st.session_state.step += 1
        if st.session_state.step >= TOTAL_STEPS:
            st.session_state.pantalla = "win"
    else:
        st.session_state.evento = resultado
        st.session_state.pantalla = "game_over"

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

# ========================
# UI
# ========================
st.markdown('<div class="title">Misión: llegar al altar</div>', unsafe_allow_html=True)

# ------------------------
# INICIO
# ------------------------
if st.session_state.pantalla == "inicio":

    st.markdown('<div class="block text">', unsafe_allow_html=True)
    st.markdown("""
    Yasmina, este es tu camino.

    Tendrás que tomar decisiones sin saber qué pasará.

    Si te desvías, descubrirás otra vida posible.

    Haz una captura de cada historia y compártela con esa amiga diciendo si te habría gustado o no vivir esa vida.

    Después, intenta llegar hasta el final.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Empezar", use_container_width=True):
        st.session_state.pantalla = "juego"
        st.rerun()

# ------------------------
# JUEGO
# ------------------------
elif st.session_state.pantalla == "juego":

    progreso = max(0.0, min(1.0, st.session_state.step / TOTAL_STEPS))
    st.progress(progreso)

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    mostrar_imagen("img/yasmina.png", 120)

    evento = obtener_evento(st.session_state.step)
    st.markdown(evento["texto"])

    st.markdown('</div>', unsafe_allow_html=True)

    for opcion in evento["opciones"]:
        if st.button(opcion["texto"], use_container_width=True):
            elegir(opcion["resultado"])
            st.rerun()

# ------------------------
# GAME OVER
# ------------------------
elif st.session_state.pantalla == "game_over":

    amiga = AMIGAS[st.session_state.evento]

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    mostrar_imagen(amiga["img"])
    st.markdown(amiga["historia"])

    st.markdown("¿Te habría gustado esta vida?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Sí"):
            st.session_state.valoracion = "Sí"

    with col2:
        if st.button("No"):
            st.session_state.valoracion = "No"

    if st.session_state.valoracion:
        texto = f"Me he desviado contigo y {st.session_state.valoracion.lower()} me habría gustado esta vida 😏"
        url = "https://wa.me/?text=" + urllib.parse.quote(texto)

        st.markdown(f"[Compartir por WhatsApp]({url})")

        if st.button("Volver a intentarlo", use_container_width=True):
            reiniciar()
            st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# WIN
# ------------------------
elif st.session_state.pantalla == "win":

    st.balloons()  # 🎉 CONFETI

    st.progress(1.0)

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    st.markdown("""
    Has llegado hasta el final.

    Haz una captura y compártelo.
    """)

    if st.button("Jugar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
