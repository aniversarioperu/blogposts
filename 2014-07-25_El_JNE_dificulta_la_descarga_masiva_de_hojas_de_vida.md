# El JNE nos dificulta la descarga masiva de las Hojas de Vida de los candidatos

En un post anterior detallé el procedimiento para descargar masivamente las Hojas de
Vida de los candidatos a las elecciones Municipales y Regionales 2014. Expliqué
que se podía hacer la descarga usando un script muy simple.

Bueno, en el transcurso de los últimos días, **el JNE ha modificado el software de
su servidor** y si antes podías visitar la hoja de vida de Susana Villarán con este
link
<http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c=104272&p=72&op=140>. Ahora
te encontrarás con este mensaje:

![](images/2014-07-25_no_existe.jpg)

Mi script usaba direcciones similares a esa para descargar las hojas de vida.
Pero la actualización del software del servidor del JNE ha logrando anular mi script.

Antes la dirección URL de cada hoja de vida incluía un identificador único
para cada candidato (ejemplo **104272** para Susana Villarán):

> http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c=**104272**&p=72&op=140

Gracias a los cambios del software, ahora la dirección es así:

> http://200.48.102.67/pecaoe/sipe/HojaVida.aspx?cod=**84In9z7iqnJG7%2F9q%2Fk6uoQ%3D%3D%0A**

Claro que ese texto está codificado para URL, si lo decodificamos nos da esto:

> http://200.48.102.67/pecaoe/sipe/HojaVida.aspx?cod=**84In9z7iqnJG7/9q/k6uoQ==**

Como ven, la dirección URL ha sido encriptada usando algún tipo de algoritmo
que no he podido identificar. Ahora están usando una serie de letras y números
a manera de código para
cada candidato (variable **cod=**). Pensé que estaban usando Base64 pero no.
Sospecho
que están usando algún método aleatorio para reemplazar el URL por esta cadena
de números, letras y símbolos. Como dirían los hackers, **le han echado sal a su
algoritmo** (ver [*sal en
        criptografía*](http://es.wikipedia.org/wiki/Sal_(criptograf%C3%ADa))).

Entonces, ahora cada candidato tiene un código único que está encriptado. Antes
se podía hacer un loop de números del 1 al 116 mil para poder descargar las
hojas de vida. Ahora hay que saber de antemano el código encriptado para cada
candidato. Eso o adivinar qué algoritmo y/o sal han usado para ofuscar el URL. 

Será que el JNE leyó mi post anterior?

Antes de la modificación al software era fácil emular un Web Browser usando la
librería Selenium. Te podías bajar de un cocacho, de un tirón, todos los datos
para cada candidato: Nombre, Apellido, Foto, Lugar Nacimiento, Email, Estudios,
     Sentencias, Ingresos, etc.
Ya no es posible gracias a la reciente modificación al software del JNE.

Pero! no todo está perdido. Tal como lo mencionó el amixer [\@royriojas](https://twitter.com/royriojas) en un
comentario a mi post anterior, es posible utilizar JavaScript descargarse la
info.
Esto es posible pero un poco más tedioso. Antes el script hacía un pedido al
servidor del JNE por cada candidato. Ahora hay que hacer, por cada candidato,
         que el script realice 18 pedidos al servidor del JNE. Cada pedido te
         regresará una fracción de los datos de cada candidato.

Se requiere un pedido para obtener el nombre, otro para la foto, otro para los bienes, etc,
   etc.
Además cada pedido debe ir acompañado de parámetros similares a estos:

> {"objOPInscritasBE":{"objProcesoElectoralBE":{"intIdProceso":"72"},"intCod_OP":"2182"}}

Así que amigo periodista, debes contactar a tu hacker más cercano y decirle que
ahora el asunto se ha complicado un poquito.
Ahora es necesario hacer pedidos AJAX a estas direcciones:

``
url: "../servicios/declaracion.asmx/OP_ObtenerNombrePorID"
url: "../servicios/declaracion.asmx/CandidatoListarPorID"
url: "../servicios/declaracion.asmx/CandidatoFotoListarPorID"
url: "../servicios/declaracion.asmx/CandidatoFamiliaListarPorCandidato"
url: "../servicios/declaracion.asmx/CandidatoExperienciaListarPorCandidato"
url: "../servicios/declaracion.asmx/EducacionBasicaListarPorCandidato"
url: "../servicios/declaracion.asmx/EducacionSuperiorListarPorCandidato"
url: "../servicios/declaracion.asmx/CargoPartidarioListarPorCandidato"
url: "../servicios/declaracion.asmx/CargoEleccionListarPorCandidato"
url: "../servicios/declaracion.asmx/RenunciasOPListarPorCandidato"
url: "../servicios/declaracion.asmx/AmbitoPenalListarPorCandidato"
url: "../servicios/declaracion.asmx/AmbitoCivilListarPorCandidato"
url: "../servicios/declaracion.asmx/CandidatoAdicionalListarPorCandidato"
url: "../servicios/declaracion.asmx/IngresoListarPorCandidato"
url: "../servicios/declaracion.asmx/BienesListarPorCandidato"
url: "../servicios/declaracion.asmx/EgresosListarPorCandidato"
url: "../servicios/simulador.asmx/Soporte_CandidatoAnotMarginal"
url: "../servicios/declaracion.asmx/ObtenerRutaFotoDNI"
``

Señores del JNE no sé si leen este blog. Si lo hacen, les dejo saluditos :-)



