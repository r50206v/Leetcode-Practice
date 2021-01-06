"""
  
The data in STDIN (lower left tab labeled "Input") is the input data for a portfolio structure where each
identifier in the first column represents a "parent" portfolio and each identifier in the second column
represents a "child" portfolio.
  
For example, the dataset:
  
A,B
A,E
C,B
C,D
D,F
  
would indicate a portfolio structure where the following statements are true:
- there are two root portfolios, A and C
- A has the direct children B, E
- C has the direct children B, D
- D has the direct child F
- B is a "duplicate" because it is the child of both A and C
- the longest portfolio path is C -> D -> F of path length 3
  
Your task is to ingest the data and produce answers for the following questions:
  
1) What are the root portfolios?
  
2) What are the duplicate portfolios?
  
3) What is the longest path? (both the nodes in the path and its length)
  
"""
import collections
class PortfolioAPI:
    
    def __init__(self):
        self.counter = collections.Counter()
        self.adjList = collections.defaultdict(list)
        self.duplicates = []
        self.root = []
         
    def add_arc(self, parent, child):
        print(f"Adding the following parent-child relationship: ({parent}) -> ({child})")
        self.adjList[parent].append(child)
        self.counter[parent] += 1
        self.counter[child] += 1
          
    def get_root_portfolio(self):
        all_child = set(sum(list(self.adjList.values()), []))
        all_parent = set(list(self.counter.keys()))
        self.root = list(all_parent - all_child)
        return self.root
        
    def get_duplicates(self):
        self.duplicates = []
        for k, v in self.counter.items():
            if v > 1:
                self.duplicates.append(k)
        return self.duplicates
    
    def find_longest_path(self):
        self.get_root_portfolio()
        
        def dfs(graph, v, path=None, seen=None):
            all_paths = []
            if not path: path = [v]
            if not seen: seen = set([])
            seen.add(v)
            
            if len(graph[v]) == 0:
                all_paths.extend([tuple(path)])
                return all_paths

            for n in graph[v]:
                if n not in seen:
                    n_path = path + [n]
                    seen.add(n)
                    all_paths.extend(dfs(graph, n, n_path, seen))
            return all_paths

        
        all_path_from_roots = []
        for r in self.root:
            all_path_from_roots.extend(dfs(self.adjList, r))
        
        finalPaths = []
        max_length = len(max(all_path_from_roots, key=len))
        for a in all_path_from_roots:
            if len(a) == max_length:
                finalPaths.append(a)
        return finalPaths
        
        
        


if __name__ == '__main__':
    import fileinput
      
    api = PortfolioAPI()
    
    input = '''ROBOT_AUTO,Robot_Contra
ROBOT_SUM,ROBOT_AUTO
ROBOT_SUM,Robot_Broker
ROBOT_SUM,Robot_Click
ROBOT_SUM,Robot
CRYPTO,bittrex
CRYPTO,xbt_cfe
CRYPTO,deribit
CRYPTO,bitmex
CRYPTO,okex
CRYPTO,gemini
CRYPTO,bitstamp
CRYPTO,binance
CRYPTO,ledgerx
CRYPTO,bitfinex
CRYPTO,btc_cme
CRYPTO,gdax
CRYPTO,itbit
ABN_I,ROBOT_SUM
ABN_I,Simba
ABN_I,RusSnP
ABN_I,FloorTrades
ABN_I,Blackbird
ABN_I,VX_Quoting
ABN_I,Nas_RV
ABN_I,DeltaOne1
ABN_I,SnP_Click
ABN_I,Dispersion
ABN_I,VIXFuturesArb
ABN_I,DeltaOne2
ABN_I,NasdaqBroker
ABN_I,NasSnP
ABN_I,Russell_Click
ABN_I,EquityDP
ABN_I,RusNas
ABN_I,VIXroll
ABN_I,Equity_Basket
WINNEBAGO,WinnebagoClick
WINNEBAGO,WinnebagoTransfer
WINNEBAGO,WinnebagoBrokerTrade
WINNEBAGO,WinnebagoFloorTrade
ABN_C,WINNEBAGO
ABN_C,CRYPTO
ABN_C,holding_listed
ABN_C,DeltaPool
ABN_C,DeltaManagement
ABN_C,GrainsAutomated
ABN_C,depot_c
ABN_C,OTCHedges
ABN_C,btc_cme
ABN_C,FloorTrades
ABN_C,Barn
ABN_C,bitmex
TOTAL,JuniorTraining
TOTAL,Blackbird
TOTAL,Broker_Trades
TOTAL,Click_Trades
TOTAL,Day_Trades
GRAND_TOTAL,TOTAL
GRAND_TOTAL,ABN_I
GRAND_TOTAL,ABN_C'''

    for line in input.split("\n"):
        api.add_arc(*line.strip().split(','))

    print(api.adjList)
    print(api.get_duplicates())
    print(api.get_root_portfolio())
    print(api.find_longest_path())

