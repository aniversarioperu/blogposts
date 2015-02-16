El último reportaje de la saga #intervenganAPDAYC se está transmitiendo desde el Congreso del República (30-Oct-2013). Además el útero de marita acaba de publicar <a href="http://utero.pe/selallevan/">una base de datos interactiva</a> con toda la repartición de las regalías que cobró APDAYC durante el 2012. También hay una <a href="http://utero.pe/guia-para-intervenir-apdayc/">hoja de ruta para intervenir APDAYC</a>.

Es ya conocido que Radio Inspiración maneja muchas radios vía la Fundación Autor que está ligada a APDAYC. Esta cadena de radios pasa muchas canciones y queríamos averiguar si hay algún patrón interesante en aquellas canciones que son más difundidas y repetidas en su programación. Por ejemplo, qué canciones tienen como autores a los directivos de APDAYC?, cuáles pertenecen al catálogo de las empresas que están íntimamente relacionadas con APDAYC? (E.T. Music?, IEPMSA?)

Para eso hice una acumulación y tabulación de los datos de las canciones más toneras de Radio Inspiración (<a href="http://inspiracionfm.com/index.php">aquí están los rankings</a>). La resolución de las imágenes era mínima y no se pudo hacer OCR. Entonces tuve que tipear las canciones una por una. Felizmente no eran muchas.

Luego era cuestión de juntar toda la información en un sólo archivo y hacer el plot usando funciones estadísticas del lenguaje de programación Python.

[caption id="attachment_289" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/top10.png"><img class="size-large wp-image-289" alt="Canciones de Radio Inspiración del top10 que son más frecuentes." src="http://aniversarioperu.files.wordpress.com/2013/10/top10.png?w=630" width="630" height="189" /></a> Canciones de Radio Inspiración del top10 que son más frecuentes.[/caption]

[caption id="attachment_290" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/top20.png"><img class="size-large wp-image-290" alt="Canciones de Radio Inspiración que son más frecuentes en el top20." src="http://aniversarioperu.files.wordpress.com/2013/10/top20.png?w=630" width="630" height="189" /></a> Canciones de Radio Inspiración que son más frecuentes en el top20.[/caption]

Sería interesante averiguar quiénes son los autores de esas canciones top-10. En teoría se podría ver cuáles son las canciones que pertenecen a cada autor y compositor registrado en APDAYC. Pero creo que eso es pedir demasiada transparencia.

<h2>Sección geek</h2>
Aquí el código para dibujar el gráfico:

Previa limpieza de datos:

[code language="shell" light="true"]
cat all_data.csv | awk -F ',' '{print $2}' | sort | uniq -c | sort -hr | sed 's/^\s\+//g' | grep -v '1 ' | sed -r 's/^([0-9]+)\s+/\1,/g' > tmp
[/code]

https://gist.github.com/aniversarioperu/7099374

https://gist.github.com/aniversarioperu/7101358

Aquí los datos:

https://gist.github.com/aniversarioperu/7099307
