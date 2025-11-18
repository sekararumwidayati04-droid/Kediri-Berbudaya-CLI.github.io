import time
import random

# ---------------- UTILITY ----------------
def garis():
    print("=" * 50)

def loading(text):
    print(text, end="", flush=True)
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)
    print("\n")

def slow(s, t=0.01):
    for ch in s:
        print(ch, end="", flush=True)
        time.sleep(t)
    print()

# ---------------- MENU UTAMA ----------------
def menu():
    garis()
    print("   SELAMAT DATANG DI GAME KEBUDAYAAN KEDIRI")
    garis()
    print("1. Sejarah Kediri")
    print("2. Tradisi & Kesenian")
    print("3. Kuliner Khas")
    print("4. Kuis Kebudayaan")
    print("5. 🧙‍♂ Temui Mbah Jayabrata - Petualangan Kediri")
    print("6. Keluar")
    garis()

def sejarah():
    garis()
    print("📜 SEJARAH KOTA KEDIRI")
    garis()
    print("""
Kediri adalah salah satu kota tertua di Jawa Timur.
Nama 'Kediri' berasal dari kata 'Kadiri' atau 'Kadhiri'.
Pada masa kerajaan, Kediri dikenal sebagai pusat pemerintahan
Kerajaan Kadiri (1042–1222) yang terkenal dengan kemakmuran
dan perkembangan sastra Jawa kuno. Raja Jayabaya dari Kediri
juga terkenal dengan ramalan-ramalannya.
""")
    input("\nTekan ENTER untuk kembali ke menu...")

def tradisi():
    garis()
    print("🎭 TRADISI & KESENIAN KEDIRI")
    garis()
    print("""
1. Jaranan  
Kesenian tradisional berupa tari dengan penari menaiki
kuda kepang. Musiknya khas dan kadang disertai trance.

2. Tari Jaranan Sentherewe  
Variasi tari Jaranan yang lebih modern dan penuh energi.

3. Upacara Pemandian Arca Ganesha  
Tradisi budaya di mana arca dibersihkan sebagai bentuk
penghormatan pada sejarah dan peninggalan leluhur.
""")
    input("\nTekan ENTER untuk kembali ke menu...")

def kuliner():
    garis()
    print("🍜 KULINER KHAS KEDIRI")
    garis()
    print("""
1. Tahu Takwa  
Tahu berwarna kuning yang dibuat dengan cara diasapi.
Ikonik banget dari Kediri.

2. Nasi Pecel Kediri  
Pecel dengan sambal kacang khas, biasanya disajikan
dengan rempeyek, tempe, dan sayuran segar.

3. Sate Emprit  
Sate unik khas Kediri yang terbuat dari burung emprit.
""")
    input("\nTekan ENTER untuk kembali ke menu...")

def kuis():
    soal = [
        {"q": "Kediri terkenal sebagai pusat kerajaan apa?", "a": "Kadiri"},
        {"q": "Tarian khas Kediri yang menggunakan kuda kepang adalah?", "a": "Jaranan"},
        {"q": "Nama raja Kediri yang terkenal dengan ramalan?", "a": "Jayabaya"},
        {"q": "Kuliner khas Kediri yang berwarna kuning adalah?", "a": "Tahu Takwa"},
        {"q": "Tradisi membersihkan arca disebut?", "a": "Pemandian Arca"}
    ]

    random.shuffle(soal)
    skor = 0

    garis()
    print("❓ KUIS KEBUDAYAAN KEDIRI")
    garis()

    for i, s in enumerate(soal, 1):
        print(f"\n{i}. {s['q']}")
        jawab = input("Jawaban: ").strip().lower()

        if jawab == s["a"].lower():
            print("✔ Benar!")
            skor += 1
        else:
            print(f"✘ Salah. Jawaban benar: {s['a']}")

    garis()
    print(f"⭐ Skor Akhir: {skor} / {len(soal)} ⭐")
    if skor == 5:
        print("Perfect! Kamu ngerti banget budaya Kediri!")
    elif skor >= 3:
        print("Lumayan! Pengetahuanmu bagus!")
    else:
        print("Masih perlu belajar, tapi semangat!")
    input("\nTekan ENTER untuk kembali ke menu...")

# ---------------- PETUALANGAN MBH JAYABRATA ----------------

# Data dialog (tidak berubah)
DIALOGS = [
    "Nak, ayo mbah ajak keliling Kediri! 🌳🏯",
    "Siap untuk petualangan seru dan menarik? 🗺️",
    "Aku punya teka-teki kecil di setiap tempat. Coba jawab ya!"
]

def greet_mbah():
    garis()
    slow("Mbah Jayabrata muncul dari balik pohon beringin...")
    slow(random.choice(DIALOGS))
    garis()

