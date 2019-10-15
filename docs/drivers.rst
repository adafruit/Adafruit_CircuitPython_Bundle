.. _adafruit-libndrivers:

Adafruit Sponsored Libraries and Drivers on GitHub
===================================================

These are libraries and drivers available in separate GitHub repos. They are
designed for use with CircuitPython and may or may not work with
`MicroPython <https://micropython.org>`_.

Foundational
------------

These libraries provide critical functionality to many of the drivers below. It
is recommended to always have them installed onto the CircuitPython file system in
the ``lib/`` directory. Some drivers may not work without them.

.. toctree::

    BusDevice Library <https://circuitpython.readthedocs.io/projects/busdevice/en/latest/>
    Register Library <https://circuitpython.readthedocs.io/projects/register/en/latest/>

Board-specific Helpers
----------------------

These libraries tie lower-level libraries together to provide an easy, out-of-box experience for
specific boards.

.. toctree::

    Adafruit CircuitPlayground Express <https://circuitpython.readthedocs.io/projects/circuitplayground/en/latest/>
    Adafruit FeatherWings <https://circuitpython.readthedocs.io/projects/featherwing/en/latest/>
    PyBadger (PyBadge and PyGamer) <https://circuitpython.readthedocs.io/projects/pybadger/en/latest/>
    Adafruit PyPortal <https://circuitpython.readthedocs.io/projects/pyportal/en/latest/>

Helper Libraries
-----------------

These libraries build on top of the low level APIs to simplify common tasks.

LED Helpers
^^^^^^^^^^^^

Helpers for animating LEDs.

.. toctree::

    Fancy LED (similar to FastLED) <https://circuitpython.readthedocs.io/projects/fancyled/en/latest/>
    LED Animation <https://adafruit-circuitpython-led-animation.readthedocs.io/en/latest/>

User Interface and GFX Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for building graphical interfaces using the displayio core module.

.. toctree::

    Cursor Control <https://circuitpython.readthedocs.io/projects/cursorcontrol/en/latest/>
    Bitmap Font <https://circuitpython.readthedocs.io/projects/bitmap-font/en/latest/>
    Display Button <https://circuitpython.readthedocs.io/projects/display_button/en/latest/>
    Display Shapes <https://circuitpython.readthedocs.io/projects/display_shapes/en/latest/>
    Display Text <https://circuitpython.readthedocs.io/projects/display-text/en/latest/>
    PYOA <https://circuitpython.readthedocs.io/projects/pyoa/en/latest/>
    Turtle Graphics <https://circuitpython.readthedocs.io/projects/turtle/en/latest/>
    Slideshow <https://circuitpython.readthedocs.io/projects/slideshow/en/latest/>
    Framebuf Module <https://circuitpython.readthedocs.io/projects/framebuf/en/latest/>
    miniQR Non-hardware QR code generator <https://circuitpython.readthedocs.io/projects/miniqr/en/latest/>
    Image Load <https://circuitpython.readthedocs.io/projects/imageload/en/latest/>
    Bitmap Saver <https://circuitpython.readthedocs.io/projects/bitmapsaver/en/latest/>
    GFX (framebuf) <https://circuitpython.readthedocs.io/projects/gfx/en/latest/>

Motor Helpers
^^^^^^^^^^^^^^

Helpers for driving motors, servos, and steppers.

.. toctree::

    DC Motor and Servo <https://circuitpython.readthedocs.io/projects/motor/en/latest/>
    MotorKit <https://circuitpython.readthedocs.io/projects/motorkit/en/latest/>
    ServoKit <https://circuitpython.readthedocs.io/projects/servokit/en/latest/>

Internet of Things Web Service Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for connecting with hosted and self-hosted internet-of-things web services.

.. toctree::

    Adafruit IO <https://circuitpython.readthedocs.io/projects/adafruitio/en/latest/>
    Amazon AWS IoT <https://circuitpython.readthedocs.io/projects/aws_iot/en/latest/>
    Azure IoT <https://circuitpython.readthedocs.io/projects/azureiot/en/latest/>
    Google Cloud IoT Core <https://circuitpython.readthedocs.io/projects/gc_iot_core/en/latest/>
    LIFX Lights <https://circuitpython.readthedocs.io/projects/lifx/en/latest/>
    Hue Lights <https://circuitpython.readthedocs.io/projects/hue/en/latest/>

Internet-of-Things/Wireless Protocol Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for interfacing with the internet or wireless communication.

