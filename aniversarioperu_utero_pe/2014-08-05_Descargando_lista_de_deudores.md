# Manual para descargar la lista de deudores al Estado

![](images/2014_08_05_jne.jpg)
Fuente [La República](http://www.larepublica.pe/14-07-2014/revisar-mas-de-cien-mil-hojas-de-vida-es-materialmente-imposible)

Me pasaron esa entrevista al jefe del Jurado Nacional de Elecciones donde dice
que es **materialmente imposible** revisar las hojas de vidas de 100 mil
candidatos a las próximas elecciones regionales y municipales.

Pero, pero, pero **no es eso lo que hemos estado haciendo las últimas
semanas?** en
el proyecto @verita_pe, el cual es una **colaboración de este @utero y la
Asociacion Civil Transparencia?**

Y producto de esta chamba colaborativa han salido varias pepas. Vean todas en
este link: <http://utero.pe/tag/elecciones-2014/>

Mi pata [@ErnestoCabralM](https://twitter.com/ernestocabralm) me dijo por
Facebook.

--- **Ernesto**: Oe Ani, deja de trollear en Twitter y descárgate la lista de deudores al Estado. Quiero hacer un cruce de datos con los candidatos.

--- **Aniversario**: Ya pe, pero eso va a demorar. Tendré que programar por un
rato.

La lista de deudores al Estado, incluyendo montos deben pagar, delitos, montos
que ya han pagado, etc se puede acceder usando este buscador del Ministerio de
Justicia <http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verWeb>

Si haces clic en el botón **LISTAR TODO** (mentira!) saldrán varios registros pero no todos.

Obviamente que ingresar uno por uno los nombres de los 100mil candidatos con la
esperanza de encontrar algún deudor es algo demoraría una eternidad. Por lo
tanto lo más eficiente es descargar todos los datos a una computadora local,
      correrle filtros y hacer el cruce de información con la lista de
      candidatos.

Para hacer la descarga escribí un **spider** usando la excelente herramienta
llamada Scrapy. En este enlace está el repositorio con el código fuente y las
instrucciones para usar el software: <https://github.com/aniversarioperu/scrapy_deudores>

El minjus tiene organizada la info por registros. Cada registro tiene un 
``id`` numérico que se incrementa a partir del ``1``.

Si hay un deudor con varias deudas entonces tendrá varios números ``id``. Con
el número ``id`` se puede acceder a la cartilla del deudor. Ejemplo para el
"doc" Vladimiro Montesinos:
<http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=317>
El resultado serán objetos JSON similares a este:

```json
{
    "fecha_ejecutoria": "",
    "pagos_pendientes": 1000000,
    "pagos_realizados": 0,
    "url": "http://pisaq.minjus.gob.pe:8080/sisca_web/DeudoresWebAction_verDeudorWeb.action?deudor.id=317",
    "nombres": "Vladimiro",
    "dni": "09296012",
    "monto_total": 1000000,
    "juzgado": "1er JPLT -2do SPL",
    "apellidos": "Montesinos Torres",
    "solidaria": "SI",
    "entidad_agraviada": "",
    "intereses": 0,
    "delito": "Defraudación Tributaria, Ocultamiento de Ingresos, Utilización de Gastos no Reales y Crédito Fiscal Inexistente",
    "reparacion_civil": 1000000,
    "fecha_sentencia": "13/05/2010",
    "domicilio": "Calle Castro Iglesias 141 Urb. Aurora. Miraflores - Lima",
    "expediente": "13-2003 -41-2004"
}
```

## Alternativa
Si estás apurado y no tienes tiempo de instalar y correr el programa. No te
preocupes que nosotros ya hicimos la descarga y hemos colgada TODA la info en
la web. Puedes acceder al archivo en [este
link](https://raw.githubusercontent.com/aniversarioperu/scrapy_deudores/master/deudor.json).
Ojo que el archivo pesa 4Mb (es que son más de 7mil deudores!) y está en formato JSON. Este archivo puede ser
inmediatamente importado a OpenRefine y convertido a otros formatos(CSV, Excel,
        etc).
