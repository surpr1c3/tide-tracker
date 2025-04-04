from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

DOMAIN = "meine_integration"

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    hass.data[DOMAIN] = entry.data
    hass.async_create_task(
        hass.config_entries.async_forward_entry_setup(entry, "sensor")
    )
    return True
