Hace un par de semanas, el portal Wikileaks publicó el documento secreto correspondiente al borrador de las negociaciones del capítulo de propiedad intelectual del TPP (Trans-Pacific Partnership).

Ya han habido <a href="http://www.hiperderecho.org/2013/05/conversatorio-propiedad-intelectual-tratados-de-libre-comercio-y-derechos-humanos/">varias alertas</a> acerca de las implicancias de estas negociaciones (una <a href="http://larepublica.pe/blogs/pasado/2013/11/26/nuevos-y-encaletados-wikileaks-sobre-peru-i/">introducción al tema aquí</a>). Además de ser negociaciones que <a href="http://www.larepublica.pe/14-05-2013/tpp-cuando-el-tratado-que-se-negocia-puertas-cerradas-se-mete-con-internet">se realizan de manera secreta</a>, preocupa que <a href="http://www.nonegociable.pe/nuestra-peticion/">esté en riesgo el libre acceso a Internet</a> y el componente de propiedad intelectual que <a href="http://www.larepublica.pe/14-05-2013/costo-de-medicamentos-se-incrementaria-con-el-tpp">pueda dificultar el </a><span style="line-height:1.5;"><a href="http://www.larepublica.pe/14-05-2013/costo-de-medicamentos-se-incrementaria-con-el-tpp">acceso a medicamentos</a>.</span>

Se supone que este tratado está apunto de ser firmado por el Perú antes de fin de año y gracias a Wikileaks recién podemos darnos cuenta de lo que realmente se ha estado negociando a puerta cerrada.

El documento filtrado al público tiene 96 páginas (si se bajan el PDF) y está <a href="http://wikileaks.org/tpp/">disponible aquí</a>. A primera vista se pueden ver los temas que se han discutido y la manera de cómo ha votado cada país. Algunas propuestas parecen provenir de ciertos países mientras que otros votan a favor o se oponen (ver figura 1).

[caption id="attachment_423" align="aligncenter" width="543"]<a href="http://aniversarioperu.files.wordpress.com/2013/12/tpp1.png"><img class="size-full wp-image-423" alt="Figura 1. Algunos países votan a favor, otros se oponen." src="http://aniversarioperu.files.wordpress.com/2013/12/tpp1.png" width="543" height="205" /></a> Figura 1. Algunos países votan a favor, otros se oponen.[/caption]

Podemos dar una lectura a todo el PDF para enterarnos <strong>"cómo es la cosa"</strong>. Pero, <strong>siendo este un blog nerd, podemos hacer un "data-mining" rudimentario</strong> para rápidamente poder averiguar algunos detalles:
<ol>
	<li>Cuántas veces Perú vota como país de manera opuesta a Estados Unidos?</li>
	<li>Cuántas veces Perú vota igual que Estados Unidos?</li>
	<li>Podemos averiguar como vota algún país vecino? digamos Chile, vota de manera diferente a Perú?</li>
	<li>Chile se opone o vota de manera similar que Estados Unidos?</li>
	<li>En qué puntos específicos hay discrepancias en las votaciones</li>
</ol>
Podría ponerme a contar la votaciones una por una pero me iba a demorar una enternidad. Entonces escribí un <strong>script in Python para hacer este data-mining</strong> (script completo en la sección geek al final de este post).

Lo bueno es que Wikileaks publicó el documento como PDF conteniendo texto (no como imágenes). Entonces, es bien fácil convertir el PDF a TXT y proceder con el minado de datos.

[code language="bash" light="true"]
pdftotext Wikileaks-secret-TPP-treaty-IP-chapter.pdf texto.txt
[/code]

