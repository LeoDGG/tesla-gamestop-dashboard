# IBM-2

## Extracción de datos de acciones de Tesla utilizando yfinance

### Parámetros

def fetch_tsla_prices(ticker: str,
                      start: str = None,
                      end: str = None,
                      interval: str = "1d") -> pd.DataFrame:
    """
    Descarga el historial de precios ajustados de TSLA
    y devuelve un DataFrame con ['Date', 'Close_USD'].
    """
    stock = yf.Ticker(ticker)
    hist  = stock.history(start=start, end=end, interval=interval)

    # Preparamos el DataFrame
    df = hist[["Close"]].reset_index()
    df.rename(columns={"Close": "Close_USD"}, inplace=True)
    return df

def main():
    # 1) Descargar datos
    df = fetch_tsla_prices(TICKER, START, END, INTERVAL)

    # 2) Mostrar información básica
    print(f"Registros descargados: {len(df)}")
    print(f"Rango de fechas: {df['Date'].min().date()} – {df['Date'].max().date()}\n")

    # 3) Últimas 5 filas
    print("Últimas 5 filas de precios TSLA:")
    print(df.tail(5).to_string(index=False))

    # 4) Gráfica rápida (opcional)
    plt.figure(figsize=(8,4))
    plt.plot(df["Date"], df["Close_USD"], label="Close Adjusted")
    plt.title("TSLA Close Adjusted Prices")
    plt.xlabel("Date")
    plt.ylabel("Close (USD)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()
