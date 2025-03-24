import yfinance as yf

class StockAccessor:

  def get_stock_price(self):

    stock_symbols = ["AAPL","MSFT","AMZN","GOOG","NVDA","META","TSLA","BRK-B","LLY","BRK-A"]
    stock_data = {}

    for symbol in stock_symbols:
        try:
            stock = yf.Ticker(symbol)
            
            stock_price = stock.history(period="1d")['Close'].iloc[-1]
            stock_data[symbol] = stock_price
        except Exception as e:
            print(f"Error fetching data for {symbol}: {e}")
            stock_data[symbol] = None

    return stock_data