Mi script funciona de la siguiente manera:
<ol>
	<li>Lee el documento TXT línea por línea</li>
	<li>Si encuentra una línea que contenga la palabra <b>Article</b> se pone alerta y se fija si hay alguna línea con las <strong>iniciales de los países PE, CL, US</strong> (osea Perú, Chile y Estados Unidos).</li>
	<li>La línea de texto que indica la votación tiene un patrón consistente: <em>países</em> <strong>oppose/propose</strong> <em>más países</em>.</li>
	<li>Entonces el script divide la lista de países en dos bandos, los que están a la derecha e izquierda de las palabras clave <strong>oppose/propose</strong></li>
	<li>Una vez divididos los bandos, solo es cuestión de contar cuántas veces se repiten las iniciales y llevar la cuenta el bando.</li>
</ol>
Estos son los resultados:
<pre>Conteo de votos de PE versus US
propose_together 26
oppose_together 6
oppose_each_other 23

---------------------

Conteo de votos de PE versus CL
propose_together 36
oppose_together 22
oppose_each_other 8

---------------------

Conteo de votos de US versus CL
propose_together 16
oppose_together 2
oppose_each_other 32</pre>

Se supone que ambos países, Perú y Chile, tenían la intención hacer propuestas alternativas a las que figuran en el TPP (<a href="http://www.iriartelaw.com/peru-planteara-cambios-capitulo-propiedad-intelectual-tpp">ver aquí</a> y <a href="http://www.larepublica.pe/columnistas/globalizaciones/apec-y-tpp-ultimos-pasos-10-10-2013">aquí</a>).

Pero al parecer, esto puede haber quedado en intenciones, al menos viendo la manera cómo ha estado votando Perú.

<strong>Perú ha votado igualito que Estados Unidos 32 veces</strong> y se ha opuesto (votado diferente) sólo 23 veces. <strong>Mientras que Chile ha votado igual que EEUU solo 18 veces</strong> y se ha opuesto 32 veces.

Parece que Chile se opone mucho a las propuestas apoyadas por EEUU mientras que Perú vota en tándem. Mi script me dice que:
<pre>
Chile se opone a US y PE 9 veces
</pre>

y se opone en estos artículos del TPP:

<pre>
* Article QQ.C.2: {Collective and Certification Marks}
    [US/PE/MX41/SG propose; AU/NZ/ VN/BN/MY/CL/CA oppose: 2. Pursuant to
* Article QQ.D.11: [CL/SG/BN/VN/MX propose82; AU/PE/US/NZ/CA/JP oppose:
* Article QQ.D.12: {Homonymous Geographical Indications}
    [NZ/CL/VN/MY/BN/SG/MX propose84; PE/US/AU oppose: 1. Each Party may
    [CL propose; AU/US/PE/NZ/VN/SG/MY/BN/MX/CA/JP oppose: 2. The Parties
    [CL/SG/BN/MX propose; AU/PE/US/NZ/CA/JP oppose: Annex […] Lists of
* Article QQ.E.9: [US/PE/AU propose; 101 CL/VN/MY/BN/NZ/CA/SG/MX oppose:
* Article QQ.H.7: {Criminal Procedures and Remedies / Criminal Enforcement}
    2. [US/AU/SG/PE propose; CL/VN/MY/NZ/CA/BN/MX oppose: Willful
* Article QQ.I.1:267 {Internet Service Provider Liability}
    280 [US/PE/SG/AU propose; CL/NZ/VN oppose: A Party may request consultations with the other Parties to
</pre>

Ahora que tenemos una idea a ojo de buen cubero cómo van las votaciones de Perú, Chile y EEUU, además de los temas potencialmente picantes. Podemos leer mejor el documento filtrado por Wikileaks.

<strong>** Spoiler ** (Uno de esos temas tiene que ver con la denominación de origen del Pisco. Chile propone, Perú y EEUU se oponen).</strong>

PD. este post se inció a sugerencia de un tuitero amixer.

<h1>Sección geek</h1>

El script corre de la siguiente manera:

[code language="bash" light="true"]
python leeme_votaciones.py texto.txt
[/code]

https://gist.github.com/aniversarioperu/7736850
