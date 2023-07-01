# # 1. 클래스 정의
# class Dog:
#     # 클래스 변수
#     species = "Canis familiaris"
#
#     # 생성자 메서드 (__init__)
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # 인스턴스 메서드
#     def bark(self):
#         print(f"{self.name} says Woof!")
#
# # 2. 객체 생성 (인스턴스화)
# my_dog = Dog("Buddy", 3)
#
# # 3. 객체의 속성 및 메서드 사용
# print(my_dog.name)   # 출력: Buddy
# print(my_dog.age)    # 출력: 3
# my_dog.bark()        # 출력: Buddy says Woof!


# class User:
#     def __init__(self,user_id,user_pw):
#         self.user_id = user_id
#         self.user_pw = user_pw
#
#
# user1 = User("hong", "12345678")

user_id_list = ["hong", "kim", "park"]
user_pw_list = ["123456789"]

userInsertedId = input("아이디를 입력해주세요 : ")

if userInsertedId in user_id_list:
    userInsertedPw = input("비밀번호를 입력해주세요 : ")
    if userInsertedPw in user_pw_list:
        print("환영합니다.")
    else:
        print("비밀번호가 틀렸습니다. 관리자에게 문의해주세요. 전화번호)1541-1234")
else:
    print("죄송합니다. 없는 아이디입니다. 회원가입을 진해해주세요.")

