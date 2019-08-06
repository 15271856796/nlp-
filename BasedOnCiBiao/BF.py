#双向匹配算法

from BasedOnCiBiao import BMM
from BasedOnCiBiao import FMM

#创建一个列表来存放词典
word_list = []

#将字典中的词都放入列表中
dic_input= open("words.txt","r",encoding="utf8")
for line in dic_input.readlines():
    words = line.strip().split()
    for word in words:
        word_list.append(word)


def cut_words(sentence,word_list):
    bmm_word_list=BMM.cut_words(sentence,word_list)
    fmm_word_list=FMM.cut_words(sentence,word_list)
    bmm_word_list_size=len(bmm_word_list)
    fmm_word_list_size = len(fmm_word_list)
    #如果两种划分的词数不相等,则返回词数小的那种划分,当两种划分的词数相等时又分为两种情况,
    # 一种是两种划分的结果完全相同那么就任返回一个,两个返回结果不同时,就返回单字数少的那种划分(因为最大匹配的思想就是单词的颗粒度越大,所能表示的含义就越确切)
    if bmm_word_list_size != fmm_word_list_size:
        if bmm_word_list_size > fmm_word_list_size:
            return fmm_word_list
        else:
            return bmm_word_list
    else:
        if bmm_word_list == fmm_word_list:
            return bmm_word_list
        else:
            bmm_signal=0
            fmm_signal=0
            for i in  bmm_word_list :
                if len(i)==1:
                    bmm_signal=bmm_signal+1
            for i in fmm_word_list:
                if len(i)==1:
                    fmm_signal=fmm_signal+1
            if bmm_signal>fmm_signal:
                return fmm_word_list
            else:
                return bmm_word_list


def main():
    while True:
        sentence = input("请输入要分词的序列:")
        if not sentence:
            break
        result = cut_words(sentence,word_list)
        print(result)

main()



