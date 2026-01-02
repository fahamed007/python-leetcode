#https://leetcode.com/problems/lru-cache/description/
#146. LRU Cache

class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.next=None
        self.prev=None

class DLL:
    def __init__(self):
        self.low=Node(0,0)
        self.high=Node(0,0)
        self.low.next=self.high
        self.high.prev=self.low

    def insert(self,node):
        prv=self.high.prev
        node.prev,node.next=self.high.prev,self.high
        prv.next,self.high.prev=node,node
    
    def remove(self,node):
        prv,nxt=node.prev,node.next
        prv.next,nxt.prev=nxt,prv
        node.prev,node.next=None,None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity =capacity
        self.cache ={}
        self.dll=DLL()

    def get(self, key: int) -> int:
        if key in self.cache:
            self.dll.remove(self.cache[key])
            self.dll.insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.dll.remove(self.cache[key])
        new_node=Node(key,value)
        self.cache[key] =new_node
        self.dll.insert(new_node)
        if len(self.cache) > self.capacity:
            low_prio_node=self.dll.low.next
            self.dll.remove(low_prio_node)
            low_key=low_prio_node.key
            del self.cache[low_key]

    

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