.. toctree::

    Bluefruit LE Connect App <https://circuitpython.readthedocs.io/projects/bluefruitconnect/en/latest/>
    Bluetooth Low Energy (BLE) <https://circuitpython.readthedocs.io/projects/ble/en/latest/>
    TinyLoRa TTN Helper <https://circuitpython.readthedocs.io/projects/tinylora/en/latest/>
    Mini ESP Tool <https://circuitpython.readthedocs.io/projects/miniesptool/en/latest/>
    MiniMQTT <https://circuitpython.readthedocs.io/projects/minimqtt/en/latest/>
    JSON Web Token (JWT) <https://circuitpython.readthedocs.io/projects/jwt/en/latest/>
    Requests <https://circuitpython.readthedocs.io/projects/requests/en/latest/>
    NTP (Network time Protocol) <https://circuitpython.readthedocs.io/projects/ntp/en/latest/>

Cryptography Helpers
^^^^^^^^^^^^^^^^^^^^^

Helpers for secure communication.

.. toctree::

    RSA <https://circuitpython.readthedocs.io/projects/rsa/en/latest/>

CPython-module Helpers
^^^^^^^^^^^^^^^^^^^^^^^

Pure-Python implementations of standard CPython libraries. Some of these
modules may have a CircuitPython Core API implementation too.

.. toctree::

    binascii <https://circuitpython.readthedocs.io/projects/binascii/en/latest/>
    IterTools <https://circuitpython.readthedocs.io/projects/itertools/en/latest/>
    Logging  <https://circuitpython.readthedocs.io/projects/logging/en/latest/>
    hashlib <https://circuitpython.readthedocs.io/projects/hashlib/en/latest/>

Audio Helpers
^^^^^^^^^^^^^^^

Music, noisemakers, and more.

.. toctree::

    MIDI <https://circuitpython.readthedocs.io/projects/midi/en/latest/>
    Ring Tone Text Transfer Language (RTTTL) <https://circuitpython.readthedocs.io/projects/rtttl/en/latest/>
    Waveform Generation <https://circuitpython.readthedocs.io/projects/waveform/en/latest/>

Miscellaneous Helpers
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

    AVR programming <https://circuitpython.readthedocs.io/projects/avrprog/en/latest/>
    Board Test Suite <https://circuitpython.readthedocs.io/projects/boardtest/en/latest/>
    Debouncer <https://circuitpython.readthedocs.io/projects/debouncer/en/latest/>
    InfraRed Remote <https://circuitpython.readthedocs.io/projects/irremote/en/latest/>
    OneWire <https://circuitpython.readthedocs.io/projects/onewire/en/latest/>
    SD Card <https://circuitpython.readthedocs.io/projects/sd/en/latest/>
    SimpleIO <https://circuitpython.readthedocs.io/projects/simpleio/en/latest/>
    USB Human Interface Device (Keyboard and Mouse) <https://circuitpython.readthedocs.io/projects/hid/en/latest/>
    Test Repo <https://circuitpython.readthedocs.io/projects/testrepo/en/latest/>


Blinky
--------

Multi-color LED drivers.

.. toctree::

    DotStar <https://circuitpython.readthedocs.io/projects/dotstar/en/latest/>
    NeoPixel <https://circuitpython.readthedocs.io/projects/neopixel/en/latest/>
    Pixie <https://circuitpython.readthedocs.io/projects/pixie/en/latest/>
    RGB LED <https://circuitpython.readthedocs.io/projects/rgbled/en/latest/>
    WS2801 <https://circuitpython.readthedocs.io/projects/ws2801/en/latest/>

Displays
-------------

Drivers used to display information. Either pixel or segment based.

Pixel based displays are implemented in two different ways. The original method called "framebuf"
uses a traditional frame buffer model where all pixels are stored in the microcontroller's ram. The
newer method called "displayio" generates the pixels on the fly and relies on the display's ram to
store the final pixels. "displayio" drivers will also work with CircuitPython to display error
messages and other output to the display when the user code is not using it.

The "displayio" drivers are recommended.

Color TFT-LCD
^^^^^^^^^^^^^^^

