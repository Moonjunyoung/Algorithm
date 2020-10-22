#include <string>
#include <vector>
#include <queue>
#include <iostream>

using namespace std;




//상하좌우

int da[4]={-1,1,0,0};
int db[4]={0,0,-1,1};


int map[501][501];
bool check[501][501];

int main() {
    int n, m;
    cin >> n >> m;

    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            cin >> map[i][j];
        }
    } //map 입력


    int land=0;
    int max_land=0;


    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (map[i][j] == 0 || check[i][j]) //해당위치가 방문할수없으면
                continue;
                land++;
                int cnt=1;

                //bfs 부분
                queue<pair<int, int>> q;
                q.push(make_pair(i, j));
                check[i][j] = true;

                //큐에 넣은좌표 상하좌우에 확인
                while (!q.empty()) {
                    int x = q.front().first;
                    int y = q.front().second;
                    q.pop();
                    //상하 좌우 탐색
                    for (int i = 0; i < 4; i++) {
                        int dx = da[i] + x;
                        int dy = db[i] + y;
                        if (dx >= 0 && dy >= 0 && dx < n && dy < m) {
                            if (!check[dx][dy] && map[dx][dy]==1) { //방문가능하면
                                check[dx][dy] = true;
                                q.push(make_pair(dx, dy));
                                cnt++;
                            }
                        }
                    }
                }
            max_land=max(max_land,cnt);
        }
        }

    cout<<land<<'\n';
    cout<<max_land<<'\n';
    }
