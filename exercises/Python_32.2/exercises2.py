# Exercício 2: Jogo da palavra embaralhada. Desenvolva um jogo em que a pessoa usuária tenha que 
# adivinhar uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de 
# palavras e escolherá uma aleatoriamente. O jogador terá três tentativas para adivinhar a palavra. 
# Ao final a palavra deve ser mostrada na tela, informando se a pessoa ganhou ou perdeu o jogo.
# 🦜 Para embaralhar uma palavra faça: scrambled_word = "".join(random.sample(word, len(word)))
# 🦜 O sorteio de uma palavra aleatória pode ser feito utilizando o método choice: 
# random.choice(["word1", "word2", "word3"]) -> "word2" .
import random

word_selected = random.choice(['programação', 'atitude', 'contribuição', 'desenvolvimento'])

scrambled_word = "".join(random.sample(word_selected, len(word_selected)))

play = 0

while (play < 3):
  play = play + 1
  response = input(f'adivinhe qual é essa palavra {scrambled_word}:')
  if word_selected == response:
    break

print('Parabéns!!você acertou') if word_selected == response else print('Não foi dessa vez!!')
