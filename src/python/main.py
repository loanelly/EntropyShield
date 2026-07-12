# ============================================================================
# PROJECT: LNL-EntropyShield (Host Client Application)
# ORGANIZATION: LNL-Engineering (https://github.com/LNL-Engineering)
# ============================================================================

import serial
import time
import sys

# CONFIGURATION / НАСТРОЙКА
# [EN] Set your board's COM port (e.g., 'COM3' on Windows or '/dev/ttyUSB0' on Linux)
# [RU] Укажите COM-порт вашей платы (например, 'COM3' для Windows или '/dev/ttyUSB0' для Linux)
SERIAL_PORT = 'COM3' 
BAUD_RATE = 115200

def harvest_entropy_key(target_bytes=32):
    """
    [EN] Reads debiased HEX data from EntropyShield hardware and assembles a secure key.
    [RU] Считывает очищенные HEX-данные с платы и собирает криптографический ключ.
    """
    print(f"[⚙️] Connecting to LNL-EntropyShield on {SERIAL_PORT}...")
    ser = None
    try:
        # Establish connection / Устанавливаем связь с платой
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        
        # Wait for microcontroller auto-reset / Ожидаем перезагрузку платы при подключении
        time.sleep(2) 
        
        # Flush any old garbage data from the buffer / Очищаем буфер от старых данных
        ser.reset_input_buffer()
        
        print("[✅] Device connected. Harvesting hardware chaos...\n")
        
        hex_key_accumulator = ""
        required_hex_chars = target_bytes * 2 # 1 byte = 2 HEX characters
        
        while len(hex_key_accumulator) < required_hex_chars:
            if ser.in_waiting > 0:
                # Read line and decode safely / Читаем строку и безопасно декодируем без падений на битых байтах
                raw_line = ser.readline().decode('utf-8', errors='replace').strip()
                clean_tokens = raw_line.split()
                
                for token in clean_tokens:
                    # Validate that the token is a proper 2-digit HEX byte
                    # Проверяем, что токен — это действительно двухзначный HEX-байт (00-FF)
                    if len(token) == 2 and all(c in "0123456789ABCDEFabcdef" for c in token):
                        hex_key_accumulator += token
                        
                        # Calculate progress / Расчет прогресса генерации
                        current_len = len(hex_key_accumulator)
                        progress = min(100, int((current_len / required_hex_chars) * 100))
                        
                        # Print updating progress line / Красивый вывод прогресса в одну строку
                        sys.stdout.write(f"\r[🔋] Generating key: {progress}% [{hex_key_accumulator[-4:] if len(hex_key_accumulator) >= 4 else hex_key_accumulator}]")
                        sys.stdout.flush()
                        
                        if len(hex_key_accumulator) >= required_hex_chars:
                            break
                            
        ser.close()
        return hex_key_accumulator[:required_hex_chars].upper()
        
    except serial.SerialException:
        print(f"\n[❌] Error: Could not open port {SERIAL_PORT}. Please check connection or port number.")
        return None
    except KeyboardInterrupt:
        print(f"\n[🛑] Process interrupted by user. Closing port safely.")
        if ser and ser.is_open:
            ser.close()
        return None

if __name__ == "__main__":
    print("="*60)
    print(" LNL-EntropyShield Client v1.1 — Cryptographic Key Generator ")
    print("="*60)
    
    # Generate a standard AES-256 key (32 bytes / 256 bits)
    # Генерируем стандартный ключ для алгоритма AES-256 (32 байта)
    secure_key = harvest_entropy_key(32)
    
    if secure_key:
        print("\n\n" + "—"*60)
        print("[🔑] CRYPTOGRAPHICALLY SECURE KEY GENERATED:")
        print(f"👉 {secure_key}")
        print("—"*60)
        print("[🛡️] Key derived successfully from physical entropy. Immune to predictive analysis.")
