import pandas as pd


def read_coefficients_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def predict_share_from_coefficients(year: int, tan: float, bias: float) -> float:
    result: float = tan * (year - 2000) + bias
    return max(0., min(result, 100.))


def main():
    coefficients = read_coefficients_from_csv("../output/coefficients.csv")
    rows_india = coefficients.loc[coefficients["Entity"] == "India"]

    print(predict_share_from_coefficients(2019, rows_india["Tan"].iloc[0], rows_india["Bias"].iloc[0]))


if __name__ == "__main__":
    main()
