# OOP

## 访问特性

### Q1

有如下类的定义:
``` cpp
class A {
    int x;

  public:
    void set(int k);
};

class B : public A {
    int y;

  public:
    void sety(int k);
};
```
则 ____ 是正确的

A. `B` 类有 2 个访问特性不相同的数据成员 <br>
B. `B` 类只有 1 个数据成员，其访问特性为 private <br>
C. 除了系统自动生成的成员函数，`B` 类只有 1 个公有的成员函数

**Answer**: A
