#데이터 상수(정수, 실수, 문자열, 불린)
#변수(값을 저장하는 저장소)
#연산자(산술 연산자:+, -, *, / ,&,// 관계 연산자:>,>=,<,<=,==,!=, 논라연산자=and,or)

#list
names = ['홍길동','심청이','강감찬']
#검색
print(1, names[2]) #[문법오류 ~~~~ 밑줄]

#입력 append='추가' insert='위치에 추가'
names.append('성춘향')
print(2, names)
names.insert(1, '유재석')
print(3, names)

#수정
names[1] = '강호동'
print(4, names)

#삭제
names.pop(0)
print(5, names)

#데이터수 (len=위치 , count=개수, )
print(6, len(names))
print(7, names.count(''))