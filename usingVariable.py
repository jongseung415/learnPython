# 파이썬 파일을 생성하는 방법
# 파이썬 파일의 확장자는 .py이다.
# 파이썬 파일을 실행하는 방법

# 변수를 설정하는 방법
# '[변수명] = [값]'의 형식으로 변수에 값을 할당한다.
# 주의!) 프로그래밍에서 =는 같다는 의미가 아니라 값을 할당한다는 의미
# 값이 같다는 의미는 파이썬에서는 '=='과 같이 표현한다.

# 변수명 작명 규칙
# 소문자와 대문자는 서로 다르게 취급된다.
# 변수의 이름은 영문자와 숫자, 밑줄(_)로 이루어진다.
# 변수의 이름 중간에 공백이 들어가면 안 된다. 단어를 구분하려면 밑줄(_)을 사용한다.

# 변수에 할당할 수 있는 데이터 종류 및 자료형에 관하여
# : 정수(integer), 실수(float), 문자열(string)

user_name = "vin diesel"

today = "23.06.23"

visitCount = 0

# print() 함수의 기능
# : 괄호 안에 적힌 내용을 화면에 출력해준다.
print("Hello, '", user_name, "' Welcome to visit my site!")
print("today : ", today)

visitCount = visitCount + 1

print("you visit hear again! / Count : ", visitCount)

