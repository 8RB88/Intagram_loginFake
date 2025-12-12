# 📸 Instagram Login Page - Clone (Propósitos Educativos/Simulación)

## ⚠️ ADVERTENCIA: Material de Apoyo Educativo y de Seguridad

Este repositorio contiene un **clon de la página de inicio de sesión de Instagram (versión antigua)**.

**El objetivo principal de este proyecto es servir como material de apoyo para la educación en ciberseguridad y para demostrar visualmente:**

1.  **Phishing (Suplantación de identidad):** Lo fácil que es replicar la apariencia de un sitio web conocido.
2.  **Riesgo de Datos:** Cómo una persona puede ser engañada al ingresar sus credenciales en un sitio web falso (o "fake log-in").
3.  **Concientización:** La importancia de verificar la URL (dirección web) de un sitio antes de ingresar cualquier dato sensible, como correos electrónicos y contraseñas.

---

## 🛠️ Tecnología Utilizada (Simulación de Backend)

Aunque la interfaz es puramente HTML/CSS, para propósitos de demostración, el proyecto incluye un backend simple simulado en Python.

* **Frontend:** HTML y CSS (imitando el diseño original de Instagram).
* **Backend (Simulación):** Python con **Flask**.
    * La aplicación simula la captura de `Correo Electrónico` y `Contraseña` y los guarda en un archivo `users.json`.
    * **NOTA:** En una aplicación real, los datos nunca deben guardarse en texto plano (como se hace en este ejemplo) y siempre deben ser manejados con medidas de seguridad robustas (hashing, encriptación, etc.).

## 📝 Instrucciones de Ejecución (Para Pruebas)

1.  **Clonar el Repositorio:**
    ```bash
    git clone [https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories](https://docs.github.com/es/repositories/creating-and-managing-repositories/quickstart-for-repositories)
    cd instagram-login-page-master
    ```

2.  **Instalar Flask:**
    ```bash
    pip install flask
    ```

3.  **Ejecutar el Servidor:**
    ```bash
    python app.py
    ```
    El servidor se iniciará en `http://127.0.0.1:5000/`.

4.  **Acceder:** Abre el archivo `index.html` directamente en tu navegador. El formulario enviará los datos al servidor Flask en ejecución.

---

## 🛑 Descargo de Responsabilidad (Disclaimer)

Este código está diseñado **únicamente con fines educativos y de concientización**.

**NO** debe ser utilizado para ningún tipo de actividad maliciosa, ilegal, o para intentar engañar o comprometer la seguridad de terceros. El autor no se hace responsable por el uso indebido de este material.
