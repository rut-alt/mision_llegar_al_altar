# MAPEO DE AMIGAS A IMÁGENES
imagenes_amigas = [
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
    "img/lorena.png",
    "img/leslie.png",
    "img/rut.png",
]

# GRID LIMPIO
for fila in range(SIZE):
    cols = st.columns(SIZE)

    for col in range(SIZE):

        idx = fila * SIZE + col

        with cols[col]:

            hay_yasmina = idx == st.session_state.yasmina
            amigas_en_casilla = [i for i, pos in enumerate(st.session_state.amigas) if pos == idx]

            # 🟢 CASILLA CLICKABLE
            if idx in posibles and not st.session_state.game_over and not st.session_state.win:
                if st.button("⬜", key=f"cell_{idx}", use_container_width=True):
                    mover_yasmina(idx)
                    st.rerun()

            # 🔴 CASILLA NORMAL
            else:
                # ALTAR
                if idx == TOTAL - 1:
                    st.markdown("💒")

                # YASMINA
                if hay_yasmina:
                    st.image("img/yasmina.png", width=60)

                # AMIGAS
                for i in amigas_en_casilla:
                    img = imagenes_amigas[i % len(imagenes_amigas)]
                    st.image(img, width=50)

                # VACÍA
                if not hay_yasmina and not amigas_en_casilla and idx != TOTAL - 1:
                    st.markdown("⬜")
