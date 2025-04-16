# wilkins gervacio 23-EISN-2-036
import gradio as gr
import librosa
import soundfile as sf
import numpy as np 
import tempfile
import openai
import os

# Configuración de la API key de OpenAI
openai.api_key = os.getenv("")
def aplicar_efecto(audio, efecto):
    if audio is None:     # Validación: si no hay audio, no procesar
        return None, None
    
    y, sr = sf.read(audio)
    
    if len(y.shape) > 1: # Si el audio es estéreo (2 canales), convertirlo a mono tomando solo el primer canal
        y = y[:, 0]
    # Aplicar el efecto seleccionado
    # wilkins gervacio 23-EISN-2-036
    if efecto == "Robot agudo y distorsionado":
        y_shifted = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=5)
        y = y_shifted * np.sign(np.sin(2 * np.pi * 30 * np.arange(len(y_shifted)) / sr))
# Disminuye el tono 5 semitonos
        
    elif efecto == "Alien, grave y distorsionado":
        y_shifted = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=-5)
        y = y_shifted * np.sign(np.sin(2 * np.pi * 15 * np.arange(len(y_shifted)) / sr))
        # Aplica una modulación más lenta (15Hz) para un efecto más grave
    elif efecto == "Ardilla, muy aguda":
        y = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=10)   # Simplemente aumenta el tono 10 semitonos para el efecto de ardilla
        
    # Crear un archivo temporal para guardar el audio procesado
    temp_path = tempfile.mktemp(suffix=".wav")
    sf.write(temp_path, y, sr)
    
    # wilkins gervacio 23-EISN-2-036
    # Intenta transcribir el audio original usando OpenAI Whisper
    try:
        with open(audio, "rb") as f:  # Llama a la API de OpenAI para transcribir el audio
            transcripcion = openai.Audio.transcribe("whisper-1", f)["text"]
    except Exception as e:  # Si hay un error durante la transcripción, captura el mensaje
        transcripcion = f"error al transcribir: {e}"
        
     # Devuelve la ruta al archivo de audio modificado y la transcripción
    return temp_path, transcripcion

# wilkins gervacio 23-EISN-2-036
# Configuración de la interfaz gráfica con Gradio
with gr.Blocks() as interfaz:
    gr.Markdown("## Modificador de voz con librosa + Transcriptor") # Títulos de la aplicación
    gr.Markdown("Sube o graba un audio, elige un efecto y mira la transcripcion del contenido. ")
    
    # Primera fila: entradas del usuario
    with gr.Row():
        entrada_audio = gr.Audio(label="Audio de entrada", type="filepath")     # Componente para subir o grabar audio
        efecto = gr.Dropdown(
            ["Robot agudo y distorsionado", "Alien, grave y distorsionado", "Ardilla, muy aguda"],
            label="Selecciona un efecto"
        )
        
    boton = gr.Button("Aplicar efecto y transcribir")
    
    # Segunda fila: salidas (resultados)
    with gr.Row():
        salida_audio = gr.Audio(label="Audio con efecto", type="filepath")
        salida_texto = gr.Textbox(label="texto transcrito")
    
    # Configura la función que se ejecutará al hacer clic en el botón
    # Conecta las entradas y salidas con la función aplicar_efecto    
    boton.click(fn=aplicar_efecto, inputs=[entrada_audio, efecto], outputs=[salida_audio, salida_texto])

# wilkins gervacio 23-EISN-2-036
# Inicia la aplicación web
interfaz.launch()
    
    
    