.. toctree::

    HX8357 (displayio) <https://circuitpython.readthedocs.io/projects/hx8357/en/latest/>
    ILI9341 and ILI9340 (displayio) <https://circuitpython.readthedocs.io/projects/ili9341/en/latest/>
    ST7735 (displayio) <https://circuitpython.readthedocs.io/projects/st7735/en/latest/>
    ST7735R (displayio) <https://circuitpython.readthedocs.io/projects/st7735r/en/latest/>
    ST7789 (displayio) <https://circuitpython.readthedocs.io/projects/st7789/en/latest/>
    RGB Displays (framebuf) <https://circuitpython.readthedocs.io/projects/rgb_display/en/latest/>

OLED
^^^^^^^^^^^^^^^

.. toctree::

    SSD1306 OLED (displayio) <https://circuitpython.readthedocs.io/projects/displayio_ssd1306/en/latest/>
    SSD1306 OLED (framebuf) <https://circuitpython.readthedocs.io/projects/ssd1306/en/latest/>
    SSD1322 OLED (displayio) <https://circuitpython.readthedocs.io/projects/ssd1322/en/latest/>
    SSD1325 OLED (displayio) <https://circuitpython.readthedocs.io/projects/ssd1325/en/latest/>
    SSD1327 OLED (displayio) <https://circuitpython.readthedocs.io/projects/ssd1327/en/latest/>
    SSD1331 OLED (displayio) <https://circuitpython.readthedocs.io/projects/ssd1331/en/latest/>
    SSD1351 OLED (displayio) <https://circuitpython.readthedocs.io/projects/ssd1351/en/latest/>

E-Paper / E-Ink
^^^^^^^^^^^^^^^

.. toctree::

    E-Paper Display (framebuf) <https://circuitpython.readthedocs.io/projects/epd/en/latest/>
    IL0373 (displayio) <https://circuitpython.readthedocs.io/projects/il0373/en/latest/>
    IL0398 (displayio) <https://circuitpython.readthedocs.io/projects/il0398/en/latest/>
    IL91874 (displayio) <https://circuitpython.readthedocs.io/projects/il91874/en/latest/>
    SSD1608 (displayio) <https://circuitpython.readthedocs.io/projects/ssd1608/en/latest/>
    SSD1675 (displayio) <https://circuitpython.readthedocs.io/projects/ssd1675/en/latest/>

Other
^^^^^^^^^^^^^^^

.. toctree::

    Character LCD <https://circuitpython.readthedocs.io/projects/charlcd/en/latest/>
    HT16K33 LED Matrices and Segment Displays <https://circuitpython.readthedocs.io/projects/ht16k33/en/latest/>
    IS31FL3731 Charlieplexed LED Matrix <https://circuitpython.readthedocs.io/projects/is31fl3731/en/latest/>
    MAX7219 LED Matrix <https://circuitpython.readthedocs.io/projects/max7219/en/latest/>
    Nokia PCD8544 Display <https://circuitpython.readthedocs.io/projects/pcd8544/en/latest/>
    RA8875 40-Pin Display Driver <https://circuitpython.readthedocs.io/projects/ra8875/en/latest/>
    Sharp Memory Display <https://circuitpython.readthedocs.io/projects/sharpmemorydisplay/en/latest/>

Real-time clocks
-----------------

Chips that keep current calendar time with a backup battery. The current date and time is available
through ``datetime``.

.. toctree::

    DS1307 Real-time Clock (5V RTC Breakout) <https://circuitpython.readthedocs.io/projects/ds1307/en/latest/>
    DS3231 Real-time Clock (Precision RTC) <https://circuitpython.readthedocs.io/projects/ds3231/en/latest/>
    PCF8523 Real-time Clock (Adalogger RTC) <https://circuitpython.readthedocs.io/projects/pcf8523/en/latest/>

Motion Sensors
----------------

Motion relating sensing including ``acceleration``, ``magnetic``, ``gyro``, and ``orientation``.

