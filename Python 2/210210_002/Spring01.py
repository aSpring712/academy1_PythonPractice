print('1')
import Spring02 as S #Spring02의 코드가 실행됨 -> 시작, 끗이 출력됨, 줄임말 S.로만 호출 가능
print('2')
import Spring02 #import는 한 번만 적용되므로 시작, 끗 출력안됨 -> 이 문장때문에 Spring02. 로도 호출 가능
print('3')
import Spring02 #한 번 import된 것은 다시 import되지 않음 -> 중복 import를 해도 에러가 나지 않는다!
print('4')

Spring02.Spring_Function() #여기는 Spring02.py 파일 안 입니다 -> 함수에 접근
S.Spring_Function() #여기는 Spring02.py 파일 안 입니다
print(S.Num) #변수에 접근
print(S.String)

#다른 디렉토리에 있는 함수, 변수에 접근할 때 import 사용 -> as 로 이름 바꿔서 사용 가능
from Sub import Test as T #Sub라는 디렉토리에서 Test.py를 import시키는데, Test를 T로 줄여 쓰겠다
from Sub import Test #줄임말X, 그대로 Test라고 쓰겠다

Test.Spring2() #스프링2가 호출됩니다
T.Spring2() #스프링2가 호출됩니다
