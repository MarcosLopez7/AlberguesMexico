from django import forms
from django.contrib.auth.models import User

from .models import Refuge, Post, Need
from .states import STATES


class UserCreateForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirma Contraseña'}))

    class Meta:
        model = User
        fields = ['email', 'password', 'password2']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password != password2:
            raise forms.ValidationError("Las contraseñas deben ser iguales deben ser iguales")

        if 8 > len(password):
            raise forms.ValidationError("La contraseña deber ser mínima de una longitud de 8 caracteres")

    def clean_email(self):
        email = self.cleaned_data.get('email')
        user = User.objects.filter(email=email)

        if user.exists():
            raise forms.ValidationError("Ya hay un usuario registrado con este email")

        return email


class UserForm(forms.ModelForm):
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña'}))

    class Meta:
        model = User
        fields = ['email', 'password']


class NeedForm(forms.ModelForm):
    product = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'producto',
                                                            'ng-model': 'need.product'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cantidad',
                                                                'ng-model': 'need.quantity'}))

    class Meta:
        model = Need
        fields = ['product', 'quantity']


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control',
                                                               'placeholder': '¿Que se necesita?...',
                                                               'ng-model': 'refuge.post.description'}))
    enable_beds = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control',
                                                                   'placeholder': 'Camas Disponible',
                                                                   'ng-model': 'refuge.post.enable_beds'}))

    class Meta:
        model = Post
        fields = ['description', 'enable_beds']


class RefugeForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre',
                                                         'ng-model': 'refuge.name'}))
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono',
                                                             'ng-model': 'refuge.phone'}))
    location = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Dirección',
                                                            'ng-model': 'refuge.location'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ciudad',
                                                         'ng-model': 'refuge.city'}))
    state = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control', 'ng-model': 'refuge.state'}),
                              choices=STATES, label='Estado')

    class Meta:
        model = Refuge
        fields = ['name', 'phone', 'location', 'city', 'state']
