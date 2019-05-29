# SQLCompiler
A simple SQL compiler

---

## Already implemented
- Type
  - string
  - integer
- Statement
  - CREATE DATABASE
  - DROP DATABASE
  - SHOW DATABASES
  - USE DATABASE
  - CREATE TABLE
  - DROP TABLE
  - SHOW TABLES
  - INSERT
  - DELETE
  - UODATE
  - SELECT

**Note:Currently only supports simple where syntax**

---

## How to run?
- Python version: 3.x
- Python package:
  - [PLY(PLY (Python Lex-Yacc))][1]:an implementation of lex and yacc parsing tools for Python
  - [PyMySQL][2]:pure Python MySQL client
- Test database:[MySQL][3]
- Test data:[testData.txt][4]
- Configure database information line 296 in yacc.py
  ``` python
  conn = pymysql.connect(host='127.0.0.1', user='root', passwd='mysql', db='mysql')
  ```
- Run
  ``` shell
  python yacc.py
  ```
- Select mode
  - 1 Read data from testData.txt
  - 2 Read data from terminal


[1]:https://www.dabeaz.com/ply/
[2]:https://github.com/PyMySQL/PyMySQL
[3]:https://www.mysql.com/
[4]:testData.txt