import pytest
from .. import main02 as ehr


@pytest.mark.parametrize(
    "user_response,expected",
    [
        ( "n", True ),
        ( "y", False ),
        ( "maybe", False ),
        ( "ljdd()09234", False ),
    ],
)
def test_is_new_patient(user_response, expected):
    ehr.input = lambda prompt: user_response
    actual = ehr.is_new_patient()
    assert actual == expected
