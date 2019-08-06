#添加自定义词典

import jieba

words=jieba.cut("何睿主演屌丝男士,挂在了微博热搜")
print("/".join(words))       #(何睿/主演/屌丝/男士/,/挂/在/了/微博热/搜)

#从上面的分词结果就知道,热搜是一个新词,未登录词,我们试试用一下HMM

words=jieba.cut("何睿主演屌丝男士,挂在了微博热搜",HMM=True)
print("/".join(words))       #(何睿/主演/屌丝/男士/,/挂/在/了/微博热/搜)


#上面用了HMM来解决新词的问题,但是呢,效果还是不好,所以我们可以试试用自定义词典,可以用来解决一些新词问题

#加载自定义词典,里面可以放入新词,比如我在词典中放入了微博和热搜这两个词,结果效果就很好
jieba.load_userdict("selfCiDian.txt")
words=jieba.cut("何睿主演屌丝男士,挂在了微博热搜")
print("/".join(words))       #(何睿/主演/屌丝/男士/,/挂/在/了/微博/热搜)

words=jieba.cut_for_search("何睿主演屌丝男士,挂在了微博热搜")
print("/".join(words))       #(何睿/主演/屌丝/男士/,/挂/在/了/微博/热搜)
