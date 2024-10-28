# Análisis y Modelado del Área Cosechada de Cultivos

Este proyecto realiza un análisis exploratorio y construye un modelo predictivo de aprendizaje automático para estimar el área cosechada de cultivos en diferentes regiones y periodos de tiempo. Se basa en datos agrícolas de Colombia entre 2019 y 2023.

## Tabla de Contenidos
- [Descripción](#descripción)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Uso](#uso)
- [Metodología](#metodología)
- [Resultados](#resultados)

## Descripción
Este notebook utiliza datos agrícolas de diferentes cultivos, municipios y años. El objetivo es realizar un análisis exploratorio de estos datos y desarrollar un modelo predictivo basado en Random Forest para predecir el área cosechada en función de múltiples variables.

## Estructura del Proyecto
- `modelo_area_cosechada.ipynb`: Notebook principal con el análisis de datos y el modelo predictivo.
- `base_agrícola_2019_2023.xlsx`: Archivo de datos en Excel con información agrícola (no incluido en este repositorio por motivos de privacidad).
- `README.md`: Este archivo README.
  
## Requisitos
El proyecto requiere las siguientes bibliotecas de Python:
- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`
- `pickle` (para guardar y cargar el modelo)

## Instalación
1. Clona el repositorio:
    ```bash
    git clone https://github.com/tu_usuario/tu_repositorio.git
    ```
2. Navega al directorio del proyecto:
    ```bash
    cd tu_repositorio
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso
1. Abre el notebook `modelo_area_cosechada.ipynb`.
2. Ejecuta las celdas secuencialmente para:
   - Cargar y explorar el conjunto de datos.
   - Entrenar el modelo `RandomForestRegressor`.
   - Evaluar el modelo utilizando métricas como `mean_squared_error` y `r2_score`.

## Metodología
1. **Carga de Datos**: Los datos se cargan desde un archivo Excel.
2. **Análisis Exploratorio**: Incluye la inspección de las columnas para limpiar datos faltantes y observar patrones en el área cosechada y otras variables.
3. **Modelo Predictivo**: El modelo Random Forest se entrena con variables seleccionadas para predecir el área cosechada.
4. **Validación Cruzada**: Se utiliza K-Fold para evaluar el rendimiento del modelo.

## Resultados
Los resultados muestran la precisión del modelo en términos de:
- **Error cuadrático medio (MSE)**: Para evaluar la dispersión del área cosechada predicha frente a los valores reales.
- **R²**: Para medir la variabilidad explicada por el modelo en los datos.

Para más detalles, consulta el notebook [modelo_area_cosechada.ipynb](modelo_area_cosechada.ipynb).

## Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un "issue" para discutir cualquier cambio importante antes de realizar un pull request.

## Licencia
[![Licencia Creative Commons](https://i.creativecommons.org/l/by/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0/)

Este proyecto está licenciado bajo la **Licencia Creative Commons Atribución 4.0 Internacional (CC BY 4.0)**. Para más detalles, consulta la [Licencia Creative Commons](https://creativecommons.org/licenses/by/4.0/).



# Instrucciones para Despliegue y Uso

Este documento describe cómo desplegar la aplicación y realizar las operaciones básicas.

### 1. Crear el entorno virtual

- Haz clic derecho en la carpeta del proyecto y selecciona **Abrir terminal**.
- Instalar las librerias
   - Flask
   - pandas
   - sklearn 

### Paso 2: Activar el Entorno Virtual
- Ejecuta el siguiente comando para activar el entorno virtual:
  
  ```
  .\source\Scripts\Activate.ps1
  ```
  ```
   python app.py
  ```

### Paso 3 : Activar Python

- Una vez que el entorno esté activo, asegúrate de que Python esté en funcionamiento. Puedes comprobarlo ejecutando:

  ```
   python --version
  ```
### Paso 4: Abrir el Navegador

- Copiar la direccion ip y pegarla en el navegador de preferencia.
  
  ```
   http://127.0.0.1:5000
  ```

## 2. Interacción con la Aplicación

[![Captura-de-pantalla-2024-10-25-213329.png](https://i.postimg.cc/Jhvt5fTM/Captura-de-pantalla-2024-10-25-213329.png)](https://postimg.cc/cK7ssbyb)

Una vez que la aplicación esté en funcionamiento, siga  estos pasos:

1️⃣ Agregar Área
 - Ingresa el área correspondiente en el campo designado.
  
2️⃣ Seleccionar Cultivo
- Elige el cultivo de la lista desplegable.
  
3️⃣ Seleccionar Departamento
- Selecciona el departamento de la lista.
  
4️⃣ Enviar
- Haz clic en el botón de Enviar para procesar la información.
  
Notas:
- Asegúrate de que todas las dependencias estén instaladas en el entorno virtual.
- Si tienes problemas con el despliegue, revisa los registros en la terminal para más detalles.
