import pandas as pd


def read_coefficients_from_csv(filename: str) -> pd.DataFrame:
    return pd.read_csv(filename, index_col=0)


def predict_share_from_coefficients(year: int, tan: float, bias: float) -> float:
    result: float = tan * (year - 2000) + bias
    return max(0., min(result, 100.))


def get_verb_form(year: int) -> str:
    current_year = 2024
    if year >= current_year:
        return "will be"
    return "was"


def predict_unconditionally(year: int, entity: str) -> float:
    coefficients = read_coefficients_from_csv("../output/coefficients.csv")

    rows = coefficients.loc[coefficients["Entity"] == entity]
    unconditional_res = predict_share_from_coefficients(year, rows["Tan"].iloc[0], rows["Bias"].iloc[0])
    rounded_unconditional_res = round(unconditional_res, 3)

    return rounded_unconditional_res


def launch_unconditionally_prediction():
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

    unconditionally_predicted_share = predict_unconditionally(chosen_year, chosen_entity)

    print("According to unconditional prediction, in", chosen_year, "the share of recycled plastic in", chosen_entity,
          get_verb_form(chosen_year),
          unconditionally_predicted_share, "%")


def predict_with_features(year: int, features: list[float], linear_regression_coefficients: pd.DataFrame) -> float:
    tan: float = 0
    bias: float = 0

    tan_bias = linear_regression_coefficients.loc["Tangent"]["intercept"]
    bias_bias = linear_regression_coefficients.loc["Bias"]["intercept"]

    del linear_regression_coefficients["intercept"]

    i = 0
    for feature in features:
        tan += feature * linear_regression_coefficients.loc["Tangent"][i]
        bias += feature * linear_regression_coefficients.loc["Bias"][i]
        i += 1

    tan += tan_bias
    bias += bias_bias

    print(tan, bias)

    predicted_share = tan * year + bias

    return max(min(predicted_share, 100), 0)


def launch_prediction_with_features():
    linear_regression_coefficients = read_coefficients_from_csv("../output/linear_regression_coefficients.csv")
    feature_values = []
    for feature_name in linear_regression_coefficients.columns:
        if feature_name == "intercept":
            continue
        print("Input", f"{feature_name}:")
        feature_values.append(float(input()))

    print("Input a year: ")
    chosen_year = int(input())

    print(predict_with_features(chosen_year, feature_values, linear_regression_coefficients))


def main():
    launch_unconditionally_prediction()
    launch_prediction_with_features()


if __name__ == "__main__":
    # while True:
    main()
