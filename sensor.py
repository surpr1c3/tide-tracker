from homeassistant.helpers.entity import Entity
from .api import MeineApi

async def async_setup_entry(hass, entry, async_add_entities):
    api = MeineApi(entry.data["base_url"], entry.data["api_key"])
    sensors = [MeineSensor(api)]
    async_add_entities(sensors, True)

class MeineSensor(Entity):
    def __init__(self, api):
        self.api = api
        self._state = None

    @property
    def name(self):
        return "Mein Sensor"

    @property
    def state(self):
        return self._state

    async def async_update(self):
        data = self.api.get_data()
        if data:
            self._state = data["value"]
