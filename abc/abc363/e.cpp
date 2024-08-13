#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

int H, W, Y;
vector<vector<int>> A;
vector<vector<int>> lands_state;

const vector<pair<int, int>> directions = { {-1, 0}, {0, 1}, {1, 0}, {0, -1} };

int cnt_sinking(int i, int j, int y) {
    deque<pair<int, int>> deq;
    deq.push_back({i, j});
    int sinking_cnt = 1;
    lands_state[i][j] = -1;

    while (!deq.empty()) {
        tie(i, j) = deq.front();
        deq.pop_front();
        for (auto [di, dj] : directions) {
            int ni = i + di;
            int nj = j + dj;
            if (0 <= ni && ni < H && 0 <= nj && nj < W) {
                if (lands_state[ni][nj] == 0) {
                    lands_state[ni][nj] = 1;
                }
                if (A[ni][nj] <= y && lands_state[ni][nj] != -1) {
                    deq.push_back({ni, nj});
                    sinking_cnt++;
                    lands_state[ni][nj] = -1;
                }
            }
        }
    }
    return sinking_cnt;
}

int main() {
    cin >> H >> W >> Y;
    A.resize(H, vector<int>(W));
    lands_state.resize(H, vector<int>(W, 0));
    
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            cin >> A[i][j];
            if (i == 0 || i == H - 1 || j == 0 || j == W - 1) {
                lands_state[i][j] = 1;
            }
        }
    }

    vector<tuple<int, int, int>> height_lands;
    for (int i = 0; i < H; ++i) {
        for (int j = 0; j < W; ++j) {
            height_lands.emplace_back(A[i][j], i, j);
        }
    }
    sort(height_lands.rbegin(), height_lands.rend());

    int not_sinking_land = H * W;
    for (int y = 1; y <= Y; ++y) {
        while (!height_lands.empty() && get<0>(height_lands.back()) <= y) {
            int i, j;
            tie(ignore, i, j) = height_lands.back();
            height_lands.pop_back();
            if (lands_state[i][j] == 1) {
                not_sinking_land -= cnt_sinking(i, j, y);
            }
        }
        cout << not_sinking_land << endl;
    }

    return 0;
}
