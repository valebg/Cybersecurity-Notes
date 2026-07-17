import cv2
from pyzbar.pyzbar import decode
import os

folder = "./Barcode_World"
barcode_data = []

print("[*] Запуск разбора штрих-кодов...")

for i in range(1, 9375):
    image_path = os.path.join(folder, f"{i}.png")
    image = cv2.imread(image_path)

    if image is None:
        continue

    decoded = decode(image)
    for barcode in decoded:
        # Декодируем байты в обычную строку (например, "65 ")
        chunk = barcode.data.decode("utf-8")
        barcode_data.append(chunk)

# Соединяем все полученные куски в одну большую строку с числами
raw_numbers_str = "".join(barcode_data)

print("\n[*] Декодирование завершено! Конвертируем десятичные коды в текст...")
print("-" * 60)

try:
    # Разбираем строку по пробелам, берем каждое число, переводим в int и затем в символ chr()
    clean_text = "".join(chr(int(num)) for num in raw_numbers_str.split() if num.isdigit())
    print(clean_text)
except Exception as e:
    print("[-] Ошибка при конвертации, выводим сырой результат:")
    print(raw_numbers_str)

print("-" * 60)