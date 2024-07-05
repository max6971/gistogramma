import csv

# Открываем исходный файл для чтения
with open('sofa_prices.csv', mode='r', newline='', encoding='utf-8') as infile:
    reader = csv.reader(infile)

    # Читаем заголовки
    headers = next(reader)

    # Читаем все строки и удаляем ненужные символы
    cleaned_data = []
    for row in reader:
        cleaned_row = [cell.replace('руб.', '').replace(' ', '') for cell in row]
        cleaned_data.append(cleaned_row)

# Открываем новый файл для записи очищенных данных
with open('sofa_grafice.csv', mode='w', newline='', encoding='utf-8') as outfile:
    writer = csv.writer(outfile)

    # Записываем заголовки
    writer.writerow(headers)

    # Записываем очищенные данные
    writer.writerows(cleaned_data)

print("Данные успешно преобразованы и записаны в файл sofa_grafice.csv")