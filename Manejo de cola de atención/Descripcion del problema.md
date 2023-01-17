# Manejo de cola de atención
***
En una determinada oficina se planificaron los horarios de atención con anterioridad,
y debido al tema a tratar se calculó un estimado de la duración de la sesión de
atención para todas las personas que solicitaron el horario. Entrarán N
personas que serán atendidas en el orden que
pidieron la cita, y debido al tema por el que pidieron la cita se calculó previamente un
tiempo de atención tentativo por persona, y la
oficina con un tiempo máximo de atención.
Debido a que la oficina cuenta con múltiples (demasiados) puestos de atención,
podrían abrirlos todos y atender a los clientes de forma simultánea, sin embargo, se
quiere calcular el mínimo número de puestos de atención necesarios para atender a
todos los clientes sin sobrepasar el tiempo de atención T dado.
Entradas:
- N: 5 -> Número de clientes que llegarán
- T: 8 -> El tiempo máximo que tiene la oficina para atenderlos a todos.
- A: [4, 7, 8, 6, 4] -> Un arreglo A, que caracteriza cuánto tiempo toma la
atención del i-ésimo cliente.
Salida: 4
Si tenemos 4 oficinas, podemos atender a los clientes de la siguiente manera:
- El cliente 1 llega al puesto 1, su atención demora 4 unidades de tiempo.
- El cliente 2 llega al puesto 2, su atención demora 7 unidades de tiempo.
- El cliente 3 llega al puesto 3, su atención demora 8 unidades de tiempo.
- El cliente 4 llega al puesto 4, su atención demora 6 unidades de tiempo.
- El cliente 5 llega al puesto 1, su atención demora 4 unidades de tiempo, pero
debe esperar 4 más a que termine la atención del cliente 1, por lo que en
total serían 8 unidades de tiempo. El tiempo total de atención no sobrepasa 8
unidades de tiempo, y este es el mínimo que cumple con la restricción.
