#함수는 세가지 일을 합니다.
#1. 변수 이름을 문자열과 숫자로 만들 듯 코드 조각에 이름을 붙입니다.
#2. 스크립트가 argv를 받듯이 실행 인자를 받습니다.
#3. 1번과 2번을 이용해 '작은 스크립트'나 '작은 명령'을 만듭니다.

#argv를 쓴 스크립트와 비슷한 함수
def 둘_출력(*args):
	실행인자1, 실행인자2 = args
	print(f"실행인자1 : {실행인자1}, 실행인자2 : {실행인자2}")

#사실 *args는 필요가 없다.
def 둘_출력_다르게(실행인자1, 실행인자2):
	print(f"실행인자1 : {실행인자1}, 실행인자2 : {실행인자2}")

def 하나_출력(실행인자1):
	print(f"실행인자1: {실행인자1}")

def 영_출력():
	print("아무것도 받지 않음")

둘_출력('신','대현')
둘_출력_다르게('신','대현')
하나_출력('하나!')
영_출력()
