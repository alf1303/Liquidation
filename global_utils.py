import requests

def getContractData(address: str) -> list:
    #'''Get all data entries from contract'''
    req_str = f"https://nodes.wavesnodes.com/addresses/data/{address}"
    res = requests.get(req_str).json()
    return res

def getContractDataByKey(address, key):
    data = getContractData(address=address)
    res = []
    for el in data:
        if key in el["key"]:
            res.append(el)
    return res
