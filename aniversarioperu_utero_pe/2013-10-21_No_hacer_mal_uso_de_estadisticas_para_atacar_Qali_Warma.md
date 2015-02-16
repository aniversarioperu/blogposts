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
<h1>Actualización 22-Oct. Otro error</h1>
El señor Pepe Botella, en un comentario a este post, me avisa que él ha encontrado otro ejemplo de uso y abuso de las estadísticas en el mentado reporte académico que la prensa usa para atacar a Qali Warma.

Quiero pensar que este ha sido un error de mal uso de estadísticas, aunque el asunto se vuelve un poco rochoso.

En la página 36 empieza un floro donde el autor manifiesta que Qali Warma gasta menos dinero en los más pobres ("pobres multidimensionales").
<blockquote>...la poca atención que reciben los pobres multidimensionales en términos de cobertura de servicios básicos genera una fuente de ineficacia en cuanto a la distribución del gasto público</blockquote>
<blockquote>La distribución departamental del gasto social está mal enfocada pues existen departamentos con un alto nivel de pobreza multidimensional que reciben un gasto social por debajo del promedio nacional</blockquote>
Osea la hipótesis es <strong>hay menor gasto en departamentos con mayor porcentaje de pobreza</strong>. Esto se debería demostrar con otra regresión lineal de ajuste significativo a la línea de tendencia. Y eso es lo que prentende hacer el autor al mostrar un gráfico muy colorido:

[caption id="attachment_300" align="aligncenter" width="607"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/plot_19.png"><img class="size-full wp-image-300" alt="Regresión lineal con cuadrantes blancos y rosados. Qué hacen los cuadrantes allí?" src="http://aniversarioperu.files.wordpress.com/2013/10/plot_19.png" width="607" height="508" /></a> Regresión lineal con cuadrantes blancos y rosados. Qué hacen los cuadrantes allí?[/caption]

Los datos están en la Tabla 4 del informe (página 37). Bajé los datos, hice el plot y calculé el coeficiente de determinación y el valor del p-value para ver si hay o no hay correlación entre las variables gasto y nivel de pobreza.

[caption id="attachment_303" align="aligncenter" width="593"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/plot_19_reloaded1.png"><img class="size-full wp-image-303" alt="Gráfico sin los cuadrantes que estorban." src="http://aniversarioperu.files.wordpress.com/2013/10/plot_19_reloaded1.png" width="593" height="349" /></a> Gráfico sin los cuadrantes que estorban.[/caption]

Y creo que ya te diste cuenta que NO hay relación entre las dos variables! Mira pé:

<strong>R<sup>2</sup> = 0.02</strong> (si hubiera correlación este <strong>debería ser cercano a 1</strong>)
<strong>p = 0.43</strong> (si hubiera correlación este <strong>debería ser menor que 0.05</strong>)

El mismo error!

Pero aquí viene lo penoso. <strong>Qué michi hacen esos cuadrantes en tu gráfico?</strong> Primera vez en mi vida que los veo en un análisis de regresión. Los cuadrantes se usan en <a href="http://131.95.113.139/courses/multivariate/CCA.pdf">análisis canónico! ca-no-nico</a>!

Si quieres demostrar algo categóricamente debes aplicar las estadísticas relevantes y que sean las más simples. Si quieres comparar 2 variables, haces regresión lineal (o ajustas una distribución exponencial, logarítmica, etc). <strong>Si quieres explicar el comportamiento de tus datos según múltiples variables haces un análisis de correspondencia canónico o similar</strong>.

No quiero pensar que estas tratanto de estirar los datos. Los desconfiados van a pensar que quieres estirar las estadísticas, forzándolas para que falsamente den soporte al resultado que quieres obtener. Debes tener cuidado chochera.

Sobre todo, causa desconfianza cuando, de todos los puntos de tu gráfico, escoges algunos, los que te conviene usar para criticar Qali Warma. Esos son datos anecdóticos. Otro broder podría escoger solo los puntos que dan una conclusión contraria y discutir ampliamente que Qali Warma hace un excelente gasto del dinero.

<strong>Para evitar esas subjetividades se hacen regresiones lineales</strong>, cálculos de coeficientes y tests de significancia (p-value). Cosa que tu informe aparenta hacer, pero no lo hace. <strong>Presentas tablas y gráficos pero haces <i>cherry picking</i> para la discusión!</strong> Además, <strong>ta que no he visto ninguna mención al R<sup>2</sup> o al <i>p-value</i></strong> en tu informe.

<span style="color: #2b6fb6; font-size: 1.5em;">Sección geek</span>

Aquí está los dos análisis estadísticos, el de ejemplo y el que rehice con los datos del informe del señor de la Universidad del Pacífico.

https://gist.github.com/aniversarioperu/7083834

Aquí los datos originales usados en el reporte académico, tomado de su tabla 31.

https://gist.github.com/aniversarioperu/7083865

Aquí los datos originales de la tabla 4

https://gist.github.com/aniversarioperu/7107980
