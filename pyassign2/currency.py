#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"""currency.py: input original currency, target currency and amount, output the exchanged amount of target currency

__author__ = "Jiangyufei"
__pkuid__ = "1800011734"
__email__ = "1800011734@pku.edu.cn"
"""




def exchange(currency_from,currency_to,amount_from):
    """exchange函数：输入原货币 目标货币和金额，即可输出转换为目标货币的金额"""
    
    """依据输入修改URL"""
    
    n = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    n = n + 'from=' + currency_from + '&to=' + currency_to + '&amt=' + str(amount_from)
   
    from urllib.request import urlopen

    doc = urlopen(n)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')

    
    """输入格式不正确时，报错"""
    
    if   'false' == jstr[38:43] :
        result = 'error'
        return result

    else:
        cdit = eval(jstr[:-22] + jstr[-15:])['to']
        result = ''
        n = 0
        while False == cdit[n].isalpha():
            result = result + cdit[n]
            n = n + 1
        return float(result)

    
"""测试函数：通过三个已知输入、输出的检验，检验exchange函数是否能够正确地运行"""

def text_A():
    assert(2.1589225 == exchange('USD','EUR','2.5'))
    
def text_B():
    assert('error' == exchange('CHN','AME','6.4'))
    
def text_C():
    assert(503.09367288543 == exchange('EUR','JPY','3.9'))
    
def textAll():
    text_A()
    text_B()
    text_C()
    print('All texts passed')


def main():
    """main函数：程序的主模块"""
    textAll()
    print(exchange(input('currency from:',),input('currency to:',),input('amount from:',)))

if __name__ == "__main__":
    main()

