{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5479f63c-6e45-4354-9a0d-2f246c0fcc2b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== SISTEM E-VOTING PEMILIHAN KETUA ORGANISASI=====\n",
      "1. Daftar Pemilih\n",
      "2. Daftar Calon Ketua\n",
      "3. Voting\n",
      "4. Tampilkan Hasil\n",
      "5. Keluar\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Pilih menu (1-6):  4\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "===== Statistik Pemilihan Umum =====\n",
      "Total Pemilih       : 1\n",
      "Sudah Memilih       : 1\n",
      "Belum Memilih       : 0\n",
      "Partisipasi         : 100.00%\n",
      "\n",
      "Hasil Suara:\n",
      "- Anby Demara (123): 1 suara\n",
      "- Nicole Demara (124): 0 suara\n",
      "\n",
      "Pemenang sementara: Anby Demara (123) dengan 1 suara\n",
      "\n",
      "===== SISTEM E-VOTING PEMILIHAN KETUA ORGANISASI=====\n",
      "1. Daftar Pemilih\n",
      "2. Daftar Calon Ketua\n",
      "3. Voting\n",
      "4. Tampilkan Hasil\n",
      "5. Keluar\n"
     ]
    }
   ],
   "source": [
    "from modul import pemilih, calon, voting, statistik\n",
    "\n",
    "def main():\n",
    "    while True:\n",
    "        print(\"\\n===== SISTEM E-VOTING PEMILIHAN KETUA ORGANISASI=====\")\n",
    "        print(\"1. Daftar Pemilih\")\n",
    "        print(\"2. Daftar Calon Ketua\")\n",
    "        print(\"3. Voting\")\n",
    "        print(\"4. Tampilkan Hasil\")\n",
    "        print(\"5. Keluar\")\n",
    "\n",
    "        pilihan = input(\"Pilih menu (1-6): \")\n",
    "\n",
    "        if pilihan == \"1\":\n",
    "            pemilih.tambahPemilih()\n",
    "        elif pilihan == \"2\":\n",
    "            calon.tambahCalon()\n",
    "        elif pilihan == \"3\":\n",
    "            voting.pemungutan()\n",
    "            break\n",
    "        elif pilihan == \"4\":\n",
    "            statistik.tampilkanStatistik()\n",
    "        elif pilihan == \"5\":\n",
    "            print(\"Terima kasih!\")\n",
    "            break\n",
    "        else:\n",
    "            print(\"Pilihan tidak valid.\")\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60db2410-2031-45af-86d4-618dfa2c506a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
