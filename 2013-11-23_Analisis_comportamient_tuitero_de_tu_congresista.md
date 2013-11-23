Como ya saben, hace unos días terminó la discusión, e idas y venidas, acerca
del grupo de trabajo de derechos humanos del Congreso, presidido por la
congresista fujimorista Martha Chavez (<a href="https://twitter.com/MarthaChavezK36">@MarthaChavezK36</a>).

La discusión degeneró tanto que llegó al tuiter. La congresista Martha Chavez
anunciaba en tuiter sus planes de trabajo dentro de la comisión y respondía a
uno que otro insulto tuitero. Era notable la cantidad de tuits emitidos por la
congresista. Pero, fueorn muchos tuits? pocos? en qué horas acostumbra tuitar
la congresista?

Usando herramientas de Linux, Python y unas cuantas librerías "open source"
podemos analizar el comportamiento tuitero de Martha Chavez.

Descargué del tuiter los 3200 tuits más recientes de la congresista. Para eso
usé un <a href="https://github.com/sferik/t">cliente de tuiter</a> usable desde
la consola Linux.

[code language="shell"]
t timeline -c -n 3200 MarthaChavezK36 > MarthaChavezK36.csv
[/code]

Aquí ven parte de los tuits descargados (click para ampliar).

<a href="http://aniversarioperu.files.wordpress.com/2013/11/tuits_descargados_martha_chavez.png"><img class="aligncenter size-medium wp-image-390" alt="3200 tuits más recientes de Martha Chavez" src="http://aniversarioperu.files.wordpress.com/2013/11/tuits_descargados_martha_chavez.png?w=300" width="300" height="126" /></a>

Hice un gráfico del número de tuits por día, usando Python.

[caption id="attachment_388" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/11/timelinemarthachavezk36-csv.png"><img class="size-large wp-image-388" alt="timeline de la congresista Martha Chavez " src="http://aniversarioperu.files.wordpress.com/2013/11/timelinemarthachavezk36-csv.png?w=630" width="630" height="472" /></a> timeline de la congresista Martha Chavez[/caption]

Este timeline comienza el 24 de julio. Vemos que <strong>tuvo bastante
actividad el 28 de Julio</strong>, mediados de Septiembre (<strong>cuando se
discutía sobre la unión civil de parejas del mismo sexo</strong>), primera y
segunda semana de Octubre (<strong>en esa época se tuiteaba sobre la renuncia
de Fujimori por fax</strong>), primera semana de Noviembre (cuando se armó el
chongo de su elección como coordinadora del grupo de trabajo sobre derechos
humanos).

Parece que su destitución del grupo de DDHH <strong>no hizo</strong> que Martha
Chavez tuitee tanto como cuando se hablaba de la unión civil (muy revelador!).

Pero <strong>supongo que Martha Chavez tuitea en sus horas libres</strong>,
cuando ya terminó sus horas de trabajo en el congreso, además de los fines de
semana.

Podemos ver esto si usamos sus tuits para generar un "punchcard":

[code language="shell" light="true"]
python analizar_tuits.py MarthaChavezK36.csv | python punchcard.py -f punchcard_Martha_Chavez.png
[/code]

<a href="http://aniversarioperu.files.wordpress.com/2013/11/punchcard_martha_chavez1.png"><img class="aligncenter size-large wp-image-395" alt="horas de tuiteo de Martha Chavez" src="http://aniversarioperu.files.wordpress.com/2013/11/punchcard_martha_chavez1.png?w=630" width="630" height="290" /></a>

Esto es alucinante! <strong>La congresista tuitea todos los días de la
semana</strong>. <strong>Tuitea a forro entre las 8 y 10 de la mañana (ni bien
llega al Congreso?</strong>). Tuitea con mayor fuerza los días Viernes.
El menor número de tuits a la 1:00pm hace suponer que a esa hora almuerza.
Sábados y Domingos, no descansa, tuitea tanto como los días lunes. Y parece que
se va a dormir a la 1:00 am. Al parecer duerme menos de 8 horas (eso no es
saludable congresista!).

Este nivel de tuits emitidos por Martha Chavez es muy alto? muy bajo? Podemos
hacer una comparación con un tuitero consumado, neto y nato. <strong>Comparemos
con el Útero de Marita</strong>:

Este es el punchcard del <a href="http://utero.pe">utero.pe</a>.

<a href="http://aniversarioperu.files.wordpress.com/2013/11/punchcard_uterope.png"><img class="aligncenter size-large wp-image-397" alt="punchcard uterope" src="http://aniversarioperu.files.wordpress.com/2013/11/punchcard_uterope.png?w=630" width="630" height="270" /></a>

Vemos que, al parecer, el útero.pe tuitea menos que la congresista.
Uterope<strong> tuitea muy poco los viernes, sábados y domingos</strong> (a
excepción de las 9:00pm cuando tuitea con furia, debe ser que a esa hora pasan
los noticieros dominicales). <strong>Qué hace el uterope los viernes y fines de
semanas que no tuitea?</strong> Debe tener buena vida. También tuitea bastante
los jueves.

Aqui les dejo el código necesario para hacer este tipo de análisis (?) con
cualquier tuitero. Pero fíjense que el tuitero no ande borrando sus tuits ni
use tuits programados ya que malograría el "análisis".

<h1>Sección geek</h1>
Código para producir el gráfico timeline y producir las fechas en formato unix, necesarias para dibujar el punchcard. El programa que hace el punchard lo saqué de aquí: <a href="https://github.com/aaronjorbin/punchcard.py">https://github.com/aaronjorbin/punchcard.py</a>

https://gist.github.com/aniversarioperu/7617926
