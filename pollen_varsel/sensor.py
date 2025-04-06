import logging
from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN, POLLEN_TYPES

_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass, entry, async_add_entities):
    """Set up sensors for Pollen Varsel from a config entry."""
    coordinator = hass.data[DOMAIN][entry.entry_id]
    sensors = [PollenSensor(coordinator, entry, pollen_type) for pollen_type in POLLEN_TYPES]
    async_add_entities(sensors)

class PollenSensor(CoordinatorEntity, SensorEntity):
    """Representation of a pollen sensor."""

    def __init__(self, coordinator, config_entry, pollen_type):
        """Initialize the sensor."""
        super().__init__(coordinator)
        self.config_entry = config_entry
        self._pollen_type = pollen_type
        self._attr_name = f"{config_entry.data['area']} {pollen_type.capitalize()} Pollen"
        self._attr_unique_id = f"{config_entry.entry_id}_{pollen_type}"

    @property
    def state(self):
        """Return the current pollen level for today."""
        data = self.coordinator.data
        if not data:
            _LOGGER.debug("No data available yet")
            return None

        selected_area = self.config_entry.data["area"].lower()
        for entry in data:
            if entry.get("name", "").lower() == selected_area:
                forecast = entry.get("forecast", {})
                today = forecast.get("today", {})
                pollen_today = today.get(self._pollen_type, {})
                _LOGGER.debug(
                    "For area '%s' and pollen type '%s', today's data: %s",
                    selected_area,
                    self._pollen_type,
                    pollen_today,
                )
                return pollen_today.get("level")
        _LOGGER.debug("No matching data for area '%s'", selected_area)
        return None

    @property
    def extra_state_attributes(self):
        """Return additional attributes including pollen color and tomorrow's forecast."""
        data = self.coordinator.data
        if not data:
            return {}

        selected_area = self.config_entry.data["area"].lower()
        for entry in data:
            if entry.get("name", "").lower() == selected_area:
                forecast = entry.get("forecast", {})
                today = forecast.get("today", {})
                pollen_today = today.get(self._pollen_type, {})
                tomorrow = forecast.get("tomorrow", {})
                pollen_tomorrow = tomorrow.get(self._pollen_type, {})
                return {
                    "color": pollen_today.get("color"),
                    "tomorrow_level": pollen_tomorrow.get("level"),
                    "tomorrow_color": pollen_tomorrow.get("color"),
                }
        return {}

    @property
    def icon(self):
        """Return the icon for the sensor based on pollen type."""
        icons = {
            "or": "mdi:flower-poppy",
            "hassel": "mdi:leaf",
            "salix": "mdi:leaf-maple",
            "bjørk": "mdi:tree-outline",
            "gress": "mdi:grass",
            "burot": "mdi:sprout",
        }
        return icons.get(self._pollen_type, "mdi:flower")
