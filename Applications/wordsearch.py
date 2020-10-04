class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        Trie=lambda:defaultdict(Trie)
        trie=Trie()
        END=True
        reduce(dict.__getitem__,word,trie)[END]=word
        d=defaultdict(int)
        d[word]=0
        def dfs(i,j,t):
            if t[END]:
                d[word]=1
                return()
            if(d[word]):
                return(1)
            letter=board[i][j]
            board[i][j]=""
            if(i>0 and board[i-1][j] in t):
                dfs(i-1,j,t[board[i-1][j]])
            if(i<(len(board)-1) and board[i+1][j] in t):
                dfs(i+1,j,t[board[i+1][j]])
            if(j>0 and board[i][j-1] in t):
                dfs(i,j-1,t[board[i][j-1]])
            if(j<(len(board[0])-1) and board[i][j+1] in t):
                dfs(i,j+1,t[board[i][j+1]])
            board[i][j]=letter
            return()
                
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] in trie):
                    dfs(i,j,trie[board[i][j]])
        
        return(d[word])
