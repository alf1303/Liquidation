import json
import requests
from datetime import datetime
import constants as CONST
from helperClasses import Asset
import logging

logging.basicConfig(filename=f'liqui.log', format='%(asctime)s %(levelname)s: %(message)s', level=logging.INFO, force=True)

def loglog(msg):
    logging.info(msg=msg)

def pprint(str):
    print(json.dumps(str, indent=4))

def get_height():
    res = 0
    req = "https://nodes.wavesnodes.com/blocks/height"
    try:
        resp = requests.get(req).json()
        if "height" in resp:
            res = resp["height"]
        else:
            loglog("Error fetching height")
    except Exception as e:
        loglog("Error fetching height glob")
    return res

def timestampToDate(tmstp):
    # print(tmstp)
    return datetime.fromtimestamp(tmstp/1000)

def dateToTimestamp(date):
    return int(datetime.timestamp(date)*1000)

def getTransactionName(type_number):
    return CONST.transaction_type_dict.get(type_number, "Unknown Transaction: " + str(type_number))

def getAssetInfo(id):
    data = {}
    if id == None or id == "WAVES":
        data['assetId'] = 'WAVES'
        data['name'] = 'WAVES'
        data['decimals'] = 8
    else:
        data = requests.get(f'{CONST.node_url}/assets/details/{id}').json()
    if 'error' in data:
        print(data)
        raise Exception("MyError while getting asset details: " + str(id))
    return data

def getAsset(id):
    if id in CONST.assets_dict:
        asset = CONST.assets_dict[id]
    else:
        ass = getAssetInfo(id)
        asset = Asset(ass["assetId"], ass["name"], ass["decimals"])
        CONST.assets_dict[id] = asset
    return asset

def isFarmToken(asset_id):
    return asset_id in CONST.wd_assets and asset_id != CONST.egg and asset_id != CONST.usdn 

def isEggToken(asset_id):
    return asset_id == CONST.egg

def addOrUpdateDict(map, key, value):
    if key in map:
        map[key] = map[key] + value
    else:
        map[key] = value

def printMap(map, decimals=0):
    for key in map:
        amount = map[key]
        if decimals != 0:
            amount = map[key]/10**decimals
        print(f"{key}: {amount}")

def printList(li):
    for el in li:
        print(el)

def getAssetDistribution(assetId, height, limit=1000, count=0):
    after = ""
    stop = False
    res = {}
    while not stop:
        reqstr = f"{CONST.node_url}/assets/{assetId}/distribution/{height}/limit/{limit}{after}"
        tmp_res = requests.get(reqstr).json()["items"]
        # print(tmp_res)
        if len(tmp_res) == 0:
            stop = True
        else:
            res.update(tmp_res)
            after = "?after=" + list(tmp_res.keys())[len(tmp_res) - 1]
    sorted_tuples = sorted(res.items(), key=lambda kv: (kv[1], kv[0]), reverse=True)
    resMap = {k: v for k, v in sorted_tuples}
    if count == 0:
        return resMap
    else:
        return {k: resMap[k] for k in list(resMap)[:count]}

def sortMap(map, reverse=True):
    sorted_tuples = sorted(map.items(), key=lambda kv: (kv[1], kv[0]), reverse=reverse)
    resMap = {k: v for k, v in sorted_tuples}
    return resMap

def sortMapByKeys(map):
    sortedKeys = sorted(map.keys())
    resMap = {k: map[k] for k in sortedKeys}
    return resMap
