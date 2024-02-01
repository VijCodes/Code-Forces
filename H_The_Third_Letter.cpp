#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
using namespace std;

bool bfs(int i, vector<long long>& res, unordered_map<int, vector<pair<int, int> > >& order, unordered_set<int>& seen) {
    queue<int> search;
    search.push(i);
    seen.insert(i);
    while (!search.empty()) {
        int node = search.front();
        search.pop();

        const vector<pair<int, int> >& neighbors = order[node];
        for (size_t j = 0; j < neighbors.size(); ++j) {
            long long dis = neighbors[j].first;
            int ch = neighbors[j].second;

            if (seen.find(ch) != seen.end()) {
                if (res[ch] != res[node] + dis) {
                    return false;
                }
            } else {
                search.push(ch);
                seen.insert(ch);
                res[ch] = res[node] + dis;  // Ensure this operation doesn't cause overflow
            }
        }
    }
    return true;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        unordered_map<int, vector<pair<int, int> > > order;
        vector<long long> res(n, 0);  // Use long long to prevent overflow
        for (int i = 0; i < m; ++i) {
            int a, b, d;
            cin >> a >> b >> d;
            order[b - 1].emplace_back(d, a - 1);
            order[a - 1].emplace_back(-d, b - 1);
        }

        unordered_set<int> seen;
        bool ans = true;
        for (int i = 0; i < n; ++i) {
            if (seen.find(i) == seen.end() && !bfs(i, res, order, seen)) {
                ans = false;
                break;
            }
        }

        if (ans) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    return 0;
}
