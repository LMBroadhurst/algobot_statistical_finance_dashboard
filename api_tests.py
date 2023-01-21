from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

from models.candle_timing import CandleTiming
from bot.trade_risk_calculator import get_trade_units
import constants.secrets as defs

def lm(msg, pair):
    print(msg, pair)

if __name__ == '__main__':
    api = OandaApi()    
    instrumentCollection.LoadInstruments("./data")

    print(get_trade_units(api, "GBP_JPY", defs.BUY, 0.4, 60, lm))
    
