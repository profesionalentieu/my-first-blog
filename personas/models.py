from django.db import models

class Domicilio(models.Model):
    calle = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    ciudad = models.CharField(max_length=50)
    codigo_postal = models.CharField(max_length=10)
    

    

    def __str__(self):
        return f"{self.calle} {self.numero}, {self.ciudad} ({self.codigo_postal})"


class Persona(models.Model):
    nombre = models.CharField(max_length=25)
    apellido = models.CharField(max_length=25)
    correo = models.CharField(max_length=50)
    dni = models.CharField(max_length=8)
    fechanacimiento = models.DateField()
    cuil = models.CharField(max_length=15)
    cvu = models.CharField(max_length=25)
    
    
    domicilio = models.ForeignKey(Domicilio, on_delete=models.CASCADE)


    class Meta:
        abstract = True


class Socios(Persona):
    disciplinasocio = models.CharField(max_length=25)
    categoriasocio = models.CharField(max_length=25)
    socioactivo=models.BooleanField(default=False)
    valorcuota=models.CharField(max_length=25)
    deuda=models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Socios"  
    
class Profesores(Persona):
    disciplinaprofesor = models.CharField(max_length=25)
    categoriaprofesor = models.CharField(max_length=25)
    class Meta:
        verbose_name_plural = "Profesores"  

class Administracion(Persona):

    class Meta:
        verbose_name_plural = "Administradores"  
    pass
    


class Menores(Socios):
    
    descmenores=models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Menores"  
    pass

class Comunes(Socios):

    class Meta:
        verbose_name_plural = "Comunes"  
    pass

class Jubilados(Socios):
    
    descjubilados=models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Jubilados"  
    pass

class MetodosDePago:
    banco=models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "MetodosDePago"  
    pass

class Transferencia(MetodosDePago):
    cvutransferencia=models.CharField(max_length=25)

class Disciplinas:
    nombredisciplina=models.CharField(max_length=25)
    valordisciplina=models.CharField(max_length=25)

    class Meta:
        verbose_name_plural = "Disciplinas"  
    pass

class Alertas(Persona):

    class Meta:
        verbose_name_plural = "Alertas"  
    pass

