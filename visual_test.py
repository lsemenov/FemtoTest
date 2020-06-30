from selenium import webdriver
import allure
import pytest
import os
from PIL import Image, ImageDraw

os.startfile(r'driver\Winium.Desktop.Driver.exe')


def process_region(image: object, x: object, y: object, width: object, height: object) -> object:
    region_total = 0

    # This is the sensitivity factor, the larger it is the less sensitive the comparison
    factor = 10

    for coordinateY in range(y, y + height):
        for coordinateX in range(x, x + width):
            try:
                pixel = image.getpixel((coordinateX, coordinateY))
                region_total += sum(pixel) / 4
            except:
                return

    return region_total / factor


@pytest.fixture()
def test_setup():
    global driver
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                              desired_capabilities={'app': r"femto_visum\FemtoVisum.exe"})
    yield
    driver.close()
    driver.quit()


@allure.feature('Ввод операцционных парамтеров ZLasik')
@allure.story('Ввод допустимого операционного параметра "Диаметр"')
@allure.severity('critical')
def test_os(test_setup):
    # Входим в меню выбора операции
    global region_staging
    window_operation = driver.find_element_by_class_name('#32770')  # Находим окно меню
    button_operation = window_operation.find_element_by_id('1021')
    button_operation.click()  # Находим кнопку операция

    # выбор операции z-lasik
    window_operation_menu = driver.find_element_by_class_name('#32770')
    window_operation_menu.find_element_by_id('1015').click()

    # Кликаем правый OS глаз
    driver.find_element_by_id("1341").click()
    # кликаем  OD глаз
    # driver.find_element_by_id("1008").click()

    # делаем скриншот
    element = driver.find_element_by_id("1001")

    # driver.save_screenshot("screenshots\prodaction\screen_production.png")
    driver.save_screenshot("screenshots\staging\staging.png")

    # сравнение c эталоном

    screenshot_staging = Image.open("screenshots\staging\staging.png")
    screenshot_production = Image.open("screenshots\prodaction\screen_production.png")
    columns = 60
    rows = 80
    screen_width, screen_height = screenshot_staging.size

    block_width = ((screen_width - 1) // columns) + 1  # this is just a division ceiling
    block_height = ((screen_height - 1) // rows) + 1

    for y in range(0, screen_height, block_height + 1):
        for x in range(0, screen_width, block_width + 1):
            region_staging = process_region(screenshot_staging, x, y, block_width, block_height)
            region_production = process_region(screenshot_production, x, y, block_width, block_height)

            if region_staging is not None and region_production is not None and region_production != region_staging:
                draw = ImageDraw.Draw(screenshot_staging)
                draw.rectangle((x, y, x + block_width, y + block_height), outline="red")

    screenshot_staging.save("screenshots\diff\Result.png")
    # diff = int(region_staging) / region_production
    print(region_staging)
    print(region_production)
    # assert diff < 1000