.. toctree::

    ADXL34x 3 Axis Accelerometer <https://circuitpython.readthedocs.io/projects/adxl34x/en/latest/>
    BNO055 Accelerometer, Magnetometer, Gyroscope and Absolution Orientation <https://circuitpython.readthedocs.io/projects/bno055/en/latest/>
    FXAS21002C Gyroscope <https://circuitpython.readthedocs.io/projects/fxas21002c/en/latest/>
    FXOS8700 Accelerometer <https://circuitpython.readthedocs.io/projects/fxos8700/en/latest/>
    GPS Global Position <https://circuitpython.readthedocs.io/projects/gps/en/latest/>
    L3GD20 3-Axis Gyroscope <https://circuitpython.readthedocs.io/projects/l3gd20/en/latest/>
    LIS3DH Accelerometer <https://circuitpython.readthedocs.io/projects/lis3dh/en/latest/>
    LSM303 Accelerometer and Magnetometer <https://circuitpython.readthedocs.io/projects/lsm303/en/latest/>
    LSM303 Accelerometer Only<https://circuitpython.readthedocs.io/projects/lsm303-accel/en/latest/>
    LSM303AGR Magnetometer Only<https://circuitpython.readthedocs.io/projects/lsm303agr-mag/en/latest/>
    LSM303DLH Magnetometer Only<https://circuitpython.readthedocs.io/projects/lsm303dlh-mag/en/latest/>
    LSM9DS0 Accelerometer, Magnetometer, Gyroscope and Temperature <https://circuitpython.readthedocs.io/projects/lsm9ds0/en/latest/>
    LSM9DS1 Accelerometer, Magnetometer, Gyroscope and Temperature <https://circuitpython.readthedocs.io/projects/lsm9ds1/en/latest/>
    MLX90390 3 Axis Magnetometer <https://circuitpython.readthedocs.io/projects/mlx90393/en/latest/>
    MMA8451 3 Axis Accelerometer <https://circuitpython.readthedocs.io/projects/mma8451/en/latest/>
    MSA301 3 Axis Accelerometer <https://circuitpython.readthedocs.io/projects/msa301/en/latest/>
    TLV493D 3 Axis Magnetometer <https://circuitpython.readthedocs.io/projects/tlv493d/en/latest/>

Environmental Sensors
----------------------

Sense attributes of the environment including ``temperature``, ``relative_humidity``, ``pressure``,
equivalent carbon dioxide (``eco2`` / ``eCO2``), and total volatile organic compounds (``tvoc`` /
``TVOC``).

.. toctree::

    AM2320 Temperature and Humidity <https://circuitpython.readthedocs.io/projects/am2320/en/latest/>
    ADT7410 High Accuracy Temperature Sensor <https://circuitpython.readthedocs.io/projects/adt7410/en/latest/>
    BME280 Temperature, Humidity and Pressure <https://circuitpython.readthedocs.io/projects/bme280/en/latest/>
    BME680 Temperature, Humidity, Pressure and Gas <https://circuitpython.readthedocs.io/projects/bme680/en/latest/>
    BMP280 Barometric Pressure and Altitude <https://circuitpython.readthedocs.io/projects/bmp280/en/latest/>
    BMP3xx Barometric Pressure and Altimeter <https://circuitpython.readthedocs.io/projects/bmp3xx/en/latest/>
    CCS811 Air Quality <https://circuitpython.readthedocs.io/projects/ccs811/en/latest/>
    DHT Temperature and Humidity <https://circuitpython.readthedocs.io/projects/dht/en/latest/>
    DS18x20 Temperature <https://circuitpython.readthedocs.io/projects/ds18x20/en/latest/>
    HTU21D Temperature and Humidity <https://circuitpython.readthedocs.io/projects/htu21d/en/latest/>
    LPS35HW Water Resistant Barometric Pressure, Temperature <https://circuitpython.readthedocs.io/projects/lps35hw/en/latest/>
    MAX31855 Thermocouple Amplifier, Temperature <https://circuitpython.readthedocs.io/projects/max31855/en/latest/>
    MAX31856 Thermocouple Amplifier, Temperature <https://circuitpython.readthedocs.io/projects/max31856/en/latest/>
    MAX31865 Thermocouple Amplifier, Temperature <https://circuitpython.readthedocs.io/projects/max31865/en/latest/>
    MCP9808 Temperature <https://circuitpython.readthedocs.io/projects/mcp9808/en/latest/>
    MLX90614 Contactless Temperature <https://circuitpython.readthedocs.io/projects/mlx90614/en/latest/>
    MP115A2 Barometric Pressure, Temperature <https://circuitpython.readthedocs.io/projects/mpl115a2/en/latest/>
    MPL3115A2 Barometric Pressure, Altitude and Temperature Sensor <https://circuitpython.readthedocs.io/projects/mpl3115a2/en/latest/>
    MPRLS Ported Absolute Pressure <https://circuitpython.readthedocs.io/projects/mprls/en/latest/>
    PCT2075 Temperature Sensor <https://circuitpython.readthedocs.io/projects/pct2075/en/latest/>
    SGP30 Air Quality <https://circuitpython.readthedocs.io/projects/sgp30/en/latest/>
    SHT31-D Temperature and Humidity <https://circuitpython.readthedocs.io/projects/sht31d/en/latest/>
    Si7021 Temperature and Humidity <https://circuitpython.readthedocs.io/projects/si7021/en/latest/>
    Thermistor Temperature <https://circuitpython.readthedocs.io/projects/thermistor/en/latest/>
    TMP006 Contactless IR Thermopile Sensor <https://circuitpython.readthedocs.io/projects/tmp006/en/latest/>
    TMP007 Contactless Temperature <https://circuitpython.readthedocs.io/projects/tmp007/en/latest/>

