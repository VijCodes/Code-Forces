// ios::sync_with_stdio(0); cin.tie(0);
// This optimizes C++ I/O operations by disabling the synchronization 
// between the C and C++ standard streams and unties cin from cout. 
// Useful for reducing I/O time in competitive programming.

// #include <bits/stdc++.h>
// This is a GCC-specific include that includes most of the C++ STL libraries. 
// It's convenient for competitive programming, but not recommended for production code due to portability issues.

// typedef long long ll;
// typedef long double ld;
// These typedefs are used for convenience and readability. 
// They define 'll' as 'long long' and 'ld' as 'long double' to save time and reduce typing errors.

// #define all(x) (x).begin(), (x).end()
// Macro to get the entire range of a container. 
// Useful for functions that operate on ranges, like sort(all(v)).

// using namespace std;
// This line imports the entire std namespace. 
// Common in competitive programming for brevity but can lead to naming conflicts in larger projects.

// vector<ll> a(n);
// Efficient dynamic array initialization. 
// Vectors are preferable over built-in arrays for dynamic size and provided utility functions.

// *max_element(all(a))
// Efficient way to find the maximum element in a container. 
// Utilizes the STL algorithm for optimized performance.

// sort(all(v));
// Sorts the entire vector 'v'. 
// Utilizes the STL sort algorithm, which is typically a hybrid of quicksort, heapsort, and insertion sort.

// upper_bound(all(v), val) - v.begin();
// Finds the index of the first element greater than 'val' in a sorted vector. 
// Uses binary search internally for efficiency.

// lower_bound(all(v), val) - v.begin();
// Finds the index of the first element not less than 'val' in a sorted vector. 
// Also uses binary search, making it efficient for large datasets.