# Class

## 构造函数与析构函数

### Q1

如果 `A` 是已经定义好的一个类，有如下定义语句:
```cpp
A *p[5];
```
则当类对象数组指针 `p` 离开它的作用域时，系统自动调用类 `A` 的析构函数 ____ 次。

A. 5 <br>
B. 1 <br>
C. 0 <br>
D. 10

**Answer**: C

### Q2

``` cpp
#include <cstring>
#include <iostream>

using namespace std;

class Person {
  private:
    char name[10];
    int age;
    static int count;

  public:
    Person(const char *str = "sjtu", int n = 104);
    ~Person() {
        count--;
        cout << "name=" << name << " count=" << count << endl;
    }
};

int Person::count = 10;

Person::Person(const char *str, int n) {
    strcpy(name, str);
    age = n;
    count++;
}

int main() {
    Person personArr[2], *p;
    p = new Person("pku", 102);
    Person &q = *p;
    delete p;
    return 0;
}

```

**Output**:

```
name=pku count=12
name=sjtu count=11
name=sjtu count=10
```

## 静态成员函数

### Q1

下面对类的静态成员函数描述中，正确的是 ____

A. 调用静态成员函数时，会有 this 指针作为函数的隐含参数 <br>
B. 静态成员函数中能够调用类中的成员函数 <br>
C. 静态成员函数不能访问类的非静态成员变量 <br>
D. 静态成员函数不能访问类的私有数成员

**Answer**: C
