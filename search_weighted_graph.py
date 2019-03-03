def create_cost(graph):
    infinity = float("inf")
    cost = {}
    for node in graph:
        cost.setdefault(node, infinity)
        if node == 's':
            for key in graph[node].keys():
                cost[key] = graph[node][key]
    return cost

def create_parent():
    return {'a':'s','b':'s','c':None,'d':None,'e':None}




if __name__ == "__main__":
    graph = {'s': {'a': 5, 'b': 2}, 'a': {'c': 4, 'd': 2}, 'b': {'a': 8, 'd': 7}, 'c': {'d': 6, 'e': 3}, 'd': {'e': 1},
             'e': {}}
    processed=[]


    def find_lowest_cost_node(costs):
        lowest_cost = float("inf")
        lowest_cost_node = None
        for node in costs:
            cost = costs[node]
            if cost < lowest_cost and node not in processed:
                lowest_cost = cost
                lowest_cost_node = node
        return lowest_cost_node

    costs=create_cost(graph)
    parents=create_parent()
    node=find_lowest_cost_node(costs)       # 在未处理的节点中找出开销最小的节点
    while node is not None:     # 如果开销最小的节点不为空
        cost=costs[node]        # 得到开销最小节点的开销
        neighbors=graph[node]   # 得到此节点的邻居的dict
        for n in neighbors.keys():  # 遍历当前节点的所有邻居
            new_cost=cost+neighbors[n]  # 得到经过此节点到邻居的开销
            if costs[n]>new_cost:       # 如果经当前节点前往邻居更近
                costs[n]=new_cost       # 更新开销矩阵
                parents[n]=node         # 更新邻居的父节点为当前节点
        processed.append(node)          # 将当前结点标记为已处理过
        node=find_lowest_cost_node(costs)   # 找出接下来要处理的节点，并循环

