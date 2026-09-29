#迪杰斯特拉算法

import heapq


def dijkstra(graph, start):
    # dist[node] 表示起点 start 到 node 的最短距离
    dist = {node: float('inf') for node in graph}
    dist[start] = 0

    # pre[node] 记录最短路径中 node 的前驱节点
    pre = {node: None for node in graph}

    # 优先队列：(当前距离, 当前节点)
    pq = [(0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        # 如果当前距离不是最优距离，跳过
        if current_dist > dist[u]:
            continue

        # 遍历 u 的所有邻居
        for v, weight in graph[u]:
            new_dist = dist[u] + weight

            # 松弛操作
            if new_dist < dist[v]:
                dist[v] = new_dist
                pre[v] = u

                heapq.heappush(pq, (new_dist, v))

    return dist, pre


# 定义图
graph = {
    1: [(2, 2), (3, 5)],
    2: [(1, 2), (3, 1), (4, 4)],
    3: [(1, 5), (2, 1), (4, 1), (5, 6)],
    4: [(2, 4), (3, 1), (5, 3)],
    5: [(3, 6), (4, 3)]
}

# 从节点 1 开始
dist, pre = dijkstra(graph, 1)

# 输出最短距离
print("从节点 1 出发的最短距离：")
for node in dist:
    print(f"1 -> {node}：{dist[node]}")
