#Konlpy설치, 자연어처리, NCT 영웅 가사 분석해보기 
from konlpy.tag import Kkma
from konlpy.utils import pprint
kkma = Kkma()
pprint(kkma.sentences(u'네, 안녕하세요. 반갑습니다.')) #단어 추출
pprint(kkma.nouns(u'질문이나 건의사항은 깃헙 이슈 트래커에 남겨주세요.')) #명사추출
pprint(kkma.nouns(u'상상조차 할 수 없었던 아주 극적인 장면 그 깊은 곳에 눈앞에 펼쳐질 새로운 세상들 손안에 잡힐 듯 내 안으로 들어와 어둠 끝에 다시 난 새로 태어나'))
pprint(kkma.pos(u'상상조차 할 수 없었던 아주 극적인 장면 그 깊은 곳에 눈앞에 펼쳐질 새로운 세상들 손안에 잡힐 듯 내 안으로 들어와 어둠 끝에 다시 난 새로 태어나'))#형태소 분석 