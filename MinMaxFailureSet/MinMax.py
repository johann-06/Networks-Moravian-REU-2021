import itertools

def IsTrivial(G):
    '''
    Check if a graph is trivial, couldnt figure out how to properly import the graphs.CompleteGraph() method
    Args:
        G::Graph // Graph object to check if its trivial
    Return:
        ::booolean // boolean of wheather or not G is trivial
    '''
    if G.order()==1:
        return True
    else:
        return False

def KPairs(k,G):
    '''
    function to get all posible k-pairs of vertices of a graph G, this essentialy returns all elements of the power set of V(G) with cardinality exatcly k
    Args:
        k::Int // Integer that determines the cardinality of the set of vertices
        G::Graph // graph object to get the k-pairs from
    Returns:
        pairs::itertools.combinations // iterable of all pairs
    '''
    #get the vertex set
    V = G.vertices()
    #caclulate the combinations
    return itertools.combinations(V,k)

def Diff(li1, li2):
    return (set(li1) - set(li2))

def FailTest(func,G):
    '''
    Function to calculate the cardinality of minimum failure set of a component of a graph G.
    Args:
        func::funcion // function to check if graph isa failure, must be a function (not graph class), and return a boolean
        
    Returns;
        N::Int // the cardinality of the smallest set it touk to make the graph fail
    '''
    
    #get an iterable [1,n-1] to check for k-pairs
    Ks = range(1,G.order())
    
    #init the low and end value
    low, high = None, None
    
    #check if the graph itself fails, that is does the 0-pair case work then set low to 0
    failed = not ( (func(G)) or IsTrivial(G) )
    if failed:
        print("Component already failed")
        low = 0
    else:
        print("Component Not Failed already")
        pass
        
    for k in Ks:
        #load up the pairs to remove
        print("Gening Pairs")
        pairs = KPairs(k,G)
        print("Finished Gening pairs")
        
        print(f"Checking {k} pairs")
        
        #loop over the found pairs
        for VCandidates in pairs:
            
            #make an induced subrapg without the candidates
            V_H = Diff(G.vertices(),VCandidates)
            H = G.subgraph(V_H)

            #check if the graph has failed
            failed = not func(H)
            
            #if the graph failed
            if ( failed or IsTrivial(H) ):
                #since this failed check if we have found the low yet
                if low==None:
                    print("Found Minimum set for component")
                    low = k

                #in the case the high hasnt been set or is lower reset the high
                if (high==None) or (high < k):
                    high = k
    return (low,high)

def FailTestNoPrint(func,G):
    '''
    Function to calculate the cardinality of minimum failure set of a component of a graph G.
    Args:
        func::funcion // function to check if graph isa failure, must be a function (not graph class), and return a boolean
        
    Returns;
        N::Int // the cardinality of the smallest set it touk to make the graph fail
    '''
    
    #get an iterable [1,n-1] to check for k-pairs
    Ks = range(1,G.order())
    
    #init the low and end value
    low, high = None, None
    
    #check if the graph itself fails, that is does the 0-pair case work then set low to 0
    failed = not ( (func(G)) or IsTrivial(G) )
    if failed:
        low = 0
        
    for k in Ks:
        #load up the pairs to remove
        pairs = KPairs(k,G)
        
        #loop over the found pairs
        for VCandidates in pairs:
            
            #make an induced subrapg without the candidates
            V_H = Diff(G.vertices(),VCandidates)
            H = G.subgraph(V_H)

            #check if the graph has failed
            failed = not func(H)
            
            #if the graph failed
            if ( failed or IsTrivial(H) ):
                #since this failed check if we have found the low yet
                if low==None:
                    low = k

                #in the case the high hasnt been set or is lower reset the high
                if (high==None) or (high < k):
                    high = k
    return (low,high)