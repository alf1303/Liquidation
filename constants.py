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

    # "3P9d7k1FvWhahnSdyk5tb4kU33Fmee6NHKF": "Farm Granja Latina",
    # "3PPtUf3rhHYiHfsERX6qzXP3j5spqdrVrRm": "Farm EggsAggerated EGGS",
    # "3PE2feY8CpBtWBRPxtLS7dt3YJkSt4Kme6U": "Farm Kolkhoz",
    # "3PFdu9Kc2sUzLGjSv4axwr6Fe7dxqoYwkKR": "Farm Forklog",
    # "3PBTLkeAM1HUEMExwJGeYwEGfuocg563zeg": "Farm Mathematical",
    # "3P5zfgXtcjJxyMZves2sfSqGoabhzaMuPpZ": "Farm Marvin Favis",
    # "3PJs4poBWAMFUM1Vn7T87mvNoZrts4esQbt": "Farm Duxplorer",
    # "3P8968LuSXboHgKi94PHvc6c17duA6i8Hw8": "Farm Duck Street",
    # "3P3L6F3yMiXkdMMXovdMrAP96FLYW7cg2Xq": "Farm Eggpoint",
    # "3PJHPDM6kH8fGkPLkzwZ7SrNqc9JDXtMiPB": "Farm Endo World",
    # "3PB6dcUYwDt6WHq6sma4ed7iUvEKvuP4b6B": "Farm Insiders by GP",
    # "3PDMQbvFVLyxBnkwzbFEYokEda4EE7ZfdgS": "Farm CGU",
    # "3PMZEydczD7NkUD45AY2kqvQRd2mTK8uqz1": "Farm Mundocrypto",
    # "3P2bbfbAf2Ddc6cMgQfkt22fqmoE1AmALmN": "Farm FOMO",
    # "3P48GkhK94aDgsavHhhsHGcYwcuLYQenWk4": "Farm Turtle",
    # "3P79Pu5NmNv7REyWN78uZLiqVVb6WSpAg1d": "Farm IDO",

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

farms = {turtle_farm.name: turtle}

egg = "C1iWsKGqLwjHUndiQ7iXpdmPum9PeCDFfyXBdJJosDRS"
usdn = "DG2xFkPdDwKUoBkzGAhQtLpSGzfXLiCYPEzeKH2Ad24p"

puzzle_id = "HEB8Qaw9xrWpWs8tHsiATYGBWDBtP2S7kcPALrMu43AS"

tsunami_id = "8t4DPWTwPzpatHA9AkTxWAB47THnYzBsDnoY7fQqbG91"

farm_only_ids = [duxplorer, math, turtle, eggseggs, latam, fomo, mundo, eggpoint, endo, marvin, eggmoon, street, kolkhoz, forklog, cgu, insiders]

farm_1_assets_ids = [duxplorer, math, turtle, eggseggs, latam, fomo, mundo, eggpoint, egg, usdn]
farm_2_assets_ids = [endo, marvin, eggmoon, street, kolkhoz, forklog, cgu, insiders]
wd_assets = (farm_1_assets_ids + farm_2_assets_ids)
other_ids = [tsunami_id]
all_ids = (wd_assets + other_ids)

