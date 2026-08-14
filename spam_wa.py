import pyautogui
import time
import random
import os

pyautogui.FAILSAFE = True 

def header():
    os.system("cls" if os.name == "nt" else "clear")

    print("=" * 70)
    print("  ______  _____  ___  __  __        __        _  ")
    print(" / ___|  | ____|/ _ \\|  \\/  |       / /       | | ")
    print(" \\___ \\  |  _| | | | | |\\/| |      / /__   ___| |")
    print("  ___) | | |___| |_| | |  | |     / / \\ \\ / / | |")
    print(" |____/  |_____|\\___/|_|  |_|    /_/   \\_/_/  |_|")
    print()
    print("              SPAMWAHD - Auto Chat Tool")
    print("=" * 70)
    print()


header()

try:
    pesan = input("📨 Masukkan pesan yang ingin dikirim: ")
    jumlah = int(input("🔢 Berapa kali pesan ingin dikirim? "))

    print("\n🖱️ Arahkan kursor ke kolom chat dalam 5 detik...")
    time.sleep(5)

    position = pyautogui.position()
    print(f"📌 Posisi dikunci di: {position}")

    print("⏳ Mulai mengirim dalam 3 detik...")
    time.sleep(3)

    terkirim = 0

    for i in range(jumlah):
        pyautogui.click(position.x, position.y)
        pyautogui.typewrite(pesan)
        pyautogui.press("enter")
        terkirim += 1
        print(f"[{terkirim}] Terkirim: {pesan}")

        delay = random.uniform(0.4, 1.0)
        time.sleep(delay)

    print(f"\n✅ Total pesan yang berhasil dikirim: {terkirim}")

except KeyboardInterrupt:
    print(f"\n⛔ Pengiriman dihentikan oleh pengguna (Ctrl + C).")
    print(f"📦 Total yang sudah terkirim: {terkirim}")

except Exception as e:
    print(f"⚠️ Terjadi kesalahan: {e}")