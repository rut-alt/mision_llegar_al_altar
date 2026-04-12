import streamlit as st
import os

st.set_page_config(layout="centered")

# CONFIG
TOTAL_STEPS = 6

AMIGAS = {
    "rut": {
        "img": "img/rut.png",
        "historia": "Te vas a México con Rut. En 48 horas estáis en una playa perdida, sin cobertura, pero con la sensación de que habéis hecho lo correcto. Nunca llegaste al altar, pero esa historia nadie te la quita.",
    },
    "marta": {
        "img": "img/marta.png",
        "historia": "Te quedas ayudando a Marta con los gatos. Uno se escapa, otro se esconde y acabas pasando el día entero buscándolos. La boda pasa a segundo plano y el caos gana.",
    },
    "lorena": {
        "img": "img/lorena.png",
        "historia": "Lorena te cambia el look a última hora. Entre pruebas, fotos y dudas, el tiempo vuela. Cuando te das cuenta, el altar ya no es una opción.",
    },
    "leslie": {
        "img": "img/leslie.png",
        "historia": "Empiezas con una copa con Leslie. Luego otra. Luego otra. La boda se convierte en una anécdota lejana y la noche en algo legendario.",
    },
    "julia": {
        "img": "img/julia.png",
        "historia": "Julia te engancha al teléfono. Lo que iba a ser una llamada rápida se convierte en horas de conversación. El tiempo pasa y la decisión ya está tomada.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "historia": "Andrea está perdida y decides ayudarla. Das vueltas durante horas sin rumbo claro. El altar queda cada vez más lejos.",
    },
}

# FUNCION IMAGEN SEGURA
def mostrar_imagen(ruta, width=150):
    if os.path.exists(ruta):
        st.image(ruta, width=width)

# INIT
if "step" not in st.session_state:
    st.session_state.step = -1  # pantalla inicial

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "win" not in st.session_state:
    st.session_state.win = False

if "evento" not in st.session_state:
    st.session_state.evento = None

if "historia_alt" not in st.session_state:
    st.session_state.historia_alt = False


def reiniciar():
    st.session_state.step = -1
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None
    st.session_state.historia_alt = False


# HISTORIA PRINCIPAL
def obtener_evento(step):
    eventos = [
        {
            "texto": "Yasmina se despierta el día de su boda. Todo empieza ahora.",
            "opciones": [
                {"texto": "Levantarse y empezar el día", "resultado": "ok"},
                {"texto": "Mirar el móvil nada más despertarse", "resultado": "rut"},
            ],
        },
        {
            "texto": "Sales de casa y alguien te frena en seco.",
            "opciones": [
                {"texto": "Seguir caminando sin parar", "resultado": "ok"},
                {"texto": "Pararte a hablar", "resultado": "julia"},
            ],
        },
        {
            "texto": "Empiezas a dudar con todo lo que llevas encima.",
            "opciones": [
                {"texto": "Seguir con lo planeado", "resultado": "ok"},
                {"texto": "Pedir opinión", "resultado": "lorena"},
            ],
        },
        {
            "texto": "Recibes un mensaje inesperado.",
            "opciones": [
                {"texto": "Ignorarlo y seguir", "resultado": "ok"},
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
                {"texto": "Ayudar a Andrea que está perdida", "resultado": "andrea"},
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
st.title("Misión: llegar al altar")

# PANTALLA INICIAL
if st.session_state.step == -1:
    st.markdown("""
    ### Instrucciones

    Yasmina, este es tu camino al altar.

    Tendrás que avanzar tomando decisiones. Concéntrate.

    Tus amigas van a intentar distraerte hasta el final.

    Si te encuentras con alguna de ellas, podrás ver cómo habría sido tu vida si hubieras elegido ese camino.

    Haz una captura de tu historia alternativa y envíasela por privado.

    Después, intenta llegar al altar y haz una captura final del resultado.
    """)

    if st.button("Empezar"):
        st.session_state.step = 0
        st.rerun()


# JUEGO
elif not st.session_state.game_over and not st.session_state.win:
    progreso = st.session_state.step / TOTAL_STEPS
    st.progress(progreso)

    mostrar_imagen("img/yasmina.png", 120)

    evento = obtener_evento(st.session_state.step)

    st.markdown(f"## {evento['texto']}")

    for opcion in evento["opciones"]:
        if st.button(opcion["texto"], use_container_width=True):
            elegir(opcion["resultado"])
            st.rerun()


# GAME OVER
elif st.session_state.game_over:
    amiga = AMIGAS[st.session_state.evento]

    st.markdown("### Has tomado otro camino")

    mostrar_imagen(amiga["img"])

    if not st.session_state.historia_alt:
        if st.button("Ver cómo habría sido tu vida con esta decisión"):
            st.session_state.historia_alt = True
            st.rerun()
    else:
        st.markdown(f"#### {amiga['historia']}")

        if st.button("Volver a intentarlo"):
            reiniciar()
            st.rerun()


# WIN
elif st.session_state.win:
    st.progress(1.0)

    st.markdown("### Has llegado al altar")

    if st.button("Jugar otra vez"):
        reiniciar()
        st.rerun()
