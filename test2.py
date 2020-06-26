from selenium import webdriver
import allure
import pytest
import os

@allure.feature('Ввод операцционных парамтеров ZLasik')
@allure.story('Ввод допустимого операционного параметра "Диаметр"')
@allure.severity('critical')
def test_ui_zlasik():
    global driver
    os.startfile(r'C:\Users\_username_\PycharmProjects\testinf_Femo\driver\Winium.Desktop.Driver.exe')
    driver = webdriver.Remote(command_executor='http://localhost:9999',
                                       desired_capabilities={'app': r"C:\Users\_username_\PycharmProjects\testinf_Femo\femto_visum\FemtoVisum.exe"})
    # Входим в меню выбора операции
    window_operation = driver.find_element_by_class_name('#32770')     # Находим окно меню
    button_operation = window_operation.find_element_by_id('1021')
    button_operation.click()  # Находим кнопку операция

    # выбор операции z-lasik
    window_operation_menu = driver.find_element_by_class_name('#32770')
    window_operation_menu.find_element_by_id('1015').click()

    # Ввод операционных парамтеров
    diameter = '9.1'

    # диаметр
    window_oper_param = driver.find_element_by_class_name('#32770')
    window_oper_param.find_element_by_id('1126').send_keys(diameter)
    driver.find_element_by_id('1015').click()
    text = str(driver.find_element_by_id('1126').text)
    assert text == diameter
    driver.quit()