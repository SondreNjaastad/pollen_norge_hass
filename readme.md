# Pollen Varsel Norge

**Pollen Varsel** is a custom Home Assistant integration that provides real-time pollen forecasts by polling a private hosted API. The integration creates six sensors—each representing a different pollen type—and allows you to select an area in Norway via a graphical configuration flow. It displays today's pollen forecast along with additional attributes for tomorrow's forecast.

## Features

- **Graphical Configuration Flow**  
  Configure the integration via Home Assistant’s UI using a dropdown menu for selecting the desired area.

- **Automated Data Polling**  
  Uses a DataUpdateCoordinator to poll the external API every 60 minutes, ensuring your data stays up-to-date.

- **Multiple Sensor Support**  
  Provides sensors for six pollen types (e.g., or, hassel, salix, bjørk, gress, burot) with support for both today's forecast and attributes for tomorrow's forecast.

- **Asynchronous Operation**  
  Fully leverages Home Assistant’s asynchronous patterns to ensure a responsive and efficient integration.

## Warning

**Important:** This integration relies on a **private hosted API** available at [https://api.nettkjeks.no/api/v1/forecast](https://api.nettkjeks.no/api/v1/forecast). Please be aware of the following:

- **Reliability Issues:**  
  The API is privately hosted, and its uptime or response times are not guaranteed. Downtime or network issues could impact the data you receive.

- **Rate Limiting:**  
  There might be limitations on the number of requests allowed over a specific period. Exceeding these limits could result in failed data updates.

- **API Changes:**  
  As the API is not officially supported, its endpoints or data structure may change without notice, potentially breaking the integration.

- **Data Accuracy:**  
  The provided pollen forecasts are sourced from the API as-is, and their accuracy cannot be guaranteed.

## Installation

1. **Download**  
   Clone or download this repository and place the `pollen_varsel` folder in your Home Assistant `custom_components` directory.

2. **Restart Home Assistant**  
   Restart your Home Assistant instance to load the new integration.

3. **Configure the Integration**  
   Add **Pollen Varsel** via the Home Assistant UI under **Configuration > Integrations**. Follow the prompts to select your desired area.

## Usage

Once installed and configured, the integration creates six sensors corresponding to the different pollen types. Each sensor displays:
- **Today's Forecast:**  
  The main state of the sensor represents today's pollen level.
  
- **Tomorrow's Forecast:**  
  Additional attributes (e.g., `tomorrow_level`) provide forecast information for tomorrow.

## Troubleshooting

- **No Data Displayed:**  
  Ensure that Home Assistant can reach the API endpoint and that your network settings allow outbound connections.

- **Sensor State Issues:**  
  Verify in Developer Tools > States that the sensor attributes (`color`, `tomorrow_color`, etc.) are correctly populated.

- **API Changes:**  
  If the integration stops working, check for any updates or changes in the API response structure.

## Contributing

Contributions, issues, and feature requests are welcome. Please check the [issues](../../issues) page if you have any questions or suggestions.

## License

This project is licensed under the [MIT License](LICENSE).
