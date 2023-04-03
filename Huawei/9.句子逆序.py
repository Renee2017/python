# 将一个英文语句以单词为单位逆序排放。例如“I am a boy”，逆序排放后为“boy a am I”
# 所有单词之间用一个空格隔开，语句中除了英文字母外，不再包含其他字符


# 用.split将输入的字符串放进列表sentence
sentence=input().strip().split()
new=sentence[::-1]
str=' '.join(new)
print(str)
