# Proyecto-de-Final-IA

## Nombre: Wilkins Ismael Gervacio Carpio

## Matrícula : 23-Eisn-2-036

## Proyecto:  Modulador  de voz 

# Modificador de Voz con Transcripción

Este proyecto es una aplicación de modificación de voz con transcripción de audio integrada. Permite aplicar diferentes efectos de sonido a archivos de audio o grabaciones en tiempo real, y además transcribe el contenido del audio original utilizando el modelo Whisper de OpenAI.

## Características

- **Modificación de voz** con tres efectos diferentes:
  - Robot agudo y distorsionado
  - Alien, grave y distorsionado
  - Ardilla, muy agudo
- **Transcripción automática** del audio utilizando OpenAI Whisper
- **Interfaz gráfica** amigable creada con Gradio

## Requisitos

Para ejecutar este proyecto necesitarás Python 3.8 o superior y las siguientes librerías:

```
gradio==5.23.3
librosa==0.11.0
soundfile==0.13.1
numpy==2.1.3
openai==0.27.0
```

## Instalación

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/modificador-de-voz.git
   cd modificador-de-voz
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Configura tu API key de OpenAI:
   - Crea un archivo `.env` en la raíz del proyecto con el siguiente contenido:
     ```
     OPENAI_API_KEY=tu_api_key_aquí
     ```
   - O configúrala como variable de entorno:
     ```bash
     export OPENAI_API_KEY=tu_api_key_aquí
     ```

## Uso

Para iniciar la aplicación, ejecuta:

```bash
python "Efectos de voz.py"
```

La interfaz web se abrirá automáticamente en tu navegador. Desde allí podrás:
1. Subir un archivo de audio o grabar directamente desde el micrófono
2. Seleccionar uno de los tres efectos disponibles
3. Hacer clic en "Aplicar efecto y transcribir"
4. Escuchar el resultado y ver la transcripción del audio original

## Estructura del proyecto

```
.
├── Efectos de voz.py   # Archivo principal con la aplicación
├── requirements.txt    # Dependencias del proyecto
├── .env                # Archivo para guardar la API key (no incluido en el repo)
└── README.md           # Este archivo
```

## Seguridad

⚠️ **IMPORTANTE**: El código actual incluye una clave API de OpenAI directamente en el código. Se recomienda encarecidamente eliminar esta clave y utilizar variables de entorno o un archivo `.env` para almacenar información sensible.

