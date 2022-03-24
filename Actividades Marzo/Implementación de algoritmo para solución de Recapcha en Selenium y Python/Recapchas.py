import os
import random
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.alert import Alert

import speech_recognition as sr
import requests, urllib, pydub


chrome_options = Options()
#chrome_options.add_experimental_option("detach", True)


def delay():
    time.sleep(random.randint(2,3))


Webs=['https://www.google.com/recaptcha/api2/demo','https://aplicaciones.adres.gov.co/bdua_internet/Pages/ConsultarAfiliadoWeb.aspx']

driver=webdriver.Chrome(os.getcwd()+'\chromedriver.exe')
driver.get(Webs[1])
driver.find_element_by_id('txtNumDoc').send_keys("70041053")

frames=driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()

driver.find_element_by_class_name("recaptcha-checkbox-border").click()

driver.switch_to.default_content()
frames=driver.find_element_by_xpath("/html/body/div[2]/div[4]").find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[0])
delay()

driver.find_element_by_id("recaptcha-audio-button").click()

driver.switch_to.default_content()
frames=driver.find_elements_by_tag_name("iframe")
driver.switch_to.frame(frames[-1])
delay()

driver.find_element_by_xpath("/html/body/div/div/div[3]/div/button").click()
src=driver.find_element_by_id("audio-source").get_attribute("src")

print(src)

prefs={'download.default_directory' : os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument("--headless")

driver2= webdriver.Chrome(os.getcwd()+'\chromedriver.exe',chrome_options=chrome_options)
driver2.get(url='https://audio.online-convert.com/es/convertir-a-wav')


driver2.find_element_by_link_text('Introducir URL').click()
time.sleep(1)
driver2.find_element_by_id('remoteUrlInput').send_keys(src)
time.sleep(1)
driver2.find_element_by_id('addRemoteUrlButton').click()
time.sleep(1)
driver2.find_element_by_id('submitBtn').click()


if os.path.isfile(os.getcwd()+"\\www_google_com-payload.wav"):
     os.remove(os.getcwd()+"\\www_google_com-payload.wav")

sw = True
while sw == True:
    if os.path.isfile(os.getcwd()+"\\www_google_com-payload.wav"):
        driver2.quit()
        sw = False

if sw == False:
    sample_audio=sr.AudioFile(os.getcwd()+"\\www_google_com-payload.wav")


r=sr.Recognizer()

with sample_audio as source:
    audio=r.record(source)
    key=r.recognize_google(audio,language="es-ES")
    print("Clave Audio: ",key)

driver.find_element_by_id("audio-response").send_keys(key.lower())
driver.find_element_by_id("audio-response").send_keys(Keys.ENTER)
