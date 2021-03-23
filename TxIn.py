class TxIn(object):
    def __init__(self, txOutId, txOutIndex, signature, pubkey):
        """
        :param txOutId: 指向此前的转入交易id
        :param txOutIndex: 上一笔交易中所引用输出的index
        :param signature 发送者用自己私钥进行加密的签名(签名数据为本次交易的id)
        用指向的前一次交易中对应output中的地址(即公钥)对该签名进行验证，即能证明该发送者是该交易及所指向的前一次交易的拥有者。
        """
        self.txOutId = txOutId
        self.txOutIndex = txOutIndex
        self.signature = signature

    