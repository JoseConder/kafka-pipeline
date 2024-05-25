Hola esta es el repo del final de De lira

Consta de 3 archivos principales: el producer, el consumer y el docker-compose

#PRODUCER
  El producer.py es el archivo que jala info de las api, por el momento solo de la api de Marvel y se la pasa a kafka como un topico.

#CONSUMER
  El consumer.py es el archivo que jala info de los topicos de kafka y los mete a la base de datos de mongodb, en este en especifico para lo de marvel, formatea los datos para conseguir el nombre del personaje y los numeros de comics y series para este.

#COMPOSE
  Despues tenemos el docker-compose, este archivo lo corren en el cmd o en la linea de comandos como un comando de docker, tienen que estar en la carpeta donde se encuentra el archivo y usar:
    docker compose -f <nombredelarchivo> up
  eso les crea el contenedor con el kafka y zookeeper, tienen que dejar esa consola abierta para que funcionen, si necesitan hacer otra cosa abrir otra consola

Principalmente eso es lo que vamos a usar, tenemos que prender el kafka, correr el producer y despues el consumer, el producer cada 60s(lo podemos cambiar) va a mandar topicos a kafka y el consumer cada vez que pueda va a insertar los topicos en la base de datos
por el momento no esta configurada para que no se repitan documentos(hay que ponerlo).

Despues tenemos el visualizer, el cual lee los docs de mongo y grafica en base a ellos, de aqui tengo duda porque en el esquema de la tarea dice que el consumer manda a la base y grafica asi que no se si este bien graficar desde la base.

Los demas archivos son extras, ya sea para borrar la base de datos facilmente, purgar los topicos de kafka o checar cuantos topicos hay en este.
