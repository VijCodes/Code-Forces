from collections import Counter

def find_longest_good_subsequence(n, k, a):
    counter = Counter(a)
    good_numbers = sorted(val for val, cnt in counter.items() if cnt >= k)
    
    if not good_numbers:
        return -1, -1

    left = 0
    max_length = 1
    ansl, ansr = good_numbers[0], good_numbers[0]

    for right in range(1, len(good_numbers)):
        if good_numbers[right] != good_numbers[right - 1] + 1:
            left = right
        elif right - left + 1 > max_length:
            max_length = right - left + 1
            ansl, ansr = good_numbers[left], good_numbers[right]

    return ansl, ansr

def main():
    for _ in range(int(input())):
        n, k = map(int, input().split())
        a = list(map(int, input().split()))
        ansl, ansr = find_longest_good_subsequence(n, k, a)
        if ansl == -1:
            print(-1)
        else:
            print(ansl, ansr)

if __name__ == "__main__":
    main()
