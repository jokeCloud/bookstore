from django import forms
from django.core.mail.message import EmailMessage

from .models import Product


class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    subject = forms.CharField(label='Subject', max_length=120)
    message = forms.CharField(label='Message', widget=forms.Textarea())

    def send_mail(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        content = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'  # noqa

        mail = EmailMessage(
            subject='Message send from bookstore',
            body=content,
            from_email='contact@yourdomain.com.br',
            to=['contact@yourdomain.com.br', ],
            headers={'Reply-To': email}
        )
        mail.send()


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'stock', 'image']
