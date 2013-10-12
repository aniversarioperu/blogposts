El <a title="#intervenganapdayc" href="http://utero.pe/category/denuncia/intervenganapdayc/">útero de marita</a> está emitiendo informes diarios acerca de los manejos del dinero que realiza APDAYC en nombre de los compositores y escritores de música del Perú.

Marco Sifuentes <a title="Goku" href="https://www.facebook.com/photo.php?fbid=10151709249014372&amp;set=a.85401814371.81628.54087089371&amp;type=1">escribió en Facebook</a> que requiere ayuda para poder asimilar mejor todos los destapes que está posteando en su blog <a title="utero.pe" href="http://utero.pe">utero.pe</a> (junto con Jonathan Castro).

Con ánimos de ayudar a la causa (<a href="https://twitter.com/search?q=%23IntervenganAPDAYC">#intervenganAPDAYC</a>) me puse a ver la cantidad de dinero que cobraron algunos directivos del APDAYC durante el 2012, por concepto de derechos de autor. En el post uterino "<a href="http://utero.pe/se-la-llevan-facil/">se la llevan facil</a>" aparecen algunos números, pero no se aprecia si esta ganancia es mucho (o poco) en comparación con lo ganado por los asociados de APDAYC que no son miembros del Consejo Directivo.

Intenté hacer un gráfico de lo ganado por los compositores más prolíficos en comparación con el dinero que cobraron los directivos de APDAYC.

Obtuve la lista de directivos de <a href="http://www.apdayc.org.pe/norganizacion11.html">aqui</a>. Y las ganancias de los 250 asociados que tuvieron más regalías durante el 2012 de <a href="http://www.scribd.com/doc/135740127/Memoria-Apdayc-2012">aqui</a>.

Tuve que bajarme el PDF, convertirlo a texto, y dibujar el gráfico. Como soy bien nerd, para convertir el texto usé comandos de Linux y para dibujar el gráfico usé el lenguaje de programación Python (con su librería gráfica <a href="http://matplotlib.org/">matplotlib</a>).

Aqui está el gráfico, y más abajo el código que tuve que tipear para hacer este "análisis" tan diligente ;-) (hacer click para agrandar la imagen).

