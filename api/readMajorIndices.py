import json

def majorIndices():
    comprador = 0
    vendedor = 0
    neutro = 0

    majorIndicesComprador = 0
    majorIndicesVendedor = 0
    majorIndicesNeutro = 0

    with open('../data/majorIndices.json', 'r') as arq:
        dadosPortifolio = json.load(arq)

    varpercentual = dadosPortifolio['majorIndices']['Var. %'].values()

    for ler in varpercentual:
        lermodificada = ler.replace(',', '.')
        lermodificadaSem = lermodificada.replace('%', '')
        variacao = float(lermodificadaSem)
        if ( variacao >= 0.3):
            comprador += 1
        elif(0.3 > variacao > -0.3):
            neutro += 1
        else:
            vendedor += 1
    
    if (comprador > neutro) & (comprador > vendedor):
        majorIndicesComprador = 1
    elif (neutro > comprador) & (neutro > vendedor) & ((comprador - vendedor) == 0):
        majorIndicesNeutro = 1
    else:
        majorIndicesVendedor = 1

    return majorIndicesComprador, majorIndicesNeutro, majorIndicesVendedor