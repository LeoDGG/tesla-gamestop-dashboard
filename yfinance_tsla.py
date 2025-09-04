df = yf.Ticker("TSLA") \
       .history(period="max") \
       .reset_index()[["Date", "Close"]] \
       .rename(columns={"Close": "Close_USD"})
# Exporta las últimas 5 filas como Markdown
md = df.tail(5).to_markdown(index=False)
with open("outputs/tsla_tail.md", "w", encoding="utf-8") as f:
    f.write(md)
