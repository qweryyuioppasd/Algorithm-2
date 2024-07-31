def DFS(grapg,start,vistied=None):
    if vistied is None:
        vistied=set()
    vistied.add(start)
    print(start)
    for i in grapg[start]:
        if i not in vistied:
            DFS(grapg,i,vistied)

graph={
    'A':['B','C'],
    'B':['A','D'],
    'C':['A'],
    'D':['B']
}
DFS(graph,'C')