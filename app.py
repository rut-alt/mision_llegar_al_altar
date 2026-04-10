import streamlit as st
import random

# CONFIG
SIZE = 6
TOTAL = SIZE * SIZE
ALTAR = TOTAL - 1

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


# 🔹 vecinos contiguos
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


# 🔹 mover amigas (SIN entrar en altar)
def mover_amigas():
    nuevas = []
    ocupadas = set()

    for pos in st.session_state.amigas:
        posibles = vecinos(pos)
        posibles = [p for p in posibles if p != ALTAR]  # 🔥 clave

        random.shuffle(posibles)

        for p in posibles:
            if p not in ocupadas:
                nuevas.append(p)
                ocupadas.add(p)
                break
        else:
            nuevas.append(pos)

    st.session_state.amigas = nuevas


# 🔹 mover yasmina
def mover_yasmina(destino):
    st.session_state.yasmina = destino

    # ganar primero
    if destino == ALTAR:
        st.session_state.win = True
        return

    mover_amigas()

    if destino in st.session_state.amigas:
        st.session_state.game_over = True


# UI
st.set_page_config(layout="centered")
st.title("💍 MISIÓN: LLEGAR AL ALTAR")

y = st.session_state.yasmina
posibles = vecinos(y)

# imágenes amigas
imagenes_amigas = [
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
]

# GRID REAL
for fila in range(SIZE):
    cols = st.columns(SIZE)

    for col in range(SIZE):
        idx = fila * SIZE + col

        with cols[col]:

            hay_yasmina = idx == st.session_state.yasmina
            amigas_en_casilla = [i for i, pos in enumerate(st.session_state.amigas) if pos == idx]

            es_clickable = idx in posibles and not st.session_state.game_over and not st.session_state.win

            # 🎨 estilo
            color = "#ffffff"
            if es_clickable:
                color = "#e8f7ff"
            if idx == ALTAR:
                color = "#d4f5d4"

            # 🟦 CAJA
            box = st.container()

            with box:
                st.markdown(
                    f"""
                    <div style="
                        background:{color};
                        border:2px solid #ccc;
                        height:90px;
                        border-radius:12px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                    ">
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                # 👇 CONTENIDO (AHORA BIEN)
                if idx == ALTAR:
                    st.image("img/altar.png", width=45)

                elif hay_yasmina:
                    st.image("img/yasmina.png", width=45)

                else:
                    for i in amigas_en_casilla:
                        st.image(imagenes_amigas[i], width=40)

            # 👇 CLICK
            if es_clickable:
                if st.button("Mover", key=f"move_{idx}", use_container_width=True):
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
