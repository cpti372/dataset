#text 가공하기 
from konlpy.tag import Kkma
import collections
kkma=Kkma()

list_sentence=["인생무상","저는 여친잇음","아버지 가방에 들어가심","아버지 가방에 들어가신다","아무노래 불러봐","엔시티존잘이다존잘","연수 존예","성공하자 연수야"]
for i in list_sentence:
    print(i)

list_result=[]
for i in list_sentence:
    print(kkma.nouns(i))
    list_result=list_result+kkma.nouns(i)
    print("=---------------------------------")
    print("list_result=",list_result)

print(collections.Counter(list_result)) #리스트 단어의 수 
print(collections.Counter(list_result).most_common(5))