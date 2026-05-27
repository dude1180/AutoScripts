import mss
import keyboard
import time

# UBAH VARIABLE MENYESUAIKAN DENGAN LAYAR ANDA
y_trigger = xxx #kordinat y untuk mendeteksi tiles

lanes = [xxx, xxx, xxx, xxx] #kordinat x untuk masing-masing lane (dari kiri ke kanan)
keys  = ['w', 'a', 's', 'd']

key_states = [False, False, False, False]

print("=== MAGIC TILES BOT By dude1180 ===")
print("Tekan '-' untuk MULAI, tahan 'q' untuk BERHENTI.")

keyboard.wait('-')
print("\nSistem Aktif! Memindai...")

with mss.MSS() as sct:
    grab_box = {
        "top"   : y_trigger,
        "left"  : lanes[0] - 20,
        "width" : (lanes[3] - lanes[0]) + 40,
        "height": 1
    }

    while not keyboard.is_pressed('q'):
        img = sct.grab(grab_box)

        for i in range(4):
            rel_x = lanes[i] - grab_box["left"]
            
            p = img.pixel(int(rel_x), 0)
            r, g, b = p[0], p[1], p[2]

            is_black = (r < 80 and g < 80 and b < 80)
            
            is_purple = (r < 140 and g < 70 and b > 150)

            if is_black or is_purple:
                if not key_states[i]:
                    keyboard.press(keys[i])
                    key_states[i] = True
            else:
                if key_states[i]:
                    keyboard.release(keys[i])
                    key_states[i] = False

# Failsafe
for k in keys: 
    keyboard.release(k)

print("\nBot DIHENTIKAN.")