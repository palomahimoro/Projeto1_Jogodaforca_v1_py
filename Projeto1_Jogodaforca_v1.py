#!/usr/bin/env python
# coding: utf-8

# In[7]:


#Jogo da forca


# In[8]:


#import
import random
from os import system, name


# In[9]:


#Funcao para limar a tela a cada execucao
def limpa_tela():
    #windows
    if name == 'nt':
        _ = system('cls')
        
    #Mac ou Linux
    else:
        _ = system('clear')


# In[10]:


#Funcao
def game():
    limpa_tela()
    
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")


# In[11]:


#lista de palavras para o jogo
palavras = ['banana', 'abacate', 'uva', 'morango', 'laranja']


# In[12]:


#Escolhe randomicamente uma palavra
palavra = random.choice(palavras)


# In[13]:


#list comprehension
letras_descobertas = ['_' for letra in palavra]


# In[14]:


#numero de chances
chances = 6


# In[15]:


#lista para as letras erradas
letras_erradas = []


# In[16]:


while chances > 0:
    #Print
    print(" ".join(letras_descobertas))
    print("\nChances restantes:", chances)
    print("Letras erradas:", " ".join(letras_erradas))

    #Tentativa
    tentativa = input("\nDigite uma letra: ").lower()

    #condicional
    if tentativa in palavra:
        index = 0
        for letra in palavra:
            if tentativa == letra:
                letras_descobertas[index] = letra
            index += 1
    else:
        chances -= 1
        letras_erradas.append(tentativa)
    #condicional
    if "_" not in letras_descobertas:
        print("\nVoce venceu, a palavra era:",palavra)
        break
#condicional
if "_" not in letras_descobertas:
    print("\nVoce venceu, a palavra era", palavra)
#bloco main
if __name__ == "__main__":
    game()
print("\nParabens. Voce esta aprendendo programacao em Python com a DSA. :)\n")


# In[ ]:





# In[ ]:





# In[ ]:




