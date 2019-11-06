# Algoritmos de ordenamiento

## Burbuja

La idea detrás del algoritmo de clasificación de burbujas es muy simple. Dada una lista desordenada, 
se comparan los elementos adyacentes en la lista y, después de cada comparación, colóquelos a la derecha 
en orden de magnitud. Esto funciona intercambiando elementos adyacentes si no están en el correcto orden. 
El proceso se repite *n-1* veces para obtener una lista de *n* elementos. En cada iteración, el elemento más 
grande está dispuesto al final. Por ejemplo, en la primera iteración, el elemento más grande se colocaría en 
la última posición de la lista, y nuevamente, se seguirá el mismo proceso para los restantes elementos *n-1*. 
En la segunda iteración, el segundo elemento más grande será colocado en el penúltimo lugar de la lista, y el 
proceso se repetirá hasta que la lista se ordene.

Ejemplo:

![BubbleSort-example](https://upload.wikimedia.org/wikipedia/commons/0/06/Bubble-sort.gif)

## Quicksort

El algoritmo conocido como *quicksort* (ordenación rápida) recibe su nombre de su autor, Tony
Hoare. La idea del algoritmo es simple, se basa en la división en particiones de la lista a ordenar,
por ello se puede considerar que aplica la técnica "divide y vencerás". El método es, posiblemente,
el más pequeño de código, más rápido, más elegante y más interesante y eficiente de
los algoritmos conocidos de ordenación.

Este método se basa en dividir los *n* elementos de la lista a ordenar en dos partes o particiones
separadas por un elemento: una partición izquierda, un elemento central denominado pivote
o elemento de partición y una partición derecha. La partición o división se hace de tal forma
que todos los elementos de la primera sublista (partición izquierda) sean menores que todos
los elementos de la segunda sublista (partición derecha). Las dos sublistas se ordenan entonces
independientemente.

Para dividir la lista en particiones (sublistas) se elige uno de los elementos de la lista y se
utiliza como pivote o elemento de partición. Si se elige una lista cualquiera con los elementos
en orden aleatorio, se puede elegir cualquier elemento de la lista como pivote, por ejemplo, el
primer elemento de la lista. Si la lista tiene algún orden parcial que se conoce, se puede tomar
otra decisión para escogerlo. Idealmente, el pivote se debe elegir de modo que se divida la lista
exactamente por la mitad de acuerdo al tamaño relativo de las claves. Por ejemplo, si se tiene
una lista de enteros de 1 a 10, 5 o 6 serían pivotes ideales, mientras que 1 o 10 serían elecciones
“pobres” de pivotes.

Una vez que el pivote ha sido elegido, se utiliza para ordenar el resto de la lista en dos sublistas:
una tiene todas las claves menores que el pivote y la otra, todos los elementos (claves) mayores o iguales que el pivote (o al revés). Estas dos listas parciales se ordenan recursivamente
utilizando el mismo algoritmo; es decir, se llama sucesivamente al propio algoritmo quicksort.
La lista final ordenada se consigue concatenando la primera sublista, el pivote y la segunda lista,
en ese orden, en una única lista. La primera etapa de quicksort es la división o “particionado”
recursivo de la lista hasta que todas las sublistas constan de sólo un elemento.

Ejemplo:

![quicksort-example](https://upload.wikimedia.org/wikipedia/commons/9/9c/Quicksort-example.gif)


## Shell

La ordenación *Shell* debe el nombre a su inventor, D. L. Shell. Se suele denominar también
ordenación por inserción con incrementos decrecientes. Se considera que el método *Shell* es una
mejora del método de inserción directa.

En el algoritmo de inserción, cada elemento se compara con los elementos contiguos de su
izquierda, uno tras otro. Si el elemento a insertar es el mas pequeño, hay que realizar muchas
comparaciones antes de colocarlo en su lugar definitivo.

El algoritmo de *Shell* modifica los saltos contiguos resultantes de las comparaciones por
saltos de mayor tamaño, y con ello se consigue que la ordenación sea más rápida. Generalmente,
se toma como salto inicial n/2 (siendo n el número de elementos), y luego se reduce el salto a la
mitad en cada repetición hasta que sea de tamaño 1.

Ejemplo:

![shellsort-example](https://i.makeagif.com/media/8-25-2016/mKGEkd.gif)

Fuente:

Baka, B. (2017). Python Data Structures and Algorithms. Birmingham, Reino Unido: Packtpub.

Joyanes-Aguilar, L., & Zahonero-Martinez, I. (2008). Estructuras de datos en Java. Madrid, España: McGraw-Hill.

