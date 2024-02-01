#include <iostream>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;

// Fast I/O
void fast_io() {
    ios::sync_with_stdio(0);
    cin.tie(0);
    cout.tie(0);
}

// Main processing function (to avoid global variables)
int process_segments(int n, int m) {
    map<int, int> adds, removals, cEnds, cStarts;
    vector<int> segs; 
    segs.reserve(2 * n); // Reserve capacity

    for (int i = 0; i < n; ++i) {
        int l, r;
        cin >> l >> r;
        --l; --r; // 0-based indexing

        segs.push_back(l);
        segs.push_back(r);
        adds[l]++;
        if (r < m) removals[r]++;
        if (r == m - 1) cEnds[l]++;
        if (l == 0) cStarts[r]++;
    }

    sort(segs.begin(), segs.end());
    segs.erase(unique(segs.begin(), segs.end()), segs.end()); // Remove duplicates

    int res = 0, currMax = 0, start = adds[0], end = 0;

    for (int i : segs) {
        currMax += adds[i];
        end += cEnds[i];
        res = max(res, currMax - min(end, start));
        start -= cStarts[i];
        currMax -= removals[i];
    }

    return res;
}

int main() {
    fast_io();

    int t;
    cin >> t;

    while (t--) {
        int n, m;
        cin >> n >> m;
        cout << process_segments(n, m) << '\n';
    }

    return 0;
}
