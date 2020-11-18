#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <string.h>


int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};

using namespace std;


int map[51][51];
bool check[51][51];



int m,n,k;

void dfs(int x,int y){
    if(!check[x][y]){
        check[x][y]=1;
    }

    for(int i=0;i<4;i++){
        int da=dx[i]+x;
        int db=dy[i]+y;
        if(da>=0 && db>=0 && da<n && db<m) {
            if (!check[da][db] && map[da][db]==1) { //배추가 심어져잇는곳
                dfs(da, db);
            }
        }

    }

}


int main() {
    int t;
    cin>>t;
    while(t--){
        cin>>m>>n>>k;
        memset(check, false, sizeof(check));
        memset(map, 0, sizeof(map));

        for(int i=0;i<k;i++){
            int a,b;
            cin>>a>>b;
            map[b][a]=1;
        }

        int cnt=0;
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(map[i][j]==1 && !check[i][j]){
                    dfs(i,j);
                    cnt++;
                }
            }
        }
        cout<<cnt<<'\n';
    }



}

