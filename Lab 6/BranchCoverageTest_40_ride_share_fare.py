
import pytest

from ride_share_fare import (
    extra_distance_fare,
    seats_and_bags_ok,
    pickup_status
)


def test_cab_type_branches():
    with pytest.raises(ValueError):
        extra_distance_fare("luxury", 10, "city", False)

    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_distance_branches():
    with pytest.raises(ValueError):
        extra_distance_fare("mini", -1, "city", False)

    assert extra_distance_fare("mini", 5, "city", False) == 0
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_subscriber_branches():
    assert extra_distance_fare("mini", 10, "city", True) == 24
    assert extra_distance_fare("sedan", 15, "city", True) == 48
    assert extra_distance_fare("suv", 15, "city", True) == 36
    assert extra_distance_fare("mini", 10, "city", False) == 60


def test_zone_and_rate_branches():
    assert extra_distance_fare("mini", 10, "city", False) == 60
    assert extra_distance_fare("mini", 10, "outstation", False) == 90

    assert extra_distance_fare("mini", 30, "city", False) == 500
    assert extra_distance_fare("mini", 30, "outstation", False) == 750


def test_seat_and_bag_branches():
    assert seats_and_bags_ok(2, 1, True) is True
    assert seats_and_bags_ok(3, 1, True) is False

    assert seats_and_bags_ok(5, 1, False) is False
    assert seats_and_bags_ok(4, 1, False) is True

    assert seats_and_bags_ok(2, 1, False) is True
    assert seats_and_bags_ok(2, 3, False) is False


def test_pickup_scheduled_branches():
    assert pickup_status(10, True, False) == "on_time"
    assert pickup_status(0, True, False) == "delayed"
    assert pickup_status(-6, True, False) == "missed"


def test_pickup_unscheduled_branches():
    assert pickup_status(5, False, False) == "on_time"
    assert pickup_status(0, False, False) == "delayed"
    assert pickup_status(-11, False, False) == "missed"


def test_airport_branches():
    assert pickup_status(20, True, True) == "on_time"
    assert pickup_status(10, True, True) == "delayed"
    assert pickup_status(4, True, True) == "missed"