dApps_dict = {
    "3PEZe3Z2FqaVbMTjWJUpnQGxhWh2JRptujM": "PUZZLE WW_POOL",
    "3P4bSEVNM3xdmFaefX5nc9qT4fDtbwo9Dx4": "PUZZLE GLOBAL_??",
    "3P9EydokbUM5XFrHgEUT9bNVgfF7fGmtxLk": "PUZZLE MUNA_BNB",
    "3PC87Z4vUzet6tTrTQmzJmW1UtouKjLhBJi": "PUZZLE DUCKLIZATION",
    "3PDrYPF6izza2sXWffzTPF7e2Fcir2CMpki": "PUZZLE DEFI",
    "3PPRHHF9JKvDLkAc3aHD3Kd5tRZp1CoqAJa": "PUZZLE FARMS_1",
    "3PKYPKJPHZENAAwH9e7TF5edDgukNxxBt3M": "PUZZLE FARMS_2",
    "3PNK5ypnPJioLmLUzfK6ezpaePHLxZd6QLj": "PUZZLE RACE_POOL",
    "3PMHkdVCzeLAYuCh92FPtusuxdLk5xMB51y": "PUZZLE EGG_POOL",
    "3PAviuHPCX8fD7M5fGpFTQZb4HchWCJb3ct": "PUZZLE WWW_POOL",
    "3PLiXyywNThdvf3vVEUxwc7TJTucjZvuegh": "PUZZLE BTC_ETH_POOL",
    "3PEStCRPQuW3phthTtQ5upGeb4WZ47kssyM": "PUZZLE SNSBT_POOL",
    "3P3Z8Gn665CJr14bTLv4d5USDBUQCTeeCaT": "SWOP.FI RACE/EGG",
    "3PHTDdjz8Kb5JcAkhzfR57MCUYoe73pyxxK": "SWOP.FI WEST/EAST",
    "3PBHyEwmERR1CEkrTNbPj2bgyisTfPRqfee": "SWOP.FI PUZZLE/USDN",
    "3PHaNgomBkrvEL2QnuJarQVJa71wjw9qiqG": "SWOP.FI WAVES/USDN",
    "3PEcDN4sLSx6Pp4Y3m9vZzrgxtExfpFJr8w": "SWOP.FI EURN/USDN",
    "3P2V63Xd6BviDkeMzxhUw2SJyojByRz8a8m": "SWOP.FI NSBT/USDN",
    "3P8bovWtkLFVToB8LxP8AZLoWVwC8rDZLQQ": "SWOP.FI ENNO/USDN",
    "3PH8Np6jwuoikvkHL2qmdpFEHBR4UV5vwSq": "SWOP.FI SWOP/WAVES",
    "3PRFKemXs4rAJYGPccNtP63Kw2UzwEdH7sZ": "SWOP.FI PUZZLE/WAVES",
    "3PNVFWopwCD9CgGXkpYWEY94oQ5XCAEXBmQ": "SWOP.FI EGG/WAVES",
    "3P4Ftyud3U3xnuR8sTc1RvV4iQD62TcKndy": "SWOP.FI SIGN/USDN",
    "3P27S9V36kw2McjWRZ37AxTx8iwkd7HXw6W": "SWOP.FI SWOP/USDN",
    "3PEeJQRJT4v4XvSUBPmxhdWKz439nae7KtQ": "SWOP.FI EGG/USDN",
    "3PKy2mZqnvT2EtpwDim9Mgs6YvCRe4s85nX": "SWOP.FI FL/USDN",
    "3PJ48P3p2wvWUjgQaQiZ2cFbr8qmxMokBGd": "SWOP.FI VIRES/USDN",
    "3P6DLdJTP2EySq9MFdJu6beUevrQd2sVVBh": "SWOP.FI WEST/USDN",
    "3PK7Xe5BiedRyxHLuMQx5ey9riUQqvUths2": "SWOP.FI WAVES/EURN",
    "3PMDFxmG9uXAbuQgiNogZCBQASvCHt1Mdar": "SWOP.FI WCT/USDN",
    "3PKi4G3VX2k42ZSmNNrmvgdDH7JzRaUhY7R": "SWOP.FI WX/USDN",
    "3P9bPVN8aqfKCvTb5JiTHjter977XkeyJPk": "SWOP.FI MUNA/USDN",
    "3P32Rjpo9YHoHaorLSxvnV6CkKFXyfDCkJh": "SWOP.FI LTC/USDN",

    "3PPNhHYkkEy13gRWDCaruQyhNbX2GrjYSyV": "WX - LP Staking",
    "3PJL8Hn8LACaSBWLQ3UVhctA5cTQLBFwBAP": "WX Token staking",
    "3PKpsc1TNquw4HAF62pWK8ka1DBz9vyEBkt": "WX Token IDO",
    "3PCENpEKe8atwELZ7oCSmcdEfcRuKTrUx99": "Waves.Exchange Pools - WX/USDN",
    "3PCBWDTA6jrFswd7gQgaE3Xk7gLM5RKofvp": "Waves.Exchange Pools - BTC/USDN",
    "3P8NCvcipinDQVQZujpczBdvG7FL5EvTqLM": "Waves.Exchange Pools - BNB/USDN",
    "3P8KMyAJCPWNcyedqrmymxaeWonvmkhGauz": "Waves.Exchange Pools - USDT/USDN",
    "3PPZWgFNRKHLvM51pwS934C8VZ7d2F4Z58g": "Waves.Exchange Pools - WAVES/USDN",
    "3PEMqetsaJDbYMw1XGovmE37FB8VUhGnX9A": "Waves.Exchange Pools - ETH/USDN",

    "3PAETTtuW7aSiyKtn9GuML3RgtV1xdq1mQW": "Waves Ducks - Farming",
    "3PEBtiSVLrqyYxGd76vXKu8FFWWsD1c5uYG": "Waves Ducks - MArketPlace",
    "3PDVuU45H7Eh5dmtNbnRNRStGwULA7NY6Hb": "Waves Ducks - Breeding",
    "3PKmLiGEfqLWMC1H9xhzqvAZKUXfFm8uoeg": "Waves Ducks - Baby Duckling",
    "3PEktVux2RhchSN63DsDo4b4mz4QqzKSeDv": "Waves Ducks - Incubator",
    "3PEjHv3JGjcWNpYEEkif2w8NXV4kbhnoGgu": "Waves.Exchange",
    "3PGFHzVGT4NTigwCKP1NcwoXkodVZwvBuuU": "Puzzle Aggregator",
    "3PPG6zVNrMKnkqMthk5i2oHWQ5SHs9ertBM": "Team Rewards",

    "3PE8KysWk7FYBkFx83RwSCfyQUaiAg8M9KQ": "WX Booster",
    "3P4ojtVYmnsAQYs8sgQZ9HjpZGBaByWNFkM": "WX Booster",
    "3PBDTqqbnqMbvM93Y7dzeSQs5o2qKksXkoS": "WX Booster",
    "3PLSRRuk1Uz98N2Vz9Tdq6DuVk6zcDUfrE5": "WX Booster",
    "3P4ohLRoRdcXG4n5wGXvT4MxaouzfT3bsDo": "WX Booster",
    "3PPF8URZjEByhzZK4DjPjAFHvSq2z1h4xBq": "WX Booster",
    "3PL9dN952HFUMXBoUktUQTQMYNXvsHMkBon": "WX Booster",

    "3PKbd7pfmyaKWt6msaNAXyYUkuaumpea3bb": "Farm Granja Latina",
    "3P3y8NLGLYDx9obVaBF8je9uPTy2BDaK5n4": "Farm EggsAggerated EGGS",
    "3PEVpbeDDkjmKqiMm25MgMZfazR7U1Eivzi": "Farm Kolkhoz",
    "3PDs3ewniAQCp4LfXPMEqb2xRECgtZu2AR5": "Farm Forklog",
    "3PB8FTBTa1JspbXf8GiZTCdhYoq86QC6zxN": "Farm Mathematical",
    "3P6gnGQpT9iEABEy5AxMzMbm6ijGHSvXyeb": "Farm Marvin Favis",
    "3PJc5HTXgVWL7CYCec3huKJUtTPwJCNmMDF": "Farm Duxplorer",
    "3PEv4CE8moSLoAJw5y1bkiRMhtUF1nPRTfx": "Farm Duck Street",
    "3P3ohGCRmJzjTsP7RQ7jZV7QNw76wB1Nsnn": "Farm Eggpoint",
    "3P5me5qyR7z28WDkCiW172coLxpRZvqzeNv": "Farm Endo World",
    "3PJroXdKXF21FmcRjY6z7osZPP8VUY5R5Go": "Farm Insiders by GP",
    "3P6SQ4yDPRSzwk2nQD7ipK3HtxaEBX3M7Jk": "Farm CGU",
    "3P7iSFkjVr74EQqwExsg7DWRXX2SMn3BA3n": "Farm Mundocrypto",
    "3P3UMGin66fAe39AhJf5whS2Yabu6dZAmCF": "Farm FOMO",
    "3PCMKXu9r2ZNSxuLgnwoPXsWYhq6nMDADNo": "Farm Turtle",
    "3PEaA3SJb6wrfc2D4TPYTZ2xmMsufd7rCFJ": "Farm IDO",

    "3P9d7k1FvWhahnSdyk5tb4kU33Fmee6NHKF": "Farm Granja Latina",
    "3PPtUf3rhHYiHfsERX6qzXP3j5spqdrVrRm": "Farm EggsAggerated EGGS",
    "3PE2feY8CpBtWBRPxtLS7dt3YJkSt4Kme6U": "Farm Kolkhoz",
    "3PFdu9Kc2sUzLGjSv4axwr6Fe7dxqoYwkKR": "Farm Forklog",
    "3PBTLkeAM1HUEMExwJGeYwEGfuocg563zeg": "Farm Mathematical",
    "3P5zfgXtcjJxyMZves2sfSqGoabhzaMuPpZ": "Farm Marvin Favis",
    "3PJs4poBWAMFUM1Vn7T87mvNoZrts4esQbt": "Farm Duxplorer",
    "3P8968LuSXboHgKi94PHvc6c17duA6i8Hw8": "Farm Duck Street",
    "3P3L6F3yMiXkdMMXovdMrAP96FLYW7cg2Xq": "Farm Eggpoint",
    "3PJHPDM6kH8fGkPLkzwZ7SrNqc9JDXtMiPB": "Farm Endo World",
    "3PB6dcUYwDt6WHq6sma4ed7iUvEKvuP4b6B": "Farm Insiders by GP",
    "3PDMQbvFVLyxBnkwzbFEYokEda4EE7ZfdgS": "Farm CGU",
    "3PMZEydczD7NkUD45AY2kqvQRd2mTK8uqz1": "Farm Mundocrypto",
    "3P2bbfbAf2Ddc6cMgQfkt22fqmoE1AmALmN": "Farm FOMO",
    "3P48GkhK94aDgsavHhhsHGcYwcuLYQenWk4": "Farm Turtle",
    "3P79Pu5NmNv7REyWN78uZLiqVVb6WSpAg1d": "Farm IDO",

    "3PC9BfRwJWWiw9AREE2B3eWzCks3CYtg4yo": "Neutrino - USDN Collateral",
    "3P8w8NXZUtYdCA13tHbDY5sW4mC27ZFJgG3": "Neutrino - NSBT Staking",
    "3PQEjFmdcjd6wf1TrpkHSuDAk3zbfLSeikb": "Neutrino - Liquidity Pool",
    "3P5Bfd58PPfNvBM2Hy8QfbcDqMeNtzg7KfP": "Neutrino - Oracles",
    "3PNikM6yp4NqcSU8guxQtmR5onr2D4e8yTJ": "Neutrino - Staking",
    "3PG2vMhK5CPqsCDodvLGzQ84QkoHXCJ3oNP": "Neutrino - Auction",
    "3PFhcMmEZoQTQ6ohA844c7C9M8ZJ18P8dDj": "Neutrino - DeFo Staking",
    "3P7Uf5GF5feqnG39dTBEMqhGJzEq3T7MPUW": "Neutrino - EURN Collateral",
    "3P5fnEVxY8DFCNqfigRqFJRCjBAUbpP6Rr4": "Neutrino - RUBN Collateral",
    "3PMsU5VCcFrFnpKMh9EMMCYhjjiYTMNpMTa": "Neutrino - UAHN Collateral",
    "3P24H3bZrLHSRYFaUr7tFgUpL6Eic55Mv2b": "Neutrino - BRLN Collateral",
    "3PMsU5VCcFrFnpKMh9EMMCYhjjiYTMNpMTa": "Neutrino - UAHN Collateral",
    "3P2xtvqBiofPU7aCrrT2iX3GXLNVodq8tUk": "Neutrino - TRYN Collateral",
    "3PPeM6UjZWjAkJDuuKoocZLwDcpyiSWNxWA": "Neutrino - CNYN Collateral",
    "3PMVZ6LtKhvcwnYB5p1e7JmhUKLUcNbdKFg": "Neutrino - GBPN Collateral",
    "3PPsoLQYRjvhQTfLYnaEm6BVeJLznBFrwZK": "Neutrino - JPYN Collateral",
    "3P4PCxsJqMzQBALo8zANHtBDZRRquobHQp7": "Neutrino - Liquidation",

    "3P9LTA2dBPNZfUhgnE7na9EyDeuqYdRSqTQ": "Dima Ivanov Main",
    "3PMyGoiQZgNQ8jWn4eKR6uZzSkRoWjdBdgW": "Dima Ivanov 2",
    "3P3188GUzTypcP2hKNe7Ys5X1S9yoNYjCU3": "Dasha Rewards",
    "3PD8eT53J3LcUM5HLnHMcYNAuLEKrQgC4bR": "Buy the Dip PUZzle",
    "3P3EgRSuPaavrVx8AavNVrTMLqtyPsNwPiy": "Dima @Kript_on"
}

