# Get Log

Este repositório foi criado com o objetivo de realizar o desafio proposto no <a href="https://gist.github.com/marcoprado17/8c93cae335d81186698865a864d263ad#file-games-log-L16"> link </a>. O desafio é dividido em 4 etapas. Na primeira etapa, o desafio é capturar logs de um jogo e gerar um json com ranking de cada jogador, com total de mortes e quantidade de jogadores de cada game. Segunda etapa um ranking geral de cada jogador. Terceira etapa criar uma API para visualizar todos os games. Quarta etapa, chamada de bônus, é agrupar o motivo de cada morte em cada game. Abaixo contém os arquivos e bibliotecas utilizadas e a explicação da solução de cada problema.

- Arquivos
  - get_log.py: Neste arquivo há a solução de 3 problemas descritos nas classes abaixo.<br>
    - Task1: Nessa task foi criado um json com os dados de total de mortes, id de cada game (partida), todos os jogadores do game e um ranking. Para o json ser criado foi analisado cada linha e definido o início e o fim da partida. Contém InitGame para o início da partida e uma sequência de traços (-) para o fim. Também é usada, a variável verificadora chamada verify, que no fim das partidas altera o valor. Por fim, há um json que é retornado na variável all.<br>
      Os elementos contidos no json são definidos através de um loop que conta cada linha, o id é contabilizado a cada início e fim da partida na variável games.<br>
      O total de mortes é definido na variável total_kills a cada vez que é encontrado a palavra killed no jogo. A variável é zerada no fim de cada partida. <br>
      Para criar o ranking também foi necessário encontrar a palavra killed, definir duas listas(n_kill e n_killed) e duas funções. As funções capturam quem matou (função eachN_kill) e quem morreu (função eachN_killed) e adicionam o seu retorno nas listas. As listas são inseridas na função endGame, onde é contabilizado o total de mortes feitas e sofridas, além disso, é eliminado o world para contabilizar o ranking. <br>
      Cada jogador que entrou na partida é adicionado na variável players que elimina as repetições de jogadores (caso alguém tenha entrado e saído). As eliminações são feitas com a função unique da biblioteca numpy. A função endGame retorna um json inicial que depois é inserido a um segundo json que contém o id de cada partida.<br>
    - Task2: A task2 é inserido o arquivo completo de log e feito um ranking e cada vez que é encontrada a palavar killed, após isso, vai para a função eachN_kill que retorna cada morte feita e adiciona na variável n_kill, novamente é usado o unique da biblioteca numpy para retirar as repetições depois entra em um looping que contabiliza com a função count cada aparição do jogador que matou<br>
    - Bonus: No bonus também é delimitado o início e o final igual na task1.<br>
    - A causa de cada morte esta em uma string de nome name, que depois é feito o split por (,) com isso transformando em uma lista com todas as causas de morte. 
    - A cada vez que é encontrada a palavra killed é adicionado as mortes na lista death, cada vez que é encontrado um motivo de morte acrescentado 1 no json final. 
  - web.py: Neste arquivo há a api desenvolvida com a framework Flask, também é feito uma importação da classe Task1 do arquivo get_log.py, que contém o json das partidas<br>
  - A framework contem dois sites e duas funções cada site para uma função. A função game aprensenta todas as partidas, para visualizar acesse localhost:5000/all. A função search_game deve ser colocar um id que vai de 1 à 21 (que é o total de partidas) e ser apresentada a apenas aquela partida, para acessar use o site localhost:5000/all/id .
  - test.py: Neste arquivo é testado todas as funções utilizadas nos dois arquivos anteriores.
  
- Bibliotecas
  - numpy: Biblioteca de Inteligencia Artificial, foi usada para retirar repetição de elementos nas listas
  - re: Biblioteca de matipulação de string, foi utilizada sua função sub para eliminação de caracteres indesejáveis na função bonus.
  - flask: Framework web, utilizada para desenvolvimento da API
  - os: Biblioteca utilizada para definição de caminho dos arquivos dos sites no frask.
