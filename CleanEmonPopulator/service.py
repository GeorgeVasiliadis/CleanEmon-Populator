"""Module intended to be run as an integrated app entry"""

from datetime import datetime

from CleanEmonCore.CouchDBAdapter import CouchDBAdapter
from CleanEmonCore import CONFIG_FILE as DB_CONFIG_FILE
from CleanEmonCore.models import EnergyData

from . import CONFIG_FILE as EMON_CONFIG_FILE
from . import SCHEMA_FILE
from .buffer import AutoBuffer

from .EmonPiAdapter import EmonPiAdapter

from CleanEmonCore.Events import Timer
from CleanEmonCore.Events import Observer


class Reporter(Observer):
    """Class used to implement the fetch-update-send cycle, as long as other
    important integration utilities.
    """

    def __init__(self, timer, *, log_to_screen=False):
        super().__init__(timer)

        self.log_to_screen = log_to_screen
        self.emon_adapter = EmonPiAdapter(EMON_CONFIG_FILE, schema_file=SCHEMA_FILE)
        self.db_adapter = CouchDBAdapter(DB_CONFIG_FILE)
        self.current_document_id = None
        self.current_date = None
        self.buffer = AutoBuffer(60)

    def on_notify(self, *args, **kwargs):
        """This function implements the fundamental fetch-update-send loop.
        As a *side effect*, it checks whether the date has changed and updates
        the document_id as needed.
        """

        self._check_date_change()
        data = self.emon_adapter.fetch_data()
        energy_data = EnergyData(date=self.current_date, energy_data=[data])
        status = self.buffer.append_data(energy_data, document=self.current_document_id)

        if self.log_to_screen:
            print(self.current_document_id)
            print(self.current_date)
            print(data)
            print(f"Uploaded: {status}")

    def _check_date_change(self):
        """If the date has changed since the last check, this means that either a
        new document must be created (usual case) or another document must be
        appended and not recreated (rare case, occurs in development).

        This function keeps
            - self.current_document_id
            - self.current_date
        up to date according to the current date.
        """

        temp = datetime.now()
        date = temp.strftime("%Y-%m-%d")

        if date != self.current_date:
            if self.log_to_screen:
                print("Changed date")
            document_id = self.db_adapter.get_document_id_for_date(date)
            if not document_id:
                energy_data = EnergyData(date=date)
                document_id = self.db_adapter.create_document(initial_data=energy_data)

            self.current_document_id = document_id
            self.current_date = date


def run():
    cooldown_timer = Timer(5)
    Reporter(cooldown_timer, log_to_screen=True)
    cooldown_timer.run()
