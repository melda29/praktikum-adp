n = int(input('Masukkan nilai n (minimal 4) : '))
if n < 4 :
    print('Nilai n harus minimal 4')
else :
    total_boom = 0
    mid = n//2

    for i in range(n):
        for j in range(n):
            if n%2==1 and i==mid and j==mid:
                print(f"{'HORE':>4}", end=" ")
            elif i==j:
                print(f"{1:>4}", end=" ")
            elif i+j==n-1:
                print(f"{2:>4}", end=" ")
            else :
                print(f"{'BOOM':>4}", end=" ")
                total_boom += 1
        
        print()

    print(f"Total BOOM yang muncul sebanyak = {total_boom}")