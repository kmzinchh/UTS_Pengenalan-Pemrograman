"""
UTS Pengenalan Pemrograman Komputer
Project : SURVIVAL KIT MAHASISWA BARU
NPM     : 2615061083
NAMA    : Muhammad Faizall
Fitur   : 1. Perencana Uang Saku Anti-Bokek
          2. Game Tebak Kode Server (Hacker Mini Game)
          3. Keluar Aplikasi
"""

import random

NPM = "2615061083"
NAMA = "Muhammad Faizall"


def tampilkan_header():
    """Menampilkan identitas (NPM & Nama) di layar."""
    print("=" * 52)
    print("      SURVIVAL KIT MAHASISWA BARU".center(52))
    print("=" * 52)
    print(f" NPM  : {NPM}")
    print(f" Nama : {NAMA}")
    print("=" * 52)


def format_rupiah(angka):
    """Mengubah angka menjadi format rupiah, contoh: Rp1.500.000"""
    return "Rp" + f"{angka:,}".replace(",", ".")


def input_angka(pesan, minimal=0):
    """Meminta input angka bulat dan mengulang sampai valid."""
    while True:
        teks = input(pesan)
        if teks.isdigit() and int(teks) >= minimal:
            return int(teks)
        print(f"  [!] Masukkan angka bulat (minimal {minimal}).")


def tentukan_status(jatah_harian):
    """Pencabangan: menentukan 'level bertahan hidup' dari jatah harian."""
    if jatah_harian >= 50000:
        return "SULTAN KAMPUS (makan enak tiap hari)"
    elif jatah_harian >= 25000:
        return "AMAN TERKENDALI (sesekali jajan)"
    elif jatah_harian >= 10000:
        return "MODE HEMAT (warteg is life)"
    else:
        return "MODE MIE INSTAN (siap-siap darurat!)"


# ============================================================
# FITUR 1 : PERENCANA UANG SAKU ANTI-BOKEK
# ============================================================
def fitur_uang_saku():
    print("\n--- PERENCANA UANG SAKU ANTI-BOKEK ---")
    uang_saku = input_angka("Uang saku per bulan (Rp)      : ", 1)
    biaya_kos = input_angka("Biaya kos/transport tetap (Rp): ")
    persen_tabung = input_angka("Target tabungan (% uang saku)  : ")

    # Proses aritmatika & operator
    tabungan = uang_saku * persen_tabung // 100
    sisa = uang_saku - biaya_kos - tabungan

    if sisa <= 0:
        print("\n[!] Anggaran minus! Kurangi tabungan atau cari tambahan uang saku.")
        return

    jatah_harian = sisa // 30
    sisa_koin = sisa % 30  # sisa pembagian = uang cadangan

    print("\n--- HASIL PERHITUNGAN ---")
    print(f"Tabungan bulanan  : {format_rupiah(tabungan)}")
    print(f"Dana bebas        : {format_rupiah(sisa)}")
    print(f"Jatah harian      : {format_rupiah(jatah_harian)}")
    print(f"Uang cadangan     : {format_rupiah(sisa_koin)}")
    print(f"Status            : {tentukan_status(jatah_harian)}")

    # Iterasi FOR: simulasi 4 minggu
    print("\n--- SIMULASI SISA SALDO PER MINGGU ---")
    saldo = sisa
    for minggu in range(1, 5):
        hari = 7 if minggu < 4 else 9  # minggu ke-4 = 9 hari (total 30 hari)
        saldo -= jatah_harian * hari
        persen = max(saldo, 0) * 100 // sisa
        bar = "#" * (persen // 5)
        print(f"Minggu {minggu} | {bar:<20} | {format_rupiah(saldo)}")

    # Tips berdasarkan pencabangan
    if persen_tabung >= 20:
        print("\nTips: Tabunganmu mantap! Masa depan cerah.")
    elif persen_tabung >= 10:
        print("\nTips: Lumayan, coba naikkan tabungan pelan-pelan.")
    else:
        print("\nTips: Sisihkan minimal 10% biar aman saat tanggal tua.")


# ============================================================
# FITUR 2 : GAME TEBAK KODE SERVER
# ============================================================
def beri_petunjuk(tebakan, kode):
    """Memberi petunjuk panas/dingin berdasarkan selisih tebakan."""
    selisih = abs(tebakan - kode)
    if selisih <= 3:
        suhu = "PANAS BANGET"
    elif selisih <= 10:
        suhu = "HANGAT"
    else:
        suhu = "DINGIN"
    arah = "terlalu kecil, naikkan!" if tebakan < kode else "terlalu besar, turunkan!"
    return f"{suhu} - {arah}"


def fitur_tebak_kode():
    print("\n--- TEBAK KODE SERVER ---")
    print("Kamu hacker yang mau membobol server kampus.")
    print("Tebak kode rahasia (1-50). Kamu punya 6 kesempatan!")

    kode = random.randint(1, 50)
    nyawa = 6
    berhasil = False

    # Iterasi WHILE
    while nyawa > 0 and not berhasil:
        tebakan = input_angka(f"\n[Sisa nyawa: {nyawa}] Tebakanmu: ", 1)
        if tebakan == kode:
            berhasil = True
        else:
            nyawa -= 1
            print("  >> " + beri_petunjuk(tebakan, kode))

    if berhasil:
        skor = (nyawa + 1) * 100 + (50 - kode)
        print(f"\nACCESS GRANTED! Server berhasil dibobol. Skor: {skor}")
    else:
        print(f"\nACCESS DENIED! Kodenya adalah {kode}. Coba lagi ya!")


# ============================================================
# PROGRAM UTAMA
# ============================================================
def main():
    while True:
        print()
        tampilkan_header()
        print(" MENU UTAMA")
        print(" 1. Perencana Uang Saku Anti-Bokek")
        print(" 2. Game Tebak Kode Server")
        print(" 3. Keluar Aplikasi")
        print("-" * 52)
        pilihan = input("Pilih menu (1/2/3): ").strip()

        if pilihan == "1":
            fitur_uang_saku()
        elif pilihan == "2":
            fitur_tebak_kode()
        elif pilihan == "3":
            print(f"\nTerima kasih, {NAMA} ({NPM}). Sampai jumpa!")
            break
        else:
            print("\n[!] Pilihan tidak valid, coba lagi.")


main()