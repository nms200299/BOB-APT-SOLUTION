# pdf-analysis-module

## 프로젝트 소개
악성으로 의심되는 PDF 파일에서 javascript를 추출하여 이에대한 파일을 생성하고, javascript 난독화 해제를 할 수 있는 프로젝트이다.



### USAGE
```

pdf-analysis-module$ python3 main.py file.pdf --obfuscate  # javascript 난독화 해제하여 추출
pdf-analysis-module$ python3 main.py file.pdf --no-obfuscate # 난독화 안된 javascript의 경우 사용

```
## dependency
* python3.6.9
* python2.7.17

## how to install
1. pdf-analysis-module$ git submodule init
2. pdf-analysis-module$ git submodule update
3. pip install slimit (python2.7 pip로 수행)

## output
your-pdf.js

