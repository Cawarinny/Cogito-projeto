import json
import datetime


def portfolio():
    neutro = 0
    vendedor = 0
    comprador = 0

    dataHoraAtual = datetime.datetime.now()
    horaAbertura = dataHoraAtual.replace(hour=10, minute=30, second=0, microsecond=0)
    horaFechamento = dataHoraAtual.replace(hour=18, minute=30, second=0, microsecond=0)

    if (horaAbertura <= dataHoraAtual <= horaFechamento):
        verificador = 0
    else:
        verificador = 1

    with open('../data/portfolio.json', 'r') as arq:
        dadosPortifolio = json.load(arq)

    varpercentual = dadosPortifolio['Portfolio']['Var. %'].values()

    for ler in varpercentual:
        lermodificada = ler.replace(',', '.')
        lermodificadaSem = lermodificada.replace('%', '')

        variacao = float(lermodificadaSem)

        if (verificador < 3):
            if ( variacao >= 0.3):
                comprador += 1
            elif(0.3 > variacao > -0.3):
                neutro += 1
            else:
                vendedor += 1
        else:
            if ( variacao <= -0.3):
                comprador += 1
            elif(0.3 > variacao > -0.3):
                neutro += 1
            else:
                vendedor += 1
        verificador += 1
    return comprador, neutro, vendedor