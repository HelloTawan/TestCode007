from django.shortcuts import render
import yfinance as yf
from django.http import JsonResponse
from datetime import datetime, timedelta

def get_mock_stock_data(symbol):
    """Provide mock data when API fails"""
    mock_data = {
        'AAPL': {
            'name': 'Apple Inc.',
            'current_price': 178.50,
            'market_cap': 2750000000000,
            'sector': 'Technology',
            'industry': 'Consumer Electronics',
            'website': 'https://www.apple.com',
            'description': 'Apple Inc. designs, manufactures, and markets smartphones, personal computers, tablets, wearables, and accessories worldwide. The company also sells various related services.',
        },
        'GOOGL': {
            'name': 'Alphabet Inc.',
            'current_price': 135.25,
            'market_cap': 1700000000000,
            'sector': 'Communication Services',
            'industry': 'Internet Content & Information',
            'website': 'https://abc.xyz',
            'description': 'Alphabet Inc. provides online advertising services in the United States, Europe, the Middle East, Africa, the Asia-Pacific, Canada, and Latin America.',
        },
        'MSFT': {
            'name': 'Microsoft Corporation',
            'current_price': 425.75,
            'market_cap': 3150000000000,
            'sector': 'Technology',
            'industry': 'Software - Infrastructure',
            'website': 'https://www.microsoft.com',
            'description': 'Microsoft Corporation develops, licenses, and supports software, services, devices, and solutions worldwide.',
        },
        'TSLA': {
            'name': 'Tesla, Inc.',
            'current_price': 248.50,
            'market_cap': 795000000000,
            'sector': 'Consumer Cyclical',
            'industry': 'Auto Manufacturers',
            'website': 'https://www.tesla.com',
            'description': 'Tesla, Inc. designs, develops, manufactures, leases, and sells electric vehicles, and energy generation and storage systems.',
        },
        'AMZN': {
            'name': 'Amazon.com, Inc.',
            'current_price': 145.25,
            'market_cap': 1520000000000,
            'sector': 'Consumer Cyclical',
            'industry': 'Internet Retail',
            'website': 'https://www.amazon.com',
            'description': 'Amazon.com, Inc. engages in the retail sale of consumer products and subscriptions in North America and internationally.',
        },
    }
    
    base_info = mock_data.get(symbol.upper(), {
        'name': f'{symbol.upper()} Corporation',
        'current_price': 125.50,
        'market_cap': 500000000000,
        'sector': 'Technology',
        'industry': 'Software',
        'website': f'https://www.{symbol.lower()}.com',
        'description': f'{symbol.upper()} is a technology company that provides various services and products.',
    })
    
    # Generate mock historical data
    historical_data = []
    base_price = base_info['current_price']
    for i in range(5):
        date = datetime.now() - timedelta(days=4-i)
        price_variation = base_price * (0.95 + (i * 0.025))  # Small daily variations
        historical_data.append({
            'date': date.strftime('%Y-%m-%d'),
            'open': round(price_variation * 0.98, 2),
            'high': round(price_variation * 1.03, 2),
            'low': round(price_variation * 0.95, 2),
            'close': round(price_variation, 2),
            'volume': 45000000 + (i * 2000000)
        })
    
    return base_info, historical_data

def home(request):
    """Home page with stock search form"""
    return render(request, 'stocks/home.html')

def stock_detail(request, symbol):
    """Display stock details and price history"""
    try:
        # Try to fetch real data first
        stock = yf.Ticker(symbol.upper())
        info = stock.info
        hist = stock.history(period="5d")
        
        # Check if we got valid data
        if not info or len(hist) == 0:
            raise Exception("No data available from API")
        
        # Prepare real data for template
        stock_data = {
            'symbol': symbol.upper(),
            'name': info.get('longName', 'N/A'),
            'current_price': info.get('currentPrice', 'N/A'),
            'market_cap': info.get('marketCap', 'N/A'),
            'sector': info.get('sector', 'N/A'),
            'industry': info.get('industry', 'N/A'),
            'website': info.get('website', 'N/A'),
            'description': info.get('longBusinessSummary', 'N/A'),
        }
        
        # Convert historical data to list for template
        historical_data = []
        for date, row in hist.iterrows():
            historical_data.append({
                'date': date.strftime('%Y-%m-%d'),
                'open': round(row['Open'], 2),
                'high': round(row['High'], 2),
                'low': round(row['Low'], 2),
                'close': round(row['Close'], 2),
                'volume': int(row['Volume'])
            })
        
        context = {
            'stock_data': stock_data,
            'historical_data': historical_data,
            'data_source': 'real'
        }
        
    except Exception as e:
        # Fall back to mock data when API fails
        mock_info, mock_historical = get_mock_stock_data(symbol)
        
        stock_data = {
            'symbol': symbol.upper(),
            'name': mock_info['name'],
            'current_price': mock_info['current_price'],
            'market_cap': mock_info['market_cap'],
            'sector': mock_info['sector'],
            'industry': mock_info['industry'],
            'website': mock_info['website'],
            'description': mock_info['description'],
        }
        
        context = {
            'stock_data': stock_data,
            'historical_data': mock_historical,
            'data_source': 'mock',
            'api_error': str(e)
        }
    
    return render(request, 'stocks/stock_detail.html', context)
