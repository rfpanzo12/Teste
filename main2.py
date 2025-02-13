import streamlit as st

st.title("📚 Progresso na Graduação")

# Entrada de dados
curso = st.text_input("Nome do curso:")
nome = st.text_input("Nome do estudante:")
total_creditos = st.number_input("Total de créditos ou carga horária do curso:", min_value=1, step=1)

concluidos = st.number_input("Créditos ou carga horária concluída:", min_value=0, max_value=total_creditos, step=1)

# Cálculo e exibição do progresso
if st.button("Calcular"):
    if not curso.strip():
        st.error("Por favor, insira o nome do curso.")
    elif not nome.strip():
        st.error("Por favor, insira o seu nome.")
    else:
        porcentagem = (concluidos / total_creditos) * 100
        st.subheader(f"📖 Curso: {curso}")
        st.write(f"📊 Progresso: **{porcentagem:.2f}%** concluído")
        st.progress(porcentagem / 100)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido por **Rufino Sérgio Panzo** @2025")
