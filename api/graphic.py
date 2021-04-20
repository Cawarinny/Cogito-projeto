import json
import readPortfolio as rp
import readMajorIndices as rm

def graphic():
    majorIndicesComprador, majorIndicesNeutro, majorIndicesVendedor = rm.majorIndices()
    portfolioComprador, portfolioNeutro, portfolioVendedor = rp.portfolio()

    comprador = majorIndicesComprador + portfolioComprador
    vendedor = majorIndicesVendedor + portfolioVendedor
    neutro = majorIndicesNeutro + portfolioNeutro

    dadosGraphic = {'Comprador': comprador, 'Vendedor': vendedor, 'Neutro': neutro}
    with open('../data/dadosGraphic.json', 'w') as arq:
        json.dump(dadosGraphic, arq, indent=4)