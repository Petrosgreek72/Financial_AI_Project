import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Επιλογή μετοχής (Apple - AAPL)
symbol = "AAPL"

# Λήψη δεδομένων τελευταίων 6 μηνών
stock = yf.Ticker(symbol)
hist = stock.history(period="6mo")

# Υπολογισμός μέσου όρου τιμών
hist['50_MA'] = hist['Close'].rolling(window=50).mean()
hist['200_MA'] = hist['Close'].rolling(window=200).mean()

# Δημιουργία γραφήματος
plt.figure(figsize=(12, 6))
plt.plot(hist.index, hist["Close"], label="Τιμή Κλεισίματος", color='blue')
plt.plot(hist.index, hist["50_MA"], label="50-day MA", color='green')
plt.plot(hist.index, hist["200_MA"], label="200-day MA", color='red')
plt.xlabel("Ημερομηνία")
plt.ylabel("Τιμή ($)")
plt.title(f"Ιστορικό Τιμών Μετοχής {symbol}")
plt.legend()
plt.grid()
plt.show()

# Ανάλυση και απόφαση αγοράς ή πώλησης
current_price = hist["Close"].iloc[-1]
average_price = hist["50_MA"].iloc[-1]

if current_price > average_price:
    recommendation = "Σύσταση: ΠΩΛΗΣΗ (Η τιμή είναι υψηλότερη από τον μέσο όρο)"
else:
    recommendation = "Σύσταση: ΑΓΟΡΑ (Η τιμή είναι χαμηλότερη από τον μέσο όρο)"

# Εκτύπωση αποτελεσμάτων
print(f"Μετοχή: {symbol}")
print(f"Τρέχουσα Τιμή: {current_price:.2f}$")
print(f"Μέσος Όρος (50 ημερών): {average_price:.2f}$")
print(recommendation)

