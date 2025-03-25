from django.core.cache import cache
import json
import yfinance as yf

class StockAccessor:

  def get_stock_price(self):

    stock_symbols = ["AAPL","MSFT","AMZN","GOOG","NVDA","META","TSLA","BRK-B","LLY","BRK-A"]
    stock_data = {}

    cached_data = cache.get('stock_data')

    if cached_data:
      stock_data = json.loads(cached_data)
      print("data from cache =====> ",stock_data)
    else:
      for symbol in stock_symbols:
        try:
            stock = yf.Ticker(symbol)
            
            stock_price = stock.history(period="1d")['Close'].iloc[-1]
            stock_data[symbol] = stock_price
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            stock_data[symbol] = None

      cache.set("stock_data", json.dumps(stock_data),900)

    return stock_data