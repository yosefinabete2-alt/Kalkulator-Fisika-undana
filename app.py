import streamlit as st

# Judul Aplikasi Web
st.title("⚡ Kalkulator Fisika FST Undana")
st.write("Aplikasi web portofolio komputasi fisika untuk kebutuhan praktikum dan perhitungan cepat.")

# Memilih menu perhitungan
menu = st.selectbox(
    "Pilih Kategori Perhitungan:",
    ["Hukum Ohm & Daya Listrik", "Informasi Pembuat"]
)

if menu == "Hukum Ohm & Daya Listrik":
    st.subheader("Kalkulator Hukum Ohm dan Daya")
    
    # Kotak input angka dari pengguna
    arus = st.number_input("Masukkan Arus Listrik (I dalam Ampere):", value=1.0)
    hambatan = st.number_input("Masukkan Hambatan (R dalam Ohm):", value=10.0)
    
    # Tombol eksekusi perhitungan
    if st.button("Hitung Sekarang"):
        # Rumus Fisika
        tegangan = arus * hambatan
        daya = tegangan * arus
        
        # Menampilkan hasil di web
        st.success("Perhitungan Berhasil!")
        st.write(f"**Tegangan (V):** {tegangan:.2f} Volt")
        st.write(f"**Daya Listrik (P):** {daya:.2f} Watt")
        st.info("Rumus yang digunakan: V = I × R dan P = V × I")

elif menu == "Informasi Pembuat":
    st.subheader("Tentang Aplikasi")
    st.write("Aplikasi ini dikembangkan sebagai portofolio komputasi fisika mahasiswa Program Studi Fisika, Fakultas Sains dan Teknik, Universitas Nusa Cendana.")
