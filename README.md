# Tercera-pre-entrega-Mauricio-Castro
Tercera pre entrega del proyecto final

Sobre la web:

Esta página es básicamente un administrador de tareas.
Cuenta con una vista de inicio donde se da la bienvenida al usuario y de esta vista se puede acceder en la esquina superior izquierda, a la segunda vista donde hay una frase “organiza tu día” y debajo hay un botón que redirige propiamente a la parte funcional de la web, que es el administrador de tareas.

Utilidad:

El botón “admin tareas” nos redirige de la vista de bienvenida a la segunda vista, donde en “IR A TAREAS” nos llevará al administrador.

Cuando ingresa un usuario a la página, le da la opción de loguearse, en caso que ya tenga una cuenta, le mostrará las tareas que tenga pendientes, así como las completas o en caso que no tenga, le dará la opción de crear nuevas.
En caso que no tenga usuario, le permitirá crear uno desde esta misma vista.Y una vez registrado, automáticamente lo logueara y le permitirá crear nuevas tareas.

Estando logueados, podremos:

1. Desloguearnos en “salir” 
2. Ir a inicio cliqueando “Inicio”
3. Crea una nueva tarea dando click en el símbolo de +
4. Buscar dentro de nuestra tareas cargadas, indicando el nombre o parte de él. Si queremos ver todas nuestras tareas dejamos en blanco esta barra y damos al botón “Buscar”
5. Eliminar tareas, dando click al boton rojo en forma de X que aparece al lado de la tarea que deseemos borrar

Sobre el programa detrás de la web:

1. Contamos con un archivo html con el nombre de base.html que contiene los datos necesarios de la vista inicial, este hereda su contenido Index.html dentro de templates/appinicio, lo mismo sucede con base2.html, aunque Index2.html solo hereda sin ningún cambio o agregación en el mismo 
2. Dentro de templates/appinicio están todos los temples necesarios para el funcionamiento de admin de tareas, lista_tareas.html es el más importante ya que maneja casi todo los enlaces del administrador de tareas. Por otro lado principal_tareas maneja todos los estilos dentro de la vista del administrador de tareas, es decir de la vista inicial del admin, borrar tareas, loguearse, etc 
3. AppInicio - Views: En Views.py se trabajo principalmente con clases y me vali de múltiples importaciones de django para poder darle el formato de administrador de tareas a la web  
4. AppInicio - Models: Debido a los cambios sugeridos por el profe en la última clase, en lugar de usar 3 modelos como lo pedía la consigna inicial, se usó un modelo y más de 4 atributos que fue lo sugerido por el.

