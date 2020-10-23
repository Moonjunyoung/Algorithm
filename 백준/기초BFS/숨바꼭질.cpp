#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <functional>
#include <cstring>


const int MAX = 200000;
bool check[MAX + 1];
int dist[MAX + 1];

using namespace std;


int main(void){
	queue<int>q;
	int n, k;
	cin >> n >> k;
    
    dist[n]=0;
    check[n]=true;
	q.push(n); //현재위치를 넣음

	while (!q.empty()) {
		int cur = q.front();
		q.pop();


		if (cur - 1 >= 0 && check[cur-1]==false) {
			q.push(cur - 1);
			dist[cur - 1] = dist[cur] + 1;
			check[cur - 1] = true;
		}
		if (cur * 2 < MAX && check[cur*2] == false) {
			q.push(cur*2);
			dist[cur *2] = dist[cur] + 1;
			check[cur * 2] = true;
		}
		if (cur + 1 < MAX && check[cur + 1] == false) {
			q.push(cur + 1);
			dist[cur + 1] = dist[cur] + 1;
			check[cur + 1] = true;
		}


	}


	cout << dist[k] << '\n';







	return 0;

}