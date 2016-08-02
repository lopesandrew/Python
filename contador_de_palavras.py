import math


def abrir_arquivo(arquivo):
    fin = open(str(arquivo) + '.txt')
    return fin


def fechar_arquivo():
    fin.close()


def numero_palavras(fin,arquivo):
	fin = open(arquivo+'.txt')
	palavras = 0
	for line in fin:
		palavras = palavras + 1
	return palavras


def porcentagem_letras(fin,arquivo):

	palavras = 0
	for line in fin:
		palavras = palavras + 1
	print palavras

	dois = 0
	tres = 0
	quatro = 0
	cinco = 0
	seis = 0
	sete = 0
	oito = 0
	nove = 0
	dezmaior = 0
	

	fin.close()
	fin = open(arquivo+'.txt')

	for line1 in fin:
	    word = line1.strip()
	    if len(word) < 3:
	        dois = dois + 1
	    elif len(word) > 2 and len(word) < 4:
	        tres = tres + 1
	    elif len(word) > 3 and len(word) < 5:
	        quatro = quatro + 1
	    elif len(word) > 4 and len(word) < 6:
	        cinco = cinco + 1
	    elif len(word) > 5 and len(word) < 7:
	        seis = seis + 1
	    elif len(word) > 6 and len(word) < 8:
	        sete = sete + 1
	    elif len(word) > 7 and len(word) < 9:
	        oito = oito + 1
	    elif len(word) > 8 and len(word) < 10:
	        nove = nove + 1
	    elif len(word) >= 10:
	        dezmaior = dezmaior + 1

	contagem = dois, tres, quatro, cinco, seis, sete, oito, nove, dezmaior
	print contagem
	for c in range(len(contagem)):
	    res = (float(contagem[c]) / float(palavras)) * 100
	    if c < 8:
	        print 'Palavras com', c + 2, ' Letras', ("{:.2f}".format(res)), '%'
	        print int(res) * '/'
	    else:
	        print 'Palvras com dez ou mais letras', ("{:.2f}".format(res)), '%'
	        print int(res) * '/'
		
ans = True
while ans:
    print("""
    1.Abrir arquivo
    2.Fechar arquivo
    3.Contar palavras
    4.Contar '%' de letras em cada palavras
    5.Sair
    """)
    ans = raw_input("Selecione a opcao desejada: ")
    if ans == "1":
    	arquivo = raw_input("Digite o nome do arquivo  ")
    	fin = abrir_arquivo(arquivo)
    	print("\nArquivo aberto!")
    elif ans == "2":
        fechar_arquivo()
        print("\n Arquivo fechado!")
    elif ans == "3":
        palavras = numero_palavras(fin,arquivo)
        print 'Existem ', palavras, ' palavras no arquivo. '
    elif ans == "4":
        print("\n Mostrando '%' de palavras: ")
        porcentagem_letras(fin,arquivo)
    elif ans == "5":
        print("\n Adeus!")
        ans = None
    else:
        print("\n Opcao invalida")
