from utils import read_data
import time

# cribbed from https://stackoverflow.com/a/38817866
def factors(n):
    step = 2 if n % 2 else 1
    return set(
        factor for i in range(1, int(n**0.5) + 1, step) if n % i == 0
        for factor in (i, n//i)
    )

def lowest_house_number_p1(minscore: int) -> int:
    curnum = 1
    while True:
        if sum(factors(curnum)) * 10 > minscore:
            return curnum
        curnum += 1

def lowest_house_number_p2(minscore: int) -> int:
    curnum = 1
    while True:
        relevant_factors = [x for x in factors(curnum) if curnum // x <= 50]
        if sum(relevant_factors) * 11 > minscore:
            return curnum
        curnum += 1

def main():
    print(f"Part one: {lowest_house_number_p1(int(read_data()))}")
    print(f"Part two: {lowest_house_number_p2(int(read_data()))}")


if __name__ == "__main__":
    start = time.monotonic()
    main()
    print(f"Time: {time.monotonic()-start}")
