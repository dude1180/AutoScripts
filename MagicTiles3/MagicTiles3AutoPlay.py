import mss
import keyboard
import time

# UBAH VARIABLE MENYESUAIKAN DENGAN LAYAR ANDA
y_trigger = xxx  #kordinat y untuk mendeteksi tiles

lanes = [xxx, xxx, xxx, xxx] #kordinat x untuk masing-masing lane (dari kiri ke kanan)
keys  = ['w', 'a', 's', 'd']

key_states = [False, False, False, False]
is_paused = False 

print("=== MAGIC TILES BOT BY DUDE1180) ===")
print("tekan '-' untuk MULAI pertama kali.")
print("tekan 'p' kapan aja untuk PAUSE / RESUME.")
print("tekan 'q' untuk BERHENTI total.")

keyboard.wait('-')
print("\nsistem aktif!")

with mss.MSS() as sct:
    grab_box = {
        "top"   : y_trigger,
        "left"  : lanes[0] - 20,
        "width" : (lanes[3] - lanes[0]) + 40,
        "height": 1
    }

    while not keyboard.is_pressed('q'):
        if keyboard.is_pressed('p'):
            is_paused = not is_paused
            
            if is_paused:
                print("\n[PAUSED] Bot istirahat. Tekan 'p' lagi untuk lanjut.")
                for i, k in enumerate(keys):
                    if key_states[i]:
                        keyboard.release(k)
                        key_states[i] = False
            else:
                print("\n[RESUMED] Bot kembali jalan!")
            time.sleep(0.3) 

            continue
        img = sct.grab(grab_box)

        for i in range(4):
            rel_x = lanes[i] - grab_box["left"]
            
            p = img.pixel(int(rel_x), 0)
            r, g, b = p[0], p[1], p[2]

            is_black = (r < 80 and g < 80 and b < 80)
            is_purple = (r < 140 and g < 70 and b > 150)
            is_cyan = (r < 60 and g > 150 and b > 200)

            if is_black or is_purple or is_cyan:
                if not key_states[i]:
                    keyboard.press(keys[i])
                    key_states[i] = True
                    time.sleep(0.005) 
            else:
                if key_states[i]:
                    keyboard.release(keys[i])
                    key_states[i] = False

for k in keys: 
    keyboard.release(k)

print("\nBot DIHENTIKAN.")
