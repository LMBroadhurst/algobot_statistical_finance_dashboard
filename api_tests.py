from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
import time

if __name__ == '__main__':
    api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    # trade_id = api.place_trade("EUR_USD", 100, 1)
    # print(trade_id, "opened")
    # time.sleep(5)
    # print(f"closing {trade_id}", api.close_trade(trade_id))
    [api.close_trade(x.id) for x in api.get_open_trades()]