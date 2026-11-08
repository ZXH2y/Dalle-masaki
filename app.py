import streamlit as st
from PIL import Image

from penyakit import PENYAKIT
from prediktor import prediksi

st.set_page_config(page_title="Tani Dongo", page_icon="🌽")

st.title("🌽 Tani dongo")
st.write("Unggah foto daun jagung untuk menganalisis penyakitnya.")

file = st.file_uploader("Pilih foto daun", type=["jpg", "jpeg", "png"])

if file is not None:
    gambar = Image.open(file).convert("RGB")

    kol_foto, kol_hasil = st.columns(2)
    kol_foto.image(gambar, caption="Foto yang diunggah", use_container_width=True)

    with st.spinner("Menganalisis..."):
        hasil = prediksi(gambar)

    kelas_top = max(hasil, key=hasil.get)
    yakin = hasil[kelas_top]
    info = PENYAKIT[kelas_top]

    with kol_hasil:
        st.subheader(info["nama"])
        st.metric("Tingkat keyakinan", f"{yakin:.0%}")

        if info["tingkat"] == "aman":
            st.success("Tanaman tampak sehat.")
        elif info["tingkat"] == "sedang":
            st.warning("Perlu penanganan.")
        else:
            st.error("Serangan berbahaya, tangani segera.")

    st.markdown(f"**Penyebab:** {info['penyebab']}")
    st.markdown(f"**Gejala:** {info['gejala']}")
    st.markdown("**Saran penanganan:**")
    for langkah in info["penanganan"]:
        st.markdown(f"- {langkah}")

    with st.expander("Lihat semua probabilitas"):
        st.bar_chart(hasil)
