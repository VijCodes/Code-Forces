#include <iostream>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <cmath>

using namespace std;

int main() {
    int n;
    cin >> n;

    map<pair<int, int>, int> segC;
    deque<int> rightA, leftA;
    map<int, int> right, left;

    for(int i = 0; i < n; ++i) {
        char op;
        int l, r;
        cin >> op >> l >> r;

        if (op == '+') {
            segC[{l, r}]++;
            rightA.insert(upper_bound(rightA.begin(), rightA.end(), r), r);
            leftA.insert(upper_bound(leftA.begin(), leftA.end(), l), l);
        } else {
            segC[{l, r}]--;
            right[r]++;
            left[l]++;
        }

        while (!leftA.empty() && left[leftA.back()]) {
            left[leftA.back()]--;
            leftA.pop_back();
        }

        int maxLeft = leftA.empty() ? numeric_limits<int>::min() : leftA.back();

        while (!rightA.empty() && right[rightA.front()]) {
            right[rightA.front()]--;
            rightA.pop_front();
        }

        int minRight = rightA.empty() ? numeric_limits<int>::max() : rightA.front();

        if (minRight < maxLeft) {
            cout << "YES" << endl;
        } else {
            cout << "NO" << endl;
        }
    }

    return 0;
}
