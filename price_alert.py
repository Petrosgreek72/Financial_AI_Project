import yfinance as yf

def check_price(symbol, threshold=2.0):
    stock = yf.Ticker(symbol)
    hist = stock.history(period="7d")  # Δεδομένα τελευταίας εβδομάδας

    # Υπολογισμός ποσοστιαίας μεταβολής
    percent_change = ((hist["Close"][-1] - hist["Close"][0]) / hist["Close"][0]) * 100

    if abs(percent_change) >= threshold:
        return f"⚠️ ALERT: Η μετοχή {symbol} άλλαξε {percent_change:.2f}% την τελευταία εβδομάδα!"
    return f"✅ Καμία σημαντική αλλαγή στη μετοχή {symbol}."

# Δοκιμή
print(check_price("AAPL"))
print(check_price("TSLA"))
