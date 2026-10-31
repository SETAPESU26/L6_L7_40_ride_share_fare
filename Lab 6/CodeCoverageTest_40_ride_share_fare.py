from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


def test_extra_distance():
    assert extra_distance_fare("mini", 10, "city", False) == 60
    assert extra_distance_fare("sedan", 20, "outstation", False) == 216
    assert extra_distance_fare("suv", 15, "city", False) == 36
    assert extra_distance_fare("mini", 30, "city", False) == 500
    assert extra_distance_fare("mini", 30, "outstation", False) == 750
    assert extra_distance_fare("sedan", 5, "city", False) == 0


def test_subscriber_fare():
    assert extra_distance_fare("mini", 10, "city", True) == 24
    assert extra_distance_fare("sedan", 15, "city", True) == 48
    assert extra_distance_fare("suv", 15, "city", True) == 36


def test_seats_and_bags():
    assert seats_and_bags_ok(2, 1, False) is True
    assert seats_and_bags_ok(5, 1, False) is False
    assert seats_and_bags_ok(4, 3, False) is False
    assert seats_and_bags_ok(2, 5, True) is True


def test_pickup_status():
    assert pickup_status(10, True, False) == "on_time"
    assert pickup_status(0, True, False) == "delayed"
    assert pickup_status(-10, True, False) == "missed"
    assert pickup_status(15, False, False) == "on_time"
    assert pickup_status(0, False, True) == "delayed"
    assert pickup_status(-10, False, True) == "missed"


def test_invalid_inputs():
    import pytest

    with pytest.raises(ValueError):
        extra_distance_fare("luxury", 10, "city", False)

    with pytest.raises(ValueError):
        extra_distance_fare("mini", -1, "city", False)