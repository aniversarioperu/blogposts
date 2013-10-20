Parece que hay un troll en tuiter que me escribe cada vez que menciono los <a href="https://twitter.com/search?q=%23narcoindultos&amp;f=realtime">#narcoindultos</a>. Este troll es aprista y le gusta alabar a los principales líderes del APRA (ya sea por tuiter, o comentando en artículos de la revista Caretas).

<strong>Como contestar a los trolls da un poco de flojera, decidí fabricar un bot que lo haga por mí</strong>. Este bot es un programa muy simple, escrito en Python, que responde a aquellos que deciden trolear mi cuenta de tuiter <a href="https://twitter.com/aniversarioperu">@AniversarioPeru</a>.

Para esto modifiqué un muy simple chat-bot que encontré aquí: <a href="http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/">http://pythonism.wordpress.com/2010/04/18/a-simple-chatbot-in-python/</a>.

<strong>Este bot necesita ser entrenado</strong>, osea hay que hacerlo "leer" unos cuantos libros para que sepa qué responder a los trolls.

Decidí hacer mi bot picaresco pero inteligente. Entonces <strong>le hice leer las Tradiciones Peruanas</strong> de don Ricardo Palma (<a href="http://www.gutenberg.org/ebooks/21282">se bajan el libro de aquí</a>).

Podría hacer otro bot que tenga lenguaje un poco achorado. Para eso, su entrenamiento consistiría en hacerlo leer las columnas antiguas del <a href="http://www.malapalabrero.pe/">malapalabrero</a>.

En resumen, <strong>este bot busca si algún troll ha empezado a fastidiar por tuiter. Si esto es cierto, responderá al troll con frases sacadas de las Tradiciones Peruanas.</strong> Este bot es muy simple y las respuestas no tienen relación con lo que haya escrito el troll. Incluso, las respuestas no tienen mucho sentido. Supongo que será suficiente para que el troll se canse de fastidiar.

Lo bueno de tener un tuitbot es que interactuaría con los trolls mientras yo estoy durmiendo, en la discoteca o de vacaciones. El bot se activa cada media hora, pero si la cantidad de trolls aumenta, podría activarse cada 10 minutos.

Tengo planes de ir mejorando poco a poco este bot. Por ahora usa una aproximación a la <a href="http://es.wikipedia.org/wiki/Cadena_de_M%C3%A1rkov">cadena Márkov</a> para construir su respuesta. Por ejemplo podría emplear <a href="http://es.wikipedia.org/wiki/Inferencia_bayesiana">estadísticas Bayesianas</a> para entrenar el bot. Lo podría entrenar para que emita saludos, preguntas, afirmaciones, despedidas, insultos etc. El bot podría usar una aproximación bayesiana para darse cuenta si el troll ha emitido una pregunta, o un insulto y responder como amerite.

La ventaja de la inferencia Bayesiana es que al analizar las palabras de un tuit, puede ir aumentando o disminuyendo la probabilidad que el tuit sea —por ejemplo— saludo o insulto. Asumamos que un tuit tenga las palabras <strong>"caviar + rojo"</strong> hay probabilidad que el troll esté insultando. Si además el tuit contiene signos de interrogación repetidos, existe alta probabilidad que este tuit sea un insulto.<strong> Los estadísticos bayesianos llaman a esto último "probabilidad posterior"</strong>.

Idealmente el bot analizaría cada tuit y decidiría qué responder si la probabilidad posterior indica que he sido insultado. Tendría que hacer que mi bot se entrene leyendo los tuits que le endilgan los trolls a @rmapalacios.

Aquí hay un ejemplo de cómo sería una interacción entre un troll y mi tuitbot actual (en rojo las respuestas del bot).
<pre><span style="color: #333333;">&gt;ola k ase</span>
<span style="color: #ff0000;">de Lima títere que el refrán: más allá esas calles. de su límite, de cucarachas. de la tía carnal; estas palabras:</span>
<span style="color: #333333;">&gt;Que triste tu vida        </span>                       
<span style="color: #ff0000;">esposa. de una vaca, de asiento, de la guitarra. de oro, de que le da colores--palabras que le sucede un tanto como hacemos</span>
<span style="color: #333333;">&gt;mermelada que defiendes!!!   </span>                                               
<span style="color: #ff0000;">el reinado de la mazamorra, de grave en una mujer del rey. de nuestras abuelas eran una formidable invasión de plano.</span>
&gt;arriba alianza!
<span style="color: #ff0000;">de la jerga franciscana. de la Monclova y el guardián del mando, de recibido varios de los jesuítas.</span>
&gt;matemáticamente podemos clasificar al mundial
<span style="color: #ff0000;">de 1796 se plantaron en el Callao constituyó en su lado, de 1746, de aquel oportuno encarcelar, de una soberana paliza
</span></pre>
<h2>Sección geek</h2>
Aqui les dejo el código completo del tuitbot. Requiere haber instalado un cliente de tuiter que se pueda usar desde una consola de comandos. En un <a href="http://aniversarioperu.wordpress.com/2013/07/26/te-recuerdo-tu-narcoindulto-via-tuitbot/">post anterior detallé como usar el cliente llamado "t"</a>.

También requiere tener instalado Python. Y configurar el programa <strong>cron</strong> para que este tuitbot se active cada 30 minutos en búsqueda de tuits emitido por trolls (<a href="http://aniversarioperu.wordpress.com/2013/07/26/te-recuerdo-tu-narcoindulto-via-tuitbot/">en este post</a> explico como configurar <strong>cron</strong>).

Una vez que un troll es identificado, es necesario incluir el nombre de usuario en la lista de trolls para que el tuitbot sepa a quién dirigir su verbo florido.

Este es el programa que sirve para entrenar al bot. Se puede usar cualquier texto (de preferencia uno o más libros).

https://gist.github.com/aniversarioperu/7060778

Este es el programa que se encarga de recibir un mensaje y responder.

https://gist.github.com/aniversarioperu/7060825

Este es el tuitbot que se encarga de leer lo que emiten los trolls y responderles via tuiter.

https://gist.github.com/aniversarioperu/7060846
