from django.db import models

# Create your models here.
class Cliente(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=100)
    email=models.EmailField(blank=True, null=True)
    telefono=models.CharField(max_length=15)
    
    def __str__(self) -> str:
                        return self.nombre + ' - ' + self.direccion

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()
    
    def __str__(self) -> str:
        return self.nombre + ' - ' + self.seccion + ' - ' + str(self.precio)
            
class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()
    #agrego el campo fecha de entrega 
    #y ademas le digo que puede ser en blanco o nulo
    #fechaEntrega=models.DateField(blank=True,null=True)
    
    def __str__(self) -> str:
        if self.entregado:
                    return str(self.numero) + '- Entregado el ' + str(self.fecha)
        else:       
                    return str(self.numero) + '- NO Entregado'
