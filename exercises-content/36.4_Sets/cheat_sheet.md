set.isdisjoint(other) : retorna True se o set não tem nenhum elemento em comum com other , ou seja, se a intersecção é vazia;

set.issubset(other) : verifica se set é um subconjunto de other , ou seja, se todo elemento de set está em other ;

set.issuperset(other): verifica se set é um superconjunto de other , ou seja, se todos os elementos de other estão em set . A diferença de um superconjunto e de um subconjunto é que no superconjunto podem haver outros elementos, além dos elementos de other já presentes dentro de set . Já no subconjunto não;
set == other: verifica se os conjuntos são iguais, ou seja, se todos os elementos de set estão em other e se todos os elementos de other estão em set . Lembre-se que a ordem não importa. Não existe função dedicada para a comparação de igualdade.
Os métodos a seguir operam sobre dois ou mais conjuntos por vez. Cada uma das operações nessa seção tem a sua versão que modifica o set original com o resultado da operação e não retorna nada.

set.union(others): retorna a união entre o set e todos os other passados;

set.intersection(others): retorna a intersecção entre set e todos os other passados;

set.difference(others): retorna a diferença entre set e todos os other passados;

set.symmetric_difference(others): retorna todos os elementos que estejam em um mas não estejam no outro conjunto (opera apenas sobre dois conjuntos).