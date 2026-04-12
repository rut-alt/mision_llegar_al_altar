import streamlit as st
import os

st.set_page_config(layout="centered")

# ========================
# CONFIG
# ========================
TOTAL_STEPS = 6

AMIGAS = {
    "rut": {
        "img": "img/rut.png",
        "historia": "Te vas a México con Rut. En menos de 24 horas estáis en un avión sin mirar atrás. Todo es improvisado, intenso y completamente distinto a lo planeado. No hay boda, pero sí una historia que contar siempre.",
    },
    "marta": {
        "img": "img/marta.png",
        "historia": "Te quedas con Marta ayudando con los gatos. Uno desaparece, otro no para de maullar y el día se convierte en un caos absoluto. El altar deja de ser prioridad.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "historia": "Lorena cambia tu look completamente. Entre pruebas, fotos y dudas, el tiempo desaparece. Cuando te das cuenta, ya es tarde para volver atrás.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "historia": "Empieza con una copa tranquila. Luego otra. La situación se transforma en una noche inesperada que cambia todos los planes.",
    },
    "julia": {
        "img": "img/julia.png",
        "historia": "Lo que iba a ser una llamada rápida se convierte en una conversación larga. El tiempo pasa sin darte cuenta y la decisión se toma sola.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "historia": "Andrea está completamente perdida y decides ayudarla. Das vueltas durante horas sin rumbo claro. El altar queda atrás.",
    },
}

# ========================
# ESTILO VISUAL (NETFLIX)
# ========================
st.markdown("""
<style>
body {
    background-color: #0f0f0f;
}
.block {
    background: #1c1c1c;
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.5);
}
.title {
    font-size: 28px;
    font-weight: bold;
    color: white;
}
.text {
    color: #d1d1d1;
    font-size: 17px;
}
button[kind="primary"] {
    background-color: #e50914;
}
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

def obtener_evento(step):
    eventos = [
        {
            "texto": "Yasmina se despierta el día de su boda.",
            "opciones": [
                {"texto": "Levantarse y empezar el día", "resultado": "ok"},
                {"texto": "Mirar el móvil", "resultado": "rut"},
            ],
        },
        {
            "texto": "Sales de casa y alguien te frena.",
            "opciones": [
                {"texto": "Seguir sin parar", "resultado": "ok"},
                {"texto": "Pararte a hablar", "resultado": "julia"},
            ],
        },
        {
            "texto": "Empiezas a dudar con tu look.",
            "opciones": [
                {"texto": "Seguir con lo planeado", "resultado": "ok"},
                {"texto": "Pedir opinión", "resultado": "lorena"},
            ],
        },
        {
            "texto": "Recibes un mensaje inesperado.",
            "opciones": [
                {"texto": "Ignorarlo", "resultado": "ok"},
                {"texto": "Responder", "resultado": "leslie"},
            ],
        },
        {
            "texto": "Te cruzas con Marta.",
            "opciones": [
                {"texto": "Seguir tu camino", "resultado": "ok"},
                {"texto": "Ayudarla con los gatos", "resultado": "marta"},
            ],
        },
        {
            "texto": "Último momento antes del altar.",
            "opciones": [
                {"texto": "Entrar sin mirar atrás", "resultado": "ok"},
                {"texto": "Ayudar a Andrea", "resultado": "andrea"},
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
    Yasmina, este es tu camino al altar.

    Tendrás que tomar decisiones importantes.

    Tus amigas van a intentar desviarte en todo momento.

    Si tomas otro camino, verás cómo habría sido tu vida con esa decisión.

    Haz una captura de cada historia alternativa y mándasela a esa amiga, diciendo si te habría gustado o no vivir esa vida.

    Después, consigue llegar al altar y haz una última captura.
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

    st.markdown(f"{evento['texto']}")

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

    if st.button("Volver a intentarlo", use_container_width=True):
        reiniciar()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------
# WIN
# ------------------------
elif st.session_state.pantalla == "win":

    st.progress(1.0)

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    st.markdown("""
    Has llegado al altar.

    Haz una captura de este momento y compártelo.
    """)

    if st.button("Jugar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
