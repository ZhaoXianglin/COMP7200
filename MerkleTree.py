from base64 import decodestring
from collections import OrderedDict
from Transaction import Transaction
from Crypto.Hash import SHA256

class MerkleTree(object):
    def __init__(self,transcation=None):
        #传入的是交易列表
        self.ori_trans_list = transcation.copy()
        self.trans_list = transcation.copy()
        # 交易列表构成的有序字典
        self.trans_tree = OrderedDict()
    
    def createtree(self):
        trans_len = len(self.trans_list)
        if trans_len < 1:
            return False
        if trans_len > 1:
            if trans_len % 2 is 1:
                self.trans_list.extend(self.trans_list[-1])
                trans_len += 1
            temp_list = []
            for i in range(0,trans_len,2):
                # 左右子叶
                left_leaf = self.trans_list[i]
                right_leaf = self.trans_list[i+1]
                # 判断是不是原始Transaction对象,是的话取交易
                if isinstance(left_leaf,Transaction):
                    left_leaf = left_leaf.txid
                    right_leaf = right_leaf.txid
                # 创建左右节点hash
                left_hash = SHA256.new(left_leaf.encode()).hexdigest()
                right_hash = SHA256.new(right_leaf.encode()).hexdigest()
                # 放到树中，自底向上
                self.trans_tree[left_leaf] = left_hash
                self.trans_tree[right_leaf] = right_hash
                temp_list.append(left_hash+right_hash)
            self.trans_list = temp_list
            self.createtree()
        else:
            # 只有一个节点了，判断这个节点状态
            root_leaf = self.trans_list[0]
            if isinstance(root_leaf,Transaction):
                # 本身就只有一个:
                root_leaf = root_leaf.txid
            root_hash = SHA256.new(root_leaf.encode()).hexdigest()
            self.trans_tree[root_leaf] = root_hash
    
    # 获取构造树的结果    
    def get_merkle_tree(self):
        return self.trans_tree
    
    # 获取merkle根
    def get_root_hash(self):
        key = self.trans_tree.keys()[-1]
        return self.trans_tree[key]

                

