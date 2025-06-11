import time
import os
from termcolor import colored

def clear_screen():
    os.system('cls')

def LED_teks(teks, lebar, langkah, durasi, warna_teks, warna_highlight):
    delay = durasi/langkah
    efek_masuk = " "*lebar + teks + " "*lebar
    berjalan = len(efek_masuk)- lebar +1

    index = 0

    for langkah in range(langkah):
        clear_screen()
        posisi = index % berjalan
        teks_terlihat = efek_masuk[posisi:posisi + lebar]
        print("-"*lebar)

        for karakter in teks_terlihat:
            print(colored(karakter, warna_teks, warna_highlight), end="")

        print()
        print("-"*lebar)
        index += 1
        time.sleep(delay)

LED_teks(teks= "Happy Eid", lebar = 10, langkah = 20, durasi = 20, warna_teks = 'red', warna_highlight="on_white")