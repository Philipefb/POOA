Nomes: Philipe Fonseca Bittencourt, Victoria Martini de Souza, Guilherme Lorençato Guimarães Lamonato


#  1 - Trabalho 2 - Princípio do Aberto-Fechado
O segundo trabalho teve como seu objetivo construir uma ferramente que encontre e baixe os títulos das notícias diárias dos principais portais de notícias(G1, UOL, etc) e também seguir os princípios SOLID:

- Princípio aberto-fechado
- Princípio da responsabilidade única


# 2 - Configuração

Para a utilização são necessários a instalação da linguagem Python e do gerenciador de pacotes pip:

- [Python](https://www.python.org/downloads/)
- [Pip](https://pip.pypa.io/en/stable/installation/)

Também é necessário o download das bibliotecas Beautiful Soup 4 e Pandas

```
$ pip install bs4
$ pip install pandas
``` 

Para executar o programa é necessário apenas:

`$ python3 main.py`

# 3 - Extensões previstas no nosso projeto

Para esse projeto pensamos em uma estratégia a fim de garantir a funcionalidade do código mesmo com futuras alterações
e/ou extensões e previnir que as mudanças feitas em um módulo de propague para outros. Nesse caso nossa função newsGeneric()
recebe como paramentro a url do site de noticia desejado e um array com as classes para pesquisa. Dessa forma é possível que a função seja feita para diferentes sites de notícias, mudando apenas os parametros desejados, a url e o array com as classes, construímos assim um módulo aberto para extensão.

Pensando na facilidade para o usuário e melhor funcionalidade do código, um exemplo válido de extensão que poderia ser aplicado no nosso projeto
seria aplicar um algoritmo de aprendizado de máquina para detectar tendências de notícias, verificar repetição de no minímo três vezes e arquivar em um array de tendencias, e também captar as diferenças entre os sites. 

