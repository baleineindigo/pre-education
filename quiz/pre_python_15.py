"""15. 주민등록번호를 입력하면 남자인지 여자인지 알려주는 프로그램을 작성하시오. 
(리스트 split 과 슬라이싱 활용) 

예시
<입력>
주민등록번호 : 941130-3002222

<출력>
남자
"""
id_num = input('주민등록번호 :')
id_split = id_num.split('-')[1]
second = list(id_split)
if second[0] == '1' or second[0] == '3':
    print("남자")
elif second[0] == '2' or second[0] == '4':
    print("여자")
else:
    print("주민번호를 잘못 입력했습니다.")
