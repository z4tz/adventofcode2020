from inputreader import aocinput
from typing import List


def earliestBus(data: List[str]):
    start = int(data[0])
    buses = [int(part) for part in data[1].strip().split(',') if part != 'x']
    diff = {bus - start % bus: bus for bus in buses}
    return min(diff) * diff[min(diff)]


def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    while r:
        quotient, remainder = divmod(old_r, r)
        old_r, r = r, remainder
        old_s, s = s, old_s - quotient * s
    return old_r, old_s


def combine_phased_rotations(a_period, a_phase, b_period, b_phase):
    gcd, s = extended_gcd(a_period, b_period)
    phase_difference = a_phase - b_phase
    pd_mult, pd_remainder = divmod(phase_difference, gcd)
    if pd_remainder:
        raise ValueError("Rotation reference points never synchronize.")

    combined_period = a_period // gcd * b_period
    combined_phase = (a_phase - s * pd_mult * a_period) % combined_period
    return combined_period, combined_phase


def offsetDeparting(data):
    buses = sorted([(int(part), i) for i, part in enumerate(data[1].strip().split(',')) if part != 'x'])
    combined_period, combined_phase = buses[0]
    for period, offset in buses[1:]:
        combined_period, combined_phase = combine_phased_rotations(combined_period, combined_phase, period, offset)
    return -combined_phase % combined_period


def main(day):
    data = aocinput(day)
    result = earliestBus(data)
    result2 = offsetDeparting(data)
    print(result, result2)


if __name__ == '__main__':
    main(13)
