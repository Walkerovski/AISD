#include <bits/stdc++.h>
#define f first
#define s second
using namespace std;
int Tab[1021][1021];
bool B[1021][1021];
int Ans[1021][1021];
vector < pair < pair<int, int>, int> > V[1021][1024];


void Dijkstra(pair<int, int> a, pair<int, int> b, int n, int m)
{
    //                          .f.f      .f.s.f .f.s.s           .s
    //                          cost      f axis s axis           rout
    priority_queue< pair< pair< int, pair<int, int> >, vector<pair<int, int>  > > > Q;
    B[a.f][a.s] = 1;
    vector<pair<int,int>>Help;
    Help.push_back(a);
    for(auto it = V[a.f][a.s].begin(); it != V[a.f][a.s].end(); it++)
        Q.push({{-it -> s, {it -> f.f, it -> f.s}}, Help});
    while(!Q.empty())
    {
        int cost = Q.top().f.f;
        a.f = Q.top().f.s.f;
        a.s = Q.top().f.s.s;
        Help = Q.top().s;
        Help.push_back(a);
        if(a == b)
        {
            cout << "\n\n" << -cost << "\n\n";
            for(auto it = Help.begin(); it != Help.end(); it++)
                Ans[it -> f][it -> s] = Tab[it -> f][it -> s];
            return;
        }
        if(!B[a.f][a.s])
        {
            B[a.f][a.s] = 1;
            for(auto it = V[a.f][a.s].begin(); it != V[a.f][a.s].end(); it++)
                if(!B[it -> f.f][it -> f.s])
                    Q.push({{cost - it -> s, {it -> f.f, it -> f.s}}, Help});
        }
        Q.pop();
    }
}


int main()
{
    int n, m;
    cin >> n >> m;
    pair<int, int> a = {0, 0}, b;
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            cin >> Tab[i][j];
            if(Tab[i][j] == 0)
                if(a == make_pair(0, 0))
                    a = {i, j};
                else
                    b = {i, j};
        }
    }

    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            V[i - 1][j].push_back({{i, j},Tab[i][j]});
            V[i + 1][j].push_back({{i, j},Tab[i][j]});
            V[i][j - 1].push_back({{i, j}, Tab[i][j]});
            V[i][j + 1].push_back({{i, j}, Tab[i][j]});
        }
    }
    Dijkstra(a, b, n, m);
    for(int i = 1; i <= n; i++)
    {
        for(int j = 1; j <= m; j++)
        {
            if(Ans[i][j] || a == make_pair(i,j) || b == make_pair(i,j))
                cout << Tab[i][j];
            else
                cout << " ";
        }
        cout << "\n";
    }
}