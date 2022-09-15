import requests
from classes import Farm
from helperClasses import Asset

node_url = 'https://nodes.wavesnodes.com'
test_node_url = 'https://nodes-testnet.wavesnodes.com'

ducksDaoTestnet_dApp = '3MxxzjRwbjN41dDGDgg5F2JJgWPrVn8HhJY'

duxplorer = "usUeJwSpvghP5FR6jE9X4fUJbgXyxXnAezSgbzoMA8K"
math = "FPzcaiEjyG6syoXLY1aghWdPwExvRezGbPXjmL3Gcofw"
turtle = "9mFbBseP3RSC2veLrBgiLJMXDjahwBiH44WnqMfdkgid"
eggseggs = "E4cL4MDRTPz9Wo1hHkxQv4ZzpxVL5136JVaki4wGz2QZ"
latam = "5JQ8yUY4vnB19s4bXSGVYsNEyA9Bag6jbMtVEgFHvYM7"
fomo = "J4iWJS2kGmAqLC4dYFuHvmqXK1E6rBJaRTA6nd1VmFkj"
mundo = "2x8vsNgrBgLq9GWpnTNSVXTGq3cMLSvWWepR8CX36fVZ"
eggpoint = "6pHc1PyBcXyS74eBEo95V3ecQvhAypL9RfsUUKtHDUq2"

endo = "6muMrLavuvuSZXgy1cQrvYm92rGbprNXGdj6Bg7HAtTV"
marvin = "6xxMPcvHneBvZk7p82oUdQw4J3F9bsFgtm7YYXQSEDxb"
eggmoon = "J3dRSWWyRoX55YuuXQhBa2uZ4bUczkqSFC94VZeCoWKA"
street = "DAGQvqQg4F5YTQCQ5JFaVJdZEVoTvecuw2W9ybL5P1hR"
kolkhoz = "BwCk5zUMTuYtFFu3euo3g6Fwdk7TALrr5C8wvdzps8R5"
forklog = "4q9KXJCi9ZbmhttXuLRabd9epgpvowVuyKDuuNdkahdC"
cgu = "HK72uehJjkM22phZ5wHhBYxprP3r41eYtk9fYu5uetne"
insiders = "EbN5GVazwSNFXhmKYPvgq9TKrMVBdVBz7LfcTQHVugrQ"

dux_farm = Farm(dApp="3PJs4poBWAMFUM1Vn7T87mvNoZrts4esQbt", asset_id=duxplorer, name="Duxplorer")
math_farm = Farm(dApp="3PBTLkeAM1HUEMExwJGeYwEGfuocg563zeg", asset_id=math, name="Mathematical")
turtle_farm = Farm(dApp="3P48GkhK94aDgsavHhhsHGcYwcuLYQenWk4", asset_id=turtle, name="Turtle")
eggs_farm = Farm(dApp="3PPtUf3rhHYiHfsERX6qzXP3j5spqdrVrRm", asset_id=eggseggs, name="EggsEggs")
latam_farm = Farm(dApp="3P9d7k1FvWhahnSdyk5tb4kU33Fmee6NHKF", asset_id=latam, name="GranjaLatina")
fomo_farm = Farm(dApp="3P2bbfbAf2Ddc6cMgQfkt22fqmoE1AmALmN", asset_id=fomo, name="Fomo")
mundo_farm = Farm(dApp="3PMZEydczD7NkUD45AY2kqvQRd2mTK8uqz1", asset_id=mundo, name="Mundocrypto")
eggpoint_farm = Farm(dApp="3P3L6F3yMiXkdMMXovdMrAP96FLYW7cg2Xq", asset_id=eggpoint, name="Eggpoint")
endo_farm = Farm(dApp="3PJHPDM6kH8fGkPLkzwZ7SrNqc9JDXtMiPB", asset_id=endo, name="EndoWorld")
marvin_farm = Farm(dApp="3P5zfgXtcjJxyMZves2sfSqGoabhzaMuPpZ", asset_id=marvin, name="Marvin Favis")
eggmoon_farm = Farm(dApp="3P79Pu5NmNv7REyWN78uZLiqVVb6WSpAg1d", asset_id=eggmoon, name="IDO Research")
street_farm = Farm(dApp="3P8968LuSXboHgKi94PHvc6c17duA6i8Hw8", asset_id=street, name="DuckStreet")
kolkhoz_farm = Farm(dApp="3PE2feY8CpBtWBRPxtLS7dt3YJkSt4Kme6U", asset_id=kolkhoz, name="Kolkhoz")
forklog_farm = Farm(dApp="3PFdu9Kc2sUzLGjSv4axwr6Fe7dxqoYwkKR", asset_id=forklog, name="Forklog")
cgu_farm = Farm(dApp="3PDMQbvFVLyxBnkwzbFEYokEda4EE7ZfdgS", asset_id=cgu, name="CGU")
insiders_farm = Farm(dApp="3PB6dcUYwDt6WHq6sma4ed7iUvEKvuP4b6B", asset_id=insiders, name="Insiders")

all_farms = [turtle_farm, dux_farm, math_farm, eggs_farm, latam_farm, fomo_farm, mundo_farm, eggpoint_farm, endo_farm, marvin_farm, eggmoon_farm, street_farm, kolkhoz_farm, forklog_farm, cgu_farm, insiders_farm]

all_farms_dict = {
    "turtle": turtle_farm, 
    "duxplorer": dux_farm, 
    "mathematical": math_farm, 
    "eggseggs": eggs_farm, 
    "latam": latam_farm, 
    "fomo": fomo_farm, 
    "mundo": mundo_farm, 
    "eggpoint": eggpoint_farm, 
    "endoworld": endo_farm, 
    "marvinfavis": marvin_farm, 
    "eggmoon(IDO)": eggmoon_farm, 
    "duckstreet": street_farm, 
    "kolkhoz": kolkhoz_farm,
    "forklog": forklog_farm, 
    "cgu": cgu_farm, 
    "insiders": insiders_farm
    }
