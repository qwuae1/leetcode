# Binary search

```text
左界逼近
Lower bound
        left = 0
        right = size - 1

        while left < right:
            # left + right 在 Python 中如果发生整型溢出，Python 会自动转成长整形
            # floor 此时 right逼近 left 向下取整
            mid = (left + right) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] < target:
                # 下一轮搜索区间是 [mid + 1, right]
                left = mid + 1
            else:
                # 下一轮搜索区间是 [left, mid]
                right = mid
        return left
```

```text
右界逼近
        left = 0
        right = size - 1

        while left < right:
            # left + right 在 Python 中如果发生整型溢出，Python 会自动转成长整形
            # floor to ceiling,此时 left 逼近 right向上取整，避免死循环
            mid = (left + right+1) // 2
            # 严格小于 target 的元素一定不是解
            if nums[mid] > target:
                # 下一轮搜索区间是 [left, mid-1]
                right= mid-1
            else:
                # 下一轮搜索区间是 [mid, right]
                left = mid
        return left
```

