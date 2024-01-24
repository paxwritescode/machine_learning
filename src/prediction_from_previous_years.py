import pandas as pd


def read_coefficients_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename)


def predict_share_from_coefficients(year: int, tan: float, bias: float) -> float:
    result: float = tan * (year - 2000) + bias
    return max(0., min(result, 100.))


def main():
    coefficients = read_coefficients_from_csv("../output/coefficients.csv")
    entities = coefficients["Entity"]

    print("Choose an entity from the following list: ")
    print(", ".join(entities))

    chosen_entity = input().strip()
    if chosen_entity not in list(entities):
        print("No such entity")
        return
    print("Input a year: ")
    chosen_year = int(input())
    rows = coefficients.loc[coefficients["Entity"] == chosen_entity]
    unconditional_res = predict_share_from_coefficients(chosen_year, rows["Tan"].iloc[0], rows["Bias"].iloc[0])
    rounded_unconditional_res = '%.3f' % unconditional_res
    current_year = 2024
    if chosen_year >= current_year:
        verb_form = "will be"
    else:
        verb_form = "was"
    print("According to unconditional prediction, шn", chosen_year, "the share of recycled plastic in", chosen_entity,
          verb_form,
          rounded_unconditional_res, "%")


if __name__ == "__main__":
    while True:
        main()
