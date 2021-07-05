## Delta Debugging

We implement a linear, recursive version of Delta Debuggign algorithm. To simulate a linear input with a specific fault triggering behaviour, `fail.txt` is provided: it contains a long sequence of integers, one number at a line. A few numbers, when collectively used as input, will cause our imaginary program to fail. We can check whether any input triggers the fault by using `check_error` function:

```
>>> import dd
>>> a = [1,2,3]
>>> dd.check_error(a)
False
>>>
```

Implement the linear, recursive DD algorithm so that we can minimise the failure triggering input in `fail.txt`.