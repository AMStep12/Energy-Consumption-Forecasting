import os, numpy as np, pandas as pd

np.random.seed(123)

def synth(days=900):
    date = pd.date_range("2023-01-01", periods=days, freq="D")
    trend = np.linspace(1000, 1300, days)
    weekly = 80*np.sin(2*np.pi*np.arange(days)/7)
    yearly = 150*np.sin(2*np.pi*np.arange(days)/365)
    noise = np.random.normal(0, 40, days)
    load = trend + weekly + yearly + noise
    df = pd.DataFrame({"date": date, "load": load})
    return df

if __name__ == "__main__":
    outdir = "data/synthetic"; os.makedirs(outdir, exist_ok=True)
    df = synth()
    df.to_csv(os.path.join(outdir,"energy.csv"), index=False)
    print(f"Wrote {len(df)} rows to {os.path.join(outdir,'energy.csv')}")
