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
        "img": "img/mexico1.png",
        "telefono": "34663413206",
        "historia": "¿Para qué miras el móvil? Te vas a México en horas. Rut ha encontrado vuelos por menos de 300€ y ha cogido uno para cada una. Todo es impulsivo y sin control. Con las prisas, ha cogido solo billetes de ida. No tenéis dinero para volver a España y montáis un puesto de quesadillas en una playa.",
    },
    "marta": {
        "img": "img/gatos1.png",
        "telefono": "34655068171",
        "historia": "Marta te ha pedido que vayas a darle de comer a los gatos. Acabas metida en un caos gatuno que no termina nunca. Pero la cosa es que te gusta, terminas convirtiendote en mamá de gatos como Marta y decides no casarte, total, estos son mas peluditos.",
    },
    "lorena": {
        "img": "img/uber1.png",
        "telefono": "34676097913",
        "historia": "Lori te pide que vayas a recogerla a Atocha porque, por qué iba a gastar ella dinero en pedir un uber? No la encuentras, tus nociones de encontrar pasajeros en las estaciones se han esfumado y te quedas dando vueltas en bucle por Atocha. No llegas al altar.",
    },
    "leslie": {
        "img": "img/matcha1.png",
        "telefono": "34688422600",
        "historia": "Te encuentras con Leslie en una cafetería tomando un matcha y pides otro. Una cosa lleva a la otra y esos matchas se convierten en copas . Una copa lleva a otra y el plan cambia por completo. Nunca llegas a la boda.",
    },
    "julia": {
        "img": "img/julia.png",
        "telefono": "34615853540",
        "historia": "Julia te llama por telefono para pedirte opinión sobre algot. Cuando empiezas a hablar con Julia, sabes cuándo empieza pero nunca cuándo acaba. La conversación se alarga más de lo esperado y nunca llegas al altar.",
    },
    "andrea": {
        "img": "img/andrea.png",
        "telefono": "34635288588",
        "historia": "Andrea te llama a última hora para decirte que no le convence el vestido. Te pierdes ayudando a Andrea, ya no te convence tampoco tu vestido y todo cambia.",
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
    if os.path.exists(file_path):
        with open(file_path, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()

        st.markdown(f"""
        <audio autoplay loop>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """, unsafe_allow_html=True)

def carrusel_fotos():

    # 🔄 SPINNER
    with st.spinner("Cargando recuerdos..."):
        fotos = glob.glob("img/foto*.png")

        def ordenar(f):
            nums = re.findall(r'\d+', f)
            return int(nums[0]) if nums else 0

        fotos = sorted(fotos, key=ordenar)
        time.sleep(2)

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
        st.warning("No hay fotos cargadas")

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
        {"texto": "Hoy todo cambia. Empieza el día de tu boda y lo primero que haces es.", "ok": "Tomar un café", "bad": "Mirar el móvil"},
        {"texto": "Algo interrumpe, Marta necesita que vayas a dar de comer a los gatos.", "ok": "Decirle que no tienes tiempo", "bad": "Ir a dar de comer a los gatos"},
        {"texto": "Lorena te llama para que la recojas.", "ok": "Que se pida un Uber", "bad": "Ir a recogerla."},
        {"texto": "Ves a alguien familiar en una cafetería.", "ok": "Ignorar", "bad": "Entrar a mirar quién es."},
        {"texto": "Llamada de Julia, que querrá?", "ok": "Son eternas, ni loca.", "bad": "Veamos qué quiere."},
        {"texto": "Último momento, llamada de Andrea.", "ok": "Colgar, no es tan urgente", "bad": "Ver qué quiere."},
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
    Hola, sabemos que dentro de poco serás una mujer casada, pero tus amigas no van a ponertelo nada fácil.Intenta llegar al altar.
    Tendrás que tomar decisiones sin saber qué pasará.
    Si te desvías, tendrás otra historia. Solo tú eres dueña de tu destino.
    ¿Ayudarás a tus amigas? ¿Son realmente tu prioridad?
    Suerte en este pequeño viaje.
    Envía captura a cada amiga diciendo si te habría gustado tu vida en un universo paralelo creado con cada decisión tomada.

    """)
    st.markdown('</div>', unsafe_allow_html=True)

    if st.button("Empezar"):
        st.session_state.pantalla = "juego"
        st.rerun()

# JUEGO
elif st.session_state.pantalla == "juego":

    progreso = max(0.0, min(1.0, st.session_state.step / TOTAL_STEPS))
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

    if not st.session_state.confetti:
        st.balloons()
        st.session_state.confetti = True

    tipo = ranking()

    st.markdown('<div class="block text">', unsafe_allow_html=True)

    st.markdown(f"""
    Has llegado al altar.

    Tipo de novia: **{tipo}**

    Aquí tienes vuestro resumen.
    NO CIERRES ESTA PANTALLA.
    ESPERA QUE CARGUE Y DISFRUTA! 
    """)

    st.markdown('</div>', unsafe_allow_html=True)

    autoplay_audio("audio/musica.mp3")

    st.markdown("### Vuestra vida")
    carrusel_fotos()

    if st.button("Jugar otra vez"):
        reiniciar()
        st.rerun()
