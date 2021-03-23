class TxOut(object):

    def __init__(self,address,amount ):
        """
        :param value: address是一个ECDSA的公钥，代表接收者
        :param amount: 交易的虚拟货币的数量
        """
        self.amount = amount
        self.address = address


    