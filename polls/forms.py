from django import forms
from .models import Pregunta, Opcion

# Formulario para crear preguntas
class PreguntaForm(forms.ModelForm):  # antes QuestionForm
    class Meta:
        model = Pregunta
        fields = ["texto_pregunta"]  # si quieres, también podrías incluir fecha_publicacion

# Formulario para agregar opciones a una pregunta
class OpcionForm(forms.ModelForm):  # antes ChoiceForm
    class Meta:
        model = Opcion
        fields = ["texto_opcion"]  # solo el campo de texto
