# Ingeniería de software II 
## Trabajo Practico : Diseño arquitectónico


Identifique las capas principales del sistema:
donde podríamos enumerar a 3. Yo mencionare 4 capas:

- Presentación
- Dominio
- servicio
- Persistencia de datos

>[!NOTE]
>Donde la capa de presentación: Es la parte de la aplicación que interactúa con el usuario.Esta no contiene ninguna lógica de negocio. 

>[!NOTE]
>La capa de dominio:Es la que se encarga de representar las entidades y su lógica interna.

>[!NOTE]
>La capa de servicio:Orquesta y coordina las operaciones lógicas establecidas, utilizando las entidades definidas en la capa de dominio. En pocas palabras es el flujo de la aplicación.

>[!NOTE]
>La capa de persistencia de datos: Como dice su  nombre se encarga en que los datos perduren , sea cual sea el medio de almacenamiento utilizado , también es un intermediario entre el sistema de almacenamiento permanente y  la aplicación. También su trabajo es la recuperación de datos.


## Eligiendo un problema sencillo del sistema:
El problema elegido es acceso centralizado a la base de datos,  Para este problema vamos a usar el patrón de diseño singleton . El patrón singleton sirve para garantizar que un objeto tenga un sola instancia en toda la aplicación y proporciona un punto de acceso global, este está clasificado como patrón creacional. 
	Este patrón ayudaría en el ahorro de recursos que costaría tener múltiples conexiones a la base de datos.

## Esquema gráfico(UML):
https://lucid.app/lucidchart/ad46a4f4-df3d-41d0-bba3-7ab4b166af25/edit?viewport_loc=-397%2C-212%2C2992%2C1488%2C0_0&invitationId=inv_c7fe68e3-2b22-43e0-a488-324a032e4f85







