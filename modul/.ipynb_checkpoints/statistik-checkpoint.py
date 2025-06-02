import json

def tampilkanStatistik():
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

    totalPemilih = len(daftarPemilih)
    sudahMemilih = sum(1 for p in daftarPemilih if p["sudahMemilih"])
    belumMemilih = totalPemilih - sudahMemilih

    partisipasi = (sudahMemilih / totalPemilih) * 100 if totalPemilih > 0 else 0

    calonTerbanyak = None
    suaraTerbanyak = -1
    for c in daftarCalon:
        if c["jumlahSuara"] > suaraTerbanyak:
            calonTerbanyak = c
            suaraTerbanyak = c["jumlahSuara"]

    print("\n===== Statistik Pemilihan Umum =====")
    print(f"Total Pemilih       : {totalPemilih}")
    print(f"Sudah Memilih       : {sudahMemilih}")
    print(f"Belum Memilih       : {belumMemilih}")
    print(f"Partisipasi         : {partisipasi:.2f}%")

    print("\nHasil Suara:")
    for c in daftarCalon:
        print(f"- {c['nama']} ({c['id']}): {c['jumlahSuara']} suara")

    if calonTerbanyak:
        print(f"\nPemenang sementara: {calonTerbanyak['nama']} ({calonTerbanyak['id']}) dengan {calonTerbanyak['jumlahSuara']} suara")
