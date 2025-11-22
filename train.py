import os, pandas as pd, numpy as np
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt

DATA = "data/synthetic/energy.csv"
FIG = "reports/figures"; os.makedirs(FIG, exist_ok=True)

if __name__ == "__main__":
    df = pd.read_csv(DATA, parse_dates=["date"]).set_index("date").sort_index()
    split = int(len(df)*0.8)
    train, test = df.iloc[:split], df.iloc[split:]
    # naive seasonal forecast (weekly)
    horizon = len(test)
    seasonal_period = 7
    naive = train["load"].iloc[-seasonal_period:].tolist() * (horizon//seasonal_period + 1)
    naive = naive[:horizon]
    mape = mean_absolute_percentage_error(test["load"], naive)
    print(f"Naive seasonal MAPE: {mape:.3f}")
    # plot
    plt.figure()
    plt.plot(train.index, train["load"], label="train")
    plt.plot(test.index, test["load"], label="test")
    plt.plot(test.index, naive, label="naive_seasonal")
    plt.legend(); plt.title("Energy Load Forecast (Naive Seasonal)")
    plt.tight_layout(); plt.savefig(os.path.join(FIG, "forecast.png"))
    print(f"Saved figure to {os.path.join(FIG,'forecast.png')}")
