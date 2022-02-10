# Exercício 3: Modifique o exercício anterior para que as palavras sejam lidas de um arquivo. 
# Considere que o arquivo terá cada palavra em uma linha.

import random

list_word = open(file='words.txt', mode='r')
word_selected = random.choice([w.replace('\n', '').strip() for w in list_word.readlines()])
list_word.close()

scrambled_word = "".join(random.sample(word_selected, len(word_selected)))

play = 0

while (play < 3):
  play = play + 1
  response = input(f'adivinhe qual é essa palavra {scrambled_word}:')
  if word_selected == response:
    break

print('Parabéns!!você acertou') if word_selected == response else print('Não foi dessa vez!!')