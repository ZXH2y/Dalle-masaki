PENYAKIT = {
    "Sehat": {
        "nama": "Daun Sehat",
        "penyebab": "-",
        "gejala": "Daun hijau merata, tanpa bercak atau perubahan warna.",
        "penanganan": [
            "Pertahankan pemupukan dan pengairan yang seimbang.",
            "Pantau tanaman secara rutin setiap minggu.",
        ],
        "tingkat": "aman",
    },
    "Bercak_Daun": {
        "nama": "Bercak Daun (Gray Leaf Spot)",
        "penyebab": "Jamur Cercospora zeae-maydis",
        "gejala": "Bercak persegi panjang abu-abu hingga cokelat, sejajar tulang daun.",
        "penanganan": [
            "Rotasi tanaman dengan non-serealia.",
            "Bersihkan sisa tanaman setelah panen.",
            "Gunakan fungisida bila serangan berat.",
        ],
        "tingkat": "sedang",
    },
    "Karat_Daun": {
        "nama": "Karat Daun (Common Rust)",
        "penyebab": "Jamur Puccinia sorghi",
        "gejala": "Pustul kecil cokelat kemerahan menyerupai karat di kedua sisi daun.",
        "penanganan": [
            "Tanam varietas tahan karat.",
            "Atur jarak tanam agar sirkulasi udara baik.",
            "Semprot fungisida pada gejala awal.",
        ],
        "tingkat": "sedang",
    },
    "Hawar_Daun": {
        "nama": "Hawar Daun (Northern Leaf Blight)",
        "penyebab": "Jamur Exserohilum turcicum",
        "gejala": "Lesi besar berbentuk cerutu, abu-abu kehijauan hingga cokel",
        "penanganan": [
            "Gunakan benih varietas tahan.",
            "Benamkan sisa tanaman terinfeksi.",
            "Aplikasi fungisida sebelum pembungaan.",
        ],
        "tingkat": "tinggi",
    },
}

KELAS = list(PENYAKIT.keys())
