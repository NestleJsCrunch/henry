import pytest
import henry.modules.data_controller as dc

INPUT = [i for i in range(10)]


@pytest.mark.parametrize(
    "data,limit,expected", ([INPUT, [5], INPUT[:5]), ([INPUT, None, INPUT)])
def test_data_controller_limit(data, limit, expected):
    result = dc.limit(data=data, limit=limit)
    assert result == expected