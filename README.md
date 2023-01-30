# FastAPI w/ RabbitMQ

> 코드 설명
main.py: FastAPI 애플리케이션 생성, RabbitMQ 연결 설정, API 엔드포인트 정의.
tasks.py: RabbitMQ 메시지 처리 태스크 정의.
services.py: 각 API 엔드포인트에서 호출할 비즈니스 로직 구현.
models.py: 프로그램에서 사용할 데이터 모델 정의.
utils.py: 프로그램에서 사용할 유틸리티 기능 구현.
tests.py: 프로그램 테스트 코드 구현.

> 동작 확인
RabbitMQ Docker 컨테이너 생성 및 실행:
```shell
$ docker run -d --hostname my-rabbit --name some-rabbit -p 15672:15672 -p 5672:5672 rabbitmq:3-management
```
FastAPI 애플리케이션 실행:
```shell
$ python main.py
```
RabbitMQ 수신자 실행:
```shell
$ python tasks.py
```
API 호출 및 결과 확인:
```shell
$ curl http://localhost:8000/items/1
```
tasks.py에서 다음이 출력됨을 확인:
```
 [x] Received '{"item_id": 1}'
```
RabbitMQ Web UI에서 큐 및 메시지 확인: http://localhost:15672/#/queues