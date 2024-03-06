from django import forms

class Clientesforms(forms.Form):
    nombre      = forms.CharField(max_length=60)
    apellido    = forms.CharField(max_length=60)
    documento   = forms.IntegerField()
    email       = forms.EmailField()

class Proveedoresforms(forms.Form):
    razon_social= forms.CharField(max_length=60)
    cuit        = forms.CharField(max_length=20)
    email       = forms.EmailField()
    telefono    = forms.IntegerField()

class Pedidosforms(forms.Form):
    fecha_pedido= forms.DateField()
    cantidad_p  = forms.IntegerField()
    monto       = forms.FloatField()
    doc_cliente = forms.IntegerField()
    

class Comprasforms(forms.Form):
    producto    = forms.CharField(max_length=60)
    cantidad    = forms.IntegerField()
    cuit_prov   = forms.CharField(max_length=20)
    fecha_comp  = forms.DateField()