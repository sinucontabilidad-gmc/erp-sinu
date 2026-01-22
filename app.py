# Estado inicial en memoria
if "caja" not in st.session_state:
    st.session_state.caja = 0

if "ingresos" not in st.session_state:
    st.session_state.ingresos = 0

if "gastos" not in st.session_state:
    st.session_state.gastos = 0

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

elif menu == "Registrar gasto":
    st.subheader("Registrar gasto")

    monto = st.number_input("Monto del gasto", min_value=0)
    if st.button("Guardar gasto"):
        st.session_state.gastos += monto
        st.session_state.caja -= monto
        st.warning(f"Gasto registrado por ${monto:,.0f}")
    st.subheader("Registrar gasto")
    monto = st.number_input("Monto del gasto", min_value=0)
    if st.button("Guardar gasto"):
        st.warning(f"Gasto registrado por ${monto:,.0f}")
elif menu == "Estados financieros":
    st.subheader("Estados financieros")

    utilidad = st.session_state.ingresos - st.session_state.gastos

    st.metric("Ingresos", f"${st.session_state.ingresos:,.0f}")
    st.metric("Gastos", f"${st.session_state.gastos:,.0f}")
    st.metric("Utilidad", f"${utilidad:,.0f}")
    st.metric("Caja", f"${st.session_state.caja:,.0f}")
