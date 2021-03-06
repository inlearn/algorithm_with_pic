# 二分查找
## 大O表示法指出了最糟情况下的运行时间,
表示所需时间增长的速度

- O(log n) 对数时间 二分查找
- O(n) 线性时间，简单查找
- O(n*log n) 快速排序
- O(n^2) 选择排序
- O(n!) 旅行商问题

链表擅长插入和删除，而数组擅长随机访问

O(c*n)
c是常量，快速查找的常量比合并查找小，因此如果它们运行
的时间都为O(nlogn),快速查找将更快。


散列函数准确指出了价格的存储位置，不用查找
* 散列函数问题将同样的输入映射到相同的索引
* 散列函数将不同的输入映射到不同的索引
* 散列函数知道数组有多大，只返回有效的索引
