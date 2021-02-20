#KAYIT FORMLARI BU KISMA GİRİLİYOR
#KAYIT FORMLARI
from django import forms

class  RegisterForm(forms.Form):
    username = forms.CharField(max_length=50,label="Kullanıcı Adı")
    password = forms.CharField(max_length=20,label="Şifre",widget=forms.PasswordInput)
    confirm = forms.CharField(max_length=20,label="Şifrenizi Doğrulayın",widget=forms.PasswordInput)

    #Kullanıcıyı çekiyoruz
    def clean(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm = self.cleaned_data.get("confirm")

        #Şartlı durumları yazıyoruz
        if password and confirm and password !=confirm :
            raise forms.ValidationError("Parolalar Eşleşmiyor")
        
        #Girilen değerleri sözlüğe ekliyoruz
        values = {
            "username":username
            "password":password
        }
        return values