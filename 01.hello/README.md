# 1. How to write and test a python program

To do :
1. write a python program to say "Hello, World!"
2. Handle command-line arguments using 'argparse'
3. Run tests for the code with Pytest
4. Learn about $PATH
5. Use tools like YAPF and Black to format the code
6. Use tools like Flake8 and Pylint to find problems in the code
7. Use the new.py program to create new programs


## 1.1 Creating your first program

언어를 시작할 때 첫 번째 프로그램은 항상 "hello world.."
파이썬은 확장자를 .py로 갖는다.  

터미널에서 01.hello 디렉토리에 hello.py 파일을 만들자.  
VSCode, Vim 등 원하는 에디터를 이용해 01.hello 디렉토리에 hello.py 파일을 만들고, 아래 문장을 입력!!
```python
print('Hello, World!')
```

파이썬 프로그램 실행은 python3 를 입력한 뒤, 그 뒤에 실행할 파이썬 프로그램명을 입력한다. 
```shell
$ python3 hello.py
Hello, World!
```


## 1.2 Comment

파이썬에서 '#'은 특수한 의미를 갖는다. 파이썬 프로그램을 실행할 때 한 라인에서 '#' 이후에 나오는 어떠한 내용도 인식되지 않는다. (무시된다)  
이를 이용해 code의 주석(comment)나 테스트나 디버깅을 할 때 임시로 해당 부분을 사용하지 않도록 할 때 사용할 수 있다.  
comment를 이용해 프로그램 내에 필요한 내용을 문서화 하는 것도 좋은 방법이다. (프로그램의 목적, 작성자, .. 등)

아래와 같은 방법으로 Comment를 사용한다. 
```python
# To Say hello
print('Hello, World!')
```

## 1.3 Testing your program

프로그램을 어떻게 테스트하는지에 대한 내용이다.  
01.hello 디렉토리에 있는 'test.py' 프로그램을 사용해서 새롭게 작성한 hello.py 프로그램을 테스트 한다.  
- 명령을 실행하기 위해 'pytest' 모듈을 사용
- 결과물로 프로그램이 얼마의(어떤) 테스트를 통과했는지..
- 옵션
    - '-v, verbose output for more information'
    - '-x, to stop on the first failing test'

테스트 프로그램 실행은 아래와 같이..
```shell
$ pytest -xv test.py
```


## 1.4 '#!' 추가하기

파이썬 프로그램의 처음에 '#!(shebang)'이라는 특수한 것을 추가해 이 프로그램을 실행할 운영체제(OS)에 이것은 파이썬 프로그램임을 알린다.  
- 이 프로그램을 실행할 때 운영체제는 이 프로그램을 파이썬을 이용해 실행해야 한다는 것을 알게끔한다. 

아래의 내용을 파이선 프로그램의 첫 라인에 입력한다.
```python
#!/usr/bin/env python3
```

env python3는 운영체제가 시스템에 설치된 python3를 찾아 실행한다.
- 우리는 python3가 어디있는지 모르더라도 운영체제는 알고있..
- 만약, python3가 설치되지 않았다면.. 

```python
#!/usr/bin/env python3
# To Say hello
print('Hello, World!')
```


## 1.5 실행 가능한 프로그램 만들기

파이썬 프로그램에 shebang('#!')을 추가하면, python3 명령 없이 바로 파이썬 프로그램을 실행할 수 있다.  
리눅스의 경우 chmod(change mode) 명령을 통해 실행 권한을 줘야 한다.  
```shell
$ chmod +x hello.py
```

실행 권한을 주면, 기존에 'python3 hello.py' 라고 입력했던 것을 './hello.py'로 입력해 실행할 수 있다.  
```shell
$ ./hello.py
Hello, World!
```

앞서 추가한 shebang을 제거하고 hello.py 프로그램을 실행하면?
```shell
$ ./hello.py
./hello.py: line 2: syntax error near unexpected token `'Hello, World!''
./hello.py: line 2: `print('Hello, World!')'
```

운영체제는 hello.py 가 무엇인지, 어떻게 실행을 해야 하는지 전혀 알지 못해 불만을 털어 놓는다.


## 1.6 프로그램에 parameter(인자)와 help 추가하기

