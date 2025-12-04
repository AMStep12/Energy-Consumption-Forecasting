import os
import pandas as pd
import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
import matplotlib.pyplot as plt

DATA_PATH = os.path.join("data", "synthetic", "energy.csv")
FIG_DIR = os.path.join("reports", "figures")

os.makedirs(FIG_DIR, exist_ok=True)

if __name__ == "__main__":
    df = pd.read_csv(DATA_PATH, parse_dates=["date"]).set_index("date").sort_index()

    split_idx = int(len(df) * 0.8)
    train = df.iloc[:split_idx]
    test = df.iloc[split_idx:]

    # Naive weekly seasonal forecast
    horizon = len(test)
    seasonal_period = 7

    history = train["load"].values
    forecast = []

    for i in range(horizon):
        idx = len(history) - seasonal_period + i
        forecast.append(history[idx])

    forecast = np.array(forecast)

    mape = mean_absolute_percentage_error(test["load"].values, forecast)
    print(f"Naive seasonal MAPE: {mape:.3f}")

    plt.figure()
    plt.plot(train.index, train["load"], label="Train")
    plt.plot(test.index, test["load"], label="Test")
    plt.plot(test.index, forecast, label="Naive seasonal forecast")
    plt.legend()
    plt.title("Energy Load Forecast (Naive Seasonal)")
    plt.xlabel("Date")
    plt.ylabel("Load")
    plt.tight_layout()

    out_path = os.path.join(FIG_DIR, "forecast.png")
    plt.savefig(out_path)
    print(f"Saved forecast plot to {out_path}")

