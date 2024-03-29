#jieba的三种模式

import jieba

#jieba的cut分词函数有三个参数,参数1是需要被分词的句子,参数2是分词方式,默认是精准模式,
#想设定成全模式,直接给参数True,第三个参数是是指对于未登录词,是否采用基于汉字成词能力的HMM模型,使用Viterbi算法,默认是False

#采用精准模式,就是将句子精准的分词
words = jieba.cut("我毕业于理工大学")
print("采用精准模式:"+"/".join(words))       #(我/毕业/于/理工大学)
#采用全模式,也就是把所有可能独立成词的全部分出来,没有解决歧义的能力
words=jieba.cut("我毕业于理工大学", cut_all=True)
print("采用全模式:"+"/".join(words))         #(我/毕业/于/理工/理工大/理工大学/工大/大学)




#jieba的cut_for_search用于实现搜索引擎的分词模式,这个函数有两个参数,参数1是要被切分的句子,参数2是对于未登录词,是否采用基于汉字成词能力的HMM模型
words=jieba.cut_for_search("我毕业于北京理工大学,后就职于中国科学院计算技术研究所")


#基于搜索词汇进行分类
print("采用搜索引擎模式:"+"/".join(words))     #(我/毕业/于/北京/理工/工大/大学/理工大/北京理工大学/,/后/就职/于/中国/科学/学院/计算/技术/研究/科学院/研究所/中国科学院计算技术研究所)