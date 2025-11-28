import streamlit as st

st.set_page_config(page_title="Kalkulator Sederhana", page_icon="🧮")

st.title("🧮 Kalkulator Sederhana")
st.write("Masukkan dua angka kemudian pilih operasi yang ingin dilakukan.")

# Input angka
num1 = st.number_input("Angka pertama", value=0.0)
num2 = st.number_input("Angka kedua", value=0.0)

# Pilihan operasi
operation = st.selectbox(
    "Pilih operasi",
    ["Tambah (+)", "Kurang (-)", "Kali (×)", "Bagi (÷)"]
)

# Tombol hitung
if st.button("Hitung"):
    if operation == "Tambah (+)":
        result = num1 + num2

    elif operation == "Kurang (-)":
        result = num1 - num2

    elif operation == "Kali (×)":
        result = num1 * num2

    elif operation == "Bagi (÷)":
        if num2 == 0:
            result = "❌ Error: Tidak bisa membagi dengan 0"
        else:
            result = num1 / num2

    st.success(f"Hasil: {result}")
