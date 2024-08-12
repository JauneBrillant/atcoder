#include <iostream>
#include <vector>
#include <set>
#include <tuple>

using namespace std;

int H, W;
vector<string> C;
vector<pair<int, int>> dir = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

bool dfs(int i, int j, set<pair<int, int>>& visited, int depth, int start_i, int start_j) {
    visited.insert({i, j});

    for (const auto& d : dir) {
        int ni = i + d.first;
        int nj = j + d.second;

        if (0 <= ni && ni < H && 0 <= nj && nj < W) {
            if (ni == start_i && nj == start_j && depth >= 3) {
                return true;
            }
            if (visited.find({ni, nj}) == visited.end() && C[ni][nj] == '.') {
                if (dfs(ni, nj, visited, depth + 1, start_i, start_j)) {
                    return true;
                }
            }
        }
    }
    return false;
}

int main() {
    cin >> H >> W;
    C.resize(H);

    for (int i = 0; i < H; ++i) {
        cin >> C[i];
    }

    // Find the starting point 'S'
    int start_i = -1, start_j = -1;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            if (C[i][j] == 'S') {
                start_i = i;
                start_j = j;
                break;
            }
        }
        if (start_i != -1) break;
    }

    set<pair<int, int>> visited;
    bool result = dfs(start_i, start_j, visited, 0, start_i, start_j);

    cout << (result ? "Yes" : "No") << endl;

  }

