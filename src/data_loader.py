import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    print("Loaded dataset shape:", df.shape)
    return df

if __name__ == "__main__":
    df = load_data("data/phishing_dataset.csv")