Light Sensors
---------------

These sensors detect light related attributes such as ``color``, ``light`` (unit-less), and
``lux`` (light in SI lux).

.. toctree::

    APDS9960 Proximity, Light, RGB, and Gesture <https://circuitpython.readthedocs.io/projects/apds9960/en/latest/>
    AS726x Color Spectrum Sensor <https://circuitpython.readthedocs.io/projects/as726x/en/latest/>
    TCS34725 Color Sensor <https://circuitpython.readthedocs.io/projects/tcs34725/en/latest/>
    TSL2561 Light Sensor <https://circuitpython.readthedocs.io/projects/tsl2561/en/latest/>
    TSL2591 High Dynamic Range Light Sensor <https://circuitpython.readthedocs.io/projects/tsl2591/en/latest/>
    VCNL4010 Proximity and Light <https://circuitpython.readthedocs.io/projects/vcnl4010/en/latest/>
    VCNL4040 Proximity and Light <https://circuitpython.readthedocs.io/projects/vcnl4040/en/latest/>
    VEML6070 UV Index <https://circuitpython.readthedocs.io/projects/veml6070/en/latest/>
    VEML6075 UV Index <https://circuitpython.readthedocs.io/projects/veml6075/en/latest/>
    VEML7700 High Accuracy Ambient Light Sensor <https://circuitpython.readthedocs.io/projects/veml7700/en/latest/>

Distance Sensors
------------------

These sensors measure the ``distance`` to another object and may also measure light level (``light`` and ``lux``).

.. toctree::

    Garmin LIDARLite I2C <https://circuitpython.readthedocs.io/projects/lidarlite/en/latest/>
    HC-SR04 Ultrasonic Range Sensors <https://circuitpython.readthedocs.io/projects/hcsr04/en/latest/>
    Slamtech RPLidar <https://circuitpython.readthedocs.io/projects/rplidar/en/latest/>
    TFmini IR Time of Flight ~30cm - 12m <https://circuitpython.readthedocs.io/projects/tfmini/en/latest/>
    US-100 Ultrasonic Distance Sensor <https://circuitpython.readthedocs.io/projects/us100/en/latest/>
    VL6180x 5 - 100 mm <https://circuitpython.readthedocs.io/projects/vl6180x/en/latest/>
    VL53L0x ~30 - 1000 mm <https://circuitpython.readthedocs.io/projects/vl53l0x/en/latest/>

Radio
--------

These chips communicate to other's over radio.

.. toctree::

    Adafruit Bluefruit LE SPI Friend <https://circuitpython.readthedocs.io/projects/bluefruitspi/en/latest/>
    ESP WiFi Co-Processor using AT Commands <https://circuitpython.readthedocs.io/projects/esp-atcontrol/en/latest/>
    ESP32 WiFi Co-Processor over SPI <https://circuitpython.readthedocs.io/projects/esp32spi/en/latest/>
    RFM9x LoRa <https://circuitpython.readthedocs.io/projects/rfm9x/en/latest/>
    RFM69 Packet Radio <https://circuitpython.readthedocs.io/projects/rfm69/en/latest/>
    PN532 NFC/RFID <https://circuitpython.readthedocs.io/projects/pn532/en/latest/>

IO Expansion
--------------

These provide functionality similar to ``analogio``, ``digitalio``, ``pulseio``, and ``touchio``.