def adventure_mbah():
    # DATA DESTINASI DENGAN KUIS KONTEKSTUAL DIDEFINISIKAN DI DALAM FUNGSI
    
    # Kategori 1: Wisata Alam
    DESTINASI_ALAM = {
        "1": ("Gunung Kelud 🌋", 
            "Gunung berapi aktif, terkenal pemandangannya!",
            "Kelud terkenal karena menghasilkan fenomena alam bernama 'Kawah...', yang sering berubah bentuk. Apa nama kawah itu?", 
            "kawah kelud"),

        "2": ("Air Terjun Dolo 🏞", 
            "Air terjun cantik di lereng pegunungan, segar banget!",
            "Untuk mencapai Air Terjun Dolo, kita harus melalui Kabupaten Kediri di lereng gunung apa?", 
            "wilis"),

        "3": ("Alun-Alun Kediri 🏙", 
            "Tempat nongkrong, ada taman & kuliner lokal.",
            "Apa nama sungai besar yang sangat dekat dan membelah kota Kediri, dekat Alun-Alun?", 
            "brantas")
    }

    # Kategori 2: Peninggalan Sejarah
    DESTINASI_SEJARAH = {
        "1": ("Museum Airlangga 🏛", 
            "Museum tentang sejarah kerajaan Kediri dan Airlangga.",
            "Museum ini menyimpan banyak peninggalan dari masa kerajaan Kediri, sering disebut juga 'Kadiri' atau...?", 
            "panjalu"),

        "2": ("Candi Tegowangi 🛕", 
            "Candi peninggalan masa kerajaan Kediri.",
            "Candi Tegowangi dibangun sebagai pendharmaan untuk siapa? (Jawaban: nama tokoh/pejabat)", 
            "bhre wengker"), 

        "3": ("Gapura Gampengrejo 🏰", 
            "Gapura bersejarah di pusat kota Kediri.",
            "Gapura ini sering dikaitkan dengan pintu masuk menuju kota pusat Kerajaan Kadiri kuno. Apa nama ibukota kerajaan itu?", 
            "daha")
    }

    # Kategori 3: Tokoh Inspiratif
    DESTINASI_TOKOH = {
        "1": ("Prabu Jayabaya 👑", 
            "Raja Kediri terkenal dengan ramalan dan kepemimpinan bijak.",
            "Apa nama karya sastra ramalan yang paling terkenal dan dikaitkan dengan Prabu Jayabaya?", 
            "jangka jayabaya"),

        "2": ("KH. Abdul Karim (Lirboyo) 🕌", 
            "Pendiri Pondok Pesantren Lirboyo, pusat keagamaan Kediri.",
            "Pesantren besar yang didirikan oleh tokoh ini di Kediri adalah Lirboyo. Apa fokus utama pengajaran di pesantren tersebut?", 
            "kitab kuning"),

        "3": ("Ibu Siti Nurbaya 👩‍🌾 (Fiktif/Perwakilan Pengusaha Tahu)", 
            "Menggambarkan semangat pengusaha lokal Tahu Takwa.",
            "Tahu khas Kediri tidak hanya kuning, tetapi juga 'Tahu...' yang namanya diambil dari sumpah prajurit?", 
            "tahu takwa")
    }
    
    # LOGIKA PETUALANGAN
    slow("=== PETUALANGAN BERSAMA MBH JAYABRATA ===")
    while True:
        greet_mbah()
        print("Kategori petualangan:")
        print("1. 🌳 Wisata Alam")
        print("2. 🏯 Peninggalan Sejarah / Museum")
        print("3. 👨‍🎓 Tokoh Inspiratif Kediri")
        print("4. 👋 Pamitan")

        kategori = input("Pilih kategori (1-4): ").strip()

        destinasi = {}
        if kategori == "1":
            destinasi = DESTINASI_ALAM
            slow("🗺 Kamu memilih Wisata Alam...")
        elif kategori == "2":
            destinasi = DESTINASI_SEJARAH
            slow("🏯 Kamu memilih Peninggalan Sejarah / Museum...")
        elif kategori == "3":
            destinasi = DESTINASI_TOKOH
            slow("👨‍🎓 Kamu memilih Tokoh Inspiratif Kediri...")
        elif kategori == "4":
            slow("Mbah: Mari, hati-hati di perjalananmu. Sampai jumpa! 👋")
            break
        else:
            print("❗ Pilihan tidak valid. Coba lagi.\n")
            continue

        # Tampilkan destinasi
        # Ambil 4 elemen, tapi hanya tampilkan nama
        for key, (nama, info, q, a) in destinasi.items():
            print(f"{key}. {nama}")
            
        pilih = input("Mau ke mana? Pilih nomor: ").strip()

        if pilih in destinasi:
            # Ambil keempat elemen data
            nama, info, q, a = destinasi[pilih] 
            
            slow(f" 🗺 Kamu menuju {nama}...")
            time.sleep(1)
            print(info)

            # Tantangan quiz yang kontekstual
            slow("Mbah: Ada teka-teki nih, jawab ya!")
            print("\nPERTANYAAN MBH:")
            print(q)
            jaw = input("Jawabanmu: ").strip().lower()

            if jaw == a.lower():
                slow("✔ Heh, pinter! Kamu dapat stiker virtual: [★ Budaya Kediri]")
            else:
                slow(f"✖ Jawaban salah. Jawaban benar adalah: {a.capitalize()}. Belajar lagi ya!")
        else:
            print("❗ Pilihan tidak valid. Kembali ke menu utama.\n")

# ---------------- MAIN PROGRAM ----------------
while True:
    menu()
    pilihan = input("Pilih menu (1-6): ").strip()

    if pilihan == "1":
        loading("Membuka sejarah")
        sejarah()
        
    elif pilihan == "2":
        loading("Memuat tradisi")
        tradisi()
    elif pilihan == "3":
        loading("Mengambil data kuliner")
        kuliner()
    elif pilihan == "4":
        loading("Menyiapkan kuis")
        kuis()
    elif pilihan == "5":
        loading("Menjalankan petualangan bersama Mbah Jayabrata 🧙‍♂")
        adventure_mbah()
    elif pilihan == "6":
        print("Terima kasih sudah bermain! 👋")
        break
    else:
        print("❗ Pilihan tidak valid. Coba lagi.\n")