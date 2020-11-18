#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>
#include <string.h>



//나이트가 이동할수있는위치
int dx[8] = {-2,-1,1,2,2,1,-1,-2};
int dy[8] = {1,2,2,1,-1,-2,-2,-1};
using namespace std;


int map[301][301];
bool check[301][301];




int main() {
    int n;
    cin>>n;

    while (n--){
        int l;
        queue<pair<int,int>>q;
        int a,b,c,d;
        cin>>l;
        cin>>a>>b;
        cin>>c>>d;


        memset(check, false, sizeof(check));
        memset(map, 0, sizeof(map));
        //초기화

        q.push(make_pair(a,b));
        //나이트 초기위치
        check[a][b]=true;

        while(!q.empty()){
            int cur_x=q.front().first;
            int cur_y=q.front().second;

            q.pop();

            for(int i=0;i<8;i++){
                int d_x=cur_x+dx[i];
                int d_y=cur_y+dy[i];

                if(d_x>=0 && d_y>=0 && d_x<l && d_y<l){
                    if(map[d_x][d_y]==0 && !check[d_x][d_y]){
                        q.push(make_pair(d_x,d_y));
                        check[d_x][d_y]=true;
                        map[d_x][d_y]=map[cur_x][cur_y]+1;

                    }
                }

            }
        }

        cout<<map[c][d]<<'\n';

        }

    }

