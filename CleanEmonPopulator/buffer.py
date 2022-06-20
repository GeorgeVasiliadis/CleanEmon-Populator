from . import CONFIG_FILE

from CleanEmonCore.CouchDBAdapter import CouchDBAdapter
from CleanEmonCore.models import EnergyData


class AutoBuffer:
    def __init__(self, capacity):
        self.db_adapter = CouchDBAdapter(CONFIG_FILE)
        self.data = {}
        self._capacity = capacity
        self._count = 0

    def _append_hook(self):
        cleared = False

        self._count += 1
        if self._count >= self._capacity:
            self._clear()
            cleared = True

        return cleared

    def _clear(self):
        for document, data_list in self.data.copy().items():
            self.db_adapter.append_energy_data(*data_list, document=document)
            del self.data[document]
        self._count = 0

    def append_data(self, energy_data: EnergyData, document: str):
        if document not in self.data:
            self.data[document] = []

        self.data[document].append(energy_data)

        cleared = self._append_hook()

        return cleared
