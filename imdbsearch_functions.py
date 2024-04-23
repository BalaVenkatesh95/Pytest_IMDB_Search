

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ImdbClass:
   def __init__(self, url):
       self.url = url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))



   # browser initiation and url navigation
   def initiation_function(self):
       try:
           self.driver.maximize_window()
           self.driver.get(self.url)
           return True
       except:
           print("ERROR : URL is incorrect/Network Error")
           return False


   # Quit browser
   def shutdown(self):
       if self.initiation_function():
           return self.driver.quit()
       else:
           return False



   def name_search(self):
       if self.initiation_function():
           # Using script facility to scroll to required object by providing pixel value
           self.driver.execute_script("window.scrollBy(0, 750);")

           # Wait for the Awards & Recognition dropdown button to be clickable using explicit wait
           awards_drop_down_button = WebDriverWait(self.driver, 15).until(
               EC.element_to_be_clickable((By.XPATH, "//div[text()='Awards & recognition']"))
           )
           awards_drop_down_button.click()

           # Wait for the Award Nominated button to be clickable using explicit wait
           award_nominated_button = WebDriverWait(self.driver, 20).until(
               EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='test-chip-id-oscar_best_actor_nominees']"))
           )
           award_nominated_button.click()
           # Using script facility to scroll to required object by providing pixel value
           self.driver.execute_script("window.scrollBy(0, -400);")


           name_dropdown_button = WebDriverWait(self.driver, 30).until(
               EC.visibility_of_element_located((By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn' and text()='Name']"))
           )
           name_dropdown_button = WebDriverWait(self.driver, 30).until(
               EC.element_to_be_clickable((By.XPATH, "//div[@class='sc-6addea7c-0 dWrCpn' and text()='Name']"))
           )

           name_dropdown_button.click()


           # Wait for the Name input field and send keys
           name_input_field = WebDriverWait(self.driver, 30).until(
               EC.visibility_of_element_located((By.XPATH, "//input[@name='name-text-input']"))
           )
           name_input_field.send_keys("christian bale")

           # Using script facility to scroll to required object by providing pixel value
           self.driver.execute_script("window.scrollBy(0, 1100);")

           gender_dropdown_button = WebDriverWait(self.driver, 30).until(
               EC.visibility_of_element_located((By.XPATH, "//div[text()='Gender identity']"))
           )
           # Wait for the Gender Identity dropdown button to click
           gender_dropdown_button = WebDriverWait(self.driver, 30).until(
               EC.element_to_be_clickable((By.XPATH, "//div[text()='Gender identity']"))
           )
           gender_dropdown_button.click()

           # Wait for the Gender Male button to click
           gender_male_button = WebDriverWait(self.driver, 25).until(
               EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='test-chip-id-MALE']"))
           )
           gender_male_button.click()

           # Wait for the See Results button to click
           see_results_button = WebDriverWait(self.driver, 15).until(
               EC.element_to_be_clickable((By.XPATH, "//span[text()='See results']"))
           )
           see_results_button.click()
       else:
           return False

