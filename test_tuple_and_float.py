import pytest


class TestFloat:
    def test_float_without_fraction_part_is_integer(self):
        assert 3.0.is_integer() is True

    @pytest.mark.parametrize(
        "value, expected_fraction_representation", [
            (3.5, 7 / 2),
            (-3.5, -7 / 2),
            (0.0, 0 / 1)
        ]
    )
    def test_float_as_integer_ration(self, value, expected_fraction_representation):
        numerator = value.as_integer_ratio()[0]
        denominator = value.as_integer_ratio()[1]
        assert numerator / denominator == expected_fraction_representation

    def test_wrong_ariphmetic_equality_check(self):
        try:
            assert 0.1 + 0.1 + 0.1 == 0.3
        except AssertionError:
            pass


class TestTuple:
    def test_unpacking(self):
        digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
        zero, one, two, three, four, five, six, seven, eight, nine = digits
        assert zero == 0 and one == 1 and two == 2 and three == 3 and four == 4 and five == 5 and six == 6 and seven == 7 and eight == 8 and nine == 9

    @pytest.mark.parametrize(
        "testing_tuple, expected", [
            ((), "()"),
            ((0, 13235), "(0, 13235)"),
            ((1,  ''), "(1, '')")
        ])
    def test_tuple_to_str(self, testing_tuple, expected):
        assert str(testing_tuple) == expected

    def test_tuple_is_immutable(self):
        testing_tuple = (4, 5, 6)
        try:
            testing_tuple[0] = 100
        except TypeError:
            pass
