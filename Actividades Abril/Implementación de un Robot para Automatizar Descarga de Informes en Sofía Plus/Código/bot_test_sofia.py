from tkinter.tix import Form
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Chrome('chromedriver.exe',options=options)
#driver= webdriver.Firefox(executable_path=r'C:/Users/User1/Dropbox/Proyecto SENA - Monitoria/Desarrollo/Bot - Selenium/Desarrollo BOT - SofiaPlus/geckodriver.exe')


driver.get('http://www.senasofiaplus.edu.co/sofia-public/')

timeout=30;

driver.implicitly_wait(20)

rol = WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.ID, 'seleccionRol:roles'))
                                             )

select_object = Select(rol)
select_object.select_by_visible_text('Aprendiz')

time.sleep(5)

Formacion = WebDriverWait(driver, timeout).until( 
        EC.presence_of_element_located((By.LINK_TEXT, 'Ejecución de la Formación'))
                                             )
Formacion.click()

Ruta = WebDriverWait(driver, timeout).until( 
        EC.presence_of_element_located((By.LINK_TEXT, 'Desarrollar Ruta de Aprendizaje'))
                                             )
Ruta.click()

Consultar = WebDriverWait(driver, timeout).until( 
        EC.presence_of_element_located((By.LINK_TEXT, 'Consultar Ruta del Aprendiz'))
                                             )
Consultar.click()

#ActionChains(driver).move_by_offset(850, 487).click().perform() # Click derecho del mouse  (850,485)

time.sleep(30)
driver.execute_script("document.getElementsByClassName('control_req').value='2340377';")  
"""

Ficha= WebDriverWait(driver, timeout).until( 
        EC.presence_of_element_located((By.ID, 'frmConsulta:j_id_jsp_102633460_66'))
                                         )


driver.implicitly_wait(20)
driver.find_element_by_xpath('/html/body[1]/div[2]/div/form/table/tbody/tr/td[2]/table/tbody/tr/td[1]/textarea')


Ficha = WebDriverWait(driver, 30).until( 
        EC.presence_of_element_located((By.ID, 'cargando'))
                                             )
Ficha.send_keys('2340377')


Consultar = WebDriverWait(driver, timeout).until( 
        EC.presence_of_element_located((By.ID, 'frmConsulta:btnSearch'))
                                             )
Consultar.click()
"""