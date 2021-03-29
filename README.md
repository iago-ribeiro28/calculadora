# Calculadora

Esse projeto foi criado para melhorar meus conhecimentos no Python.
Aqui irei expor a algumas funcionalidades da calculadora e mostrar o que eu aprendi durante o processo de criação dela

O repertório em questão se trata de uma calculadora, que foi criada usando o módulo PySimpleGUI.


## Layout

![layout da calculadora](https://github.com/iago-ribeiro28/calculadora/blob/master/layout.jpeg)

## Funcionalidades

Além dos botões de cada número a calculadora conta com os botões de somar, subtrair, multiplicar, dividir e igual, 
também contém o botão ponto, para colocar em números decimáis, dois botões de apagar, um que apaga todos 
os dados da calculadora e outro para apagar o último número inserido. 
Ela também tem a funcionalidade de trocar o sinal da operação.

## O que eu aprendi durante a criação

Nota:
Para modelo inicial usei a calculadora criada pelo Israel Dryer.
Se vc deseja ver o projeto dele, pode acessar usando o seguinte link:
https://github.com/israel-dryer/PyDataMath-II

Para melhor explicar o processo de criação irei dividir em três partes:
 - Layout
 - Refatoração
 - Funções

### Layout

Para começar eu decidi mudar os temas para se adequar ao meu gosto.
Também adicinei um novo botão, o de mudar o sinal '+/-', com isso diminui o tamanho do botão do sinal de igual.

Aqui aprendi a mexer de forma melhor na criação de layout e a criar uma janela nova com o  PySimpleGUI.

### Refatoração

Para tornar o código mais legível, decidi criar 3 novos arquivos, uma para colocar as variáveis, 
para colocar o Layout e outra para colocar as funções da calculadora, deixando o loop principal no
arquivo original.
Também adicionei legendas para explicar o que cada parte da variável é responsável e o que cada função faz. 

### Funções

Ao usar o modelo inicial da calculadora percebi alguns bugs,
Então me concentrei em arrumá-los.

O primeiro bug encontrado foi o uso do botão 'Ce'.
Ao usar esse botão, se espera que somente o último número fosse apagado,
porém não era o que acontecia, então o modifiquei, criando uma nova função
para que somente o último dígito fosse apagado.

O segundo bug arrumado, foi pelo uso do '%'.
Ao usa-lo em uma calculadora normal, espera-se que o número colocado seja dividido por 100,
e logo após estar pronto para o usuário escrever o dígito que deseja para ser multiplicado, 
porém não era isso que acontecia.
Então eu criei uma nova função para que isso aconteça.

O terceiro bug, foi na hora de fazer uma conta com 3 números ou mais, onde o algorítmo não salvava mais que dois números,
então quando se colocava o terceiro ele apagava o priméiro. Eu corrigi esse bug para que fosse possível realizar várias 
operações em sequência.

Para adicionar o botão '+/-', foi necessário criar uma nova função e uma variável para ela. 

Essas foram as principais modificações feitas no código.
