#include <iostream>
#include <unordered_map>

using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int t;
    cin >> t;

    for (int j = 0; j < t; ++j) {
        int n;
        cin >> n;
        
        unordered_map<int, int> countV, countH, countP, countN;
        long long res = 0;

        for (int i = 0; i < n; ++i) {
            int x, y;
            cin >> x >> y;

            // Add matches over vertical line
            res += countV[x];
            countV[x]++;

            // Add matches over horizontal line
            res += countH[y];
            countH[y]++;

            // Add matches over positive slope
            res += countP[x - y];
            countP[x - y]++;

            // Add matches over negative slope
            res += countN[x + y];
            countN[x + y]++;
        }

        cout << res * 2 << '\n';
    }

    return 0;
}
