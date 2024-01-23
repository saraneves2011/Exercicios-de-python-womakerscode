def multiplicacao():
    mult = 10 * 2
    file = 'arquivo.txt'
     
    #open leitura
    arquivoLeitua = open(file,"r")
    
    #open escritura
    arquivoEscrita = open(file,"w")
    arquivoEscrita.write(f'O resultado da multiplicação é {mult}')
    arquivoEscrita.close()
    #arquivo binario
    # arquivoBinario = open(file,"wb")
    
    #escrita
    
    
    #leitura
    arquivoLeitua = open(file,'r')
    leitura = arquivoLeitua.read()
    print(leitura)
    arquivoLeitua.close()
    
    
multiplicacao()