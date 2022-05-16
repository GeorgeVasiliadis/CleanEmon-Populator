from CleanEmonPopulator.service import Reporter
from CleanEmonPopulator.Events.builtins import Timer


def test_reporter():
    assert Reporter(Timer(2))
