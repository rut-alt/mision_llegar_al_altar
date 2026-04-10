import streamlit as st
import random

# CONFIG
SIZE = 10
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

    # choque
    if destino in st.session_state.amigas:
        st.session_state.game_over = True

    # win
    if destino == TOTAL-1:
        st.session_state.win = True

# UI
st.set_page_config(layout="wide")

st.title("💍 MISIÓN: LLEGAR AL ALTAR")

# GRID HTML REAL
<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    👯
</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>

</div>

<div style='
    border:2px solid #999;
    height:60px;
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:24px;
    border-radius:6px;
'>
    💒
</div>
</div>
