import json

def tambahPemilih():
    idPemilih = input("Masukan Id Pemilih: ")
    nama = input("Masukan Nama Pemilih: ")
    jurusan = input("Masukan Jurusan Pemilih: ")

    file = open("data/pemilih.json", "r")
    content = file.read()
    file.close()

    if content.strip() == "":
        data = []
    else:
        data = json.loads(content)

    for p in data:
        if p["id"] == idPemilih:
            print("Id sudah digunakan pemilih lain, gunakan Id lain!")
            return

    data.append({
        "id": idPemilih,
        "nama": nama,
        "jurusan": jurusan,
        "sudahMemilih": False
    })

    file = open("data/pemilih.json", "w")
    json.dump(data, file)
    file.close()

    print("Pemilih berhasil ditambahkan!!!")
