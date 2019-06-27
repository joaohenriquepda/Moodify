# Moodify

Moodify é uma aplicação feita para o projeto final da disciplina de Tópicos Especiais em Engenharia de Software ministrada por Diego Dorgam na Universidade de Brasília.

O projeto consiste em uma aplicação capaz de estipular a emoção que uma música reflete a partir dos dados fornecidos pela API do Spotify, podendo então analisar o histórico de músicas ouvidas pelo usuário e classificar o tipo de humor que o usuário teve em um determinado período de tempo.

## Integrantes
| Nome | Matrícula | Github |
| --- | --- | --- |
| Guilherme Marques Rosa | 16/0007739 | @guilhesme23 |
| Pedro Féo | 17/0020461 | @phe0 |

## Emoções

Inicialmente, as emoções escolhidas pela equipe para serem classificadas são:

- Felicidade
- Tristeza
- Amor / Paixão

## Metodologia

Inicialmente, o dataset será montado utilizando playlists já existentes no Spotify que o título represente alguma das emoções listadas acima.

Após o dataset montado, será escolhido uma arquitetura de rede neural que se adeque a proposta do projeto, e serão testados hiperparâmetros que melhor classifiquem os dados de teste.

Com o modelo treinado e testado, será criado uma API que receba os dados do usuário e use o modelo para classificar o humor deste usuário com base no seu histórico de reprodução.

Com a API completa, será feito um front-end que apresente essas informações de uma forma amigável ao usuário.

