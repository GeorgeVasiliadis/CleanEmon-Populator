import pytest

from CleanEmonPopulator.buffer import AutoBuffer
from CleanEmonCore.models import EnergyData


@pytest.mark.skip
def test_buffer():
    a = AutoBuffer(10)
    data = EnergyData("test", [{"delete_me": 34}])
    for i in range(10):
        print(i)
        a.append_data(data, "06580f5a9b5b888e3a0ad8fb8a035bda")
    print("Done")
    for i in range(10):
        print(i)
        a.append_data(data, "06580f5a9b5b888e3a0ad8fb8a035bda")
    print("done")