private_wallets_dict = {
    "3P9LTA2dBPNZfUhgnE7na9EyDeuqYdRSqTQ": "Dima Ivanov Main",
    "3PMyGoiQZgNQ8jWn4eKR6uZzSkRoWjdBdgW": "Dima Ivanov 2",
    "3P3188GUzTypcP2hKNe7Ys5X1S9yoNYjCU3": "Dasha Rewards",
    "3PD8eT53J3LcUM5HLnHMcYNAuLEKrQgC4bR": "Buy the Dip PUZzle"
}

# wd_farming = "3PAETTtuW7aSiyKtn9GuML3RgtV1xdq1mQW"
# wd_market = "3PEBtiSVLrqyYxGd76vXKu8FFWWsD1c5uYG"
# waves_exchange = "3PEjHv3JGjcWNpYEEkif2w8NXV4kbhnoGgu"

# dApps_Names_dict = {
#     wd_farming: "Waves Ducks Farming",
#     wd_market: "Waves Ducks MarketPlace",
#     waves_exchange: "Waves.Exchange"
# }

transaction_type_dict = {
    4: "Asset Transfer",
    6: "Asset Burn",
    7: "Exchange",
    11: "Mass Payment",
    16: "Invoke Function"
}

TRANS_DIRECTIONS = {
    "IN": "IN",
    "OUT": "OUT",
    "DUAL": "DUAL"
}

def initAssets(assetList):
    assets = {}
    tmpstr = ""
    tmpsepar = ""
    for a in assetList:
        tmpstr += tmpsepar + a
        if tmpsepar == "":
            tmpsepar = "&id="
    assetDetails = requests.get(f'{node_url}/assets/details?id={tmpstr}').json()
    for item in assetDetails:
        if 'error' in item:
            if item['message'] == 'Asset does not exist: WAVES':
                item['assetId'] = 'WAVES'
                item['name'] = 'WAVES'
                item['decimals'] = 8
        tmpasset = Asset(item["assetId"], item["name"], item['decimals'])
        assets[item['assetId']] = tmpasset
    return assets

def getAsset(id):
    if id in assets_dict:
        return assets_dict[id]
    else:
        item = requests.get(f'{node_url}/assets/details/{id}').json()
        print(f"id: {id} --> {item}")
        tmpasset = Asset(item["assetId"], item["name"], item['decimals'])
        assets_dict[item['assetId']] = tmpasset
        return tmpasset

assets_dict = initAssets(all_ids)
