# IBM-2

## Extracción de datos de acciones de Tesla utilizando yfinance


def fetch_tsla_close(ticker: str, start: str) -> pd.DataFrame:
    """Descarga el precio de cierre ajustado y devuelve DataFrame con Date y Close_USD."""
    df = (
        yf.Ticker(ticker)
          .history(start=start)[["Close"]]
          .rename(columns={"Close": "Close_USD"})
          .reset_index()
    )
    return df

def save_outputs(df: pd.DataFrame):
    """Crea carpeta, exporta tabla Markdown y gráfico PNG."""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    ### Últimas 5 filas en Markdown
    with open(MD_FILENAME, "w", encoding="utf-8") as f:
        f.write(df.tail(5).to_markdown(index=False))
    
    ### Gráfica de toda la serie
    plt.figure(figsize=(8, 4))
    plt.plot(df["Date"], df["Close_USD"], lw=1, label=TICKER)
    plt.title(f"{TICKER} Adjusted Close Prices")
    plt.xlabel("Date")
    plt.ylabel("Close (USD)")
    plt.tight_layout()
    plt.savefig(PNG_FILENAME, dpi=150)

def main():
    df = fetch_tsla_close(TICKER, START_DATE)
    print(df.tail(5).to_string(index=False))
    save_outputs(df)

if __name__ == "__main__":
    main()
