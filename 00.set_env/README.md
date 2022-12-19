# 환경 설정

## 파이썬 버전  

파이썬3 3.6 이상이 설치되어 있어야 함.  

## 관련 소스 코드  

Tiny Python Projects의 저자 Kyclark의 github에서 관련 소스를 확인 할 수 있음.   
[Tiny Python Projects sources](https://github.com/kyclark/tiny_python_projects)

```
$ git clone https://github.com/kyclark/tiny_python_projects
```

## 필요한 모듈 설치

python3 pip 모듈을 이용해 아래 모듈 설치.  
```
$ python3 -m pip install black flake8 ipython mypy pylint pytest yapf
```

또는, 첨부된 파일(requirements.txt)를 이용해 설치.  
```
$ python3 -m pip install -r requirements.txt
```

## Tiny Python Projects에서 새로운 프로그램(파일)을 작성하는 방법

Tiny Python Project 예제를 따라하기 위해서 텍스트 에디터로 프로그램을 작성할 수 있다.  
하지만, 프로그램 작성을 쉽게 하기 위해서 기본적으로 사용할 코드를 /bin/new.py 파일을 준비해 두었다.  

사용법은 아래와 같다.  
chapter 2의 crowsnest.py 프로그램을 시작하기 위해 Root 디렉토리에서 다음과 같이 입력한다.   
```
$ bin/new.py 02_crowsnest/crowsnest.py
```

이 후, 필요한 부분을 직접 작성하여 프로그램을 실행할 수 있다.

