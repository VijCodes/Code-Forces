#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef long double ld;

int main() {
    ios::sync_with_stdio(0); 
    cin.tie(0);

    int t;
    cin >> t; // Number of test cases

    while (t--) {
        int n;
        cin >> n;
        cin.ignore(); // Ignore the newline after the integer input

        string s;
        getline(cin, s); // Read the entire line for string s

        vector<pair<int, int>> adj(n+1);
        for (int i = 1; i <= n; ++i) {
            int l, r;
            cin >> l >> r;
            adj[i] = {l, r};
        }

        int res = INT_MAX; // Use max value for infinity
        deque<pair<int, int>> search; // Queue for BFS
        search.push_back({1, 0}); // Start from node 1 with 0 changes

        vector<bool> seen(n+1, false); // Track seen nodes
        seen[1] = true;

        while (!search.empty()) {
            int node = search.front().first;
            int changes = search.front().second;
            search.pop_front();

            if (adj[node].first == 0 && adj[node].second == 0) {
                res = min(res, changes);
            }

            // Check the left child
            if (adj[node].first && !seen[adj[node].first]) {
                int new_change = changes + (s[node - 1] != 'L');
                search.push_back({adj[node].first, new_change});
                seen[adj[node].first] = true;
            }

            // Check the right child
            if (adj[node].second && !seen[adj[node].second]) {
                int new_change = changes + (s[node - 1] != 'R');
                search.push_back({adj[node].second, new_change});
                seen[adj[node].second] = true;
            }
        }

        if (res == INT_MAX) {
            cout << "-1\n"; // If no result was found, output -1 or another error indicator
        } else {
            cout << res << '\n';
        }
    }

    return 0;
}
