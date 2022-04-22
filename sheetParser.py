import pandas as pd

def excelParser(path: str, firstLine: int):
    workbook = pd.read_excel(path)

    arList = []

    for i in workbook.head(100)['Ips'][firstLine - 2:100 - firstLine + 2]:
        arList.append(i)

    return arList
