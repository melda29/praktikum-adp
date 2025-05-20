titik = []

i = 0
while i < 3:
    print("Masukkan titik ke-", i+1)
    x = float(input("x: "))
    y = float(input("y: "))
    titik.append([x, y])
    i += 1

sisi = [0, 0, 0]
for i in range(3):
    x1 = titik[i][0]
    y1 = titik[i][1]
    if i<2:
        x2 = titik[i+1][0]
        y2 = titik[i+1][1]
    else:
        x2 = titik[0][0]
        y2 = titik[0][1]
    dx = x1-x2
    dy = y1-y2
    sisi[i] = (dx*dx + dy*dy)** 0.5

if sisi[0]==sisi[1] or sisi[1]==sisi[2] or sisi[0]==sisi[2]:
    print("Segitiga sama kaki")
else:
    print("Bukan segitiga sama kaki")

