import numpy as np
import pytest
import pandas as pd

from prediction_from_previous_years import predict_share_from_coefficients, predict_unconditionally, \
    predict_with_features


def test_predict_share():
    assert np.isclose(predict_share_from_coefficients(2000, 0.3, 1.5), 1.5)
    assert 0 <= predict_share_from_coefficients(2030, 4, 2.0) <= 100
    assert predict_share_from_coefficients(2024, 0, 0) >= 0
    assert predict_share_from_coefficients(2024, -1, -1) >= 0


def test_predict_unconditionally():
    with pytest.raises(Exception):
        predict_unconditionally(2000, "Russia")  # Should fail: Russia is not in list of entities
    assert predict_unconditionally(2100, "United States") <= 100
    assert predict_unconditionally(1900, "Oceania") >= 0


def test_predict_with_features():
    void_df = pd.DataFrame()
    with pytest.raises(Exception):
        predict_with_features(2000, [], void_df)
