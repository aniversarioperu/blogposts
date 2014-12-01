# Ha sido una buena semana para Manolo

Si eres lector habitual de este blog, y si has seguido las noticias durante la
última semana, probablemente has notado de la **no tan nueva** herramienta
digital denominada "Manolo, buscador de lobistas".

**"Manolo"** es un aplicativo **open source** que se encarga de cosechar los
datos que aparecen en los registros oficiales de las personas que visitan
diversas instituciones del Estado peruano.

La resolución ministerial, sobre la transparencia de entidades estatales,
203-2012-PCM dice así 
[[link PDF](http://www.peru.gob.pe/docs/PLANES/133/PLAN_133_R.M_N%C2%B0_203-2012-PCM_-_Modifican_Directiva_sobre_2013.pdf)]:

> Que, en aras de mejorar los niveles de transparencia
de la función pública, resulta importante que **las entidades
de todos los niveles de gobierno implementen el Registro
de Visitas en Línea** y se incorpore en el Portal de
Transparencia Estándar a través de un ícono que facilite
su acceso al ciudadano;

Si bien algunas entidades tienen el registro en línea tal como la ley manda, es
muy difícil buscar las visitas de alguna persona determinada. Para decirlo de
una manera suave: **los registros en línea del Estado son una desgracia,
son prácticamente inutilizables**.

Si quieres buscar a alguien solo se puede hacer por días, y hay que buscar día
por día, página por página.

Para eso existe **"Manolo"!**. Manolo tiene un bot que se activa todos los días
a las 3:00 am y se encarga de cosechar la lista de visitas de diversas
instituciones. Una vez que tiene los datos, los guarda e indexa en su base de
datos. Manolo también tiene un buscador amigable que te hace extremadamente
fácil y rápido buscar entre todos los registros.

Manolo está funcionando calladamente desde hace unos meses y ya tiene casi
medio millón de registros indexados. Estos datos han sido obtenidos de la
Oficina de Contrataciones del Estado (OSCE), Ministerio de Vivienda, Ministerio
de Defensa, Ministerio de la Mujer, Presidencia de Consejo de Ministros y los
registros de Presidencia (los que visitan Palacio de Gobierno).

Un buen día, el periodista Martín Hidalgo se puso a utilizar el aplicativo
Manolo **y a que no sabes lo que encontró**:

Encontró que ["Chocherín", el socio del prófugo Martín Belaunde Lossio visitó
Palacio de Gobierno 33 veces](http://utero.pe/2014/11/24/exclusivo-chocherin-el-socio-de-martin-belaunde-visito-palacio-de-gobierno-33-veces/).
El uso de Manolo le permitió encontrar este dato en un santiamén.

Gracias a "Manolo", en esa semana se pudieron generar cuatro portadas cuatro:

>- fig portadas

Los datos siempre han estado en las webs de las entidades estatales. Pero tuvo
que aparecer Manolo para que estas pepas recién puedan ser encontradas.

En el útero somos demasiado pánfilos que ponemos a la disposición de otros
medios periodísticos (la competencia) los datos y herramientas que con tanto
esfuerzo conseguimos. Y esto ha causado que mi sitio web que aloja Manolo haya
tenido muchas más visitas de lo normal. 

Estos son los "Manolos" disponibles

* [Manolo OSCE](http://www.aniversarioperu.me/manolo/)
* [Manolo Vivienda](http://www.aniversarioperu.me/manolo_vivienda/)
* [Manolo Defensa](http://www.aniversarioperu.me/manolo_defensa/)
* [Manolo Min. Mujer](http://www.aniversarioperu.me/manolo_mujer/)
* [Manolo PCM](http://www.aniversarioperu.me/manolo_pcm/)
* [Manolo Presidencia](http://www.aniversarioperu.me/manolo_presidencia/)

-< fig visitas

Están exigiendo bastante a mi pequeño servidor que está sufriendo al tener que
buscar entre casi medio millón de registros cada vez que algún usuario usa
Manolo para tratar de encontrar algún lobista.

>>-- fig ram

Por ahora "Manolo" es super básico y rudimentario. Lo ideal sería comprar otro
servidor para que lo datos sean almacenados en una base de datos mejor. Se
podría usar un servicio sofisticado de motor de búsqueda para que "Manolo"
tenga la opción de hacer rankings de resultados, opción de autocompletado,
      opción de sugerir palabras de búsqueda en caso el usuario haya ingresado
      algún nombre incorrecto, o sin tilde, etc.

Si bien las herramientas que hacen esto posible son *open source* (gratuitas)
    lo costoso es el pago mensual del servidor. Este servidor deberá ser
    potente y tener bastante memoria RAM para poder entregar los resultados de
    búsqueda sin demora.
      

Otro gasto adicional es el uso de proxies para cosechar los datos. Ya que por
alguna razón las entidades estatales tienen la mala costumbre de bloquear a
"Manolo". Al parecer el Estado considera que "Manolo" exige de sobre
manera sus servidores. Manolo solo realiza alrededor de 40 pedidos diarios a 
las 3:00am a cada institución estatal. Manolo es buena gente, no lo bloqueen
porfas.

Por ahora todos estos gastos salen de mi bolsillo. Es un gusto que me doy ya
que estas cosas son mi hobby, mi vacilón. Se podría hacer algo más sofisticado
de mayor utilidad y sacar el jugo a la tecnología, pero eso no es barato.

Así que amigo lector, si te interesa este tipo de iniciativas hay varias
maneras de colaborar poniendo el hombro: costeando servidores, costeando
proxies, y/o programando Manolo. Lo bueno es que este es un proyecto *open 
source* y el [código fuente está aquí](https://github.com/aniversarioperu/django-manolo) y si sabes programar estaré gustoso de
aceptar contribuciones de código.

Además, tú también puedes crear tu propio "Manolo, buscador de lobistas" para
tu institución estatal favorita. [Aquí las instrucciones](http://django-manolo.readthedocs.org/en/latest/).
