import os
import pandas as pd
from ucimlrepo import fetch_ucirepo

def download_dataset():
    # ── Paths ──────────────────────────────────────────────
    script_dir = os.path.dirname(os.path.abspath(__file__))
    raw_dir    = os.path.join(script_dir, "raw")
    os.makedirs(raw_dir, exist_ok=True)

    output_path = os.path.join(raw_dir, "diabetes_raw.csv")

    
    if os.path.exists(output_path):
        print(f"[INFO] Data already exists at: {output_path}")
        print("[INFO] Delete the file and re-run to force re-download.")
        return

    # ── Fetch from UCI ─────────────────────────────────────
    print("[INFO] Fetching dataset from UCI ML Repository...")
    diabetes = fetch_ucirepo(id=296)

    X = diabetes.data.features
    y = diabetes.data.targets

    df = pd.concat([X, y], axis=1)

    # ── Save ───────────────────────────────────────────────
    df.to_csv(output_path, index=False)
    print(f"[SUCCESS] Dataset saved → {output_path}")
    print(f"[INFO] Shape: {df.shape}")
    print(f"[INFO] Columns: {df.columns.tolist()}")

if __name__ == "__main__":
    download_dataset()