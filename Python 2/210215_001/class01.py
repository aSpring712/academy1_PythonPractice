#p.101
class AutoMobile: #클래스 'AutoMobile' 선언
    name = "" #클래스 변수 'name'을 만들어서 문자열로 지정(자바 : null)
    velocity = 0 #변수에 0 넣어둠 -> 실행 시 name은 "", velocity는 0으로 초기화 된다
    def velocityPlus(self) : #객체의 기능인 메소드(함수 velocityPlus) 선언   (self) -> 자바의 this : 자신 객체, 자신을 인자로 받는다
        self.velocity = self.velocity + 1 #자신의 velocity 0에 +1 시켜서 저장
        print("속도는 %d 입니다." %self.velocity) # % 출력 모양을 뒤에 나오는 알파벳 형태로 출력하라 -> %d : decimal 10진수 -> % self.velocity 를 10진수로 출력
        # %o -> 라고 적으면 8진수로 출력됨 -> 이렇게 원하는 형태로 출력이 가능함
        # %x -> 16진수 ex) 15 -> f , %X -> 대문자 ex) 15 -> F     ==> 자바에도 있음
        # %는 "" 안에 쓰이는 형식지정자
    def velocityDw(self) : #메소드 선언
        self.velocity = self.velocity - 1
        if self.velocity < 0 :
            self.velocity = 0
        print("속도는 %d 입니다." %self.velocity)
#여기까지가 클래스

#아래는 클래스 사용
ac = AutoMobile() #객체 생성
ac.velocityPlus() #메소드 호출  -> 속도는 1 입니다.
ac.velocity = 20 #객체 속성에 값을 대입
ac.velocityDw() #메소드 호출    -> 속도는 19 입니다.
