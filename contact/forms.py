from django import forms

# Formulario en django, los cuales captan distintos tipos de datos (char,email,char,en este caso)
# se ocupan los diseños por defectos de django pero se añaden diseños de Bootstrap en los tributos
# del modulo "attrs" pasados en forma de "diccionario"
class ContactForm(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={
            'class' : 'form-control',
            'placeholder': 'Nombre',
        }
    ),max_length=100)
    email = forms.EmailField(label="Email", required=True, widget=forms.EmailInput(
        attrs={
            'class' : 'form-control',
            'placeholder': '@gmail.com',
        }
    ),max_length=100)
    content = forms.CharField(label="Contenido", required=True,widget=forms.Textarea(
        attrs={
            'class' : 'form-control',
            'rows': 4,
            'placeholder': 'Escribe tu mensaje',
        }
    ),max_length=1000)