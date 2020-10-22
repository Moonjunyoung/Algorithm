#include <string>
#include <vector>
#include <queue>
#include <iostream>


using namespace std;



int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

int map[101][101];
int check[101][101];

int main() {
    int n,m;
    queue<pair<int,int>>q;

    cin>>n>>m;

    for(int i=0;i<n;i++){
        for(int j=0;j<m;j++){
            scanf("%1d",&map[i][j]);
        }
    }


    q.push(make_pair(0,0));

    check[0][0]=1; //0,0 시작점

    int cnt=1;
    while(!q.empty()){
        int x=q.front().first; //시작점좌표
        int y=q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int da=dx[i]+x;
            int db=dy[i]+y;
            if(da>=0 && db>=0 && da<n && db<m){
                if(check[da][db]==0 && map[da][db]) {
                    q.push(make_pair(da,db));
                    check[da][db]=check[x][y]+1; //시작점 좌표에서 한칸이동했으므로  시작점좌표값 +1
                }
            }
        } //주변 상하 좌우 값들 다 초기화
        }

    cout<<check[n-1][m-1]<<'\n';



}
