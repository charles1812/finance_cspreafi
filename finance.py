import yfinance as yf
import numpy as np
import matplotlib.pyplot as plt

# Fonction pour calculer la volatilité
def calculate_volatility(prices):
    returns = np.log(prices / prices.shift(1))
    volatility = returns.std() * np.sqrt(252)  # 252 est le nombre typique de jours de trading dans une année
    return volatility

# Symbole de l'action à récupérer
symbol = "T"  # Remplacez "AAPL" par le symbole de l'action de votre choix

# Récupérer les données historiques de l'action
data = yf.download(symbol, start="2010-01-01", end="2022-12-31")  # Modifier les dates si nécessaire

# Extraire les cours de clôture
closing_prices = data["Close"]

# Calculer la volatilité
volatility = calculate_volatility(closing_prices)

# Afficher les résultats
print(f"Volatilité de {symbol}: {volatility}")

# Fonction pour calculer la volatilité
def calculate_volatility(prices):
    returns = np.log(prices / prices.shift(1))
    volatility = returns.std() * np.sqrt(252)  # 252 est le nombre typique de jours de trading dans une année
    return volatility

# Symbole de l'action à récupérer
symbol = "AAPL"  # Remplacez "AAPL" par le symbole de l'action de votre choix

# Récupérer les données historiques de l'action
data = yf.download(symbol, start="2022-01-01", end="2022-12-31")  # Modifier les dates si nécessaire

# Extraire les cours de clôture
closing_prices = data["Close"]

# Calculer la volatilité
volatility = calculate_volatility(closing_prices)

# Créer le graphique de la volatilité
plt.figure(figsize=(10, 6))
plt.plot(volatility)
plt.title(f"Volatilité de {symbol}")
plt.xlabel("Date")
plt.ylabel("Volatilité")
plt.grid(True)
plt.show()