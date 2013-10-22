El programa de alimentación a niños en edad escolar ha sido atacado estas últimas semanas. Uno de los ataques principales viene de un estudio académico de un profesor de Economía de la Universidad de Pacífico. Se pueden bajar el reporte de aquí: <a href="http://srvnetappseg.up.edu.pe/siswebciup/Files/DD1307%20-%20Vasquez.pdf">http://srvnetappseg.up.edu.pe/siswebciup/Files/DD1307%20-%20Vasquez.pdf</a>

Estuve mirando rápidamente el reporte en cuestión y vi que una de las críticas se basa en una mala interpretación de al menos uno de los análisis estadísticos.

En la página 93 dice:
<blockquote>El Gráfico 50 muestra los resultados obtenidos para el caso de los escolares. En este caso se comparó el gasto presupuestado por escolar contra el porcentaje de niños entre 6 y 11 años que viven en hogares con déficit calórico, información basada en los resultados del IPM. Este muestra resultados preocupantes, a diferencia del caso para preescolares: se observa una relación negativa entre ambas variables. Esto quiere decir que el presupuesto por escolar no está distribuido equitativamente, pues es mayor en los departamentos con menor déficit calórico.</blockquote>
Este es el gráfico 50:

<a href="http://aniversarioperu.files.wordpress.com/2013/10/grafico_50.png"><img class="aligncenter size-large wp-image-262" alt="grafico_50" src="http://aniversarioperu.files.wordpress.com/2013/10/grafico_50.png?w=630" width="630" height="504" /></a>
<h2>Rehaciendo el análisis</h2>
Al ojo se vé que no hay relación entre las variables. Copié los datos que están en la tabla 31 (de la página 123) y ajusté una <a href="http://es.wikipedia.org/wiki/Regresi%C3%B3n_lineal">regresión lineal</a> en el programa estadístico R.

<strong>Mira los puntos todos aglomerados al centro. No dejes que la línea de tendencia te engañe</strong>. El coeficiente de determinación R<sup>2</sup> es casi cero (0.04) y el <i>p-value</i> no es significativo ( p &gt; 0.05).

Tarán! los resultados dicen que <strong>NO hay correlación entre las variables </strong>y que <strong>las conclusiones del autor de líneas arriba están erradas.</strong> NO es cierto que los datos indiquen que se gaste menos dinero en áreas con mayor deficiencia calórica.

<a href="http://aniversarioperu.files.wordpress.com/2013/10/plot_50_reloaded.png"><img class="aligncenter size-full wp-image-263" alt="plot_50_reloaded" src="http://aniversarioperu.files.wordpress.com/2013/10/plot_50_reloaded.png" width="557" height="433" /></a>

<strong>Si hubiera una correlación entre dos variables</strong>, osea una relación entre gasto y nivel de deficiencia calórica, deberíamos de tener un gráfico así. Mira los puntos distribuidos a lo largo de la línea de tendencia, no están aglomerados!:

[caption id="attachment_279" align="aligncenter" width="553"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/plot_ejemplo1.png"><img class="size-full wp-image-279" alt="Ejemplo de correlación significativa" src="http://aniversarioperu.files.wordpress.com/2013/10/plot_ejemplo1.png" width="553" height="431" /></a> Ejemplo de correlación significativa[/caption]

Hay obvia correlación, a mayor valor de x, menor valor de y. Además los valores de R<sup>2</sup> y <em>p-value</em> son: <strong>R<sup>2</sup> = 0.82, p = 0.0002. El coeficiente R<sup>2</sup> es cercano a 1, y el <em>p-value</em> es mucho menor que 0.05. Osea altamente significativo</strong>.

Pero los valores que salen de analizar los datos del estudio académico son los siguientes:

<strong>R<sup>2</sup> = 0.04</strong> (es casi cero, <strong>si fuera cercano a 1</strong> sabes que <strong>hay correlación. Pero en este caso <strong>no tiene nada!</strong>)</strong>

<strong>p = 0.157</strong> (es mayor que 0.05, osea datos no significativos).

Ya ves chocherita,<strong> no hay tendencia, no hay correlación, no hay causación.</strong> Señores, no tiene nada!
<h2>Pero hay más</h2>
El autor del estudio académico da como ejemplo (pag. 93) que en Puno (con alto déficit calórico) se gasta menos por niño que en Lima. <strong>Pero este es un dato anecdótico</strong>. Ya pe causa! <strong>Estudios académicos no se basan en datos anecdóticos</strong>. Además si tú criticas que la política de Qali Warma está mal, debes demostrar que en su conjunto se está gastando menos dinero donde más se necesita. Pero lamentablemente los datos y estadísticas duras refutan tus conclusiones.<strong> En este punto en particular la política será desordenada, o sin ningún patrón o tendencia, pero no es lo que afirmas pe varón.</strong>

Ya otras personas han criticado este dichoso trabajo, <a href="http://www.larepublica.pe/columnistas/contracandela/quien-quiere-comerse-la-comida-de-los-ninos-pobres-20-10-2013">@rmapalacios</a>, la ministra <a href="http://www.larepublica.pe/21-10-2013/hariamos-mal-minando-un-programa-que-busca-alimentar-a-nuestros-ninos">Mónica Rubio</a>, y <a href="http://diario16.pe/noticia/39580-campana-tremendista-comercio-enrique-vasquez-contra-programas-sociales">Diario16</a>.

Cuando tenga tiempo libre revisaré el resto del trabajo académico.
<h2>Sección geek</h2>
Aquí está los dos análisis estadísticos, el de ejemplo y el que rehice con los datos del informe del señor de la Universidad del Pacífico.

https://gist.github.com/aniversarioperu/7083834

Aquí los datos originales usados en el reporte académico, tomado de su tabla 31.

https://gist.github.com/aniversarioperu/7083865
