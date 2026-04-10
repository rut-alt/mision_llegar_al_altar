import streamlit as st
import random

# CONFIG
SIZE = 10
TOTAL = SIZE * SIZE

# INIT ESTABLE
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


def mover_amigas():
    nuevas = []
    ocupadas = set()

    for pos in st.session_state.amigas:
        posibles = [pos-1, pos+1, pos-SIZE, pos+SIZE]
        posibles = [p for p in posibles if 0 <= p < TOTAL]

        random.shuffle(posibles)

        for p in posibles:
            if p not in ocupadas:
                nuevas.append(p)
                ocupadas.add(p)
                break
        else:
            nuevas.append(pos)

    st.session_state.amigas = nuevas


def mover_yasmina(destino):
    st.session_state.yasmina = destino

    mover_amigas()

    if destino in st.session_state.amigas:
        st.session_state.game_over = True

    if destino == TOTAL - 1:
        st.session_state.win = True


# UI
st.set_page_config(layout="wide")
st.title("💍 MISIÓN: LLEGAR AL ALTAR")

# GRID REAL
grid_html = "<div style=\"display:grid; grid-template-columns: repeat(10, 1fr); gap:5px;\">"

for i in range(TOTAL):

    contenido = ""

    if i == TOTAL - 1:
        contenido = "💒"
    elif i == st.session_state.yasmina:
        contenido = "👰"
    elif i in st.session_state.amigas:
        contenido = "👯"

    grid_html += f"""
    <div style=\"border:2px solid #999; height:60px; display:flex; align-items:center; justify-content:center; font-size:24px; border-radius:6px;\">
        {contenido}
    </div>
    """

grid_html += "</div>"

st.markdown(grid_html, unsafe_allow_html=True)


# MOVIMIENTO
st.markdown("### Movimiento")

y = st.session_state.yasmina
posibles = [y+1, y-1, y+SIZE, y-SIZE]
posibles = [p for p in posibles if 0 <= p < TOTAL]

cols = st.columns(len(posibles))

for i, p in enumerate(posibles):
    with cols[i]:
        if st.button(f"Ir a {p}", use_container_width=True):
            mover_yasmina(p)
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
