# 定义一个区块
class Block(object):
    def __init__(
            self,
            index,
            timestamp,
            previousHash,
            currentHash,
            difficulty,
            nonce):
        """
        :param index: <int> 区块索引
        :param timestamp: <str> 时间戳
        :param previousHash: <str> 前一区块的hash地址
        :param currentHash: <str> 当前区块的hash值
        :param difficulty: <int> 难度系数
        :param nonce: <str> POW随即数
        """
        # 区块头
        self.index = index
        self.timestamp = timestamp
        self.previousHash = previousHash
        self.currentHash = currentHash
        self.difficulty = difficulty
        self.nonce = nonce
        self.merkleroot = None

        # 区块内容，Transaction对象数组
        self.transactions = None  # 
    
    # 获取区块json值
    def get_json(self):
        output = {
            'index': self.index,
            'previous_hash': self.previousHash,
            'current_hash': self.currentHash,
            'difficulty': self.difficulty,
            'timestamp': self.timestamp,
            'nonce': self.nonce,
            'merkleroot': self.merkleroot,
            'transactions': [tx.get_json() for tx in self.transactions]
        }
        return output


if __name__ == '__main__':
    block = Block(1,1111,1,2,2,2)
    block.get_json()
