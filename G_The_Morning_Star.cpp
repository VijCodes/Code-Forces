#include <iostream>
#include <map>
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

        map<ll, ll> countV, countH, countP, countN;

        ll res = 0;

        for (ll i = 0; i < n; ++i) {
            ll x, y;
            cin >> x >> y;

            // Add matches over vertical line
            res += countV[x];
            countV[x]++;

            // Add matches over horizontal line
            res += countH[y];
            countH[y]++;

            // Add matches over positive slope (x - y)
            res += countP[x - y];
            countP[x - y]++;

            // Add matches over negative slope (x + y)
            res += countN[x + y];
            countN[x + y]++;
        }

        cout << res * 2 << '\n';
    }

    return 0;
}
