import json

def tambahCalon():
    idCalon = input("Masukan ID Calon: ")
    nama = input("Masukan Nama Calon: ")

    file = open("data/calon.json", "r")
    content = file.read()
    file.close()
    if content.strip() == "":
        daftarCalon = []
    else:
        daftarCalon = json.loads(content)

    for c in daftarCalon:
        if c["id"] == idCalon:
            print("ID calon sudah terdaftar!")
            return

    calonBaru = {
        "id": idCalon,
        "nama": nama,
        "jumlahSuara": 0
    }

    daftarCalon.append(calonBaru)

    file = open("data/calon.json", "w")
    json.dump(daftarCalon, file)
    file.close()

    print("Calon berhasil ditambahkan.")
