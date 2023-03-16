# FastAPI Toy Project
> 실제 애플리케이션에 적용하기 전에 테스트할 프로젝트   

## Structure
> 이 프로젝트는 FastAPI를 사용하여 구축되었으며, 다음과 같은 디렉터리 구조로 구성되어 있습니다:

```
.
├── app
│   ├── main.py
│   ├── core
│   │   ├── config.py
│   │   └── middleware.py
│   ├── api
│   │   └── document_ocr.py
│   ├── schemas
│   │   └── image.py
│   └── utils
│       └── helpers.py
├── log
│   └── document_ocr.log
├── assets
└── README.md
```

### app/main.py
> FastAPI 애플리케이션 인스턴스를 생성하고 미들웨어 및 라우터를 등록하는 엔트리 포인트입니다.   

### app/core
> 애플리케이션의 핵심 구성 및 미들웨어 설정을 포함하는 폴더입니다.
- config.py: 애플리케이션 구성 변수를 정의하는 파일입니다.
- middleware.py: 사용자 정의 미들웨어를 정의하는 파일입니다.   

### app/api
> 라우터 및 관련 엔드포인트 로직을 포함하는 폴더입니다.
- document_ocr.py: OCR 관련 엔드포인트를 정의하는 파일입니다.   

### app/schemas
> Pydantic 모델을 정의하는 스키마 파일을 포함하는 폴더입니다.
- image.py: 이미지 정보와 관련된 Pydantic 모델을 정의하는 파일입니다.   

### app/utils
> 재사용 가능한 유틸리티 함수 및 클래스를 포함하는 폴더입니다.
- helpers.py: 여러 라우터에서 사용되는 도우미 함수를 포함하는 파일입니다.   

## How to Run
> 가상 환경을 생성하고 활성화합니다.
```
pip install -r requirements.txt
uvicorn app.main:app --reload
```