.. toctree::

    Adafruit SeeSaw <https://circuitpython.readthedocs.io/projects/seesaw/en/latest/>
    ADS1x15 Analog-to-Digital Converter  <https://circuitpython.readthedocs.io/projects/ads1x15/en/latest/>
    Crickit Robotics Boards <https://circuitpython.readthedocs.io/projects/crickit/en/latest/>
    DS2413 OneWire GPIO Expander <https://circuitpython.readthedocs.io/projects/ds2413/en/latest/>
    FocalTech Capacitive Touch <https://circuitpython.readthedocs.io/projects/focaltouch/en/latest/>
    MCP230xx GPIO Expander <https://circuitpython.readthedocs.io/projects/mcp230xx/en/latest/>
    MCP3xxx SPI ADC <https://circuitpython.readthedocs.io/projects/mcp3xxx/en/latest/>
    MCP4725 Digital-to-Analog Converter <https://circuitpython.readthedocs.io/projects/mcp4725/en/latest/>
    MPR121 Capacitive Touch Sensor <https://circuitpython.readthedocs.io/projects/mpr121/en/latest/>
    PCA9685 16 x 12-bit PWM Driver <https://circuitpython.readthedocs.io/projects/pca9685/en/latest/>
    TCA9548 I2C Multiplexer <https://circuitpython.readthedocs.io/projects/tca9548a/en/latest/>
    TLC5947 24 x 12-bit PWM Driver <https://circuitpython.readthedocs.io/projects/tlc5947/en/latest/>
    TLC59711 12 x 16-bit PWM Driver <https://circuitpython.readthedocs.io/projects/tlc59711/en/latest/>

Miscellaneous
----------------

.. toctree::

    74HC595 Shift Register <https://circuitpython.readthedocs.io/projects/74hc595/en/latest/>
    ATECCx08 Cryptographic Co-Processor <https://circuitpython.readthedocs.io/projects/atecc/en/latest/>
    AMG88xx Grid-Eye IR Camera <https://circuitpython.readthedocs.io/projects/amg88xx/en/latest/>
    BD3491FS Audio Processor  <https://circuitpython.readthedocs.io/projects/bd3491fs/en/latest/>
    CAP1188 8-Key Capacitive Touch <https://circuitpython.readthedocs.io/projects/cap1188/en/latest/>
    DRV2605 Haptic Motor Controller <https://circuitpython.readthedocs.io/projects/drv2605/en/latest/>
    DS3502 I2C Potentiometer <https://circuitpython.readthedocs.io/projects/ds3502/en/latest/>
    Fingerprint Sensor <https://circuitpython.readthedocs.io/projects/fingerprint/en/latest/>
    FRAM Non-Volatile Memory <https://circuitpython.readthedocs.io/projects/fram/en/latest/>
    INA219 High Side Current <https://circuitpython.readthedocs.io/projects/ina219/en/latest/>
    INA260 Current and Power Monitor <https://circuitpython.readthedocs.io/projects/ina260/en/latest/>
    Matrix Keypad <https://circuitpython.readthedocs.io/projects/matrixkeypad/en/latest/>
    MAX9744 Audio Amplifier  <https://circuitpython.readthedocs.io/projects/max9744/en/latest/>
    NeoTrellis 4x4 Keypad <https://circuitpython.readthedocs.io/projects/neotrellis/en/latest/>
    NeoTrellis M4 4x8 Keypad <https://circuitpython.readthedocs.io/projects/trellism4/en/latest/>
    PyPixelbuf <https://circuitpython.readthedocs.io/projects/pypixelbuf/en/latest/>
    Si4713 Stereo FM Transmitter <https://circuitpython.readthedocs.io/projects/si4713/en/latest/>
    Si5351 Clock Generator <https://circuitpython.readthedocs.io/projects/si5351/en/latest/>
    STMPE610 Resistive Touchscreen <https://circuitpython.readthedocs.io/projects/stmpe610/en/latest/>
    Thermal Printer <https://circuitpython.readthedocs.io/projects/thermal_printer/en/latest/>
    Touchscreen 4-Wire Resistive <https://circuitpython.readthedocs.io/projects/touchscreen/en/latest/>
    TPA2016 Audio Amplifier with AGC <https://circuitpython.readthedocs.io/projects/tpa2016/en/latest/>
    Trellis 4x4 Keypad <https://circuitpython.readthedocs.io/projects/trellis/en/latest/>
    VC0706 TTL Camera <https://circuitpython.readthedocs.io/projects/vc0706/en/latest/>
    VS1053 Audio Codec <https://circuitpython.readthedocs.io/projects/vs1053/en/latest/>
    Dymo Scale <https://circuitpython.readthedocs.io/projects/dymoscale/en/latest/>
    Nunchuk <https://circuitpython.readthedocs.io/projects/nunchuk/en/latest/>
