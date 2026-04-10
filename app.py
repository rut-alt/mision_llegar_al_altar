import streamlit as st
import random
import os

# CONFIG
SIZE = 6
TOTAL = SIZE * SIZE

# INIT
if "yasmina" not in st.session_state:
    st.session_state.yasmina = 0

if "amigas" not in st.session_state:
    st.session_state.amigas = random.sample(range(1, TOTAL-1), 6)

if "game_over" not in st.session_state:
    st.session_state.game_over = False

if "win" not in st.session_state:
    st.session_state.win = False


def reiniciar():
    st.session_state.yasmina = 0
    st.session_state.amigas = random.sample(range(1, TOTAL-1), 6)
    st.session_state.game_over = False
    st.session_state.win = False


# 🔹 MOSTRAR IMAGEN SEGURA
def mostrar_imagen(path, size=50, fallback="⬜"):
    if os.path.exists(path):
        st.image(path, width=size)
    else:
        st.markdown(f"<div style='font-size:28px'>{fallback}</div>", unsafe_allow_html=True)


# 🔹 MOVIMIENTO CONTIGUO
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


# 🔹 MOVER AMIGAS
def mover_amigas():
    nuevas = []
    ocupadas = set()

    for pos in st.session_state.amigas:
        posibles = vecinos(pos)
        random.shuffle(posibles)

        for p in posibles:
            if p not in ocupadas:
                nuevas.append(p)
                ocupadas.add(p)
                break
        else:
            nuevas.append(pos)

    st.session_state.amigas = nuevas


# 🔹 MOVER YASMINA
def mover_yasmina(destino):
    st.session_state.yasmina = destino

    mover_amigas()

    if destino in st.session_state.amigas:
        st.session_state.game_over = True

    if destino == TOTAL - 1:
        st.session_state.win = True


# UI
st.set_page_config(layout="centered")
st.title("💍 MISIÓN: LLEGAR AL ALTAR")

y = st.session_state.yasmina
posibles = vecinos(y)

# 📸 IMÁGENES AMIGAS
imagenes_amigas = [
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
]

# GRID
# GRID PRO
for fila in range(SIZE):
    cols = st.columns(SIZE)

    for col in range(SIZE):

        idx = fila * SIZE + col

        with cols[col]:

            hay_yasmina = idx == st.session_state.yasmina
            amigas_en_casilla = [i for i, pos in enumerate(st.session_state.amigas) if pos == idx]

            # 🎨 ESTILO CASILLA
            es_clickable = idx in posibles and not st.session_state.game_over and not st.session_state.win

            color = "#ffffff"
            borde = "2px solid #ccc"

            if es_clickable:
                color = "#e8f7ff"   # azul claro clickable
                borde = "2px solid #00aaff"

            if idx == TOTAL - 1:
                color = "#eaffea"   # altar verde

            # 📦 CONTENIDO HTML
            contenido = ""

            if idx == TOTAL - 1:
                contenido += "<div style='font-size:24px'>💒</div>"

            if hay_yasmina:
                contenido += "<img src='img/yasmina.png' width='40'>"

            for i in amigas_en_casilla:
                img = imagenes_amigas[i % len(imagenes_amigas)]
                contenido += f"<img src='{img}' width='35'>"

            if not hay_yasmina and not amigas_en_casilla and idx != TOTAL - 1:
                contenido += "⬜"

            # 🟦 CASILLA VISUAL
            st.markdown(
                f"""
                <div style="
                    background:{color};
                    border:{borde};
                    height:70px;
                    display:flex;
                    flex-direction:column;
                    align-items:center;
                    justify-content:center;
                    border-radius:10px;
                ">
                    {contenido}
                </div>
                """,
                unsafe_allow_html=True
            )

            # 👇 CLICK ENCIMA
            if es_clickable:
                if st.button(" ", key=f"click_{idx}", use_container_width=True):
                    mover_yasmina(idx)
                    st.rerun()


# GAME OVER
if st.session_state.game_over:
    st.error("💥 ¡UNA AMIGA TE HA PARADO! ¡NO TE CASES!")
    if st.button("🔁 Reiniciar"):
        reiniciar()
        st.rerun()


# WIN
if st.session_state.win:
    st.success("💒 ¡HAS LLEGADO AL ALTAR!")
    if st.button("🔁 Otra vez"):
        reiniciar()
        st.rerun()
