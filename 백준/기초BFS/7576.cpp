#include <string>
#include <vector>
#include <queue>
#include <iostream>


using namespace std;



int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

int map[1001][1001];
bool check[1001][1001];
int dist[1001][1001];

int main() {
    int n,m;
    queue<pair<int,int>>q;

    cin>>n>>m;

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
        scanf("%d",&map[i][j]);
        }
    }

    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(map[i][j]==1){
                q.push(make_pair(i,j));
            }
         }
    }

    while(!q.empty()){
        int x=q.front().first;
        int y=q.front().second;
        q.pop();

        for(int i=0;i<4;i++){
            int a=dx[i]+x;
            int b=dy[i]+y;
            if(a>=0 && b>=0 && a<m && b<n) {
                if (map[a][b] == 0 && check[a][b] == false) { //덜익은토마토면
                    check[a][b] = true; //방문
                    q.push(make_pair(a,b));//큐에넣고
                    dist[a][b]=dist[x][y]+1; //기록
                }
            }
        }
    }
    int answer=0;
    for(int i=0;i<m;i++){
        for(int j=0;j<n;j++){
            if(!check[i][j] && map[i][j]==0) { //덜익은게하나라도잇으면
                answer=-1;
                break;
            }
            else {
                answer = max(answer, dist[i][j]);
            }
        }
        if(answer==-1){
            break;
        }
    }
    cout<<answer<<'\n';






}
