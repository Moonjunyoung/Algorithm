#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;

int m, n, k;
int dx[4] = {1,0,-1,0};
int dy[4] = {0,1,0,-1};
int map[110][110];
bool check[110][110];

int ans=0;

void dfs(int x,int y){

    if(!check[x][y]) {
        check[x][y] = true;
        ans++;
    }

    for(int i=0;i<4;i++){
        int da=dx[i]+x;
        int db=dy[i]+y;

        if(da>=0 && db>=0 && da<m && db<n){
            if (!check[da][db] && map[da][db]==0) { //미방문이고 색칠이 안되어있을시
                dfs(da, db);
            }
        }
    }

}


int main() {

    int x1, y1, x2, y2;
    vector<int>answer;

    cin >> m;
    cin >> n;
    cin >> k;

    while(k--){
    int x1,x2,y1,y2;
    cin>>x1>>y1;
    cin>>x2>>y2;

    //직사각형 x는가로길이 y는 세로길이

    for(int i=y1;i<y2;i++){
        for(int j=x1;j<x2;j++){
            if(map[i][j]==0){
                 map[i][j]=1; //색칠하기
            }
        }
    }
    }
    int cnt=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(map[i][j]==0 && !check[i][j]){//미방문일시
                dfs(i,j);
                cnt++;
                answer.push_back(ans);
                ans=0;
            }
        }
    }

    cout<<cnt<<'\n';
    sort(answer.begin(),answer.end());
    for(int i=0;i<answer.size();i++){
        cout<<answer[i]<<' ';
    }

}
