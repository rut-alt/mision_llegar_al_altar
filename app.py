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
        "historia": "Te vas a México con Rut. En 48 horas estáis en una playa perdida. No hubo boda, pero sí una historia inolvidable.",
    },
    "marta": {
        "img": "img/marta.png",
        "historia": "Te quedas ayudando a Marta con los gatos. El caos se apodera del día y el altar deja de existir.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "historia": "Lorena cambia todo tu look. Entre pruebas y dudas, el tiempo se esfuma.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "historia": "Empieza con una copa… y acaba siendo una noche que cambia los planes.",
    },
    "julia": {
        "img": "img/julia.png",
        "historia": "La llamada se alarga más de lo esperado. El tiempo pasa y la decisión se toma sola.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "historia": "Andrea está perdida y decides ayudarla. El altar queda cada vez más lejos.",
    },
}

# ========================
# ESTILOS
# ========================
st.markdown("""
<style>
.block {
    background: #ffffff;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.08);
    margin-bottom: 20px;
}
.title {
    font-size: 26px;
    font-weight: bold;
}
.subtitle {
    font-size: 18px;
    color: #555;
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
    # 👉 reinicia DIRECTO al juego
    st.session_state.pantalla = "juego"
    st.session_state.step = 0
    st.session_state.evento = None
    st.session_state.historia_alt = False

def obtener_evento(step):
    eventos = [
        {
            "texto": "Yasmina se despierta el día de su boda.",
            "opciones": [
                {"texto": "Levantarse y empezar", "resultado": "ok"},
                {"texto": "Mirar el móvil", "resultado": "rut"},
            ],
        },
        {
            "texto": "Sales de casa y alguien te frena.",
            "opciones": [
                {"texto": "Seguir sin parar", "resultado": "ok"},
                {"texto": "Pararte", "resultado": "julia"},
            ],
        },
        {
            "texto": "Dudas con lo que llevas puesto.",
            "opciones": [
                {"texto": "Seguir igual", "resultado": "ok"},
                {"texto": "Pedir opinión", "resultado": "lorena"},
            ],
        },
        {
            "texto": "Recibes un mensaje.",
            "opciones": [
                {"texto": "Ignorarlo", "resultado": "ok"},
                {"texto": "Responder", "resultado": "leslie"},
            ],
        },
        {
            "texto": "Te cruzas con Marta.",
            "opciones": [
                {"texto": "Seguir", "resultado": "ok"},
                {"texto": "Ayudar con los gatos", "resultado": "marta"},
            ],
        },
        {
            "texto": "Último momento antes del altar.",
            "opciones": [
                {"texto": "Entrar", "resultado": "ok"},
                {"texto": "Ayudar a Andrea", "resultado": "andrea"},
            ],
        },
    ]
    return eventos[step]

def elegir(resultado):
    if resultado == "ok":
        st.session_state.step += 1
        if st.session_state.step >= TOTAL_STEPS:
            st.session_state.step = TOTAL_STEPS
            st.session_state.pantalla = "win"
    else:
        st.session_state.evento = resultado
        st.session_state.pantalla = "game_over"

# ========================
# INIT STATE
# ========================
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "step" not in st.session_state:
    st.session_state.step = 0

if "evento" not in st.session_state:
    st.session_state.evento = None

if "historia_alt" not in st.session_state:
    st.session_state.historia_alt = False

# ========================
# UI
# ========================
st.markdown('<div class="title">Misión: llegar al altar</div>', unsafe_allow_html=True)

# ------------------------
# INICIO
# ------------------------
if st.session_state.pantalla == "inicio":

    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.markdown("""
    Yasmina, este es tu camino al altar.

    Tendrás que tomar decisiones importantes.

    Tus amigas van a intentar desviarte en todo momento.

    Si eliges otro camino, podrás ver cómo habría sido tu vida.

    Haz capturas y compártelas.
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Empezar", use_container_width=True):
        st.session_state.pantalla = "juego"
        st.rerun()

# ------------------------
# JUEGO
# ------------------------
elif st.session_state.pantalla == "juego":

    st.session_state.step = max(0, min(TOTAL_STEPS, st.session_state.step))

    progreso = st.session_state.step / TOTAL_STEPS if TOTAL_STEPS > 0 else 0
    progreso = max(0.0, min(1.0, progreso))

    st.progress(progreso)

    st.markdown('<div class="block">', unsafe_allow_html=True)

    mostrar_imagen("img/yasmina.png", 120)

    evento = obtener_evento(st.session_state.step)

    st.markdown(f'<div class="subtitle">{evento["texto"]}</div>', unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    for opcion in evento["opciones"]:
        if st.button(opcion["texto"], use_container_width=True):
            elegir(opcion["resultado"])
            st.rerun()

# ------------------------
# GAME OVER
# ------------------------
elif st.session_state.pantalla == "game_over":

    amiga = AMIGAS[st.session_state.evento]

    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.markdown("Has tomado otro camino")

    mostrar_imagen(amiga["img"])

    if not st.session_state.historia_alt:
        if st.button("Ver historia alternativa", use_container_width=True):
            st.session_state.historia_alt = True
            st.rerun()
    else:
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

    st.markdown('<div class="block">', unsafe_allow_html=True)

    st.markdown("Has llegado al altar")

    st.markdown("""
    Haz una captura de este momento.

    Compártelo y demuestra que lo has conseguido.
    """)

    if st.button("Jugar otra vez", use_container_width=True):
        reiniciar()
        st.rerun()

    st.markdown('</div>', unsafe_allow_html=True)
