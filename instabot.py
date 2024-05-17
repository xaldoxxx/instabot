# ubstabot014.py
import tkinter as tk
from tkinter import filedialog, messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
import os

class Locators:
    CAMPO_USUARIO = (By.XPATH, "//input[@name='username']")
    CAMPO_CONTRASEÑA = (By.XPATH, "//input[@name='password']")
    BOTON_INICIAR_SESION = (By.XPATH, "//button[@type='submit']")
    BOTON_AHORA_NO1 = (By.XPATH, "//div[@role='button']")
    BOTON_AHORA_NO2 = (By.XPATH, "//button[@class='_a9-- _ap36 _a9_1']")
    BOTON_PLUS = (By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[2]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[7]/div[1]/span[1]/div[1]/a[1]/div[1]/div[1]/div[1]/div[1]/*[name()='svg'][1]")
    INPUT_ARCHIVO = (By.XPATH, "//input[@type='file']")
    BOTON_SIGUIENTE1 = (By.XPATH, "//div[contains(text(),'Siguiente')]")
    BOTON_SIGUIENTE2 = (By.XPATH, "//div[contains(text(),'Siguiente')]")
    BOTON_COMPARTIR = (By.XPATH, "//div[contains(text(),'Compartir')]")
    BOTON_LISTO = (By.XPATH, "/ html[1] / body[1] / div[6] / div[1] / div[1] / div[2] / div[1] / div[1] / * [name() = 'svg'][1]")

class BotInstagram:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = None

    def iniciar_sesion(self, carpeta_imagenes):
        """Inicia sesión en Instagram y sube imágenes desde una carpeta especificada."""
        try:
            chrome_options = webdriver.ChromeOptions()
            # Configurar opciones de Chrome
            self.user_agent = self.generar_user_agent()
            chrome_options.add_argument(f"user-agent={self.user_agent}")

            self.driver = webdriver.Chrome(options=chrome_options)
            self.driver.get("https://www.instagram.com/accounts/login/")
            self.tomar_captura_pantalla("login_page.png")
            self.esperar_random()

            wait = WebDriverWait(self.driver, 10)

            campo_usuario = wait.until(EC.visibility_of_element_located(Locators.CAMPO_USUARIO))
            campo_usuario.send_keys(self.username)
            self.tomar_captura_pantalla("username_ingresado.png")
            self.esperar_random()

            campo_contraseña = wait.until(EC.visibility_of_element_located(Locators.CAMPO_CONTRASEÑA))
            campo_contraseña.send_keys(self.password)
            self.tomar_captura_pantalla("password_ingresado.png")
            self.esperar_random()

            boton_iniciar_sesion = wait.until(EC.element_to_be_clickable(Locators.BOTON_INICIAR_SESION))
            boton_iniciar_sesion.click()
            self.tomar_captura_pantalla("boton_iniciar_sesion.png")
            self.esperar_random()

            boton_ahora_no1 = self.driver.find_element(*Locators.BOTON_AHORA_NO1)
            boton_ahora_no1.click()
            self.esperar_random()

            boton_ahora_no2 = self.driver.find_element(*Locators.BOTON_AHORA_NO2)
            boton_ahora_no2.click()
            self.esperar_random()

            self.subir_imagenes(carpeta_imagenes)

        except Exception as e:
            print("Error durante el inicio de sesión:", e)

    def subir_imagenes(self, carpeta_imagenes):
        """Sube imágenes desde una carpeta especificada."""
        try:
            imagenes = os.listdir(carpeta_imagenes)
            for imagen in imagenes:
                ruta_imagen = os.path.join(carpeta_imagenes, imagen)
                # Hacer clic en el botón "plus" para subir una imagen
                boton_plus = self.driver.find_element(*Locators.BOTON_PLUS)
                boton_plus.click()
                self.esperar_random()

                # Seleccionar archivo de imagen
                input_archivo = self.driver.find_element(*Locators.INPUT_ARCHIVO)
                input_archivo.send_keys(ruta_imagen)
                self.esperar_random()

                # Hacer clic en el botón de siguiente
                boton_siguiente1 = self.driver.find_element(*Locators.BOTON_SIGUIENTE1)
                boton_siguiente1.click()
                self.esperar_random()

                # Hacer clic en el botón de siguiente
                boton_siguiente2 = self.driver.find_element(*Locators.BOTON_SIGUIENTE2)
                boton_siguiente2.click()
                self.esperar_random()

                # Hacer clic en el botón de compartir
                boton_compartir = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.BOTON_COMPARTIR))
                boton_compartir.click()
                self.esperar_random()

                boton_listo = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Locators.BOTON_LISTO))
                boton_listo.click()
                self.esperar_random()

        except Exception as e:
            print("Error durante la realización de acciones adicionales:", e)

    def tomar_captura_pantalla(self, nombre_archivo):
        """Toma una captura de pantalla y la guarda con el nombre especificado."""
        if self.driver:
            self.driver.save_screenshot(nombre_archivo)

    def cerrar_navegador(self):
        """Cierra el navegador."""
        if self.driver:
            self.driver.quit()

    def esperar_random(self):
        """Espera un tiempo aleatorio entre 3 y 9 segundos para simular un comportamiento humano."""
        time.sleep(random.uniform(3, 9))

    def generar_user_agent(self):
        """Genera un user agent aleatorio para simular un comportamiento humano."""
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36"
        ]
        return random.choice(user_agents)

def iniciar_bot():
    """Función para iniciar el bot con los datos ingresados en la GUI."""
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    carpeta_imagenes = filedialog.askdirectory()

    if not usuario or not contraseña or not carpeta_imagenes:
        messagebox.showwarning("Advertencia", "Todos los campos son obligatorios")
        return

    bot = BotInstagram(usuario, contraseña)
    bot.iniciar_sesion(carpeta_imagenes)

# Configuración de la GUI con Tkinter
ventana = tk.Tk()
ventana.title("Bot de Instagram")

tk.Label(ventana, text="Usuario:").grid(row=0, column=0)
entrada_usuario = tk.Entry(ventana)
entrada_usuario.grid(row=0, column=1)

tk.Label(ventana, text="Contraseña:").grid(row=1, column=0)
entrada_contraseña = tk.Entry(ventana, show="*")
entrada_contraseña.grid(row=1, column=1)

boton_iniciar = tk.Button(ventana, text="Iniciar Bot", command=iniciar_bot)
boton_iniciar.grid(row=2, columnspan=2)

ventana.mainloop()
