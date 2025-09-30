from django.shortcuts import render
import yfinance as yf

def stock_analysis(request):
	symbol = request.GET.get('symbol', 'AAPL')  # ค่าเริ่มต้นคือ Apple
	stock = yf.Ticker(symbol)
	hist = stock.history(period="5d")
	info = stock.info
	context = {
		'symbol': symbol,
		'history': hist.reset_index().to_dict('records'),
		'info': info,
	}
	return render(request, 'stock_analysis.html', context)
