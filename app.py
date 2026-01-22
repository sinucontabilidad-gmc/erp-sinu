import streamlit as st

st.set_page_config(page_title="ERP SINU", layout="wide")

st.title("🛁 ERP CONTABLE — SINU")

menu = st.sidebar.radio(
    "Menú principal",
    [
        "Inicio",
        "Registrar ingreso",
        "Registrar gasto",
        "Estados financieros"
    ]
)

if menu == "Inicio":
    st.subheader("Bienvenida")
    st.success("ERP SINU operativo desde iPad ✅")

elif menu == "Registrar ingreso":
    st.subheader("Registrar ingreso")
    monto = st.number_input("Monto del ingreso", min_value=0)
    if st.button("Guardar ingreso"):
        st.success(f"Ingreso registrado por ${monto:,.0f}")

elif menu == "Registrar gasto":
    st.subheader("Registrar gasto")
    monto = st.number_input("Monto del gasto", min_value=0)
    if st.button("Guardar gasto"):
        st.warning(f"Gasto registrado por ${monto:,.0f}")

elif menu == "Estados financieros":
    st.subheader("Estados financieros")
    st.info("Aquí se mostrarán los estados financieros")
