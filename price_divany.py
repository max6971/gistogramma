import time
import csv
import time
import csv

import driver
import prices
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

# Настройки для Firefox
options = Options()
options.headless = True  # Запуск браузера в фоновом режиме

# Укажите путь к geckodriver
service = Service(GeckoDriverManager().install())

# Запуск браузера
driver = webdriver.Firefox(service=service, options=options)

# URL сайта с диванами
url = 'https://www.divan.ru/novosibirsk/category/divany-i-kresla'

try:
    # Открытие страницы
    # Открытие страницы
    driver.get(url)

    # Ждем загрузки элементов с ценами
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, "//span[contains(@class, 'ui-LD-ZU ui-SVNym bSEDs')]")))

    # Ищем элементы с ценами диванов
    price_elements = driver.find_elements(By.XPATH, "//span[contains(@class, 'ui-LD-ZU ui-SVNym bSEDs')]")

    # Проверяем, что элементы найдены
    if not price_elements:
      print("Цены не найдены на странице.")
    else:
        print(f"Найдено {len(price_elements)} цен.")

    # Извлечение текстовых значений
    prices = [price.text for price in price_elements]

    # Проверяем, что цены извлечены
    if not prices:
        print("Не удалось извлечь цены.")
    else:
        print(f"Извлечено {len(prices)} цен.")

    # Запись данных в CSV файл
    with open('sofa_prices.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Price'])
        for price in prices:
            writer.writerow([price.strip()])

    print("Данные успешно сохранены в файл sofa_prices.csv")

except Exception as e:
    print(f"Ошибка: {e}")

finally:
    # Закрытие браузера
    driver.quit()