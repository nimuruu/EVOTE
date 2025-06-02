import json

def pemungutan():
    idPemilih = input("Masukan ID Pemilih: ")

    file = open("data/pemilih.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftarPemilih = []
    else:
        daftarPemilih = json.loads(content)

    file = open("data/calon.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftarCalon = []
    else:
        daftarCalon = json.loads(content)

    for p in daftarPemilih:
        if p["id"] == idPemilih:
            if p["sudahMemilih"]:
                print("Anda sudah memilih sebelumnya!")
                return
            else:
                print("\nDaftar Calon:")
                for i, c in enumerate(daftarCalon):
                    print(f"{i + 1}. {c['nama']} (ID: {c['id']})")
                pilihan = int(input("Pilih Nomor Calon: ")) - 1
                if 0 <= pilihan < len(daftarCalon):
                    daftarCalon[pilihan]["jumlahSuara"] += 1
                    p["sudahMemilih"] = True

                    file = open("data/pemilih.json", "w")
                    json.dump(daftarPemilih, file)
                    file.close()

                    file = open("data/calon.json", "w")
                    json.dump(daftarCalon, file)
                    file.close()

                    print("Voting berhasil, terima kasih telah menggunakan hak suara Anda!")
                    break
                else:
                    print("Pilihan tidak valid!")
                    return

    print("ID pemilih tidak ditemukan.")
