#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <string.h>


int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

using namespace std;


int dist[101][101];
int map[101][101];
bool check[101][101];

int answer=0;

int n;

void dfs(int x,int y){
    if(!check[x][y]){
        check[x][y]=1;
    }

    for(int i=0;i<4;i++){
        int da=dx[i]+x;
        int db=dy[i]+y;
        if(da>=0 && db>=0 && da<n && db<n) {
            if (!check[da][db] && dist[da][db]==1) { //물이 안잠기는 영역이면 방문
                dfs(da, db);
            }
        }

    }

}


int main() {
    cin>>n;

    int min_weight=999;
    int max_weight=-1;

    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            int size=0;
            cin>>size;
            map[i][j]=size;
            min_weight=min(size,min_weight);
            max_weight=max(size,max_weight);
        }
    }


    for(int q=0;q<=max_weight;q++){ //물의 높이가 0인점부터

        int cnt=0;

        memset(check, false, sizeof(check));
        memset(dist, 0, sizeof(dist));

        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(map[i][j]>q){ //물에 안잠기는 영역만넣음
                    dist[i][j]=1; //물이 안잠기는영역
                }
            }
        }


        for(int i=0;i<n;i++){
            for(int j=0;j<n;j++){
                if(dist[i][j]==1 && !check[i][j]){ //물에 안잠기는지역
                    dfs(i,j);
                    cnt++;
                }
            }
        }
        answer=max(cnt,answer);
    }

    cout<<answer<<'\n';


}

