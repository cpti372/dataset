#데이터 시각화
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt 

#x축 
label=["a","b","c","d"]
#인덱스 받아오기
index=np.arange(len(label))
#바 형태 그래프, 도수 함께 제시 
plt.bar(index,[10,5,20,10])
plt.title("my title")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.xticks(index,label)
plt.show()

# 수집한 데이터 불러오기 
list_data=[('코로나',6),('코나',16),('로나',26),('나',36),('코로나나나',46),('코',56),('코코로나',16)]
list_string=[]
list_number=[]
for a,n in list_data:
    print(a,n)
    list_string.append(a)
    list_number.append(n)

label=list_string
index=np.arange(len(label))
plt.title("my title")
plt.xlabel("x-label")
plt.ylabel("y-label")
plt.xticks(index,label)
plt.xticks(rotation=60)
plt.show()