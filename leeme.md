
REPO REMOTO   https://github.com/astorniolo/ESOA_2024.git

Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line
echo "# ESOA_2024" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/astorniolo/ESOA_2024.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/astorniolo/ESOA_2024.git
git branch -M main
git push -u origin main
…or import code from another repository
You can initialize this repository with code from a Subversion, Mercurial, or TFS project.



#py y App  panel de ctrl, stock, ventas, pagos, envios, promociones
python -m pip install Django
django-admin  startproject  productosWeb 
cd productosWeb 
python manage.py makemigrations
python manage.py migrate
python manage.py runserver     
cambiar idioma a español
    en archivo settings.py
        # Internationalization
        LANGUAGE_CODE = 'es-la'
Crear app
    python manage.py startapp gestionProductos
    CREAR MODELO DE DATOS archivo models.py !!!!!!!!!
    python manage.py makemigrations
    python manage.py sqlmigrate gestionProductos 0001
    python manage.py migrate

DATABASE
sqlite3
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

MySQL
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'nombre_de_tu_database',
            'USER': 'root' ,
            'PASSWORD':'tupasword',
            'HOST':'localhost',
        }
    }

Postgress
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'nombre_de_tu_database',
            'USER': 'posgres' ,l
            'PASSWORD':'tupasword',
            'HOST':'localhost',
            'DATABASE_PORT':'5432'
        }
    }

python manage.py makemigrations
python manage.py migrate
----------------------------
panel de administracion
    caMPOS REQUERIDOS
        todos los campos son requeridos por defecto .... sino blank=true,null=true
        migrar
    CAMBIO NOMBRES DE CAMPOOS DE TABLAS
        NOMBRE DE CAMPOS por defecto Capitalize y cambia "_" por " "
        verbose_name="aca pongo otro nombre del campo"
        metodo --str--
        migrar => python manage.py makemirations
                  Python managepy migrate 
    CAMPOS PARA VER
        en admin.py 
        crear ueva clase con los campors qque quiero proyectar
            class ClientesAdmin(admin.ModelAdmin):
                list_display("nombre","direccion")
            admin.site.register(Clinetes, ClientesAdmin)
            listo
    AGREGAR CAMPOS DE BUSQUEDA
             class ClientesAdmin(admin.ModelAdmin):
                list_display("nombre","direccion")
                search_fields("nonbre","telefono")
    FILTRAR REGISTROS
            class ArticulosAdmin(admin.ModelAdmin):
                list_filter=("seccion",)   ·los filtros son como tuplas nombre campo valorpor eso la coma, el valor lo ponemos en el administrador 
    aparece el panel de fitros
            podemos filtrar por fecha datetime PUTENTE
    AGREGAR USUARIOS y GRUPOS
        usuarios
            si es o no staff   permitido entrar al panel de administracion
            pero puedo limitar acceso
            ver filtros
            1 SUPERUSUARIO 
            staff
            activo 
            no activo no aacede a ninguna url que requiera autenticacion
    como soy super usuario voy a
        autenticacion autorizacion y creo nuevos usuarios
        añadir usuario
        nombre cpntraseña cumplir requisitos guardar
         ver como encryta
         activo check     si staff  para que entre administrador
        grupos y permisos  
          si no toco nada nop puede entrar a nada
          si solo de doy a tabla clientes pues entrara ahi
          puedo agregar grupo que todos modificquen clientes 
            nuevo gurpo modificar_clientes 
            ELIJO LOS PERMISOS ASIGNADOS
        grabar 
--------------------------
formularios!!!!
    1- busqueda  method get
    2- contacto methos post
        adicional usamos un libreria para enviar mails : core.mail
        necsito establecer los parametros de a que correo lo envio asi que utilizo  settings.py para establecer esos parametros
            email.backends
            ojo configurar gmail!!!! para enviarle correo electronico
-------------- 
formularios API FORM     ver en documentacion oficial
    simplifica la creacion de formularios y hace validaciones 
    archivo forms.py    conteniendo una clase para cada clase de formulario que necesitemos
    




        
