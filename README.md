# Sprint 8 - Cohorte 11 - Maria Romero
## Descripción del Proyecto Urban Routes Page, Pruebas Automatizadas de aplicaciones web.


Este proyecto utiliza Selenium para automatizar pruebas de la página web de UrbanRoutes. El objetivo principal es verificar que las funcionalidades clave de la página, como la selección de direcciones, selección de la Tarifa Comfort, el ingreso de número de telefono, adquirir código de SMS, metodo de pago con tarjeta de crédito, selección de requisitos al pedido como Manta y Pañuelos y 2 Helados. Finalmente la prueba arroja un modal de búsqueda de conductor y culmina con una cuenta regresiva mientras se asigna un conductor.

### Estructura del Proyecto
#### Archivos Principales
**data.py: **Contiene los datos necesarios para las pruebas, como URLs, direcciones, números de teléfono, numero de tarjeta y codigo CVV.
**test_urban_routes.py:** Contiene las pruebas automatizadas usando Selenium.

#### Código Principal
retrieve_phone_code(driver)

Recupera el código de confirmación del teléfono desde los registros de rendimiento del navegador. Se utiliza para verificar la funcionalidad de entrada de códigos de confirmación.

##### UrbanRoutesPage

Una clase que contiene todos los selectores y métodos necesarios para interactuar con la página de UrbanRoutes.

##### Métodos principales:
**set_from(address): **Establece la dirección de origen.
**set_to(address): **Establece la dirección de destino.
**call_taxi():** Solicita un taxi.
**select_comfort_tariff():** Selecciona la tarifa Comfort.
**select_phone_button(): **Selecciona el botón de número de teléfono.
**set_phone(phone):** Establece el número de teléfono.
**select_next_button():** Selecciona el botón Siguiente.
**set_code(code): **Establece el código SMS.
**select_confirm_button():** Selecciona el botón Confirmar.
**select_payment_method_button():** Selecciona el botón Método de Pago.
**select_add_card_button():** Selecciona el botón para añadir tarjeta.
**select_add_card_number(card): **Establece el número de tarjeta.
**select_add_card_cvv(cvv):** Establece el código CVV.
**select_agregar_button(): **Selecciona el botón Agregar.
**select_close_popup_button():** Selecciona el botón para cerrar el popup.
**select_click_message_field():** Selecciona el campo de mensaje.
**set_message_field(message): **Establece el mensaje para el conductor.
**select_mantas_panuelos_button():** Selecciona el botón de mantas y pañuelos.
**select_plus_button():** Selecciona el botón para incrementar la cantidad.
**select_pedir_taxi_button():** Selecciona el botón para pedir el taxi.
**Métodos get_from() y get_to():** Obtienen los valores actuales de los campos de origen y destino, respectivamente.

##### TestUrbanRoutes

Clase que contiene los métodos de configuración y prueba

**Métodos principales:**
**setup_class(cls):** Configura el entorno del navegador.
**teardown_class(cls):** Cierra el navegador.
**setup_method(self): **Abre la página de UrbanRoutes.

**test_urban_route_page(self):** Realiza una prueba completa del flujo de trabajo de la página, incluyendo:
- Establecer la dirección de origen y destino.
- Solicitar un taxi.
- Seleccionar la tarifa Comfort.
- Introducir un número de teléfono.
- Recuperar y establecer el código de confirmación.
- Seleccionar un método de pago.
- Añadir una tarjeta de crédito.
- Establecer un mensaje para el conductor.
- Pedir el taxi.

##### Uso de return y assert
###### return:

Se utiliza en los métodos get_from() y get_to() para devolver el valor de los campos de origen y destino. Esto permite verificar el estado actual de estos campos durante las pruebas.

###### assert:

Se usa en las pruebas para validar que los valores esperados coincidan con los valores reales. Por ejemplo, en test_urban_route_page, se utilizan assert para verificar que las direcciones de origen y destino se establecen correctamente.

#### Para Ejecutar las Pruebas se necesitará:
-  Tener Python y Selenium instalados.
- Ejecutar pytest para iniciar las pruebas.

### Notas extra:
Algunas funciones utilizan ***time.sleep()*** para manejar tiempos de espera entre cada acción.
