# __💣 Auto BombParty__
- Script criado com a função de automatizar o jogo de palavras [BombParty](https://jklm.fun/), onde você recebe uma combinação de letras aleatórias (por exemplo, “vol”) e precisa digitar uma palavra que contenha essas letras (Ex: **vol**ante) antes que uma bomba exploda em você. <br>


# __👨‍💻 Como funciona__
- Ele começa carregando um dicionário de palavras de um site externo e usando-o para criar um objeto defaultdict. Em seguida, ele usa o webdriver do Chrome para navegar até o site e espera o jogo carregar. Assim que o jogo é detectado, entra em um loop onde constantemente procura a sílaba da rodada atual e usa-a para encontrar palavras correspondentes no defaultdict. Em seguida, escolhe uma dessas palavras aleatoriamente e a insere no jogo. O script também inclui tratamento de erros para problemas de conexão à internet e timeout. <br>

# __📷 Exemplo__
![](/gif_exemplo.gif?raw=true "Exemplo")<br>

# __📌 Dependências__
1. [Google Chrome](https://www.google.com/intl/pt-BR/chrome/)
2. [Python](https://www.python.org/downloads/)
3. Bibliotecas Selenium & Requests

Caso você não queira baixar o Chrome e/ou o Selenium, também vou estar disponibilizando a versão semi-automática, onde você digita as combinações de letras no console e precisa colar a resposta no navegador.

# __🤔 Como utilizar?__
1. Baixe e execute o arquivo PY<br>
2. O script começará carregando o dicionário de palavras e abrindo o navegador Chrome.
3. Entre em alguma sala PT-BR e aguarde até que o script detecte o jogo.
4. Uma vez que o jogo é detectado, o script entrará em um loop e começará a jogar automaticamente, escolhendo as palavras correspondentes à sílaba atual e as digitando na caixa de entrada.
