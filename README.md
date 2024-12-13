Proyecto Final CoderHouse

-------------------------------------------

Dentro de este directorio encontrarán los archivos correspondientes al proyecto, los cuales pueden ser ejecutados con el comando "python manage.py runserver" parados sobre el directorio raíz del proyecto.

Credenciales de usuario admin Django: Diego
ricardo01 - la contraseña 

Las funcionalidades que tiene la propuesta son:
- Landing Page página de Ropa Argentina IT , con visualización de Productos tales como "Remeras", "Buzos" y "Pantalones" en forma de etiquetas de bootstrap. Cada producto es un modelo con sus propios atributos (Chequear /AppPreEntreg3/models.py) *Los items de los productos están debajo de los buttons para agregar/buscar.
<img width="281" alt="image" src="https://cdn.discordapp.com/attachments/693302804852244491/1316923569636114522/image.png?ex=675cd026&is=675b7ea6&hm=558f588d3a019bc44c68d6d42913b6fd7805800a973038ad03b2c391cad784da&">
- Agregar prendas (Únicamente registrado con el usuario administrador de Django).: En la página correspondiente a cada producto, hay un button el cual nos permite agregar nuevas prendas (Desarrollado con Forms).
- Buscar prendas: En la página correspondiente a cada producto, hay un button el cual nos permite buscar prendas ya cargadas a la BD por su atributo "nombre".
<img width="143" alt="image" src="https://cdn.discordapp.com/attachments/693302804852244491/1316923871995101257/image.png?ex=675cd06e&is=675b7eee&hm=babd9f482e5a1178f08ee054e712ac47967e28cda82dcf2c554bd771838cb266&"> 
-Si , Use a discord como anotador de imagenes XD
- Editar prendas (Únicamente registrado con el usuario administrador de Django).
- Eliminar prendas (Únicamente registrado con el usuario administrador de Django).
- Edición de Perfil (Cambio de avatar e información personal).
-Si ves en el admin de Django avatares raros juego calabozos y dragones y no tenia nada mejor.

Algunas posibles Pruebas a realizar son:
- Agregar Producto (Remera por ejemplo) y chequear en la seccion de "Remeras" su posterior aparición (Solo como admin)..
- Buscar el producto agregado en el item anterior, el resultado debería de ser una pagina HTML con herencia de padre.html (La cual muestra el MATCH).
- Eliminar producto (Solo como admin).
- Editar producto (Solo como admin).
- Crear nuevo perfil desde "nav -> Registrarse".

Espero que les guste,
Saludos!

Diego Leonel Gonzalez 
