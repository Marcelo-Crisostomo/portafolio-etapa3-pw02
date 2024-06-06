from django.db import models  # Importa el módulo models de Django, que proporciona un marco para trabajar con modelos.

# Crear tus modelos aquí.

class Categoria(models.Model):  # Define la clase Categoria que hereda de models.Model.
    nombre = models.CharField(max_length=100, unique=True)  # Campo de texto con longitud máxima de 100 caracteres, debe ser único.

    def __str__(self):  # Método que define la representación en cadena del objeto.
        return self.nombre  # Devuelve el nombre de la categoría.

class Tecnologia(models.Model):  # Define la clase Tecnologia que hereda de models.Model.
    nombre = models.CharField(max_length=50, unique=True)  # Campo de texto con longitud máxima de 50 caracteres, debe ser único.

    def __str__(self):  # Método que define la representación en cadena del objeto.
        return self.nombre  # Devuelve el nombre de la tecnología.

# Modelo para los proyectos de portafolio.

class Proyecto(models.Model):  # Define la clase Proyecto que hereda de models.Model.
    titulo = models.CharField(max_length=200)  # Campo de texto con longitud máxima de 200 caracteres.
    imagen = models.ImageField(upload_to='proyectos/')  # Campo de imagen, las imágenes se suben a la carpeta 'proyectos/'.
    descripcion = models.TextField()  # Campo de texto largo para la descripción.
    tecnologias = models.ManyToManyField(Tecnologia)  # Relación muchos a muchos con el modelo Tecnologia.
    link_sitio = models.URLField(max_length=200)  # Campo de URL con longitud máxima de 200 caracteres para el link del sitio.
    link_repositorio = models.URLField(max_length=200)  # Campo de URL con longitud máxima de 200 caracteres para el link del repositorio.
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)  # Relación muchos a uno con el modelo Categoria, borrado en cascada.

    def __str__(self):  # Método que define la representación en cadena del objeto.
        return self.titulo  # Devuelve el título del proyecto.

# Defino el modelo del formulario de contacto.

class Contacto(models.Model):  # Define la clase Contacto que hereda de models.Model.
    nombre = models.CharField(max_length=100)  # Campo de texto con longitud máxima de 100 caracteres.
    email = models.EmailField()  # Campo de email.
    mensaje = models.TextField()  # Campo de texto largo para el mensaje.
    fecha = models.DateTimeField(auto_now_add=True)  # Campo de fecha y hora, se establece automáticamente a la fecha y hora actuales.

    def __str__(self):  # Método que define la representación en cadena del objeto.
        return self.nombre  # Devuelve el nombre del contacto.