[caption id="attachment_161" align="aligncenter" width="300"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/cobraron_mas_apdayc_2012.png"><img class="size-medium wp-image-161" alt="Los que más cobraron, APDAYC 2012" src="http://aniversarioperu.files.wordpress.com/2013/10/cobraron_mas_apdayc_2012.png?w=300" width="300" height="142" /></a> Los que más cobraron, APDAYC 2012[/caption]

Manya, son haaaaaartos los compositores que cobran regalías. Pero son unos pocos quien se llevan harta plata, y son muchos los que cobran poquito (se lleva 3 mil soles al año el que está en puesto 250).

Debemos alegrarnos por los miembros del Consejo Directivo de APDAYC que son afortunados en estar entre los que más regalías se llevaron durante el 2012 (por ejemplo José Escajadillo, Armando Massé y Julio Andrade, entre otros).
<h1>[Actualización 6 de Octubre 2013]</h1>
Un tuitero/bloguero influyente me sugirió averiguar si hay un patrón de las ganancias recibidas por los socios que tienen mayor poder de decisión en APDAYC. Osea <strong>ver si los que cortan en jamón en APDAYC ganan más o ganan menos en comparación con los socios que tienen menor voto</strong> en los manejos de la Sociedad Colectiva APDAYC.

<a href="http://utero.pe/soy-apdayc-y-hago-lo-que-quiero/">El útero de marita nos cuenta que no todos los socios de APDAYC tienen el mismo derecho a voto</a>. Por ejemplo <strong>cada voto de los socios principales vale por 5</strong>, cada voto de los <strong>socios vitalicios vale como 4 votos</strong>, c<strong>ada voto de socios activos vale por 3</strong>.

Se supone que en una democracia cada persona es igual a un voto, pero en APDAYC eso no es así. Entonces los que tienen mayor poder de decisión del rumbo de APDAYC, <strong>los que parten y reparten son</strong> principalmente ese grupo de <strong>socios principales, vitalicios y activos</strong>.
<h2>Cuanto reciben de regalías los que cortan el jamón en APDAYC?</h2>
Estuve mirando otra vez los datos y me di cuenta que <strong>estos socios privilegiados son casi la mitad (138 socios, o el 55%) pero se llevan la mayoría de plata</strong> recaudada en APDAYC. El 84% del dinero cobrado por regalías durante el 2012 (7 millones de soles) se lo llevaron este grupo de socios con voto privilegiado. Mientras que la otra mitad de socios le corresponde poco más de 1 millon (16% del total).

Resulta interesante que los que cortan el jamón en APDAYC se lleven el 84% del dinero (a pesar de ser la mitad de socios con derecho a voto).

Bueno <strong>dicen que el que parte y reparte se lleva la mayor parte</strong>?

Aqui les dejo el gráfico para digerir mejor los datos (al final de este post está todo el código usado para los análisis).

[caption id="attachment_168" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/socios_principales_vitalicios_activos.png"><img class="size-large wp-image-168" alt="Ganancias de socios principales, vitalicios y activos" src="http://aniversarioperu.files.wordpress.com/2013/10/socios_principales_vitalicios_activos.png?w=630" width="630" height="420" /></a> La mitad de socios tiene voto privilegiado, cada voto vale de 3 a 5 veces que los votos de la otra mitad. Es curioso que además se lleven la mayor tajada de las regalías recaudadas por APDAYC.[/caption]
<h1>[Actualización 7 Oct 2013]</h1>
<h2>Pero qué porcentaje de TODAS las regalías recibe este grupo de socios?</h2>
<a href="http://www.scribd.com/doc/135740127/Memoria-Apdayc-2012">En la Memoria de APDAYC del 2012, señalan en la página 12</a> (o página 22 en
realidad), que se repartieron 29 millones de soles entre todos sus asociados.

Según el <a href="http://bit.ly/18HEiF5">útero de marita</a> <strong>"APDAYC tiene más de 8 mil afiliados, pero sólo 248 tienen derecho a voto en la Asamblea General"</strong>.

Supongamos que APDAYC tiene 8 mil socios, entonces entre ellos repartieron 29 millones de soles durante el 2012.

Quiero saber:
<ul>
	<li>Qué porcentaje de estos 8mil son los socios con votos privilegiados (principales, vitalicios y activos).</li>
	<li>Qué porcentaje del dinero total se llevan estos socios con voto privilegiado?</li>
</ul>
Estos son los datos:
<ul>
	<li>Dinero total: 29,197,272 Soles</li>
	<li>Número total de socios: 8000</li>
	<li>Total socios con voto privilegiado: 138</li>
	<li>Dinero recibido por socios principales: 1240,041.19</li>
	<li>Dinero recibido por socios vitalicios: 59,347.69</li>
	<li>Dinero recibido por socios activos: 5731,717.18</li>
	<li>Porcentaje de socios con voto privilegiado: 1.7%</li>
	<li>Porcentaje del dinero que se recibe este grupo: 24.08%</li>
</ul>
Y este es el gráfico resultante:

[caption id="attachment_172" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/socios_pva_versus_total1.png"><img class="size-large wp-image-172" alt="Porcentaje de ganancias de socios con voto privilegiado" src="http://aniversarioperu.files.wordpress.com/2013/10/socios_pva_versus_total1.png?w=630" width="630" height="518" /></a> Porcentaje de ganancias de socios con voto privilegiado, APDAYC 2012[/caption]

Pues <strong>es de esperarse que el 1.7% de socios se lleve la cuarta parte de las regalías</strong>. Si vemos otra vez el gráfico de los socios más rendidores, los que más plata reciben, veremos que <strong>son los socios principales y activos</strong> (con voto multiplicado por 5 y por 3) quienes reciben más regalías.

[caption id="attachment_178" align="aligncenter" width="630"]<a href="http://aniversarioperu.files.wordpress.com/2013/10/mas_productivos_apdayc_4.png"><img class="size-large wp-image-178" alt="Los socios principales y activos son los que más regalías cobraron durante el 2012." src="http://aniversarioperu.files.wordpress.com/2013/10/mas_productivos_apdayc_4.png?w=630" width="630" height="290" /></a> Los socios principales y activos son los que más regalías cobraron durante el 2012.[/caption]
<h1>Sección para geeks</h1>
Aqui el código en la consola de Linux:

[code language="bash" light="true"]
# convertir pdf a texto y extraer nombres y ganancias
cat mas_productivos_2012.txt | sed 's/S\/\.//g' | sed 's/\$//g' | sed 's/\s\+/ /g' | sed -r 's/([A-Z]),/\1/g' | sed 's/,//g' | sed -r 's/(([A-Z]+\s)+)/\1,/g' | sed 's/ ,/,/g' | sed -r 's/^[0-9]+\s[0-9]+\s//g' | sed -r 's/\s*$//g' > tmp_mas_productivos.txt

# dibujar el gráfico usando Python y matplotlib
python mas_productivos.py
[/code]

Y aqui el código <strong>actualizado</strong> en el lenguage Python:

[code language="python"]
# -*- coding: utf-8 -*-
import codecs
import locale
import prettyplotlib as ppl
import numpy as np
from prettyplotlib import plt

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

f = codecs.open("output/tmp_socios_principales.txt", encoding="utf-8")
data = f.read()
f.close()

# Esta es la lista de "Socios principales"
data = data.split("\n")
principales = []
vitalicios = []
activos = []
for line in data:
    line = line.strip()
    if len(line) > 0:
        line = line.split(",")
        if line[1] == "PRINCIPAL":
            principales.append(line[0])
        if line[1] == "VITALICIO":
            vitalicios.append(line[0])
        if line[1] == "ACTIVO":
            activos.append(line[0])

# cantidad de regalias por "socios principales"
f = codecs.open("output/tmp_mas_productivos.txt", encoding="utf-8")
data = f.read()
f.close()

data = data.split("\n")
princi_money = float()
vitali_money = float()
activo_money = float()
otros_money = float()

for i in data:
    if len(i) > 0:
        i = i.split(",")
        author = i[0]
        money = i[1].split(" ")
        money = money[len(money)-1]
        if author in principales:
            princi_money += float(money)
        elif author in vitalicios:
            vitali_money += float(money)
        elif author in activos:
            activo_money += float(money)
        else:
            otros_money += float(money)

## DO principales + vitalicios
## numero de socios por categoria
numero_socios = [str(len(principales) + len(vitalicios)),
                 str(250-len(principales)-len(vitalicios))]

print "Socios privilegiados con el voto " + str(len(principales) +
        len(vitalicios) + len(activos))

y = [princi_money + vitali_money, activo_money + otros_money]
annotate = [locale.format("%d", y[0], grouping=True) + " S/.",
            locale.format("%d", y[1], grouping=True) + " S/."]

width = 0.35
bar_color = ["r", "#66c2a5"]
plt.rc('font', **{'family': 'DejaVu Sans'})
fig, ax = plt.subplots(1, figsize=(8,6))
ind = np.arange(2)
xdata = ind + 0.05 + width
ax.bar(ind, y)
ax.set_xticks(ind + 0.4)
ax.set_xticklabels(["principales y vitalicios\n(" + numero_socios[0] + " socios)",
                    "otros socios\n(" + numero_socios[1] + " socios)",
                    ],
                    rotation="horizontal", multialignment="center")
ax.autoscale()
ax.set_title(u'Ganancias de socios principales y vitalicios\n comparados con el resto de socios',
        fontdict = {'fontsize':22}
        )

y_labels = ["0", "1,000,000", "2,000,000", "3,000,000", "4,000,000",
                "5,000,000", "6,000,000", "7,000,000", "8,000,000"]
ax.set_yticklabels(y_labels)

plt.ylabel(u'Regalías en S/.', fontdict={'fontsize':18})
plt.xlabel(u'Beneficiarios', fontdict={'fontsize':22})

ppl.bar(ax, np.arange(len(y)), y, grid="y", annotate=annotate, color=bar_color)
fig.tight_layout()
fig.savefig("output/socios_principales.png")
output = "Plot de socios Principales + Vitalicios guardados en archivo "
output += "``output/socios_principales.png``\n"
print output

## DO principales + vitalicios + activos
## numero de socios por categoria
numero_socios = [str(len(principales) + len(vitalicios) + len(activos)),
                 str(250-len(principales) - len(vitalicios) - len(activos))]

# Porcentaje de socios principales+vitalicios+activos versus otros
percent_pva = float((len(principales)+len(vitalicios)+len(activos))*100/250)
percent_socios_otros = 100.0 - percent_pva

# Porcentaje de DINERO de socios principales+vitalicios+activos versus otros
y = [princi_money + vitali_money + activo_money, otros_money]
percent_money_pva = int(float(princi_money + vitali_money + activo_money)*100/(y[0] + y[1]))
percent_money_otros = 100 - percent_money_pva

annotate = [locale.format("%d", y[0], grouping=True) +
                " S/.",
            locale.format("%d", y[1], grouping=True) +
                " S/."]

width = 0.35
bar_color = ["r", "#0099FF"]
plt.rc('font', **{'family': 'DejaVu Sans'})
fig, ax = plt.subplots(1, figsize=(9,6))
ind = np.arange(2)
xdata = ind + 0.05 + width

# write percentaje of money to plot
ax.annotate(str(percent_money_pva) +"%\ndel dinero", ha="center", color="w",
        size=38, xy=(0.2,1.2), xytext=(0.4, 2500000))
ax.annotate(str(percent_money_otros) +"%\ndel dinero", ha="center", color="w",
        size=18, xy=(0.2,1.2), xytext=(1.4, 150000))

ax.bar(ind, y)
ax.set_xticks(ind + 0.4)
ax.set_xticklabels(["principales, vitalicios y activos\n(" +
                            str(int(percent_pva)) + "% del total)",
                    "otros socios\n(" +
                            str(int(percent_socios_otros)) + "% del total)"
                    ],
                    rotation="horizontal", multialignment="center")
ax.autoscale()
ax.set_title(u'Ganancias de socios principales, vitalicios y activos'
        + '\ncomparados con el resto de socios',
        fontdict = {'fontsize':22}
        )

y_labels = ["0", "1,000,000", "2,000,000", "3,000,000", "4,000,000",
                "5,000,000", "6,000,000", "7,000,000", "8,000,000"]
ax.set_yticklabels(y_labels)

plt.ylabel(u'Regalías en S/.', fontdict={'fontsize':18})
plt.xlabel(u'Beneficiarios', fontdict={'fontsize':22})

ppl.bar(ax, np.arange(len(y)), y, annotate=annotate, color=bar_color)
fig.tight_layout()
fig.savefig("output/socios_principales_vitalicios_activos.png")
output = "Plot de socios Principales + Vitalicios + Activos guardados en archivo "
output += "``output/socios_principales_vitalicios_activos.png``\n"
print output
[/code]

Código de cuáles miembros del consejo directivo se llevan más regalías

https://gist.github.com/aniversarioperu/6891888

<h3>Aquí el código y datos para generar el pie-chart</h3>
https://gist.github.com/aniversarioperu/6863753

Y aquí el código necesario para hacer el plot usando el <a href="http://www.r-project.org/">paquete estadístico R</a>.

[code language="r"]
library(ggplot2)
datos <- read.csv("output/socios_pva_versus_total.csv", sep=",",
              header=FALSE)
money <- datos[3:4,]
names(money) <- c("Socios","Regalías")

png(filename="output/socios_pva_versus_total.png",
      width=950, height=630, units="px")
ggplot(money, aes(x="", y=Regalías, fill=Socios)) +
  theme(text = element_text(size=22)) +
  geom_bar(width=1, stat="identity") +
  coord_polar("y", start=pi/3) +
  labs(title="Repartición de regalías, APDAYC 2012")
dev.off()
[/code]
