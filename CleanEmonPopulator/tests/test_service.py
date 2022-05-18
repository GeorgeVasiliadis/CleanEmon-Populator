from CleanEmonPopulator.service import Reporter
from CleanEmonCore.Events.builtins import Timer


def test_reporter():
    assert Reporter(Timer(2))
