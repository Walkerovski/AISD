#include <bits/stdc++.h>
#include <fstream>
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


int main(int argc, char *argv[])
{
    if(argc != 2){
        cout << "Podaj nazwe pliku!";
        return 0;
    }
    ifstream infile(argv[1]);
    int n = 0, m = 0;
    string line;
    pair<int, int> a = {0, 0}, b;
    while(getline(infile, line)){
        for(int i = 0; i < line.size(); i++){
            Tab[n + 1][i + 1] = (int)line[i] - (int)'0';
            if(Tab[n + 1][i + 1] == 0)
                if(a == make_pair(0, 0))
                    a = {n + 1, i + 1};
                else
                    b = {n + 1, i + 1};
        }
        if(m == 0) m = line.size();
        n++;
    }
    infile.close();
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