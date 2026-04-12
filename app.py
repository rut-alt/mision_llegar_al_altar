import streamlit as st
import os

st.set_page_config(layout="centered")

# CONFIG
TOTAL_STEPS = 6

AMIGAS = {
    "rut": {
        "img": "img/rut.png",
        "historia": "Te vas a México con Rut. En 48 horas estáis en una playa perdida. No hubo boda, pero sí una historia que nadie puede quitarte.",
    },
    "marta": {
        "img": "img/marta.png",
        "historia": "Te quedas ayudando a Marta con los gatos. El caos escala y el día desaparece. El altar deja de importar.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "historia": "Lorena te cambia el look. El tiempo vuela entre pruebas y dudas. Cuando reaccionas, ya es tarde.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "historia": "Empieza con una copa. Luego otra. El día se transforma en una noche que lo cambia todo.",
    },
    "julia": {
        "img": "img/julia.png",
        "historia": "La llamada se alarga más de lo esperado. El tiempo pasa y la decisión ya está tomada.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "historia": "Decides ayudar a Andrea. Das vueltas sin rumbo y el altar queda atrás.",
    },
}

# FUNCION IMAGEN SEGURA
def mostrar_imagen(ruta, width=150):
    if os.path.exists(ruta):
        st.image(ruta, width=width)
    else:
        st.warning(f"No se encuentra la imagen: {ruta}")

# INIT
if "pantalla" not in st.session_state:
    st.session_state.pantalla = "inicio"

if "step" not in st.session_state:
    st.session_state.step = 0

if "evento" not in st.session_state:
    st.session_state.evento = None

if "historia_alt" not in st.session_state:
    st.session_state.historia_alt = False


def reiniciar():
    st.session_state.pantalla = "inicio"
    st.session_state.step = 0
    st.session_state.evento = None
    st.session_state.historia_alt = False


# HISTORIA
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


# UI
st.title("Misión: llegar al altar")

# 👉 INICIO
if st.session_state.pantalla == "inicio":

    st.markdown("""
    ### Instrucciones

    Yasmina, este es tu camino al altar.

    Tendrás que avanzar tomando decisiones. Concéntrate.

    Tus amigas van a intentar desviarte en todo momento.

    Si eliges mal, podrás ver cómo habría sido tu vida con esa decisión.

    Haz una captura de ese momento y compártelo.

    Después, intenta llegar al altar.
    """)

    if st.button("Empezar"):
        st.session_state.pantalla = "juego"
        st.rerun()


# 👉 JUEGO
elif st.session_state.pantalla == "juego":

    # proteger step
    st.session_state.step = max(0, min(TOTAL_STEPS, st.session_state.step))

    progreso = st.session_state.step / TOTAL_STEPS if TOTAL_STEPS > 0 else 0
    progreso = max(0.0, min(1.0, progreso))

    st.progress(progreso)

    mostrar_imagen("img/yasmina.png", 120)

    evento = obtener_evento(st.session_state.step)

    st.markdown(f"## {evento['texto']}")

    for opcion in evento["opciones"]:
        if st.button(opcion["texto"], use_container_width=True):
            elegir(opcion["resultado"])
            st.rerun()


# 👉 GAME OVER
elif st.session_state.pantalla == "game_over":

    amiga = AMIGAS[st.session_state.evento]

    st.markdown("### Has tomado otro camino")

    mostrar_imagen(amiga["img"])

    if not st.session_state.historia_alt:
        if st.button("Ver historia alternativa"):
            st.session_state.historia_alt = True
            st.rerun()
    else:
        st.markdown(amiga["historia"])

        if st.button("Volver a intentarlo"):
            reiniciar()
            st.rerun()


# 👉 WIN
elif st.session_state.pantalla == "win":

    st.progress(1.0)
    st.markdown("### Has llegado al altar")

    if st.button("Jugar otra vez"):
        reiniciar()
        st.rerun()
