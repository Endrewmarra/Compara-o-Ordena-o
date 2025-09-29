# Comparando metodos de ordenação
Código onde aplico, testo e comparo velocidade e eficiencia de metodos de ordenação que aprendo.
Uso uma biblioteca Random para gerar listas aleatorias de numeros, copio a lista original para cada um dos metodos que eu pretendo usar, defino o metodo por meio de funções.
A função com o metodo de ordenação recebe uma lista (copia da lista original), inicia um timer utilizando a biblioteca TIME, apos o timer segue o algoritimo de ordenação em questão, e por fim a parada do timer, e assim a função retorna tanto a lista ordenada, quanto o tempo que levou para concluir o processo.
O programa recebe uma entrada com o tamanho desejado a se gerar a lista, e em seguida se deseja que a lista seja embaralhada ou não, após esta escolha o programa começa a ordenação um metodo por vez, e mostra o tempo levado para cada um dos metodos.
Para fins de comparação o programa tambem roda o tim sort nativo do python atraves de .sort, e apresenta o tempo deste metodo nativo junto com os demais.
