#include <iostream>
#include <vector>
#include <unordered_map>
#include <algorithm>
using namespace std;

typedef long long ll;

int main() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    int t;
    cin >> t;

    while (t--) {
        ll n;
        cin >> n;

        vector<ll> a(n);
        unordered_map<ll, ll> c;
        vector<ll> uniqueVals;

        for (ll i = 0; i < n; ++i) {
            cin >> a[i];
            if (a[i] <= n) {
                if (c[a[i]]++ == 0) {
                    uniqueVals.push_back(a[i]);
                }
            }
        }

        sort(uniqueVals.begin(), uniqueVals.end());

        vector<ll> res(n + 1, 0);
        for (ll val : uniqueVals) {
            for (ll i = val; i <= n; i += val) {
                res[i] += c[val];
            }
        }

        cout << *max_element(res.begin(), res.end()) << '\n';
    }

    return 0;
}
