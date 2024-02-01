#include <iostream>
#include <vector>
#include <set>
#include <stack>
#include <tuple>

using namespace std;

int main() {
    int t;
    cin >> t; // Number of test cases

    while (t--) {
        int a, b, c;
        cin >> a >> b >> c; // Input for a, b, and c

        vector<int> res(3, 0);
        stack<tuple<int, int, int>> stack;
        set<tuple<int, int, int>> seen;

        stack.push(tuple<int, int, int>(a, b, c));
        seen.insert(tuple<int, int, int>(a, b, c));

        while (!stack.empty()) {
            tie(a, b, c) = stack.top();
            stack.pop();

            if (a == 0 && b == 0 && c > 0) {
                res[2] = 1;
            } else if (b == 0 && c == 0 && a > 0) {
                res[0] = 1;
            } else if (a == 0 && c == 0 && b > 0) {
                res[1] = 1;
            } else {
                if (a > 0 && b > 0 && seen.find(tuple<int, int, int>(a - 1, b - 1, c + 1)) == seen.end()) {
                    stack.push(tuple<int, int, int>(a - 1, b - 1, c + 1));
                    seen.insert(tuple<int, int, int>(a - 1, b - 1, c + 1));
                }
                if (b > 0 && c > 0 && seen.find(tuple<int, int, int>(a + 1, b - 1, c - 1)) == seen.end()) {
                    stack.push(tuple<int, int, int>(a + 1, b - 1, c - 1));
                    seen.insert(tuple<int, int, int>(a + 1, b - 1, c - 1));
                }
                if (a > 0 && c > 0 && seen.find(tuple<int, int, int>(a - 1, b + 1, c - 1)) == seen.end()) {
                    stack.push(tuple<int, int, int>(a - 1, b + 1, c - 1));
                    seen.insert(tuple<int, int, int>(a - 1, b + 1, c - 1));
                }
            }
        }

        // Output the result
        for (int i = 0; i < 3; ++i) {
            cout << res[i];
            if (i < 2) cout << " "; // Add space between numbers
        }
        cout << endl; // Newline for each test case
    }
    return 0;
}
