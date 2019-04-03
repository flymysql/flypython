#include <stdio.h>
int main()
{
    // 兰州小红鸡的注释测试
    // 这是一条独立行的注释测试
    int a,b;
    a=0;
    b=1; /* 
    这样的注释测试 
    */a=a+b;
    printf("%d",a);     // 这是一条同行的注释测试
    return 0;
    /*
    多行注释测试
    */
}
