# 取一个list或tuple的部分元素是非常常见的操作。比如，一个list如下：
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# 对这种经常取指定索引范围的操作，用循环十分繁琐，因此，Python提供了切片（Slice）操作符，能大大简化这种操作。
# 对应上面的问题，取前3个元素，用一行代码就可以完成切片：
L[0:3]
# L[0:3]表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。

# 如果第一个索引是0，还可以省略：
L[:3]

# 类似的，既然Python支持L[-1]取倒数第一个元素，那么它同样支持倒数切片，试试：

# -2 到 0
L[-2:]


L[-2:-1]


# 记住倒数第一个元素的索引是-1

# 切片操作十分有用。我们先创建一个0-99的数列：
L = list(range(100))

L[:10]

# 后10个数：
L[-10:]

# 前11-20个数：
L[10:20]

# 前10个数，每两个取一个：

L[:10:2]

# [0, 2, 4, 6, 8]
