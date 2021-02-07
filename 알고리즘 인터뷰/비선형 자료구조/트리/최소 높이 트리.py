"""
leetcode: minimum-height-trees
노드 개수와 무방향 그래프를 입력받아 트리가 최소 높이가 되는 루트의 목록을 리턴하라
"""
import collections
from typing import List


# class Solution:
#     def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
#







    # def findMinHeightTrees_prac(self, n: int, edges: List[List[int]]) -> List[int]:
    #     if n <= 1:
    #         return [0]
    #
    #     graph = collections.defaultdict(list)
    #
    #     for i, j in edges:
    #         graph[i].append(j)
    #         graph[j].append(i)
    #
    #     leaves = []
    #     for i in range(n + 1):
    #         if len(graph[i]) == 1:
    #             leaves.append(i)
    #
    #     while n > 2:
    #         n -= len(leaves)
    #         new_leaves = []
    #
    #         for leaf in leaves:
    #             neighbor = graph[leaf].pop()
    #             graph[neighbor].remove(leaf)
    #
    #             if len(graph[neighbor]) == 1:
    #                 new_leaves.append(neighbor)
    #
    #         leaves = new_leaves
    #
    #     return leaves