Este proyecto ha sido realizado por Pablo Vázquez Zambrano con el fin de cumplimentar un proyecto que ha sido requerido para la asignatura de Inteligencia Artificial, 
del Departamento de Ciencias de la Computación e Inteligencia Artificial de la Escuela Técnica Superior de Ingeniería Informática (ETSII) 
de la Universidad de Sevilla.

El proyecto consiste en proponer diferentes opciones de configuración a un circuito reconfigurable con el fin de que se comporte como si no tuviera ni un fallo interno.

El proyecto se divide en 4 archivos principales:
	- AG.py donde se han implementado los métodos del algoritmo genético.
	- Puerta.py, que define la clase Python Puerta(), de lo que se compondrán los circuitos.
	- Circuito.py donde, tal y como su nombre indica, se definen las tareas básicas con respecto a los circuitos 
	(como por ejemplo el calcular la salida dada una entrada).
	- Main.py, donde se ejecuta el algoritmo y se realizan las pruebas.

Para ejecutar el programa, bastará con lanzar el archivo main.py y este creará un circuito aleatorio que se diagnosticará y si se detecta algún fallo en el mismo
lanzará el proceso del algoritmo genético para buscar una solución. Las filas y columnas que queremos que tenga el circuito deseado se pueden modificar en la clase 
Circuito.py, además de las puertas de este que vayamos a considerar que están defectuosas, las cuales tienen que estar dentro del rango [0][0] y [filas-1][columnas-1].
Las puertas defectuosas las tendremos que señalar también dentro del método evaluar_individuo del archivo AG.py, las cuales deben de ser las mismas posiciones 
que las anteriores. Además, dentro del método mainAG del archivo AG.py podremos modificar los parámetros referidos al algoritmo genético, como son los números
de generaciones o la cantidad de población inicial.