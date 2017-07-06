#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
/***********************************************************************************/
/* Aluno: Joana D'arc                                                              */
/* Matrículas: 1526-12                                                             */
/* Curso: Ciência da Computação                                                     */
/* 2º Trabalho Prático -- Vinte Questões                                            */
/* DCC254 -- 2017 -- IFSEMG, turma Especiais/K                                      */
/* Prof. Flávio Augusto de Freitas                                                  */
/* Compilador: IDLE(Python GUI) versão 2.7                                           */
/* Sistema Operacional: Windows vista                                                */
/********************************************************************************/"""

 
class Arvore:
    def __init__(self, conteudo, esquerda=None, direita=None):
        self.conteudo = conteudo
        self.esquerda= esquerda
        self.direita= direita
         
    def __str__(self):
        return str(self.conteudo)
    
    def getEsquerda(self):
        return self.esquerda

    def getDireita(self):
        return self.direita

 
def verdadeiro(decisao):
    from string import lower
    resposta = lower(raw_input(decisao))
    return (resposta[0] == 's' or resposta[0] == 'S')

def imprimeArvore(arvore):
    while(arvore!=None):
        imprimeArvore(arvore.getEsquerda())
        print "R:",arvore.conteudo
        imprimeArvore(arvore.getDireita())
        return
        

def lerArquivo():
    try:
        arquivoEntrada = raw_input("Qual o nome do arquivo?")
        arquivo = open(arquivoEntrada,"r")
        print "Lendo do arquivo..."
        for line in arquivo:
            print line
    except IOError:
          print "Nao foi possivel encontrar o arquivo"

def escreverArquivo(arvore):
    try:
            arquivoSaida = raw_input("Qual o nome do arquivo?")
            arquivo = open(arquivoSaida,"a+")
            arquivo.write(arvore.getEsquerda())
            arquivo.write("\n" ,arvore.conteudo)
            arquivo.write(arvore.getDireita())
            print "Arquivo guardado com sucesso..."
            arquivo.close()
    except IOError:
        print "Nao foi possivel escrever no arquivo"

        

 
 
def main():
    print "Bem-vindo ao jogo de 20 Perguntas!"
    print "Pense em alguma coisa e eu vou adivinhar"
    if verdadeiro("Devo me lembrar de nossos jogos anteriores?"):
        lerArquivo()

    cont = 0
    vitorias = 0
    continuar = True
    raiz = Arvore("pessoa")
    while continuar:
        cont = cont+1
        if not verdadeiro("Esta pensando em alguma coisa? "): break
        arvore = raiz
        while arvore.esquerda!= None:
            if verdadeiro("Q:"+ arvore.conteudo + "? "):
                arvore = arvore.esquerda
            else:
                arvore = arvore.direita
         
        pessoa = arvore.conteudo
        if verdadeiro("Q:E um(a) " + pessoa + "? "):
            vitorias = vitorias +1
            imprimeArvore(arvore)
            print "Eu ganhei de voce amigo >_<!"
            if verdadeiro(" Deseja jogar de novo?"):
                continue
            print " Jogadas realizadas:" ,cont
            print " Eu ganhei",vitorias
            if not verdadeiro("Devo lembrar-me desse jogo?"):break
            escreverArquivo(arvore)
        #pegando novas informacoes do usuario   
        novo = raw_input("Eu perdi amigo(a) -_-...O que voce havia pensado? ")
        informacao = raw_input("Faca uma pergunta que diferencia um(a) " + pessoa + " do que voce havia pensado ?")
        diferenca = "Qual e a resposta <s/n>para essa pergunta? " 
        #adicionando novas informacoes na arvore
        arvore.conteudo = informacao
        #quando uma nova informacao e adicionada a arvore,a nova pergunta passa a ser a raiz e
        #e o novo pensamento do usuário e a raiz anterior se tornam filhos
        if verdadeiro(diferenca):
            arvore.esquerda= Arvore(pessoa)
            arvore.direita = Arvore(novo)
        else:
            arvore.direita = Arvore(pessoa)
            arvore.esquerda= Arvore(novo)
            imprimeArvore(arvore)
 
    return 0
 
if __name__ == '__main__':
    main()
