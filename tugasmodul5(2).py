nilai_x = [i for i in range(-7,8)]
nilai_f =[]

print("|   x |   f(x)   |")
for x in nilai_x :
    if x > 0 :
        nilai_f.append(x**3 - x)
    elif x < 0 :
        nilai_f.append(1/(x**2))
    else :
        nilai_f.append(1)

for i in range(len(nilai_x)):
    print(f"| {nilai_x[i] : 3} | {nilai_f[i] :< 8.2f} |")