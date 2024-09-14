from selenium import webdriver
from chromedriver_py import binary_path
from selenium.webdriver.common.by import By
import time

svc = webdriver.ChromeService(executable_path=binary_path)
driver = webdriver.Chrome(service=svc)
def autoriz(login, password):
    driver.get("https://www.saucedemo.com/")

    # Поиск элементов и присваивание к переменным.
    input_username = driver.find_element(By.NAME,"user-name")
    input_password = driver.find_element(By.NAME,"password")
    login_button = driver.find_element(By.NAME,"login-button")

    # Действия с формами
    input_username.send_keys(login)
    input_password.send_keys(password)
    login_button.click()

    # Поиск и проверка попадания на главную страницу
    title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text.lower() == "products":
        return True
    return False

    time.sleep(3)
def tovarAddToCart(tovar):
    for i in range(101):
        item_name = driver.find_element(By.XPATH,f"//*[@id=\"item_{i}_title_link\"]/div")
        if item_name.text.lower() == tovar.lower():
            item_name.click()
            time.sleep(3)
            item_add_button = driver.find_element(By.NAME,"add-to-cart")
            item_add_button.click()
            time.sleep(3)
            card_button = driver.find_element(By.ID, "shopping_cart_container")
            card_button.click()
            title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
            if title_text.text.lower() == "your cart":
                time.sleep(3)
                item_name_card = driver.find_element(By.XPATH, f"//*[@id=\"item_{i}_title_link\"]/div")
                if item_name_card.text.lower() == tovar.lower():
                    print(item_name_card.text.lower())
                    time.sleep(3)
                    return True
    return False
def zakaz(f_name,l_name,p_code):
    check_button = driver.find_element(By.ID, "checkout")
    check_button.click()
    time.sleep(3)
    # Поиск и проверка попадания на страницу заказа
    title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
    if title_text.text.lower() == "checkout: your information":
        first_name = driver.find_element(By.ID, "first-name")
        last_name = driver.find_element(By.ID, "last-name")
        postal_code = driver.find_element(By.ID, "postal-code")
        continue_button = driver.find_element(By.ID, "continue")

        first_name.send_keys(f_name)
        last_name.send_keys(l_name)
        postal_code.send_keys(p_code)
        continue_button.click()
        time.sleep(3)
        title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
        if title_text.text.lower() == "checkout: overview":
            finish_button = driver.find_element(By.ID, "finish")
            finish_button.click()
            time.sleep(3)
            title_text = driver.find_element(By.XPATH, "//*[@id=\"header_container\"]/div[2]/span")
            if title_text.text.lower() == "checkout: complete!":
                return True
    return False

if __name__ == '__main__':
    if autoriz("standard_user","secret_sauce"):
        print("Вы попали на главную страницу")
        if tovarAddToCart("Sauce Labs Backpack"):
            print("Товар в корзине")
            if zakaz("petr","bobrov","123"):
                print("Заказ оформлен")
            else:
                print("Не удалось оформить заказ")
        else:
            print("Товар не найден в корзине")
    else:
        print("Вы не авторизованы")


