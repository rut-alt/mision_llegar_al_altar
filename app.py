import streamlit as st
import random

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


# MOVIMIENTO AMIGAS
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
st.set_page_config(layout="centered")
st.title("💍 MISIÓN: LLEGAR AL ALTAR")

y = st.session_state.yasmina

# movimientos posibles (solo 1 casilla)
posibles = [y+1, y-1, y+SIZE, y-SIZE]
posibles = [p for p in posibles if 0 <= p < TOTAL]

# GRID SERPIENTE
for fila in range(SIZE):
    cols = st.columns(SIZE)

    for col in range(SIZE):

        # zig-zag visual
        if fila % 2 == 0:
            idx = fila * SIZE + col
        else:
            idx = fila * SIZE + (SIZE - 1 - col)

        with cols[col]:

            contenido = "⬜"

            if idx == TOTAL - 1:
                contenido = "💒"
            elif idx == st.session_state.yasmina:
                contenido = "👰"
            elif idx in st.session_state.amigas:
                contenido = "👯"

            # CLICK SOLO SI ES MOVIMIENTO VÁLIDO
            if idx in posibles and not st.session_state.game_over and not st.session_state.win:
                if st.button(contenido, key=f"cell_{idx}", use_container_width=True):
                    mover_yasmina(idx)
                    st.rerun()
            else:
                st.markdown(f"<div style='text-align:center; font-size:28px; padding:10px'>{contenido}</div>", unsafe_allow_html=True)


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
