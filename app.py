import streamlit as st
import random

# CONFIG
SIZE = 6
TOTAL = SIZE * SIZE
ALTAR = TOTAL - 1

# AMIGAS (AHORA CON MENSAJE)
AMIGAS = [
    {"nombre": "Lorena", "msg": "💅 ¡Outfit urgente!", "img": "img/lorena.png"},
    {"nombre": "Leslie", "msg": "🍷 He abierto vino...", "img": "img/leslie.png"},
    {"nombre": "Rut", "msg": "😏 Sin mí no hay boda", "img": "img/rut.png"},
    {"nombre": "Marta", "msg": "🔥 Drama máximo", "img": "img/lorena.png"},
    {"nombre": "Julia", "msg": "📞 Llámame YA", "img": "img/leslie.png"},
    {"nombre": "Andrea", "msg": "🚗 Estoy perdida", "img": "img/rut.png"},
]

# INIT
if "yasmina" not in st.session_state:
    st.session_state.yasmina = 0

if "amigas" not in st.session_state:
    st.session_state.amigas = random.sample(range(1, TOTAL-1), 6)

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "win" not in st.session_state:
    st.session_state.win = False

# 🔥 NUEVO
if "evento" not in st.session_state:
    st.session_state.evento = None


def reiniciar():
    st.session_state.yasmina = 0
    st.session_state.amigas = random.sample(range(1, TOTAL-1), 6)
    st.session_state.game_over = False
    st.session_state.win = False
    st.session_state.evento = None


# MOVIMIENTOS
def vecinos(pos):
    fila = pos // SIZE
    col = pos % SIZE

    opciones = []

    if col > 0:
        opciones.append(pos - 1)
    if col < SIZE - 1:
        opciones.append(pos + 1)
    if fila > 0:
        opciones.append(pos - SIZE)
    if fila < SIZE - 1:
        opciones.append(pos + SIZE)

    return opciones


# 🔹 MOVER AMIGAS (SIN ALTAR)
def mover_amigas():
    nuevas = []
    ocupadas = set()

    for pos in st.session_state.amigas:
        posibles = [p for p in vecinos(pos) if p != ALTAR]
        random.shuffle(posibles)

        for p in posibles:
            if p not in ocupadas:
                nuevas.append(p)
                ocupadas.add(p)
                break
        else:
            nuevas.append(pos)

    st.session_state.amigas = nuevas


# 🔹 MOVER YASMINA (AQUÍ ESTÁ LA CLAVE)
def mover_yasmina(destino):

    # mover yasmina
    st.session_state.yasmina = destino

    # ganar directo
    if destino == ALTAR:
        st.session_state.win = True
        return

    # mover amigas
    mover_amigas()

    # 💥 detectar QUIÉN te pilla
    for i, pos in enumerate(st.session_state.amigas):
        if pos == destino:
            st.session_state.game_over = True
            st.session_state.evento = AMIGAS[i]
            return


# UI
st.set_page_config(layout="centered")
st.title("💍 MISIÓN: LLEGAR AL ALTAR")

y = st.session_state.yasmina
posibles = vecinos(y)

# GRID
for fila in range(SIZE):
    cols = st.columns(SIZE)

    for col in range(SIZE):
        idx = fila * SIZE + col

        with cols[col]:

            hay_yasmina = idx == st.session_state.yasmina
            amigas_en_casilla = [i for i, pos in enumerate(st.session_state.amigas) if pos == idx]

            es_clickable = idx in posibles and not st.session_state.game_over and not st.session_state.win

            # estilo
            color = "#ffffff"
            borde = "2px solid #ccc"

            if es_clickable:
                color = "#e8f7ff"
                borde = "2px solid #00aaff"

            if idx == ALTAR:
                color = "#eaffea"

            # contenido
            contenido = ""

            if idx == ALTAR:
                contenido = "💒"
            elif hay_yasmina:
                contenido = "👰"
            elif amigas_en_casilla:
                contenido = "👯"
            else:
                contenido = ""

            st.markdown(
                f"""
                <div style="
                    background:{color};
                    border:{borde};
                    height:80px;
                    border-radius:10px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    font-size:28px;
                ">
                    {contenido}
                </div>
                """,
                unsafe_allow_html=True
            )

            if es_clickable:
                if st.button("Mover", key=f"move_{idx}", use_container_width=True):
                    mover_yasmina(idx)
                    st.rerun()


# 💥 GAME OVER (AHORA PERSONALIZADO)
if st.session_state.game_over:
    amiga = st.session_state.evento

    if amiga:
        st.error(f"💥 HAS COINCIDIDO CON {amiga['nombre'].upper()}")
        st.markdown(f"### {amiga['msg']}")
    else:
        st.error("💥 ¡TE HAN PILLADO!")

    if st.button("🔁 Reiniciar"):
        reiniciar()
        st.rerun()


# WIN
if st.session_state.win:
    st.success("💒 ¡HAS LLEGADO AL ALTAR!")

    if st.button("🔁 Otra vez"):
        reiniciar()
        st.rerun()
