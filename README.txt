Este proyecto ha sido realizado por Pablo V�zquez Zambrano con el fin de cumplimentar un proyecto que ha sido requerido para la asignatura de Inteligencia Artificial, 
del Departamento de Ciencias de la Computaci�n e Inteligencia Artificial de la Escuela T�cnica Superior de Ingenier�a Inform�tica (ETSII) 
de la Universidad de Sevilla.

El proyecto consiste en proponer diferentes opciones de configuraci�n a un circuito reconfigurable con el fin de que se comporte como si no tuviera ni un fallo interno.

El proyecto se divide en 4 archivos principales:
	- AG.py donde se han implementado los m�todos del algoritmo gen�tico.
	- Puerta.py, que define la clase Python Puerta(), de lo que se compondr�n los circuitos.
	- Circuito.py donde, tal y como su nombre indica, se definen las tareas b�sicas con respecto a los circuitos 
	(como por ejemplo el calcular la salida dada una entrada).
	- Main.py, donde se ejecuta el algoritmo y se realizan las pruebas.

Para ejecutar el programa, bastar� con lanzar el archivo main.py y este crear� un circuito aleatorio que se diagnosticar� y si se detecta alg�n fallo en el mismo
lanzar� el proceso del algoritmo gen�tico para buscar una soluci�n. Las filas y columnas que queremos que tenga el circuito deseado se pueden modificar en la clase 
Circuito.py, adem�s de las puertas de este que vayamos a considerar que est�n defectuosas, las cuales tienen que estar dentro del rango [0][0] y [filas-1][columnas-1].
Las puertas defectuosas las tendremos que se�alar tambi�n dentro del m�todo evaluar_individuo del archivo AG.py, las cuales deben de ser las mismas posiciones 
que las anteriores. Adem�s, dentro del m�todo mainAG del archivo AG.py podremos modificar los par�metros referidos al algoritmo gen�tico, como son los n�meros
de generaciones o la cantidad de poblaci�n inicial.