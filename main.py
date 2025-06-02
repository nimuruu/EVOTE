from modul import pemilih, calon, voting, statistik

def main():
    while True:
        print("\n===== SISTEM E-VOTING PEMILIHAN KETUA ORGANISASI=====")
        print("1. Daftar Pemilih")
        print("2. Daftar Calon Ketua")
        print("3. Voting")
        print("4. Tampilkan Hasil")
        print("5. Keluar")
        print("=======================================================")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            pemilih.tambahPemilih()
        elif pilihan == "2":
            calon.tambahCalon()
        elif pilihan == "3":
            voting.pemungutan()
            break
        elif pilihan == "4":
            statistik.tampilkanStatistik()
        elif pilihan == "5":
            print("Terima kasih!")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()