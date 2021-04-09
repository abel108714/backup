import yfinance as yf
import plotly.graph_objects as go

symbol = '2330.TW'
inter = '1d'
peri = '200d'

prices = yf.Ticker(symbol).history(period=peri,interval=inter)
prices

fig0=go.Figure(
	data=[
		go.Candlestick(
			x=prices.index,
			open=prices['Open'],
			high=prices['High'],
			low=prices['Low'],
			close=prices['Close']
		)
	]
)

fig0.show()