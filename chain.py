import hashlib

class ChainedHash:

    def hash(self, capacity : int) -> None:
        #""초기화""
        self.capacity = capacity
        self.table = [None] * self.capacity

        def hash_value(self, key : Any) -> int:
            #해쉬값을 구하는 함수

            if instance(key, int):
                return key % self.capacity
            return(int(hash.lib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)

        
##capacity = 해시테이블의 크기(배열의 원소수)
##table = 해시 테이블을 저장하는 list형 배열
        
##key가 정수가 아닐때는 바로 나눌수 없기 때문에 표준라이브러리(hashlib)를 이용하여 형 변환을
##하여 해시값을 얻어냄

##sha256 알고리즘 : hashlib모듈에서 byte문자열의 해쉬값을 구함
##
##encode() : 문자열의 인수를 전달해야해서 key를 str문자열로 변환하여 함수로 전달해 바이트 문자열 생성
##
##hexdigest() : sha256 알고리즘에서 해시값을 16진수 문자열로 꺼냄.

