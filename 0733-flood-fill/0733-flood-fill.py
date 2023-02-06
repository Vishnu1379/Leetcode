class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if(image[sr][sc]==color):
            return image
        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
    def dfs(self,image,sr,sc,color,curr):
        if(sr<0 or sr>=len(image) or sc<0 or sc>=len(image[0]) or curr!=image[sr][sc]):
            return 
        image[sr][sc]=color
        self.dfs(image,sr+1,sc,color,curr)
        self.dfs(image,sr-1,sc,color,curr)
        self.dfs(image,sr,sc+1,color,curr)
        self.dfs(image,sr,sc-1,color,curr)
        
        