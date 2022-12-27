# Yeelight Developer Mode Script

This project contains a Python script that enables developer mode for a Yeelight device using the `python-miio` library.

For Mi Smart LED Bulb Essential (White and Color) / yeelink.light.color5 / MJDPL01YL (GPX4021GL)

## Dependencies

To use this script, you will need to install the following dependency:

- [python-miio](https://pypi.org/project/python-miio/)
- [Xiaomi-cloud-tokens-extractor](https://github.com/PiotrMachowski/Xiaomi-cloud-tokens-extractor)

## Usage

To use the script, run the following command:

```bash
python3 blub.py
```
The script will prompt you for the IP and TOKEN values for your Yeelight device. Once you have entered these values, the script will enable developer mode for the device.

⚠️ JUST COPY blub.py TO Xiaomi-cloud-tokens-extractor ROOT FOLDER ⚠️

Example
```bash
Copy code
Enter the IP of your device: 192.168.1.123
Enter the TOKEN for your device: 1111b99d22e6a436523b5116566691e1

Enabling developer mode for Yeelight device at IP 192.168.1.123...
Developer mode enabled.
```
## Notes

Make sure that your device is turned on and connected to the same network as the computer running the script.
The TOKEN value can be obtained using the Xiaomi cloud tokens extractor script.
Enabling developer mode on a Yeelight device allows you to access advanced features and make changes to the device's firmware. Use caution when using these features, as they may cause the device to behave unexpectedly or become unstable.
