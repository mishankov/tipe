from tipe import Pipe


def test_simple():
    assert Pipe(1).pipe(lambda x: x + 1).unwrap() == 2


def test_not_that_simple():
    assert Pipe([2, 3, 4]).pipe(len).pipe(lambda x: x + 1).pipe(float).unwrap() == 4.0


def test_generator():
    assert (
        Pipe((i**i for i in range(5)))
        .pipe(lambda x: (y for y in x))
        .pipe(sum)
        .unwrap()
        == 289
    )
