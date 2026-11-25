from __future__ import annotations
import json
class QuadTree:
    NB_NODES : int = 4
    def __init__(self, hg: bool | QuadTree, hd: bool | QuadTree, bd: bool | QuadTree,bg: bool | QuadTree):
        pass

    @property
    def depth(self) -> int:
        """ Recursion depth of the quadtree"""
    
        return 1

    @staticmethod
    def from_file(filename: list) -> QuadTree:
        with open(filename, "r", encoding='utf-8') as f:
            lines = f.read()
            l = json.loads(lines)
        print (l)
        return l

    @staticmethod
    def fromList(data: list) -> QuadTree:
        """ Generates a Quadtree from a list representation"""
        return QuadTree(data[0], data[1], data[2], data[3])
        pass

class TkQuadTree(QuadTree):
    def paint(self):
        """ TK representation of a Quadtree"""        
        pass
