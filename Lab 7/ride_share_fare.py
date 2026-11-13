
import math


def parse_trip(text):
    try:
        if not isinstance(text, str) or text.count(':') != 1:
            return None

        cab, km = text.split(':')
        cab = cab.strip()

        if not cab:
            return None

        distance = float(km.strip())

        if not math.isfinite(distance) or distance < 0:
            return None

        return cab.title(), distance

    except (ValueError, TypeError):
        return None


def fare_average(fares_csv):
    try:
        if not isinstance(fares_csv, str) or not fares_csv.strip():
            return None

        values = [int(r.strip()) for r in fares_csv.split(',')]

        if any(value < 0 for value in values):
            return None

        return sum(values) // len(values)

    except (ValueError, TypeError):
        return None


def payable_fare(text):
    try:
        if not isinstance(text, str) or text.count('|') != 1:
            return None

        fare, promo = text.split('|')

        fare = float(fare.strip())
        promo = float(promo.strip())

        if not math.isfinite(fare) or not math.isfinite(promo):
            return None

        if fare < 0 or promo < 0:
            return None

        total = fare * 1.18 - promo
        return max(total, 0)

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_trip ====")
    user_input = input("Enter cab:distance in km (e.g. sedan:12): ")
    result = parse_trip(user_input)
    print("Cab and Distance:", result if result is not None else "Invalid input")

    print("\n==== Running fare_average ====")
    user_input = input("Enter fares as CSV (e.g. 120,95,210): ")
    result = fare_average(user_input)
    print("Average Fare:", result if result is not None else "Invalid input")

    print("\n==== Running payable_fare ====")
    user_input = input("Enter fare|promo (e.g. 250|30): ")
    result = payable_fare(user_input)
    print("Payable Fare:", result if result is not None else "Invalid input")


if __name__ == "__main__":
    main()
