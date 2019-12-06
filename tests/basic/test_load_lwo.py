from lwo_strut.lwoObject import lwoObject
from scripts.lwo_helper import LwoFile


def test_load_lwo_box0_pass():
    infile = "tests/basic/src/LWO2/box/box0.lwo"
    f = LwoFile(infile)
    f.check_file()

    x = lwoObject(infile)
    x.read()

    f.setup_pickle(x)
    b = f.load_pickle()

    assert x == b


def test_load_lwo_box0_fail():
    infile = "tests/basic/src/LWO2/box/box0.lwo"
    f = LwoFile(infile)
    f.check_file()

    x = lwoObject(infile)
    x.read()

    # f.setup_pickle(x)
    f.picklefile = "tests/basic/pickle/LWO2/box/box0.lwo.error0.pickle"
    b = f.load_pickle()

    assert not x == b

def test_load_lwo_box3():
    infile = "tests/basic/src/LWO/box/box3-uv-layers.lwo"
    f = LwoFile(infile)
    f.check_file()

    x = lwoObject(infile)
    x.read()

    f.setup_pickle(x)
    b = f.load_pickle()

    assert x == b

def test_load_lwo_box6():
    infile = "tests/basic/src/LWO2/box/box6-hidden.lwo"
    f = LwoFile(infile)
    f.check_file()

    x = lwoObject(infile)
    x.read()

    f.setup_pickle(x)
    b = f.load_pickle()

    assert x == b

