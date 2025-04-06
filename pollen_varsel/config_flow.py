import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant import config_entries
from .const import AVAILABLE_AREAS, DOMAIN

class PollenVarselConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Pollen Varsel."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            area = user_input.get("area")
            if area not in AVAILABLE_AREAS:
                errors["base"] = "invalid_area"
            else:
                return self.async_create_entry(title=area, data=user_input)

        data_schema = vol.Schema({
            vol.Required("area", default=list(AVAILABLE_AREAS)[0]):
                vol.In({area: area for area in AVAILABLE_AREAS})
        })
        return self.async_show_form(
            step_id="user",
            data_schema=data_schema,
            errors=errors
        )
