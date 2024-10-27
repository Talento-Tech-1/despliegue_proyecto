from flask import Flask, render_template, request
import pickle  # Importar pickle
import pandas as pd

app = Flask(__name__, static_folder='statics')

# Lista con número de columnas necesarias para los modelo
nuevas_columnas = [
    'Área sembrada (ha)',
    'Cultivo_Aguacate',
    'Cultivo_Ahuyama',
    'Cultivo_Arroz',
    'Cultivo_Arveja',
    'Cultivo_Banano',
    'Cultivo_Cacao',
    'Cultivo_Café',
    'Cultivo_Caña',
    'Cultivo_Cebolla de bulbo',
    'Cultivo_Cebolla de rama',
    'Cultivo_Chontaduro',
    'Cultivo_Coco',
    'Cultivo_Fique',
    'Cultivo_Frijol',
    'Cultivo_Limón',
    'Cultivo_Mandarina',
    'Cultivo_Mango',
    'Cultivo_Maíz',
    'Cultivo_Mora',
    'Cultivo_Naranja',
    'Cultivo_Palma de aceite',
    'Cultivo_Papa',
    'Cultivo_Patilla',
    'Cultivo_Piña',
    'Cultivo_Plátano',
    'Cultivo_Soya',
    'Cultivo_Tomate',
    'Cultivo_Yuca',
    'Cultivo_Ñame',
    'Departamento_Amazonas',
    'Departamento_Antioquia',
    'Departamento_Arauca',
    'Departamento_Archipiélago de San Andrés, Providencia y Santa Catalina',
    'Departamento_Atlántico',
    'Departamento_Bolívar',
    'Departamento_Boyacá',
    'Departamento_Caldas',
    'Departamento_Caquetá',
    'Departamento_Casanare',
    'Departamento_Cauca',
    'Departamento_Cesar',
    'Departamento_Chocó',
    'Departamento_Cundinamarca',
    'Departamento_Córdoba',
    'Departamento_Guainía',
    'Departamento_Guaviare',
    'Departamento_Huila',
    'Departamento_La Guajira',
    'Departamento_Magdalena',
    'Departamento_Meta',
    'Departamento_Nariño',
    'Departamento_Norte de Santander',
    'Departamento_Putumayo',
    'Departamento_Quindío',
    'Departamento_Risaralda',
    'Departamento_Santander',
    'Departamento_Sucre',
    'Departamento_Tolima',
    'Departamento_Valle del Cauca',
    'Departamento_Vaupés',
    'Departamento_Vichada'
]


# Cargar los modelos 
with open(r'C:\Users\Lenovo\Desktop\Talento Tech\Proyecto\despliegue\modelo_1.pkl', 'rb') as file:
    modelo1 = pickle.load(file)

with open(r'C:\Users\Lenovo\Desktop\Talento Tech\Proyecto\despliegue\modelo_2.pkl', 'rb') as file:
    modelo2 = pickle.load(file)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predecir', methods=['POST'])
def predecir():
    # Obtener los datos del formulario
    cultivo = request.form.get('cultivo')
    area = float(request.form.get('area'))
    departamento = request.form.get('departamento')

    # Preprocesar los datos
    nuevos_datos = pd.DataFrame({
        'Área sembrada (ha)': [area],
        'Cultivo': [cultivo],
        'Departamento': [departamento]
    })

    # Aplicar el preprocesamiento común
    datos_preprocesados = preprocesar_datos(nuevos_datos)

    # Realizar predicciones con ambos modelos
    prediccion1 = modelo1.predict([datos_preprocesados])
    prediccion2 = modelo2.predict([datos_preprocesados])

    # Formatear los resultados
    area_productiva = f"Área productiva esperada: {prediccion1[0]:.5f} (ha)"
    rendimiento = f"Rendimiento esperado: {prediccion2[0]:.5f} (t/ha)"

    # Renderizar la plantilla de resultados
    return render_template('response.html', area=area_productiva, rendimiento=rendimiento)

def preprocesar_datos(nuevos_datos):
    # Aplicar one-hot encoding a las columnas 'Cultivo' y 'Departamento'
    nuevos_datos_encoded = pd.get_dummies(nuevos_datos, columns=['Cultivo', 'Departamento'], dtype=int)

    # Df con el número de columnas necesarias para el modelo 
    nuevos_datos_encoded = nuevos_datos_encoded.reindex(columns=nuevas_columnas, fill_value=0)

    # Retornar los datos preprocesados como una lista
    return nuevos_datos_encoded.values.flatten()  

if __name__ == '__main__':
    app.run(debug=True)


