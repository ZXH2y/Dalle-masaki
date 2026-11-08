import random
from penyakit import KELAS


def prediksi(gambar):
    """Mengembalikan dict {nama_kelas: probabilitas}. sementara masih di acak."""
    angka = [random.random() for _ in KELAS]
    total = sum(angka)
    return {k: a / total for k, a in zip(KELAS, angka)}
