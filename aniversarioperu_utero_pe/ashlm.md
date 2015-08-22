# El leak de Ashley Madison
Los hackers responsables de robarse toda la lista de usuarios de la Web para
aventuras amorosas han publicado casi 10 gigabytes de información en un
torrent que se puede encontrar en [PirateBay](https://thepiratebay.mn/torrent/12237184/The_Complete_Ashley_Madison_Dump_from_the_Impact_Team).

![](images/2015-08-25_tpb1.png)

Hace unos días me fijé y habían 6 mil personas compartiendo los archivos
(*seeders*) y más de 5 mil personas descargándolos (*leechers*).

![](images/2015-08-22_ashley_maddison_01.png)

Decidí descargarme los datos para ver si mi email estaba registrado como
usuario de Ashley Madison.

Luego de descargarlos me di cuenta que los archivos estaban comprimidos. Estos
son los archivos .dump.gz que se descomprimen con esta herramienta de Linux:

> gunzip archivo.dump.gz

Para leer los archivos es mejor guardar los en una base de datos MySQL lo cual
se puede hacer fácilmente con este otro comando:

> mysql ashley -uuser -ppassword < archivo.dump

Luego de esperar un largo rato tendrás todo listo para hacer búsquedas de
emails. Me busqué usando el comando ``select`` pero no me encontré:

![](images/2015-08-22_ashley_maddison_02.png)

Me puse a buscar el email de mi vecino tramposín y oh! sorpresa allí estaba.

Por curiosidad busqué cuantos correos válidos de dominio **.PE** existen en el
leak. Hay 908 email confirmados.

![](images/2015-08-22_ashley_maddison_03.png)

Hay emails de universidades peruanas, institutos peruanos, escritores peruanos,
    ingenieros peruanos, defensores de Nadine, haters de Nadine, etc.


Sin mucho esfuerzo, también es posible cruzar una lista de emails con la base
de datos y ver cuáles emails de la lista han sido clientes de Ashley Madison.

Un archivo que tenga una lista que sea así:

email1@gmail.com
email2@yahoo.com
email3@hotmail.com
etc
etc

se puede cruzar con la ayuda de un pequeño script en Python:

>>>>>>>>> codigo
import sys

import dataset


filename = sys.argv[1].strip()

db = dataset.connect('mysql://user:password@localhost/ashley')
table = db['aminno_member_email']

with open(filename, 'r') as handle:
    for line in handle:
        line = line.strip()
        res = table.find_one(email=line)
        if res:
            print(res, res['pnum'])


>>>>>>>>> codigo

Solo basta correrlo con el comando:

> python search_emails.py email_lista.txt

## Casos preocupantes
Entre estos correos peruanos (confirmaods) 
hay 7 que son del dominio **.GOB.PE**. Esto significa que empleados públicos
usaron cuentas
que les dio el Estado para entrar a este sitio web de trampeo.

![](images/2015-08-22_ashley_maddison_04.png)

Hay 3 emails que son del dominio **.MIL.PE**. Esos son emails de militares?
Ya peeeee.

![](images/2015-08-22_ashley_maddison_05.png)

Esto no es mal uso de recursos del Estado? Se supone que para estas cosas
privadas deben usar su correo personal en Gmail u otro no?

## El leak también incluye IPs
Además de coordenadas geográficas. Los administradores de Ashley Madison
guardaban las direcciones IP y ubicación geográfica desde el aparato que usaban
sus usuarios para conectarse al servicio.

Estos datos geográficos son los que permitieron a [Associate Press ubicar](http://bigstory.ap.org/article/065953e72e9649e0bc6efb69b06295ed/evidence-infidelities-spreads-online-wake-hack) 
congresistas y cientos de empleados públicos de EEUU que usaron computadoras
estatales para acceder a sus cuentas de Ashley Madison.

## También incluye transacciones de tarjetas de crédito
Cualquier investigación fiscal o periodística puede acceder a las transacciones
de tarjetas de crédito liberadas en el leak y darse cuenta si los emails
encontrados en la base de datos son verdaderos o no.

Estos hackers son terribles.

## Ay pero una cuenta de email no cuesta nada
Esto no es cierto y Google tiene la culpa de la ilusión que no cuesta crear y
mantener cuentas de email.

Los hackeos pasados a los emails oficiales de los ministros peruanos han puesto en
evidencia una cosa:

El Estado peruano tiene sus propios servidores de cuentas de email. Y hacer
esto es bien caro. Tienes que tener:

* servidores
* discos duros para almacenar email
* sistema redundante del tipo RAID
* copias de seguridad
* software especializado front-end, back-end
* balance loaders para distribuir la carga entre varios servidores
* software bayesiando anti-spam
* personal técnico que dé mantenimiento y maneje todo este sistema.

lo más dificil debe ser manejar el software para el servicio de email. No es
cuestion de instalar un programa y ya. Hay que instalar, configurar y mantener
numerosos softwares que deben funcionar en una delicada sincronización.

Además los ingenieros de sistemas que manejan estos servidores en el Estado
ganan entre 7mil y 10mil soles al mes. No cobran con canje.
http://www.devida.gob.pe/wp-content/uploads/2015/07/Convocatoria-CAS-N-181-Bases-de-Perfil.pdf
Me parece bien que tengan buen sueldo. Pero el gasto en personal que mantenga
los sistemas informaticos no es un ripio.

Es posible además que todo este hardware + software + entrenamiento haya sido
vendido como un paquete completo al Estado por parte de IBM, o Microsoft.
Como tú comprenderás, ellos no cobran barato. Por ejemplo, según el protal de
Transparencia del Ministerio de Economía, el Estado peruano le paga cada año a
IBM entre 4 y 64 millones de soles por hardware y software. Claro que no todo
se gasta en mantener el sistema de emails, pero al menos una parte de tantos
millones debe servir para eso.

![](images/2015-08-20_ibm.png)



