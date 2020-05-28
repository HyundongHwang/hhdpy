# hhdpy

- 파이썬 생활화를 위해서 이제부터 커맨드라인 유틸리티를 모두 파이썬으로 만들자
- 우선 typora의 기능보완을 위한 유틸리티부터 제작 시작! 

## 설치

```
pip install hhdpy
```

## 사용

```
hhdpy typora_new_file "실험결과 최종보고서"
hhdpy typora_github_io_article_step1 "200101 실험결과 최종보고서.md"
hhdpy typora_github_io_article_step2 "2020-01-01-실험결과-최종보고서.md" 
```

## 개발

### 프로젝트 클론

```
git clone git@github.com:HyundongHwang/hhdpy.git
cd hhdpy
```

### virtualenv 설치, 설정

- virtualenv 설치

```
pip install virtualenv
virtualenv v_hhdpy
```

- virtualenv 활성화

```
.\v_hhdpy\Scripts\activate.ps1
```

- virtualenv 비활성화

```
deactivate
```

### 스크립트 개발, 테스트

- `hhdpy\__main__.py` 파일에서 개발시작
    - `hhdpy\*` 

- 테스트
    - ![](https://i.postimg.cc/nLWrCsVn/screenshot-11.png)


### pip 배포, 테스트

- pypi.org에 개발자계정 만들기(한번만)
    - https://upload.pypi.org/legacy/ 에 접속해서 만들기
    - 이메일 인증도 받아야 한다 

- 필요한 라이브러리 설치(한번만)

```
pip install setuptools
pip install wheel
pip install twine
```

- 버전업
    - `setup.py` 에서 버전 수정

- 빌드

```
rm -Recurse -Force build, dist, *.egg-info
python setup.py bdist_wheel
twine upload dist/*.whl
```

- 테스트

```powershell
# pypi.org의 캐시정책 때문에 2번정도 해야 성공한다.
pip install -U hhdpy
pip install -U hhdpy
pip show hhdpy
hhdpy
```