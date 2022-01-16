# 异常处理

### Q1

以下关于异常处理的描述错误的是 ____

A. 异常抛出语句 `throw <操作数>` 的操作数可以是任何类型 <br>
B. 处理了异常规格说明中指定的所有异常，程序就不会异常中止 <br>
C. 异常处理将异常检测和异常处理分开 <br>
D. 采用异常处理机制可以使程序的主线条更加清晰

**Answer**: BC

- B
  - http://cplusplus.com/doc/tutorial/exceptions/#exception_specification
  - https://zh.cppreference.com/w/cpp/language/except_spec
- C
  - [教材 p.344] C++ 把异常处理工作分成了**异常抛出**，以及**异常捕获和处理**两个部分
  - 检测和处理是在一起的
