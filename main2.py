import numpy as np
import matplotlib.pyplot as plt

# Генерация двух наборов случайных данных
num_samples = 100  # Количество образцов
data_x = np.random.rand(num_samples)
data_y = np.random.rand(num_samples)

# Создание диаграммы рассеяния
plt.scatter(data_x, data_y, color='blue', alpha=0.5, edgecolors='w', linewidths=0.5)

# Добавление заголовка и меток осей
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('Значения X')
plt.ylabel('Значения Y')

# Показ диаграммы
plt.show()