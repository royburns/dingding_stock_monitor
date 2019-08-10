import tushare as ts
pro = ts.pro_api()

class Stock(object):
    def __init__(self):
        pass

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, stock_code):
        self._code = stock_code

    def get_stock_info(self):
        try:
            print(self._code)
            stock_info = ts.get_realtime_quotes(self._code)
            # stock_info = df = pro.daily(ts_code='000001.SZ', 
            print(stock_info)
            return stock_info[['name', 'price']].iloc[0].to_dict()
        except Exception as e:
            print('get_stock_info -- ', e)
            return None