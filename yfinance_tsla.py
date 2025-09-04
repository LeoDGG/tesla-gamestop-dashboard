#!/usr/bin/env python3

import yfinance as yf
import pandas as pd

# Parámetros de descarga
TICKER    = "TSLA"
START     = "2010-06-29"   # fecha de salida a bolsa de Tesla
END       = None           # hasta la fecha actual
INTERVAL  = "1d"           # datos diarios

def fetch_tsla_prices(ticker: str, start: str, end: str, interval: str) -> pd.DataFrame:
    """
    Descarga el historial de precios de cierre ajustado de TSLA
    y devuelve un DataFrame con columnas ['Date', 'Close'].
    """
    stock = yf.Ticker(ticker)
    hist  = stock.history(start=start, end=end, interval=interval)

    # Reset del índice para tener Date como columna
    df = hist[["Close"]].reset_index()
    df.rename(columns={"Close": "Close_USD"}, inplace=True)
    return df

def main():
    # 1) Descargar datos
    df = fetch_tsla_prices(TICKER, START, END, INTERVAL)

    # 2) Informar rango de fechas y filas descargadas
    print(f"Datos TSLA descargados: {len(df)} registros")
    print(f"Rango: {df['Date'].min().date()} – {df['Date'].max().date()}\n")

    # 3) Mostrar últimas 5 filas
    print("Últimas 5 filas de precios TSLA:\n")
    print(df.tail(5).to_string(index=False))

if __name__ == "__main__":
    main()
