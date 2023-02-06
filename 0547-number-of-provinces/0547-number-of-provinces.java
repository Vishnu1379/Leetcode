class Solution {
    public int findCircleNum(int[][] isConnected) {
        int v=isConnected.length;
        boolean[]visit=new boolean[v];
        int count=0;
        for(int i=0;i<v;i++){
            if(!visit[i]){
                count++;
                dfs(isConnected,i,visit);
            }
        }
        return count;
    }
    private void dfs(int[][] isConnected,int i,boolean[] visit){
        for(int j=0;j<isConnected[i].length;j++){
            if(!visit[j] && isConnected[i][j]!=0){
                visit[j]=true;
                dfs(isConnected,j,visit);
            }
        }        
    }
}