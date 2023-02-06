class Solution {
    public static void dfs(ArrayList<ArrayList<Integer>> adj,int node,int visit[]){
        visit[node]=1;
        for(Integer neigh:adj.get(node)){
            if(visit[neigh]==0){
                dfs(adj,neigh,visit);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int v=isConnected.length;
        ArrayList<ArrayList<Integer>> adj=new ArrayList<ArrayList<Integer>>();
        for(int i=0;i<v;i++){
            adj.add(new ArrayList<Integer>());
        }
        for(int i=0;i<v;i++){
            for(int j=0;j<v;j++){
                if(isConnected[i][j]==1){
                    adj.get(i).add(j);
                    adj.get(j).add(i);
                }
            }
        }
        int visit[]=new int[v];
        int c=0;
        for(int i=0;i<v;i++){
            if(visit[i]==0){
                c++;
                dfs(adj,i,visit);
            }
        }
        return c;
        
    }
}