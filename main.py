import time
from lib2to3.pgen2 import driver

import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


# no modificar
def retrieve_phone_code(driver) -> str:
    """Este código devuelve un número de confirmación de teléfono y lo devuelve como un string.
    Utilízalo cuando la aplicación espere el código de confirmación para pasarlo a tus pruebas.
    El código de confirmación del teléfono solo se puede obtener después de haberlo solicitado en la aplicación."""
    import json
    import time
    from selenium.common import WebDriverException
    code = None
    for i in range(10):
        try:
            logs = [log["message"] for log in driver.get_log('performance') if log.get("message")
                    and 'api/v1/number?number' in log.get("message")]
            for log in reversed(logs):
                message_data = json.loads(log)["message"]
                body = driver.execute_cdp_cmd('Network.getResponseBody',
                                              {'requestId': message_data["params"]["requestId"]})
                code = ''.join([x for x in body['body'] if x.isdigit()])
        except WebDriverException:
            time.sleep(1)
            continue
        if not code:
            raise Exception("No se encontró el código de confirmación del teléfono.\n"
                            "Utiliza 'retrieve_phone_code' solo después de haber solicitado el código en tu aplicación.")
        return code


class UrbanRoutesPage:
    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    button_round = (By.CLASS_NAME, "button.round")
    comfort_tariff = (By.CLASS_NAME, "i-button tcard-i active")
  #  phone_field = (By.ID, 'phone')
  #  add_card_button = (By.ID, 'add_card')
  #  card_number_field = (By.ID, 'card_number')
  #  card_code_field = (By.ID, 'code')
  #  link_button = (By.ID, 'link')
  #  message_field = (By.ID, 'message')
  #  blanket_checkbox = (By.ID, 'blanket')
  #  tissues_checkbox = (By.ID, 'tissues')
  #  ice_cream_selector = (By.ID, 'ice_cream')
  #  find_taxi_button = (By.ID, 'find_taxi')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, address):
        from_element = self.driver.find_element(*self.from_field)
        from_element.clear()
        from_element.send_keys(address)

    def set_to(self, address):
        to_element = self.driver.find_element(*self.to_field)
        to_element.clear()
        to_element.send_keys(address)

    def call_taxi(self):
        button_round_element = self.driver.find_element(*self.button_round)
        button_round_element.click()

    def select_comfort_tariff(self):
        comfort_tariff_element = self.driver.find_element(*self.comfort_tariff)
        comfort_tariff_element.click()

  #  def set_phone(self, phone_number):
    #    self.driver.find_element(*self.phone_field).send_keys(phone_number)

   # def add_credit_card(self, card_number, card_code):
     #   self.driver.find_element(*self.add_card_button).click()
      #  self.driver.find_element(*self.card_number_field).send_keys(card_number)
       # self.driver.find_element(*self.card_code_field).send_keys(card_code)
        #self.driver.find_element(*self.card_code_field).send_keys(Keys.TAB)
        #WebDriverWait(self.driver, 10).until(
         #   EC.element_to_be_clickable(self.link_button)
       # ).click()

    #def set_message(self, message):
     #   self.driver.find_element(*self.message_field).send_keys(message)

    # def request_blanket_and_tissues(self):
      #  self.driver.find_element(*self.blanket_checkbox).click()
       # self.driver.find_element(*self.tissues_checkbox).click()

    #def request_ice_cream(self, quantity):
     #   selector = self.driver.find_element(*self.ice_cream_selector)
      #  for _ in range(quantity):
       #     selector.send_keys(Keys.UP)

    #def find_taxi(self):
           # self.driver.find_element(*self.find_taxi_button).click()

    def call_taxi(self):
            self.driver.find_element(*self.button_round).click()

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')


class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        from selenium.webdriver.chrome.service import Service
        from selenium.webdriver.chrome.options import Options
        options = Options()
        options.set_capability("goog:loggingPrefs", {'performance': 'ALL'})
        cls.driver = webdriver.Chrome(service=Service(), options=options)
        cls.driver.maximize_window()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        self.driver.get(data.urban_routes_url)
        self.routes_page = UrbanRoutesPage(self.driver)

    def test_set_route(self):
        time.sleep(2)
        self.routes_page.set_from(data.address_from)
        time.sleep(2)
        self.routes_page.set_to(data.address_to)
        time.sleep(2)
        assert self.routes_page.get_from() == data.address_from
        assert self.routes_page.get_to() == data.address_to
        time.sleep(2)
        self.routes_page.call_taxi()
        time.sleep(2)
        button_round = self.driver.find_element(By.CLASS_NAME, "button.round")
        button_round.click()
        time.sleep(2)
        self.routes_page.select_comfort_tariff()
        time.sleep(2)


#    def test_complete_taxi_order(self):
#        time.sleep(2)
#       self.routes_page.set_from(data.address_from)
#       time.sleep(2)
#        self.routes_page.set_to(data.address_to)
#      time.sleep(2)
#       self.routes_page.select_comfort_tariff()
#     time.sleep(2)
#      self.routes_page.set_phone(data.phone_number)
#    time.sleep(2)
#      self.routes_page.add_credit_card(data.card_number, data.card_code)
#      phone_code = retrieve_phone_code(self.driver)
#     time.sleep(2)
#      self.routes_page.set_message(data.message_for_driver)
#     time.sleep(2)
#       self.routes_page.request_blanket_and_tissues()
#     time.sleep(2)
#       self.routes_page.request_ice_cream(2)
#     time.sleep(2)
#       self.routes_page.find_taxi()
#     time.sleep(2)

# Aquí puedes agregar más aserciones según lo que esperes después de hacer clic en "find_taxi"


if __name__ == "__main__":
    import pytest

    pytest.main()
