from django import forms
from users.models import User

# Formulario que se usara para el primer registro de usuario.
class UserForm(forms.ModelForm):

    nombres = forms.CharField(label='Nombres', required=True, widget=forms.TextInput(attrs={'size': '30'}))
    apellidos = forms.CharField(label='Apellidos', required=False, widget=forms.TextInput(attrs={'size': '30'}))
    edad = forms.IntegerField(label='Edad', required=False)
    email = forms.EmailField(label='Correo', max_length=300, required=True)

    class Meta:
        model = User
        fields = ['nombres', 'apellidos', 'edad', 'email']

    # Validacion para ver si el correo ya existe.
    def clean_email(self):
        data = self.cleaned_data['email']
        mail_exist = User.objects.filter(email=data).first()

        if mail_exist:
            raise forms.ValidationError('Correo existe, intente con otro')

        return data

# Formlario para el guardado de claves y activacion del usuario.
class RegistroFrom(forms.ModelForm):
    id = forms.IntegerField(widget=forms.HiddenInput())
    clave = forms.CharField(label='Clave', required=True, widget=forms.PasswordInput(attrs={'size': '30'}), max_length=30)
    clave2 = forms.CharField(label='Reingrese Clave ', required=True, widget=forms.PasswordInput(attrs={'size': '30'}), max_length=30)

    class Meta:
        model = User
        fields = ['clave', 'id']

    #Validacion de que ambas claves sean iguales.
    def clean(self):

        if self.cleaned_data['clave'] != self.cleaned_data['clave2']:
            raise forms.ValidationError('Las claves no coinciden')
        return self.cleaned_data
