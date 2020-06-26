from selenium import webdriver
import allure
import pytest
import os

diameter1 = '9.1'
diameter2 = '9.5'
diameter3 = '9.9'
diameter4 = '7.0'

depth1 = '90'
depth2 = '100'
depth3 = '120'

angle1 = '30'
angle2 = '90'
angle3 = '120'

@pytest.fixture()
def test_setup():
    global driver
    os.startfile(r'driver\Winium.Desktop.Driver.exe')
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                              desired_capabilities={'app': r"femto_visum\FemtoVisum.exe"})
    yield
    # f: Указывает, что процесс принудительно завершен.
    # im (ImageName): Указывает имя изображения процесса прекращается.
    driver.quit()
    os.system("taskkill /f /im Winium.Desktop.Driver.exe")


@allure.feature('Ввод операцционных парамтеров ZLasik')
@allure.story('Ввод допустимого операционного параметра "Диаметр"')
@allure.severity('critical')
def test_diameter(test_setup):
    # Входим в меню выбора операции
    window_operation = driver.find_element_by_class_name('#32770')  # Находим окно меню
    button_operation = window_operation.find_element_by_id('1021')
    button_operation.click()  # Находим кнопку операция

    # выбор операции z-lasik
    window_operation_menu = driver.find_element_by_class_name('#32770')
    window_operation_menu.find_element_by_id('1015').click()

    # Ввод допустимого диапозона значений диаметра

    # Dдиаметр 9.1
    window_oper_param = driver.find_element_by_class_name('#32770')
    window_oper_param.find_element_by_id('1126').send_keys(diameter1)
    driver.find_element_by_id('1015').click()
    text1 = str(driver.find_element_by_id('1126').text)
    assert text1 == diameter1

    # Dдиаметр 9.5
    window_oper_param.find_element_by_id('1126').send_keys(diameter2)
    driver.find_element_by_id('1015').click()
    text2 = str(driver.find_element_by_id('1126').text)
    assert text2 == diameter2

    # Dдиаметр 9.9
    window_oper_param.find_element_by_id('1126').send_keys(diameter3)
    driver.find_element_by_id('1015').click()
    text3 = str(driver.find_element_by_id('1126').text)
    assert text3 == diameter3

    # Диаметр 7.0
    window_oper_param.find_element_by_id('1126').send_keys(diameter4)
    driver.find_element_by_id('1015').click()
    driver.find_element_by_id('1004').send_keys('popa')
    driver.find_element_by_id('1015').click()
    driver.find_element_by_id('1004').send_keys('-7.1')
    driver.find_element_by_id('1015').click()
    driver.find_element_by_id('1016').click()
    text4 = str(driver.find_element_by_id('1126').text)
    assert text4 != diameter4


def test_depth(test_setup):
    # Входим в меню выбора операции
    window_operation = driver.find_element_by_class_name('#32770')  # Находим окно меню
    button_operation = window_operation.find_element_by_id('1021')
    button_operation.click()  # Находим кнопку операция

    # Выбор операции z-lasik
    window_operation_menu = driver.find_element_by_class_name('#32770')
    window_operation_menu.find_element_by_id('1015').click()

    # Ввод допустимых значений параметра глубина
    # Глубина 90
    window_oper_param = driver.find_element_by_class_name('#32770')
    window_oper_param.find_element_by_id('1312').send_keys(depth1)
    driver.find_element_by_id('1015').click()
    text1 = str(driver.find_element_by_id('1312').text)
    assert text1 == depth1

    # Глубина 100
    window_oper_param.find_element_by_id('1312').send_keys(depth2)
    driver.find_element_by_id('1015').click()
    text2 = str(driver.find_element_by_id('1312').text)
    assert text2 == depth2

    # Глубина 120
    window_oper_param.find_element_by_id('1312').send_keys(depth3)
    driver.find_element_by_id('1015').click()
    text3 = str(driver.find_element_by_id('1312').text)
    assert text3 == depth3


def test_angle(test_setup):
    # Входим в меню выбора операции
    window_operation = driver.find_element_by_class_name('#32770')  # Находим окно меню
    button_operation = window_operation.find_element_by_id('1021')
    button_operation.click()  # Находим кнопку операция

    # Выбор операции z-lasik
    window_operation_menu = driver.find_element_by_class_name('#32770')
    window_operation_menu.find_element_by_id('1015').click()

    # Ввод допустимых значений параметра угол краевого реза
    # Угол краевого реза 30
    window_oper_param = driver.find_element_by_class_name('#32770')
    window_oper_param.find_element_by_id('1282').send_keys(angle1)
    driver.find_element_by_id('1015').click()
    text1 = str(driver.find_element_by_id('1282').text)
    assert text1 == angle1

    # Угол краевого реза 90
    window_oper_param.find_element_by_id('1282').send_keys(angle2)
    driver.find_element_by_id('1015').click()
    text2 = str(driver.find_element_by_id('1282').text)
    assert text2 == angle2

    # Угол краевого реза 120
    window_oper_param.find_element_by_id('1282').send_keys(angle3)
    driver.find_element_by_id('1015').click()
    text3 = str(driver.find_element_by_id('1282').text)
    assert text3 == angle3
