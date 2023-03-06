from tipe import Pipe


def test_simple():
    assert Pipe(1).pipe(lambda x: x + 1).unwrap() == 2
