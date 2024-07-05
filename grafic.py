import pandas as pd
import matplotlib.pyplot as plt

# Чтение данных из файла sofa_grafice.csv
data = pd.read_csv('sofa_grafice.csv')

# Предположим, что цены находятся в колонке 'price'
# Преобразуем столбец 'price' в числовой формат
data['Price'] = pd.to_numeric(data['Price'], errors='coerce')

# Удаляем строки с некорректными значениями (NaN)
data = data.dropna(subset=['Price'])

# Находим среднее значение
average_price = data['Price'].mean()
print(f"Среднее значение цены: {average_price:.2f} руб.")

# Строим гистограмму значений
plt.figure(figsize=(10, 6))
plt.hist(data['Price'], bins=20, color='skyblue', edgecolor='black')
plt.title('Гистограмма цен на диваны')
plt.xlabel('Цена (руб.)')
plt.ylabel('Количество')
plt.axvline(average_price, color='red', linestyle='dashed', linewidth=1)
plt.text(average_price, plt.ylim()[1]*0.9, f'Среднее: {average_price:.2f}', color='red')
plt.grid(True)
plt.show()