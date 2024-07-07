import time


import data
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By



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
    comfort_tariff = (By.XPATH, '//div[contains(@class, "tcard") and .//div[contains(@class, "tcard-title") and text()="Comfort"]]')
    phone_button = (By.XPATH, "//div[@class='np-button']//div[@class='np-text' and text()='Número de teléfono']")
    phone_field = (By.ID, 'phone')
    next_button = (By.XPATH, "//button[@type='submit' and @class='button full' and text()='Siguiente']")
    sms_code = (By.ID, "code")
    confirm_button = (By.XPATH, "//button[text()='Confirmar']")
    payment_method_button = (By.XPATH, "//div[@class='pp-text' and text()='Método de pago']")
    add_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/div[2]/div[3]/div[2]')
    add_card_number = (By.ID, 'number')
    add_card_cvv = (By.XPATH, '(//*[@id="code"])[2]')
    agregar_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_popup_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    click_message_field = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[3]/div/label')
    message_field = (By.ID, 'comment')
    mantas_panuelos_button = (By.CLASS_NAME, 'slider')
    plus_button = (By.CLASS_NAME, 'counter-plus')
    pedir_taxi_button = (By.XPATH, '//*[@id="root"]/div/div[3]/div[4]/button')

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

    def select_phone_button(self):
        phone_button_element = self.driver.find_element(*self.phone_button)
        phone_button_element.click()

    def set_phone(self, phone):
        phone_field_element = self.driver.find_element(*self.phone_field)
        phone_field_element.clear()
        phone_field_element.send_keys(phone)

    def select_next_button(self):
        next_button_element = self.driver.find_element(*self.next_button)
        next_button_element.click()

    def set_code(self, code):
        sms_code_element = self.driver.find_element(*self.sms_code)
        sms_code_element.clear()
        sms_code_element.send_keys(code)

    def select_confirm_button(self):
        confirm_button_element = self.driver.find_element(*self.confirm_button)
        confirm_button_element.click()

    def select_payment_method_button(self):
        payment_method_button_element = self.driver.find_element(*self.payment_method_button)
        payment_method_button_element.click()

    def select_add_card_button(self):
        add_card_button_element = self.driver.find_element(*self.add_card_button)
        add_card_button_element.click()

    def select_add_card_number(self, card):
        add_card_number_element = self.driver.find_element(*self.add_card_number)
        add_card_number_element.clear()
        add_card_number_element.send_keys(card)

    def select_add_card_cvv(self, cvv):
        add_card_cvv_element = self.driver.find_element(*self.add_card_cvv)
        add_card_cvv_element.clear()
        add_card_cvv_element.send_keys(cvv)

    def select_agregar_button(self):
        agregar_button_element = self.driver.find_element(*self.agregar_button)
        agregar_button_element.click()

    def select_close_popup_button(self):
        close_popup_button_element = self.driver.find_element(*self.close_popup_button)
        close_popup_button_element.click()

    def select_click_message_field(self):
        click_message_field_element = self.driver.find_element(*self.click_message_field)
        click_message_field_element.click()

    def set_message_field(self, message):
        message_field_element = self.driver.find_element(*self.message_field)
        message_field_element.clear()
        message_field_element.send_keys(message)

    def select_mantas_panuelos_button(self):
        mantas_panuelos_button_element = self.driver.find_element(*self.mantas_panuelos_button)
        mantas_panuelos_button_element.click()

    def select_plus_button(self):
        plus_button_element = self.driver.find_element(*self.plus_button)
        plus_button_element.click()
        plus_button_element.click()

    def select_pedir_taxi_button(self):
        pedir_taxi_button_element = self.driver.find_element(*self.pedir_taxi_button)
        pedir_taxi_button_element.click()

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

    def test_urban_route_page(self):
        time.sleep(2)
        self.routes_page.set_from(data.address_from)
        assert self.routes_page.get_from() == data.address_from, f"Expected 'from' field to be '{data.address_from}', but got '{self.routes_page.get_from()}'"
        time.sleep(1)
        self.routes_page.set_to(data.address_to)
        assert self.routes_page.get_to() == data.address_to, f"Expected 'to' field to be '{data.address_to}', but got '{self.routes_page.get_to()}'"
        time.sleep(1)
        self.routes_page.call_taxi()
        time.sleep(1)
        self.routes_page.select_comfort_tariff()
        time.sleep(1)
        self.routes_page.select_phone_button()
        self.routes_page.set_phone(data.phone_number)
        time.sleep(1)
        self.routes_page.select_next_button()
        time.sleep(2)
        sms_code = retrieve_phone_code(self.driver)
        self.routes_page.set_code(sms_code)
        time.sleep(2)
        self.routes_page.select_confirm_button()
        time.sleep(3)
        self.routes_page.select_payment_method_button()
        time.sleep(2)
        self.routes_page.select_add_card_button()
        time.sleep(2)
        self.routes_page.select_add_card_number(data.card_number)
        time.sleep(3)
        self.routes_page.select_add_card_cvv(data.card_code)
        time.sleep(2)
        self.routes_page.select_agregar_button()
        time.sleep(2)
        self.routes_page.select_close_popup_button()
        time.sleep(2)
        self.routes_page.select_click_message_field()
        time.sleep(2)
        self.routes_page.set_message_field(data.message_for_driver)
        time.sleep(2)
        self.routes_page.select_mantas_panuelos_button()
        time.sleep(2)
        self.routes_page.select_plus_button()
        time.sleep(2)
        self.routes_page.select_pedir_taxi_button()
        time.sleep(45)

