学习笔记

queue:(作为一个接口，有六种方法，分别为add,offer,remove,poll,element,peek)

ArrayDeque:

分析addFirst方法：

1.如果对象为空直接抛出空异常

2.创建一个数组将elements中的元素

3.如果head不小于零，就将添加的对象放在head-1这个位置

4.不然，将要添加的对象放在数组长度-1的位置

5.判断head==tail,如果等于，就进行grow（1）

grow就有点看不懂了

priority queue:

offer()函数：

1.如果要加入对象为空直接抛出空异常

2.如果当前队列对象个数大于等于队列的长度

3.将队列长度增加一倍或者增加50%

4.将要添加的对象与队列里的优先级进行比较。插入要添加的队形

5.size+1