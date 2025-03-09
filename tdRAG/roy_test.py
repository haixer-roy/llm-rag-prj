# basic_data_types.py
# 파이썬 기본 자료형과 연산 예제

# 숫자형 (Numbers)
print("===== 숫자형 =====")
a = 10
b = 3.14
c = complex(2, 3)  # 복소수: 2+3j

print(f"정수: {a}, 타입: {type(a)}")
print(f"실수: {b}, 타입: {type(b)}")
print(f"복소수: {c}, 타입: {type(c)}")

# 기본 연산
print("\n===== 기본 연산 =====")
print(f"덧셈: {a} + 5 = {a + 5}")
print(f"뺄셈: {a} - 5 = {a - 5}")
print(f"곱셈: {a} * 5 = {a * 5}")
print(f"나눗셈: {a} / 3 = {a / 3}")
print(f"몫: {a} // 3 = {a // 3}")
print(f"나머지: {a} % 3 = {a % 3}")
print(f"제곱: {a} ** 2 = {a ** 2}")

# 문자열 (Strings)
print("\n===== 문자열 =====")
name = "파이썬"
message = '안녕하세요!'

print(f"문자열 연결: {name} + ' ' + {message} = {name + ' ' + message}")
print(f"문자열 반복: {name} * 3 = {name * 3}")
print(f"문자열 길이: len({message}) = {len(message)}")
print(f"인덱싱: {message}[0] = {message[0]}")
print(f"슬라이싱: {message}[0:3] = {message[0:3]}")

# 리스트 (Lists)
print("\n===== 리스트 =====")
fruits = ['사과', '바나나', '오렌지', '포도']
print(f"리스트: {fruits}")
print(f"첫 번째 항목: {fruits[0]}")
print(f"마지막 항목: {fruits[-1]}")
fruits.append('키위')
print(f"항목 추가 후: {fruits}")
fruits.remove('바나나')
print(f"항목 제거 후: {fruits}")

# 튜플 (Tuples) - 변경 불가능한 리스트
print("\n===== 튜플 =====")
coordinates = (10, 20)
print(f"튜플: {coordinates}")
print(f"x좌표: {coordinates[0]}, y좌표: {coordinates[1]}")

# 딕셔너리 (Dictionaries)
print("\n===== 딕셔너리 =====")
person = {
    'name': '홍길동',
    'age': 25,
    'city': '서울'
}
print(f"딕셔너리: {person}")
print(f"이름: {person['name']}")
print(f"나이: {person['age']}")
person['job'] = '개발자'
print(f"직업 추가 후: {person}")

# 집합 (Sets)
print("\n===== 집합 =====")
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(f"집합1: {set1}")
print(f"집합2: {set2}")
print(f"합집합: {set1 | set2}")
print(f"교집합: {set1 & set2}")
print(f"차집합: {set1 - set2}")

