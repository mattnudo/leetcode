class Solution:
    #complexity: O(n*m) mem: O(1)
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        def dfs(image: List[List[int]], sr: int, sc: int, color: int, og_color:int):
            #base: if the color matches new color, if out of bounds, return
            if(out_of_bounds(image, sr,sc) or image[sr][sc]==color or image[sr][sc] != og_color):
                return image
            #change color
            before_color = image[sr][sc]
            image[sr][sc] = color
            #dfs on adjacent cells
            dfs(image, sr+1, sc, color, before_color )
            dfs(image, sr, sc+1, color, before_color )
            dfs(image, sr-1, sc, color, before_color )
            dfs(image, sr, sc-1, color, before_color )

            return image
            
        def out_of_bounds(images: List[List[int]], sr: int, sc: int):
            if(sr < 0 or sr >= len(image) or sc<0 or sc >= len(image[0]) ):
                return True
            return False

        #dfs on adjacent pixels
        if(len(image)==0):
            return []
        dfs(image, sr, sc, color, image[sr][sc] )
        
        return image