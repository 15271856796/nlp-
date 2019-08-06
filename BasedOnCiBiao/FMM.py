#正向最大匹配算法

# -*- coding:utf-8 -*-

#创建一个列表来存放词典
word_list = []

#将字典中的词都放入列表中
dic_input= open("words.txt","r",encoding="utf8")
for line in dic_input.readlines():
    words = line.strip().split()
    for word in words:
        word_list.append(word)



def cut_words(sentence,word_list):
    #统计词典中最长的词
    print(type(word_list))
    max_length=max(len(words) for words in word_list)
    sentence=sentence.strip()
    #取出句子的长度
    sentens_length= len(sentence)
    #存放切分好的词
    cut_word_list=[]
    while sentens_length>0:
        max_cut_length=min(max_length,sentens_length)
        subSentence=sentence[0:max_cut_length]
        while max_cut_length>0:
            if subSentence in word_list:
                cut_word_list.append(subSentence)
                break
            elif max_cut_length==1:
                cut_word_list.append(subSentence)
                break
            else:
                max_cut_length=max_cut_length-1
                subSentence=subSentence[0:max_cut_length]
        sentence=sentence[max_cut_length:]
        sentens_length= len(sentence)
    words="/".join(cut_word_list)
    return words

def main():
    while True:
        sentence = input("请输入要分词的序列:")
        if not sentence:
            break
        result = cut_words(sentence,word_list)
        print(result)
if __name__ == '__main__':
    main()







