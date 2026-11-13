
from hypothesis import given, strategies as st
from ride_share_fare import parse_trip, fare_average, payable_fare
import math


# Test 1: Random inputs should not crash parse_trip
@given(st.one_of(st.text(), st.none()))
def test_parse_trip_no_crash(s):
    try:
        parse_trip(s)
    except Exception as e:
        assert False, f"parse_trip crashed: {type(e).__name__}"


# Test 2: Valid trip inputs should return correct results
@given(
    cab=st.text(alphabet="abcdefghijklmnopqrstuvwxyz", min_size=1),
    km=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False)
)
def test_parse_trip_valid(cab, km):
    result = parse_trip(f"{cab}:{km}")
    assert result == (cab.title(), km)


# Test 3: Random inputs should not crash fare_average
@given(st.one_of(st.text(), st.none()))
def test_fare_average_no_crash(s):
    try:
        fare_average(s)
    except Exception as e:
        assert False, f"fare_average crashed: {type(e).__name__}"


# Test 4: Valid fare lists should produce the correct average
@given(st.lists(st.integers(min_value=0, max_value=100000), min_size=1, max_size=20))
def test_fare_average_valid(values):
    csv = ",".join(map(str, values))
    expected = sum(values) // len(values)
    assert fare_average(csv) == expected


# Test 5: Random inputs should not crash payable_fare
@given(st.one_of(st.text(), st.none()))
def test_payable_fare_no_crash(s):
    try:
        payable_fare(s)
    except Exception as e:
        assert False, f"payable_fare crashed: {type(e).__name__}"


# Test 6: Valid payment inputs should calculate correctly
@given(
    fare=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False),
    promo=st.floats(min_value=0, max_value=100000, allow_nan=False, allow_infinity=False)
)
def test_payable_fare_valid(fare, promo):
    result = payable_fare(f"{fare}|{promo}")
    expected = max(fare * 1.18 - promo, 0)
    assert math.isclose(result, expected, rel_tol=1e-9, abs_tol=1e-9)
