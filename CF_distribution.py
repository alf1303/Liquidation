
from constants import farm_only_ids
from utils import getAssetDistribution, getAssetInfo, printMap
import pywaves as pw

h = pw.height() - 1

for el in farm_only_ids:
    name = getAssetInfo(el)["name"]
    distr = getAssetDistribution(assetId=el, height=h, count=15)
    print(f" -- {name}")
    printMap(distr, decimals=8)
    print("*******************************")