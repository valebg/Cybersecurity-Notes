#!/usr/bin/env python3
from PIL import Image
import os

def extract_red_channel_lsb(image_path):
    if not os.path.exists(image_path):
        print(f"[-] Файл {image_path} не найден.")
        return

    print(f"[+] Анализ файла {image_path}...")
    img = Image.open(image_path)
    pixels = img.load()
    width, height = img.size

    binary_data = ""
    for y in range(height):
        for x in range(width):
            pixel = pixels[x, y]
            r = pixel[0]
            binary_data += str(r & 1)

    all_chars = []
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        if len(byte) == 8:
            all_chars.append(chr(int(byte, 2)))

    decoded_text = "".join(all_chars)
    print("[+] Декодирование завершено. Ищем сигнатуру флага...")

    if "SBT" in decoded_text:
        print("[!] Флаг успешно обнаружен в потоке данных!")
    else:
        print("[-] Сигнатура флага не найдена. Возможно, данные закодированы иначе.")

if __name__ == "__main__":
    extract_red_channel_lsb("Dalgona.png")
