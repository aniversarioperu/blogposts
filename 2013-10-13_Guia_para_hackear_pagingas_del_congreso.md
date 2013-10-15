Según Wikipedia, un hacker es:

"A person who enjoys exploring the details of programmable systems and stretching their capabilities, as opposed to most users, who prefer to learn only the minimum necessary."

Algunos creen equivocadamente que hacker = malechor, delincuente. Pero lo cierto es que hay varios tipos de hackers.

Aquel que infringe medidas de seguridad con fines maléficos, también se le conoce como "cracker".
Un miembro de la comunidad Unix de programas de computación libre y "open source", o alguien que usa este principio para desarrollo de software o hardware.
Además individuos considerados como hackers de la subcultura de programadores pueden hacer tareas repititivas de 100 a 1,000 veces más rapido que usuarios que no son hackers (gracias a que usan de técnicas de computación avanzadas).

El congreso peruano ha aprobado una ley de delitos informáticos recontra ridícula que ha sido criticada por muchos, por ejemplo en el blog http://iriartelaw.com y http://www.hiperderecho.org, además de ser considerada una ley Frankenstein. Esto evidencia que el congreso legisla sobre temas que desconoce.

Para demostrar qué tan mal redactada está la ley ex-beingolea. He decidido hackear las páginas web del Congreso de la República. Y aquí detallo el procedimiento.

Quiero hacer uso de programas informáticos para averiguar cúantos proyectos de ley ha propuesto cada congresista durante este año 2013.

Hay que buscar la página web del congreso que tiene la lista de los proyectos de ley emitidos este año:

Buscar la página con los proyectos de ley.
Buscar la página con los proyectos de ley.
Listado de proyectos de ley por fecha.
Listado de proyectos de ley por fecha.
Si vemos el código original HTML de esa página (hacer CTRL-U, si están en Mozilla Firefox) veremos que está compuesta de 4 "frames". Cada "frame" corresponde a una parte de la página. Me interesa el último "frame", el que contiene la lista de links a los proyectos de ley.

Código HTML de la página del congreso
Código HTML de la página del congreso
Si hacemos click al último "frame" nos encontramos con esta página:

"Frame" conteniendo la lista de proyectos de ley.
"Frame" conteniendo la lista de proyectos de ley.
Esta página lista 100 proyectos de ley, y al ver la dirección URL de esta página, nos damos cuenta que basta con cambiar el último parámetro Start=1 por Start=100 para obtener los siguientes 100 proyectos de ley.

Osea cambiar:

http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2011.nsf/PAporNumeroInverso?OpenView&Start=1

por:

http://www2.congreso.gob.pe/Sicr/TraDocEstProc/CLProLey2011.nsf/PAporNumeroInverso?OpenView&Start=100

Puedo escribir un hack (osea script) que me colecte rápidamente todas las páginas que contienen los links. En lugar de bajarme documento por documento (lo cual me tomaría muuuuucho tiempo), lo puedo hacer al toque si hago uso de las tecnologías de información y comunicación que tanto miedo causa a los congresistas:

https://gist.github.com/aniversarioperu/6963012

Hay 812 proyectos de ley para examinar. Necesitamos descargar cada proyecto de ley y copiar la lista de autores para contar cuántos proyectos ha sido emitido por cada congresista. Obviamente hacer esto manualmente me demoraría una eternidad. Para eso he creado un segundo hack. Es un script in Python que examina cada link, y extrae los nombres de los congresistas que son autores de cada proyecto de ley. Junta todos los nombres y hace un gráfico para poder visualizar los datos (el código de programación está al final de este post).

Bueno, el script estaba demorando mucho, me cansé de esperar y cancelé el programa por lo que no pude colectar toda la info. Pero la idea se entiende no?

Número de proyectos de ley presentado por cada congresista durante el 2013
Número de proyectos de ley presentado por cada congresista durante el 2013
Aquí se pueden descargar la dichosa ley http://www.hiperderecho.org/wp-content/uploads/2013/09/nuevaleybeingolea.pdf.

Hagamos recuento de las veces que he faltado a la ley:

Artículo 3. Atentado a la integridad de datos informáticos
El que, a través de las tecnologias de la información o de la comunicación, introduce,
borra, deteriora, altera, suprime o hace inaccesibles datos informáticos, será reprimido
con pena privativa de libertad

-> Al escribir este post he introducido datos informáticos al servidor de Wordpress usando tecnologías de la comunicación.

Articulo 6. Tráfico ilegal de datos
El que, crea, ingresa, o utiliza indebidamente una base de datos sobre una persona natural o jurídica, identificada o identificable, para comercializar; traficar, vender, promover, favorecer o facilitar información relativa a cualquier ámbito de la esfera personal, familiar, patrimonial, laboral, financiera u otro de naturaleza análoga, creando o no perjuicio, será reprimido con pena privativa de libertad no menor de tres ni mayor de cincó años.

-> Al bajarme la lista de proyectos de Ley del Congreso he ingresado a su base de datos para facilitar la información relativa al ámbito laboral de cada congresista sin crear perjuicio (ojo que no es necesario causar perjuicio para ir en contra de la ley).

Artículo 1O. Abuso de mecanismos y dispositivos informáticos
El que fabrica, diseña, desarrolla, vende, facilita, distribuye, importa u obtiene para su utilización, uno o más mecanismos, programas informáticos, dispositivos, contraseñas, códigos de acceso o cualquier otro dato informático, específicamente diseñados para la comisión de los delitos previstos en la presente Ley, o el que ofrece o presta servicio que contribuya a ese propósito, será reprimido con pena privativa de libertad no menor de uno
ni mayor de cuatro años y con treinta a noventa días-multa.

-> En este post publico el programa informático que he fabricado, diseñado y desarrollado con el fin de específicamente incumplir los artículos 3 y 6 de la presente Ley.

Conclusión
He violado la ley de delitos informáticos (ley ex-beingolea) 3 veces
Señores congresistas métanme preso. Quiero cárcel dorada como Antauro y Fujimori. Gracias.

Sección para geeks
Aqui está el código para bajarse los nombres de los congresistas que fueron autores de proyectos de ley durante el 2013:

https://gist.github.com/aniversarioperu/6964023

Y aquí el código para plotear los datos:

https://gist.github.com/aniversarioperu/6965803
