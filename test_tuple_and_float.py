import pytest


class TestFloat:
    def test_wrong_ariphmetic_equality_check(self):
        try:
            assert 0.1 + 0.1 + 0.1 == 0.3
        except AssertionError:
            pass

    @pytest.mark.parametrize(
        "value, expected_fraction_representation", [
            (3.5, 7/2),
            (-3.5, -7/2),
            (0.0, 0/1)
        ]
    )
    def test_float_as_integer_ration(self, value, expected_fraction_representation):
        numerator = value.as_integer_ratio()[0]
        denominator = value.as_integer_ratio()[1]
        assert numerator/denominator == expected_fraction_representation

    def test_float_without_fraction_part_is_integer(self):
        assert 3.0.is_integer() is True


class TestTuple:
    @pytest.mark.parametrize(
        "testing_tuple, expected", [
            ((), "()"),
            ((0, 13235), "(0, 13235)"),
            ((1,  ''), "(1, '')")
        ])
    def test_tuple_to_str(self, testing_tuple, expected):
        assert str(testing_tuple) == expected

    def test_tuple2(self):
        pass

    def test_tuple3(self):
        pass
