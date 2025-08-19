import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

BASE_URL = "http://127.0.0.1:8000"

class MiCanchaTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome() 
        self.driver.implicitly_wait(3)

    def tearDown(self):
        self.driver.quit()

    def test_01_registro_usuario(self):
        driver = self.driver
        driver.get(f"{BASE_URL}/usuarios/registro/")
        driver.find_element(By.NAME, "username").send_keys("pruebat12")
        driver.find_element(By.NAME, "password1").send_keys("123qwe!")
        driver.find_element(By.NAME, "password2").send_keys("123qwe!")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)  
        self.assertIn("Bienvenido", driver.page_source)

    def test_02_login(self):
        driver = self.driver
        driver.get(f"{BASE_URL}/usuarios/login/")
        driver.find_element(By.NAME, "username").send_keys("usuario_test")
        driver.find_element(By.NAME, "password").send_keys("Prueba123!")
        driver.find_element(By.TAG_NAME, "button").click()
        time.sleep(3)
        self.assertIn("Cerrar sesión", driver.page_source)

    def test_03_ver_canchas(self):
        driver = self.driver
        driver.get(BASE_URL)
        time.sleep(2)
        self.assertIn("Canchas Disponibles", driver.page_source)

    def test_04_reservar_cancha(self):
        driver = self.driver
        driver.get(BASE_URL)
        reservar_btn = driver.find_element(By.XPATH, "//form[@method='POST']/button")
        reservar_btn.click()
        time.sleep(4)
        self.assertIn("¡La reserva", driver.page_source)

    def test_05_historial_reservas(self):
        driver = self.driver
        driver.get(f"{BASE_URL}/historial_reservas/")
        time.sleep(2)
        self.assertIn("Mi Historial de Reservas", driver.page_source)


    def test_06_editar_usuario(self):
        driver = self.driver
        driver.get(f"{BASE_URL}/usuarios/perfil/")
        time.sleep(2)

     
        first_name_input = driver.find_element(By.NAME, "first_name")
        last_name_input = driver.find_element(By.NAME, "last_name")
        email_input = driver.find_element(By.NAME, "email")

        first_name_input.clear()
        first_name_input.send_keys("UsuarioEditado")
        time.sleep(1)
        last_name_input.clear()
        last_name_input.send_keys("Prueba")
        time.sleep(1)
        email_input.clear()
        email_input.send_keys("usuario_editado@test.com")
        time.sleep(1)

    
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(3)

    
        self.assertIn("Cuenta actualizada", driver.page_source)

    def test_07_cancelar_reserva(self):
        driver = self.driver
        driver.get(f"{BASE_URL}/historial_reservas/")
        driver.find_element(By.XPATH, "//button[contains(text(),'Cancelar')]").click()
        time.sleep(4)
        self.assertIn("cancelada", driver.page_source)

    def test_08_detalles_cancha(self):
        driver = self.driver
        driver.get(BASE_URL)
        driver.find_element(By.LINK_TEXT, "Detalles").click()
        time.sleep(4)
        self.assertIn("Descripción", driver.page_source)

    def test_09_navegar_canchas(self):
        driver = self.driver
        driver.get(BASE_URL)
        links = driver.find_elements(By.LINK_TEXT, "Detalles")
        self.assertGreater(len(links), 0)
        time.sleep(2)

    def test_10_logout(self):
        driver = self.driver
        driver.get(BASE_URL)
        driver.find_element(By.LINK_TEXT, "Cerrar sesión").click()
        time.sleep(3)
        self.assertIn("Iniciar sesión", driver.page_source)

if __name__ == "__main__":
    unittest.main()
