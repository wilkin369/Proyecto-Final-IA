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
    if efecto == "robot agudo y disporsionado":  # Primero aumenta el tono 5 semitonos usando librosa
        y_shifted = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=5)
        y = y_shifted * np.sign(2 * np.pi * 30 * np.arange(len(y_shifted)) / sr)
        
    elif efecto == "Alien, grave y distorsionada":
        y_shifted = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=-5) # Disminuye el tono 5 semitonos
        y = y_shifted * np.sign(2 * np.pi * 15 * np.arange(len(y_shifted)) / sr) 
        # Aplica una modulación más lenta (15Hz) para un efecto más grave
    elif efecto == "Ardilla, muy aguda":
        y = librosa.effects.pitch_shift(y.astype(float), sr=sr, n_steps=10)   # Simplemente aumenta el tono 10 semitonos para el efecto de ardilla
        
    # Crear un archivo temporal para guardar el audio procesado
    temp_path = tempfile.mkdtemp(suffix=" .wav")
    sf.write(temp_path, y, sr)
    
    