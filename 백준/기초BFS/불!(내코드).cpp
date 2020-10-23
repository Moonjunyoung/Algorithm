#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <algorithm>

using namespace std;



// 논리는 맞는데 왜 메모리초과가 계속뜨는지모르겟음 빡쳐서 그냥 다른사람 코드 넣어서
//제출함

int dx[4]={-1,1,0,0};
int dy[4]={0,0,-1,1};

string map[1002];
int human[1002][1002];
int fire[1002][1002];


int main() {
    int r,c;
    queue<pair<int,int>>q;

    queue<pair<int,int>>q2;


    cin>>r>>c;

    for(int i=0;i<r;i++){
        cin>>map[i];
    }



    for(int i=0;i<r;i++){
        fill(human[i],human[i]+c,-1);
        fill(fire[i],fire[i]+c,-1);

    }


    for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            if(map[i][j]=='J'){ //지훈이의 위치
                q.push(make_pair(i,j));
                human[i][j]=0;
            }

            if(map[i][j]=='F'){//불의위치
                q2.push(make_pair(i,j));
                fire[i][j]=0;
            }
        }
    }



    while(!q2.empty()){ //불 계산
        int a=q2.front().first;
        int b=q2.front().second;
        q2.pop();

        for(int i=0;i<4;i++){
            int da=dx[i]+a;
            int db=dy[i]+b;

            if(da>=0 && db>=0 && da<r && db<c){
                if(map[da][db]=='.' && fire[da][db]==-1){
                    fire[da][db]=fire[a][b]+1;
                    q2.push(make_pair(da,db));
                }
            }
        }
    }


    while(!q.empty()){ //지훈이 계산
        int cur_x=q.front().first; //현재 지훈이의 위치
        int cur_y=q.front().second;
        q.pop();

        for(int i=0;i<4;i++){ //불을 피할수있는곳을찾는다.
            int da=dx[i]+cur_x;
            int db=dy[i]+cur_y;

            if(da<0 || db<0 || da>=r || db>=c) { //맵 밖에있는경우 = 탈출 성공
                cout<<human[cur_x][cur_y]+1<<'\n';
                return 0;
            }

            else { //맵안에 있는경우
                if (map[da][db] == '.' && human[da][db] + 1 < fire[da][db]) { //갈수있는경우
                    human[da][db] = human[cur_x][cur_y] + 1; //지훈이가 다음으로 갈곳을 계산
                    q.push(make_pair(da, db)); //다음으로 갈곳을 넣는다.
                }
            }
        }
    }

    cout<<"IMPOSSIBLE"<<'\n';


}
