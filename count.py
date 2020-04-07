#단어 개수 새기 
import collections
print(collections.Counter(["가","나","다","라","마","가","나"]))
print(collections.Counter(["가","나","다","라","나나나"]))
for k,v in collections.Counter(["가","나","다","라","마","가","나","가","나","가가가가"]).items():
    print(k,":",v)
list_a=["가","나","다","라","마","가","나","가","나","가가가가"]
list_b=["rj","dfdf"]
list_c=list_a+list_b
print(list_c)
collections.Counter(list_c)
collections.Counter(list_a).most_common(2)