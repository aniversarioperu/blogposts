Ministros y ex-primer ministros de este gobierno coinciden en pensar que la inseguridad ciudadana es una percepción, ilusión de la gente, producto de estados mentales histéricos y que no hay que quejarse tanto.

Lo cierto es que según los datos del INEI. <a href="http://www.inei.gob.pe/media/MenuRecursivo/Cap08005.xls">El número total de delitos a nivel nacional</a> está aumentando:

[caption id="attachment_371" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/11/delitos_totales.png"><img class="size-large wp-image-371" alt="Número total de delitos. Fuente INEI http://www.inei.gob.pe/media/MenuRecursivo/Cap08005.xls" src="http://aniversarioperu.files.wordpress.com/2013/11/delitos_totales.png?w=630" width="630" height="94" /></a> Figura 1. Número total de delitos. Fuente INEI <a href="http://www.inei.gob.pe/media/MenuRecursivo/Cap08005.xls">http://www.inei.gob.pe/media/MenuRecursivo/Cap08005.xls</a>[/caption]

<h2>Estadísticas frecuentistas</h2>
Una regresión lineal nos confirma la tendencia:

[caption id="attachment_372" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/11/delitos_totales_nivel_nacional.png"><img class="size-large wp-image-372" alt="Regresión lineal de número total de delitos versus año." src="http://aniversarioperu.files.wordpress.com/2013/11/delitos_totales_nivel_nacional.png?w=630" width="630" height="551" /></a> Figura 2. Regresión lineal de número total de delitos versus año.[/caption]

La regresión lineal (y el gráfico) nos dice que conforme pasan los años ha aumentado la delincuencia (<strong>R<sup>2</sup> = 0.67</strong>) de manera significativa (<strong><i>p-value</i> = 0.008</strong>).

Se observa que entre los años 2008 y 2011 ocurrió un punto de quiebre y la delicuencia aumentó, pero no podemos apuntar con precisión en qué año comenzó esta racha de mayor número de delitos. Además que los datos no se ajustan muy bien a la línea de tendencia. Pareciera que el aumento de delitos no es lineal, parece ser exponencial! Esta incertidumbre es parte de las limitaciones de las estadísticas que estoy usando, esta corriente llamada <strong>estadísticas frecuentistas</strong>.

<h2>Estadísticas bayesianas</h2>
Pero afortunadamente existen las <strong>estadísticas bayesianas</strong> que nos pueden dar algo más de información respecto a este tema.

Estas estadísticas nos pueden ayudar a estimar en qué año aumentó la delincuencia. Por ejemplo, el promedio de delitos anuales antes de este incremento puede ser considerado como la <strong>variable $latex \lambda_1$</strong>, el promedio de delitos después del punto de quiebre pueder ser la <strong>variable $latex \lambda_2$</strong>, y el año en que ocurrió el punto de quiebre puede ser la <strong>variable <i>tau</i></strong>.

Podemos estimar el rango de valores más probables que puede tener cada variable si es que usamos simulaciones de números aleatorios.

<em>[Paréntesis]</em>
Los estadísticos bayesianos conocen la probabilidad más alta de estos valores como <strong>probabilidad posterior</strong>. Por ejemplo, cuando tú amig@ lector(a) recibes un email (digamos de Gmail), la empresa Google tiene un software que aplica estadísticas bayesianas al contenido del mensaje. Lo que hace es buscar palabras clave que indiquen que el email recibido es spam. Si el contenido tiene las palabras "viagra", "penis", "enlargement". <strong>Existirá alta probabilidad posterior que este correo es spam</strong>, y el software de Google lo enviará directamente a la carpeta Junk. Por eso las estadísticas bayesianas son importantes, y además las usas a diario sin darte cuenta.
<em>[/Paréntesis]</em>

Volviendo a nuestro problema, el lenguaje de programación Python tiene una librería muy chévere para hacer estadísticas bayesianas. Es el paquete <strong>pymc</strong>. Entonces solo es cuestion de simular muchas veces los valores de números totales de delito antes y después del incremento, y el año de incremento en la tasa delincuencial (osea $latex \lambda_1, \lambda_2,$ y <em>tau</em>).

Realicé una simulación de 50 mil generaciones usando una <a href="http://en.wikipedia.org/wiki/Markov_chain_Monte_Carlo">cadena Markov Monte Carlo</a>, descarté las primeras 10 mil generaciones y dibujé los resultados:

<a href="http://aniversarioperu.files.wordpress.com/2013/11/plot1.png"><img class="aligncenter size-large wp-image-376" alt="" src="http://aniversarioperu.files.wordpress.com/2013/11/plot1.png?w=630" width="630" height="540" /></a>

<strong>Vemos que hay una diferencia notable entre el total esperado de delitos antes ($latex \lambda_1$) y después ($latex \lambda_2$) del incremento</strong> (casi 160 mil delitos antes y 230 mil delitos luego del incremento de la delincuencia).

También vemos que es <strong>más probable que en el 6to año (osea año 2011) ocurrió la aceleración de la delincuencia</strong> en el Perú. 

Podemos combinar estas tres variables en un solo gráfico:

<a href="http://aniversarioperu.files.wordpress.com/2013/11/plot2.png"><img src="http://aniversarioperu.files.wordpress.com/2013/11/plot2.png?w=630" alt="" width="630" height="472" class="aligncenter size-large wp-image-377" /></a>

Este gráfico muestra los valores esperados de delito antes, después y durante la aceleración en el nivel de delicuencia. Vemos que esto ocurrió del año 2010 al 2011.

Ahora, pregunto <strong>qué acontecimiento ocurrió entre 2010 y 2011 que fue el causante del aumento de la delicuencia en nuestro país?</strong> El que sepa "que levante la mano".


<h1>Sección geek</h1>

Aquí está el código para hacer la regresión lineal en R:

https://gist.github.com/aniversarioperu/7292990

Aquí el código para hacer el análisis bayesiano (usa Python, pymc, y prettyplotlib):

https://gist.github.com/aniversarioperu/7293034
