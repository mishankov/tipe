[![PyPI](https://img.shields.io/pypi/v/tipe)](https://pypi.org/project/tipe/)

# Tipe - typed pipe

Tipe allows you to create constructions similar to [pipe operator](https://elixirschool.com/en/lessons/basics/pipe_operator), where result of a function used as an input of next function

## Instalation

```bash
pip install tipe
```


## Examples

```python
>>> from tipe import Pipe
>>> 
>>> Pipe(2).pipe(lambda x: x + 1).pipe(float).unwrap()
3.0
>>> Pipe([2, 3, 4]) \
...         .pipe(len) \
...         .pipe(lambda x: x + 1) \
...         .pipe(float) \
...         .unwrap()
4.0
>>> Pipe(2).pipe(range, 4).pipe(len).unwrap()
2
```

Equivalent for examples above would be

```python
>>> float(2+1)
3.0
>>> float(len([2, 3, 4]) + 1)
4.0
>>> len(range(2, 4))
2
```


## API

### `Pipe()`

To use `.pipe()` on a value wrap it with `Pipe` class

```python
>>> Pipe(2)
Pipe(2)
```

### `Pipe.pipe()`

Pass function to execute on `Pipe` value and additional params for it. Wraps function result in `Pipe` and returns it


### `Pipe.check()`

Like `Pipe.pipe()` but does not change the value inside `Pipe`. May be useful for debugging purposes

```python
>>> Pipe(2).pipe(lambda x: x ** x).check(print).pipe(float).unwrap()
4
4.0
```

### `Pipe.unwrap()`

Returns value from `Pipe`


### Short forms

For convenience you can use `P` as short version of `Pipe` and short versions of the methods:
- `p`: `pipe`
- `c`: `check`
- `u`: `unwrap`


## Types

`tipe` tries its best to stay typesafe, so every function knows what exactly what it returns as long as it is inferable from arguments
