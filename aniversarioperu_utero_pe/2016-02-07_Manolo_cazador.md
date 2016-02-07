#Con Manolo-cazador podrás rebuscar el pasado de tus candidatos favoritos


## El problema
Cada vez que se presentan la listas de candidatos al Congreso siempre pienso:

> Sería chévere si existiera alguna herramienta que permita averiguar si algunos de estos candidatos
> tienen sentencias, juicios, deudas con el Estado por reparación civil, etc.

## Un poco de historia
Durante las pasadas elecciones regionales y municipales del 2014, estuvimos descargando bases de datos 
del Estado para hacer cruces de información con las listas de candidatos de aquella vez.

En el año 2014, como parte del proyecto Verita, encontramos que 
[hartos candidatos habían sido sentenciados](http://utero.pe/2014/08/19/verita-final-violadores-y-ladrones-tambien-postulan-en-estas-elecciones-ademas-los-mas-condenados/)
por peculado, homicidio, no pasaban pensión a sus hijos/cónyuges, etc. Es decir, siempre se presentan 
una sarta de malhechores.

Con mi amixer [\@matiskay](https://twitter.com/matiskay) nos pusimos a reciclar buena parte del software que se generó para Verita durante el año 2014. Este software consiste en spiders que van a una página web del Estado, por ejemplo los deudores por alimentos, y descargan todos los registros de las personas fichadas allí. También se descarga el monto que deben y si no le pasan pensión a uno o más niños/cónyuges.

**Ojo que toda esta info está colgada en las páginas del Estado** y son de libre acceso para cualquier hijo de vecino. Lo que hace el software es descargar datos públicos de manera eficiente y veloz. No hacemos nada de hackeo, no rompemos contraseñas ni explotamos vulnerabilidades. Todos somos legales pe varón.

Lo bueno es que el software de Verita es *open source* y siempre ha estado colgada en la red social para nerds [conocida como Github](https://github.com/veritape), para vista y paciencia de cualquiera.
Entre las miles de líneas de código se encuentran spiders para descargar:

* lista de deudores de reparación civil por agravio al Estado peruano ((link al software)[https://github.com/veritape/scrapy_deudores]).
* spider para descargar todos los deudores por alimentos ((link al software)[https://github.com/ventanita/scraper_redam]).

También hay código proporcionado amablemente por usuarios anónimos como el amixer **@escribiendocodigo** quien hizo un spider para descargar datos de la Superintendencia de Transporte Terrestre (SUTRAN). Link [aquí](https://github.com/ventanita/scraper_sutran).

El amixer **@wesitos** escribió un spider para descargar datos de Infogob. Link (aquí)[https://github.com/ventanita/scraper_infogob].

## El software
Estos spiders tienen la función de scrapear datos. Es decir, es software que visita una página web, y descubre los links en cada una de las páginas y prosigue a visitarlas. En cada visita examina el contenido de la página, y si existe algún dato importante lo descarga y guarda en el disco duro local. 

Estos spiders son de fácil fabricación ya que se basan en el *framework open source* llamado
 **Scrapy**. Este framework se encarga de lidiar con cookies, reintentos si alguna página no se pudo visitar, redirecciones, automaticamente obecede las indicaciones de **robots.txt**, permite fácil extracción de datos basados en tags HTML, XML y CSS. [**Scrapy**](http://scrapy.org/) está escrito en el lenguaje Python y es de uso gratuito (por ser *open source*).

## Manolo-cazador
Lo que hemos hecho con @matiskay es:

* utilizar los spiders de Verita,
* descargar los datos
* subirlos a un servidor
* hacer un indexado para poder hacer búsquedas de manera rápida,
* implementar un buscador adicional en la exitosa aplicación conocida como [Manolo, buscador de lobistas](http://manolo.rocks).

Este buscador se llama **Manolo cazador**. La idea es que cuando los partidos políticos publiquen sus listas de candidatos al Congreso. Tú puedas hacer como Acuña, un copy/paste de la lista y pergarla dentro del buscador **Manolo cazador**. Si tu candidato se portó mal y figura en las bases de datos que hemos scrapeado, aparecerá en el resultado de búsqueda.

O sea ya no es necesario buscar a cada persona de la lista entre las distintas y diversas bases de datos del Estado. Todo está en un solo lugar, Manolo-cazador. Y hacer un cruce de información de 130 nombres no te tomará más de unos segundos.

Esperamos que esta herramienta sea de utilidad a ciudadanos de a pie y a los amigos periodísticos.

# Los datos en Manolo-cazador
Actualmente Manolo-cazador tiene en su masiva base de datos la siguiente información:

* deudores de alimentos (REDAM)
* deudores de reparaciones al Estado peruano
* candidatos a las elecciones Municipales y Regionales 2014 que indicaron tener sentencias,
* y las personas que recibieron conmutación de pena durante el 2do gobierno aprista (a.k.a narcoindultos).

Si tienen sugerencias de bases de datos a incorporar a Manolo-cazado pasen la voz que @matiskay y yo somos todo oídos.


///////////////////////////////////////////////////////////////////////////////////////////////////////////

Big Disclaimer:
El autor es empleado de la empresa Scrapinghub. Esta empresa creó y mantiene el framework Scrapy.

///////////////////////////////////////////////////////////////////////////////////////////////////////////