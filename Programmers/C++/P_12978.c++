#include <iostream>
#include <vector>
#include <queue>
using namespace std;

vector<pair<int, int>> v[55];
vector<int> Dist;

void Dijkstra(){
    priority_queue<pair<int,int>> pq;
    pq.push(make_pair(0,1));
    Dist[1] = 0;
    
    while(!pq.empty()){
        int cur_dist = -pq.top().first;
        int cur_node = pq.top().second;
        pq.pop();
        
        for(int i=0;i<v[cur_node].size();i++){
            int next_node = v[cur_node][i].first;
            int next_dist = v[cur_node][i].second;
            int dist = next_dist + cur_dist;
            
            if(Dist[next_node] > dist){
                Dist[next_node] = dist;
                pq.push(make_pair(-dist, next_node));
            }
        }
    }
}

int solution(int N, vector<vector<int> > road, int K) {
    Dist.resize(N+1, 2e9);
    for(int i=0;i<road.size();i++){
        int start = road[i][0];
        int end = road[i][1];
        int dis = road[i][2];
        
        v[start].push_back(make_pair(end, dis));
        v[end].push_back(make_pair(start, dis));
    }
    
    Dijkstra();
    
    int answer = 0;
    
    for(int i=1;i<=N;i++){
        if(Dist[i] <= K) answer++;
    }

    return answer;
}