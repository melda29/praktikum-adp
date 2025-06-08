#file text data praktikan
data = [
    "2410431019, Lexania, 85, 80, 89",
    "2410431039, Zazkia, 90, 90, 0",
    "2410432041, Melda, 100, 100, 95",
    "2410431003, Aisyah, 70, 100, 0",
    "2410433011, Kheisya, 90, 100, 82",
    "2410432046, Nailul, 100, 100, 95",
    "2410433001, Zahra Adelia, 70, 100, 0",
    "2410431001, Rifqa, 90, 70, 85",
    "2410432038, Desy, 90, 90, 80",
    "2410432039, Aulya, 100, 100, 55",
]

with open("data_praktikan.txt", "w") as f:
    for line in data :
        f.write(line + "\n")

#baca file, simpan data ke dictionary
praktikan_dict = {}

with open("data_praktikan.txt", "r") as f:
    lines = f.readlines()

for line in lines:
    line = line.strip()
    bagian = line.split(",")
    nim = bagian[0]
    nama = bagian[1]
    pretest = int(bagian[2])
    posttest = int(bagian[3])
    tugas = int(bagian[4])

    praktikan_dict[nim]={
        "nama": nama,
        "pretest": pretest,
        "posttest": posttest,
        "tugas": tugas
    }

#Nilai akhir praktikan dan simpan ke file baru
with open("data_nilai_akhir.txt", "w") as f:
    f.write("NIM, Nama, Pretest, Posttest, Tugas, Nilai Akhir\n")

    for nim in praktikan_dict:
        pre = praktikan_dict[nim]["pretest"]
        post = praktikan_dict[nim]["posttest"]
        tugas = praktikan_dict[nim]["tugas"]
        total = (35*pre+35*post+30*tugas)/100
        praktikan_dict[nim]["nilai_akhir"]= total

        f.write(nim + "," + praktikan_dict[nim]["nama"] + ", " + str(pre) + ", " + str(post) + ", " + str(tugas) + ", " + str(total) + "\n")

#nilai tertinggi dan terendah serta rata-rata nilai akhir
total_nilai = 0
jumlah = 0

for nim in praktikan_dict:
    total_nilai = total_nilai + praktikan_dict[nim]["nilai_akhir"]
    jumlah = jumlah+1

rata_rata = total_nilai / jumlah

pertama = True
for nim in praktikan_dict:
    nilai = praktikan_dict[nim]["nilai_akhir"]
    if pertama:
        tertinggi_nilai = nilai
        tertinggi_nim = nim
        terendah_nilai = nilai
        terendah_nim = nim
        pertama = False
    else:
        if nilai>tertinggi_nilai:
            tertinggi_nilai=nilai
            tertinggi_nim=nim
        if nilai<terendah_nilai:
            terendah_nilai=nilai
            terendah_nim=nim

#banyak praktikan yang mendapat nilai dibawah rata-rata
jumlah_bawah_rata = 0
for nim in praktikan_dict:
    if praktikan_dict[nim]["nilai_akhir"]<rata_rata:
        jumlah_bawah_rata= jumlah_bawah_rata+1

print("=== HASIL ANALISIS DATA ===")
print("Rata-rata nilai akhir:", rata_rata)
print("Nilai tertinggi:", praktikan_dict[tertinggi_nim]["nama"], "(", tertinggi_nim, ")=", tertinggi_nilai)
print("Nilai terendah:", praktikan_dict[terendah_nim]["nama"], "(", terendah_nim, ")=", terendah_nilai)
print("Jumlah yang dibawah rata-rata:", jumlah_bawah_rata)