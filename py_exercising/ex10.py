탭_냥이 = "\t {}"
줄_냥이 = "{} \n{}"
역슬래시_냥이 = "나는 \\ 고 \\ 양이."

뚱뚱_냥이 = """
할 일 목록 : 
\t* 고양이 밥
\t* 물고기
\t* 개박하\n\t* 오리새
"""

print(탭_냥이.format("나는 탭이 됨."))
print(줄_냥이.format("나는","분리됨."))
print(역슬래시_냥이)
print(뚱뚱_냥이)

탈출_문자열 = """
역슬래시 : \\\\
작은 따옴표 : \\\'
큰 따옴표 : \\\"
ASCII 벨소리 : \\a
ASCII 백스페이스 : \\b
ASCII 폼 피드 : \\f
ASCII 줄바꿈 : \\n
유니코드 데이터베이스에서 name이라는 이름이 붙은 문자(유니코드 전용) : \\N{name}
캐리지 리턴 : \\r
수평 탭 : \\t
16비트 16진수 xxxx에 해당하는 문자(유니코드 전용) : \\uxxxx
32비트 16진수 xxxxxxxx에 해당하는 문자(유니코드 전용) : \\Uxxxxxxxx
ASCII 수직 탭 : \\v
8진수 값 ooo 에 해당하는 문자 : \\ooo
16진수 값 hh에 해당하는 문자 : \\xhh
"""
print(탈출_문자열)
