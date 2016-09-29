import pytest

from binpacker.binpacker import Bin
from binpacker.binpacker import Binpacker
from binpacker.binpacker import Item


def test_item():
    """Test Item
    """

    i = Item('A', 10)
    assert i.name == 'A'
    assert i.weight == 10


def test_item_cmp():
    """Test Item __cmp__
    """

    i = Item('A', 10)
    j = Item('B', 4)
    assert i > j
    i = Item('C', 5)
    j = Item('D', 5)
    assert i == j
    i = Item('E', 6)
    j = Item('F', 10)
    assert i < j


def test_bin():
    """Test Bin class
    """

    b = Bin(10)
    assert b.capacity == 10
    b.push(Item('C', 1))
    b.push(Item('D', 2))
    b.push(Item('E', 3))
    assert b.get_items() == [Item('C', 1), Item('D', 2), Item('E', 3)]
    assert b.get_items('name', 'C') == [Item('C', 1)]
    assert b.utilization == 60.00
    assert b.total_weight == 6
    b.pop()
    assert b.get_items() == [Item('D', 2), Item('E', 3)]
    b.push(Item('F', 7))
    b.remove('E')
    assert b.get_items() == [Item('D', 2), Item('F', 7)]
    b.name = 'Cool Bin'
    assert b.name == 'Cool Bin'


def test_binpacker():
    """Test bin packer
    """

    packer = Binpacker(9)
    expected_items = [
        Item('A', 4), Item('B', 1), Item('C', 2),
        Item('D', 6), Item('E', 9), Item('F', 3),
    ]
    packer.items = expected_items
    assert packer.items == expected_items
    packer.pack_items()
    expected = Bin(9)
    expected.push(Item('C', 2))
    expected.push(Item('A', 4))
    expected.push(Item('F', 3))
    actual = []
    for b in packer.bins:
        actual.append(sorted([i.name for i in b.get_items()]))
    assert ['A', 'C', 'F'] in actual
    assert ['E'] in actual
    assert ['B', 'D'] in actual
    expected_bins = [
        Bin(2), Bin(3)
    ]
    packer.bins = expected_bins
    assert packer.bins == expected_bins


def test_get_truth_table():
    """Test get_truth_table
    """

    bp = Binpacker(9)
    items = [
        Item('A', 1), Item('B', 1), Item('C', 2),
        Item('D', 2), Item('E', 9), Item('F', 3),
        Item('G', 7), Item('H', 2), Item('I', 5)
    ]
    actual = bp.get_truth_table(9, items)
    expected = [
        [True, True, False, False, False, False, False, False, False, False],
        [True, True, True, False, False, False, False, False, False, False],
        [True, True, True, True, True, False, False, False, False, False],
        [True, True, True, True, True, True, True, False, False, False],
        [True, True, True, True, True, True, True, False, False, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True],
        [True, True, True, True, True, True, True, True, True, True]]
    assert actual == expected


def test_capacity_exceeded():
    """Test Item's weight exceeds maximum capacity
    """

    bp = Binpacker(9)
    items = [
        Item('A', 1), Item('B', 1), Item('C', 2),
        Item('D', 2), Item('E', 9), Item('F', 3),
        Item('G', 7), Item('H', 2), Item('I', 10)
    ]

    with pytest.raises(Exception) as err:
        bp.items = items
    assert 'Weight of Item: "I" exceeds the maximum bin capacity: 9'
