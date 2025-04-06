import asyncio
import logging
from datetime import timedelta
import aiohttp

from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.core import HomeAssistant

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, entry):
    """Set up Pollen Varsel from a config entry."""
    session = aiohttp.ClientSession()
    coordinator = DataUpdateCoordinator(
        hass,
        _LOGGER,
        name="Pollen Forecast",
        update_interval=timedelta(minutes=60),
        update_method=lambda: async_fetch_data(session)
    )
    await coordinator.async_config_entry_first_refresh()

    hass.data.setdefault(DOMAIN, {})[entry.entry_id] = coordinator

    # Use the plural method to forward the config entry to sensor platforms.
    await hass.config_entries.async_forward_entry_setups(entry, ["sensor"])

    return True

async def async_fetch_data(session):
    """Fetch data from the external API."""
    url = "https://api.nettkjeks.no/api/v1/forecast"
    try:
        async with session.get(url) as response:
            if response.status != 200:
                raise UpdateFailed(f"Error fetching data: {response.status}")
            return await response.json()
    except Exception as err:
        raise UpdateFailed(err)
