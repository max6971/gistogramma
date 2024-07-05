import time
import pandas as pd
import matplotlib.pyplot as plt
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def fetch_divan_prices(url):
    options = Options()
    options.headless = True
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)

    driver.get(url)
    time.sleep(15)  # Дайте время странице загрузиться

    prices = []
    price_elements = driver.find_elements(By.CLASS_NAME,'ui-LD-ZU KIkOH')  # Замените 'price__number' на соответствующий класс

    for price_element in price_elements:
        price_text = price_element.text.replace('₽', '').replace(' ', '').strip()
        try:
            price = int(price_text)
            prices.append(price)
        except ValueError:
            continue

    driver.quit()
    return prices


def save_to_csv(prices, filename):
    df = pd.DataFrame(prices, columns=['Price'])
    df.to_csv(filename, index=False)


def main():
    url = 'https://www.divan.ru/novosibirsk/category/divany-i-kresla'  # Подставьте правильный URL
    prices = fetch_divan_prices(url)

    if not prices:
        print("No prices found.")
        return

    save_to_csv(prices, 'divan_prices.csv')

    # Calculate and print the average price
    average_price = sum(prices) / len(prices)
    print(f"Средняя цена: {average_price:.2f} руб.")

    # Plot the histogram
    plt.hist(prices, bins=20, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (руб.)')
    plt.ylabel('Количество')
    plt.show()


if __name__ == '__main__':
    main()