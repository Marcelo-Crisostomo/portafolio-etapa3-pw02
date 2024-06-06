from django import forms  # Importa el módulo forms de Django, que proporciona un marco para trabajar con formularios.
from .models import Contacto  # Importa el modelo Contacto desde el archivo models.py del mismo directorio.

class ContactoForm(forms.ModelForm):  # Define una clase Contacto que hereda de forms.ModelForm.
    class Meta:  # Clase interna Meta para definir metadatos sobre el formulario.
        model = Contacto  # Especifica que el formulario está basado en el modelo Contacto.
        fields = ['nombre', 'email', 'mensaje']  # Define los campos del modelo que se incluirán en el formulario.
        widgets = {  # Define los widgets para personalizar los campos del formulario.
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),  # Personaliza el campo 'nombre' con un widget TextInput y añade la clase 'form-control' para estilos CSS.
            'email': forms.EmailInput(attrs={'class': 'form-control'}),  # Personaliza el campo 'email' con un widget EmailInput y añade la clase 'form-control' para estilos CSS.
            'mensaje': forms.TextInput(attrs={'class': 'form-control'}),  # Personaliza el campo 'mensaje' con un widget TextInput y añade la clase 'form-control' para estilos CSS.
        }
