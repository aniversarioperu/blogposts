Como ya saben, [@verita_pe](https://twitter.com/verita_pe) está realizando
buenos destapes respecto al pasado turbio de algunos candidatos:

* [1400 candidatos en todo el Perú tienen sentencias penales y civiles](http://utero.pe/2014/07/17/1400-candidatos-en-todo-el-peru-tienen-sentencias-penales-y-civiles/)

Este trabajo está siendo realizado por el equipo de la Asociación
Civil Transparencia con el equipo
del Útero de Marita. Yo estoy ayudando un poquito. 

Los datos de las hojas de vida están colgadas en el servidor del Jurado
Nacional de Elecciones. El servidor es muy lento y el buscador que tienen no es
muy amigable o fácil de usar y a veces se cuelga.

Por lo tanto, para hacer una búsqueda rápida y eficiente de la información es
necesario descargar TODOS los datos, guardarlos en el disco duro de tu
computadora y meterlos a una base de datos para generar gráficos y
estadísticas.

Si trabajas en una redacción periodística y te interesa descargar TODAS las
hojas de vida de los candidatos, has llegado al post indicado.
Apúrate y contáctate con el hacker más cercano para que te ayude a seguir las
siguientes instrucciones:

## Manual para descargar las hojas de vida de manera automática
Luego de patalear un rato y soltar unas cuantas lisuras he podido escribir un
pequeño y simple software que te ayudará a descargar y extraer rapidito la
información de la hoja de vida de cada candidato.

A manera de ejemplo explicaré el procedimiento para descargar los datos de
Susana Villarán.

Aquí está el software
[gist:216b1a35946529b0ed13](https://gist.github.com/aniversarioperu/216b1a35946529b0ed13).

Y hay que notar varias cosas importantes:

* Necesitas instalar el lenguaje Python y la librería selenium.
* Necesitas tener el navegador Firefox.
* El JNE ha asignado un identificador único a cada candidato.  Este id corresponde un número consecutivo que va del 1 al 116721.
* A Susana Villarán le corresponde el número 104272. Mi software usa este valor
para construir el URL de la hoja de vida de S. Villarán, descargar la página
HTML y extraer los datos. Este es el URL para nuestro ejemplo
<http://200.48.102.67/pecaoe/sipe/HojaVida.htm?c=104272&p=72&op=140>
* Amigo periodista, debes decir a tu hacker que haga un loop que vaya del 1 al
116721 y vaya reemplazando donde corresponde en el URL mencionado. Dile nomás, el hacker entenderá
lo que tiene que hacer.
* Durante cada ciclo de este loop deberá correr el script el cual extraerá los
datos de interés.

Aquí está el resultado de correr el script sobre el URL de Susana Villarán.

    {
        "fecha_nacimiento": "16/08/1949", 
        "apellido_paterno": "VILLARAN", 
        "apellido_materno": "DE LA PUENTE", 
        "lugar_provincia_residencia": "LIMA", 
        "nombres": "SUSANA MARIA DEL CARMEN", 
        "dni": "08051943", 
        "lugar_departamento_residencia": "LIMA", 
        "cargo_postula": "ALCALDE PROVINCIAL", 
        "lugar_tiempo_residencia": "63 A\u00d1OS", 
        "correo_electronico": "SUSANAVILLARAN2014@GMAIL.COM", 
        "lugar_distrito_residencia": "SAN MIGUEL", 
        "lugar_residencia": "CALLE BERTOLOTTO 111 DPTO. 711", 
        "lugar_postula": "LIMA - LIMA -"
    } 

Cada ítem de información corresponde al HTML tag que ha usado el JNE en la
página de las hojas de vida. Para **fecha de nacimiento** están usando este
tag: ``txtFechaNacimiento``.

Si ves mi script encontrarás que estoy extrayendo esa pieza de información con
el siguiente código:

    content = browser.find_element_by_xpath('//span[@id="txtFechaNacimiento"]')
    obj['fecha_nacimiento'] = content.text

Para obtener su email he usado este código:

    content = browser.find_element_by_xpath('//span[@id="txtCorreoElectronico"]')
    obj['correo_electronico'] = content.text

Fácil no?

Amigo periodista, debes decir a tu hacker que busque los **id**  de las piezas
de información que te interesan para que puedan ser extraídas. Esos ids se ven
en el código fuente HTML de la página de hoja de vida.
Una vez que haya
ingresado todo el código necesario en mi script, podrá correr el loop y luego
de un rato habrá podido descargar todas las hojas de vida de nuestros queridos
candidatos.

Como ves, son más de 100 mil candidatos en total. Necesitamos que grupos
periodísticos, sociedad civil y ciudadanos de a pie (y de a bicicleta) se unan
para fiscalizar a los candidatos y así poder elegir mejores autoridades.
