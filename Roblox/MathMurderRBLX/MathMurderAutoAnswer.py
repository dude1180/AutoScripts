import mss
import easyocr
import keyboard
import time
import numpy as np
import cv2  

# 1. KALIBRASI VARIABEL SENSOR MATA (AREA SOAL)
# Ganti xxx dengan angka koordinat dari layarmu! (liat readme untuk cara kalibrasi)
box_top    = xxx   
box_left   = xxx   
box_width  = xxx
box_height = xxx

# 2. VARIABEL SENSOR UI & KLIK
click_x = xxx
click_y = xxx

trigger_x = xxx
trigger_y = xxx

reader = easyocr.Reader(['en'], gpu=False)

print("\n=== ROBLOX MATH MURDER AUTO ANSWER By dude1180 ===")
print(f"sensor UI aktif di piksel ({trigger_x}, {trigger_y}).")
print("tekan 'p' untuk TEMBAK MANUAL (jika sensor telat/gagal).")
print("tahan 'q' untuk MEMATIKAN bot.")
print("[!] PASTIKAN CMD / VSCODE BERJALAN SEBAGAI ADMINISTRATOR!")

grab_box = {"top": box_top, "left": box_left, "width": box_width, "height": box_height}
trigger_box = {"top": trigger_y, "left": trigger_x, "width": 1, "height": 1}

sedang_menjawab = False 

with mss.MSS() as sct:
    while not keyboard.is_pressed('q'):
        
        img_trigger = sct.grab(trigger_box)
        p_pixel = img_trigger.pixel(0, 0)
        r, g, b = p_pixel[0], p_pixel[1], p_pixel[2]
        
        ui_ready = abs(r - 178) <= 3 and abs(g - 178) <= 3 and abs(b - 178) <= 3
        manual_trigger = keyboard.is_pressed('p')

        if (ui_ready or manual_trigger) and not sedang_menjawab:
            
            if manual_trigger:
                print("\n[!] MANUAL OVERRIDE (p) DITEKAN! Mengeksekusi Soal...")
            else:
                print("\n[+] Sinyal UI B2B2B2 Terdeteksi! Mengeksekusi Soal...")
                
            sedang_menjawab = True 
            
            img = sct.grab(grab_box)
            img_np = np.array(img) 
            img_bgr = cv2.cvtColor(img_np, cv2.COLOR_BGRA2BGR)
            
            batas_bawah_putih = np.array([90, 90, 90], dtype=np.uint8)
            batas_atas_putih  = np.array([255, 255, 255], dtype=np.uint8)
            
            img_hanya_putih = cv2.inRange(img_bgr, batas_bawah_putih, batas_atas_putih)

            cv2.imwrite("debug_mata.png", img_hanya_putih)
            
            hasil = reader.readtext(img_hanya_putih, allowlist='0123456789+-*/=xX: ')
            gabungan_teks = " ".join([deteksi[1] for deteksi in hasil])
            
            if '=' in gabungan_teks:
                gabungan_teks = gabungan_teks.split('=')[0]
                
            teks_clean = gabungan_teks.replace('x', '*').replace('X', '*').replace('÷', '/').replace(':', '/')
            
            char_legal = "0123456789+-*/"
            rumus_final = "".join([char for char in teks_clean if char in char_legal])

            while len(rumus_final) > 0 and not rumus_final[0].isdigit():
                rumus_final = rumus_final[1:]  
                
            while len(rumus_final) > 0 and not rumus_final[-1].isdigit():
                rumus_final = rumus_final[:-1] 

            if rumus_final.isdigit() and len(rumus_final) >= 2:
                mid = len(rumus_final) // 2
                rumus_final = f"{rumus_final[:mid]} - {rumus_final[mid:]}"

            try:
                rumus_final = rumus_final.strip()
                if rumus_final != "" and rumus_final[0].isdigit() and rumus_final[-1].isdigit():
                    jawaban = int(eval(rumus_final))
                    print(f"Target Terkunci: {rumus_final} | Eksekusi Jawaban: {jawaban}")

                    jawaban_str = str(jawaban)
                    for angka in jawaban_str:
                        keyboard.send(angka)
                        time.sleep(0.05)
                    
                    time.sleep(0.1)
                    keyboard.send('enter')
                else:
                    print(f"-> [Abaikan] Rumus cacat/tidak lengkap: '{rumus_final}'")
            except Exception:
                print(f"-> [Error] Gagal mengeksekusi rumus: '{rumus_final}'")
            
            time.sleep(0.5) 
            print("[-] Gembok terkunci. Menunggu warna UI / lepas tombol...")

        elif not ui_ready and not manual_trigger and sedang_menjawab:
            sedang_menjawab = False
            print("[+] Reset Selesai. Standby untuk ronde baru.")

        time.sleep(0.01)

print("\nBot DIHENTIKAN.")