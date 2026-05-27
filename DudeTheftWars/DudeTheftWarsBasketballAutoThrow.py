import pyautogui
import time
import keyboard

# CHANGE THE VARIABEL ACCORDING TO YOUR EMULATOR RESOLUTION 
start_x, start_y = xxx, xxx  # Koordinat awal
end_x, end_y = xxx, xxx      # Koordinat akhir
swipe_duration = 0.2         # Kecepatan swipe
delay_lemparan = x.xx         # Waktu tunggu reset

print("=== SCRIPT BASKETBALL AUTO THROW DUDE THEFT WARS ===")
print("1. Pastikan script dijalankan sebagai ADMINISTRATOR.")
print("2. Buka emulator, pastikan karakter siap di lapangan.")
print("3. Tekan tombol '-' di keyboard untuk MEMULAI.")
print("4. Tahan tombol 'q' untuk BERHENTI.")
print("------------------------------------------")

keyboard.wait('-')

print("\nScript DIMULAI! Jangan gerakkan mouse manual...")
time.sleep(0.5)

lemparan_ke = 0


def check_stop_during_delay(seconds):
    end_time = time.time() + seconds
    while time.time() < end_time:
        if keyboard.is_pressed('q'):
            return True  
        time.sleep(0.05) 
    return False

while True:
    if keyboard.is_pressed('q'):
        break

    lemparan_ke += 1
    print(f"Mengeksekusi lemparan ke-{lemparan_ke}...")

    pyautogui.moveTo(start_x, start_y)
    time.sleep(0.1) 
    
    pyautogui.mouseDown(button='left')
    pyautogui.moveTo(end_x, end_y, duration=swipe_duration)
    pyautogui.mouseUp(button='left')

    if check_stop_during_delay(delay_lemparan):
        break

print("\nGrinding DIHENTIKAN. Silakan cek cash-mu.")