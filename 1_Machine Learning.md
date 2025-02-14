***Explique com suas palavras qual seria o impacto de um dataset desbalanceado em um modelo de classificação e proponha uma solução para mitigar esse problema.***


O modelo tende a aprender a prever a classe mais comum, já que ela aparecerá com mais frequência, consequentemente prejudicando a classe minoritária.

Com um dataset de treino desbalanceado, o dataset de teste também estará desbalanceado, o que faz com que as medidas de acurácia sejam altas, porém o modelo em produção pode não performar com o mesmo percentual.

Alternativas:

    Balancear o dataset.
    Algoritmos específicos para desbalanceamento: