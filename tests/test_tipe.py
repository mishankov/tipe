from tipe import Pipe


def test_simple():
    assert Pipe(1).pipe(lambda x: x + 1).unwrap() == 2


def test_not_that_simple():
    assert Pipe([2, 3, 4]).pipe(len).pipe(lambda x: x + 1).pipe(float).unwrap() == 4.0


def test_generator():
    assert (
        Pipe((i**i for i in range(5))).pipe(lambda x: (y for y in x)).pipe(sum).unwrap()
        == 289
    )


def test_additional_params():
    def add(a: int, b: int) -> int:
        return a + b

    assert Pipe(1).pipe(add, 2).unwrap() == 3
    assert Pipe(2).pipe(range, 4).pipe(len).unwrap() == 2


def test_check_run(capsys):
    assert Pipe(1).check(print).unwrap() == 1

    captured = capsys.readouterr()
    assert captured.out == "1\n"


def test_check_immutability():
    assert Pipe(1).check(lambda x: x + 1).unwrap() == 1
