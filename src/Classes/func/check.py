class Checker:
    
    def check(M, size, winFactor):
        row = [0 for _ in range(size)]
        colunm = [0 for _ in range(size)]
        
        digs = {
            "0": 0, "1": 0
        }
        
        for iI, i in enumerate(M):
            for iJ, j in enumerate(i):
                row[iI] += j.ownerVal
                colunm[iJ] += j.ownerVal
                
                if(iJ == iI):
                    digs["0"] += j.ownerVal
                if (size-1-iI == iJ):
                    digs["1"] += j.ownerVal
                
        for i in row:
            if abs(i) >= winFactor: return i/abs(i)
    
        for j in colunm:
            if abs(j) >= winFactor: return j/abs(j)
        
        for d in digs:
            if abs(digs[d]) >= winFactor: return digs[d]/abs(digs[d])
        
        return 0
        