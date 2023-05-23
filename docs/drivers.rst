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

    BusDevice Library <https://docs.circuitpython.org/projects/busdevice/en/latest/>
    Register Library <https://docs.circuitpython.org/projects/register/en/latest/>

Board-specific Helpers
----------------------

These libraries tie lower-level libraries together to provide an easy, out-of-box experience for
specific boards.

.. toctree::

    Adafruit CircuitPlayground <https://docs.circuitpython.org/projects/circuitplayground/en/latest/>
    Adafruit CLUE <https://docs.circuitpython.org/projects/clue/en/latest/>
    Adafruit ESP32S2TFT <https://docs.circuitpython.org/projects/esp32s2tft/en/latest/>
    Adafruit FeatherWings <https://docs.circuitpython.org/projects/featherwing/en/latest/>
    Adafruit FunHouse <https://docs.circuitpython.org/projects/funhouse/en/latest/>
    Adafruit MacroPad <https://docs.circuitpython.org/projects/macropad/en/latest/>
    Adafruit MagTag <https://docs.circuitpython.org/projects/magtag/en/latest/>
    Adafruit MONSTER M4SK <https://docs.circuitpython.org/projects/monsterm4sk/en/latest/>
    Adafruit PortalBase <https://docs.circuitpython.org/projects/portalbase/en/latest/>
    Adafruit PyPortal <https://docs.circuitpython.org/projects/pyportal/en/latest/>
    PyBadger (PyBadge and PyGamer) <https://docs.circuitpython.org/projects/pybadger/en/latest/>
    MatrixPortal (Metro M4 Airlift + RGB Shield) <https://docs.circuitpython.org/projects/matrixportal/en/latest/>

Helper Libraries
-----------------

These libraries build on top of the low level APIs to simplify common tasks.

LED Helpers
^^^^^^^^^^^^

Helpers for animating LEDs.

.. toctree::

    Fancy LED (similar to FastLED) <https://docs.circuitpython.org/projects/fancyled/en/latest/>
    LED Animation <https://docs.circuitpython.org/projects/led-animation/en/latest/>
    PixelMap <https://docs.circuitpython.org/projects/pixelmap/en/latest/>

User Interface and GFX Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for building graphical interfaces using the displayio core module and framebuf code module (framebuf is deprecated).

.. toctree::

    Cursor Control <https://docs.circuitpython.org/projects/cursorcontrol/en/latest/>
    Bitmap Font <https://docs.circuitpython.org/projects/bitmap-font/en/latest/>
    Bitmap Saver <https://docs.circuitpython.org/projects/bitmapsaver/en/latest/>
    Display Button <https://docs.circuitpython.org/projects/display-button/en/latest//>
    Display Notification <https://docs.circuitpython.org/projects/display_notification/en/latest/>
    Display Shapes <https://docs.circuitpython.org/projects/display-shapes/en/latest/>
    Display Text <https://docs.circuitpython.org/projects/display_text/en/latest/>
    Framebuf Module <https://docs.circuitpython.org/projects/framebuf/en/latest/>
    GFX (framebuf) <https://docs.circuitpython.org/projects/gfx/en/latest/>
    Image Load <https://docs.circuitpython.org/projects/imageload/en/latest/>
    miniQR Non-hardware QR code generator <https://docs.circuitpython.org/projects/miniqr/en/latest/>
    Pixel Framebuf Module <https://docs.circuitpython.org/projects/pixel_framebuf/en/latest/>
    ProgressBar <https://docs.circuitpython.org/projects/progressbar/en/latest/>
    PYOA <https://docs.circuitpython.org/projects/pyoa/en/latest/>
    Slideshow <https://docs.circuitpython.org/projects/slideshow/en/latest/>
    Simple Text Display <https://docs.circuitpython.org/projects/simple-text-display/en/latest/>
    Turtle Graphics <https://docs.circuitpython.org/projects/turtle/en/latest/>
    WSGI <https://docs.circuitpython.org/projects/wsgi/en/latest/>
    DisplayIO Layout <https://docs.circuitpython.org/projects/displayio-layout/en/latest/>
    Dash Display <https://docs.circuitpython.org/projects/dash_display/en/latest/>

Motor Helpers
^^^^^^^^^^^^^^

Helpers for driving motors, servos, and steppers.

.. toctree::

    DC Motor and Servo <https://docs.circuitpython.org/projects/motor/en/latest/>
    EMC2101 Fan Controller and Temperature monitor <https://docs.circuitpython.org/projects/emc2101/en/latest/>
    MotorKit <https://docs.circuitpython.org/projects/motorkit/en/latest/>
    ServoKit <https://docs.circuitpython.org/projects/servokit/en/latest/>

Internet of Things Web Service Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for connecting with hosted and self-hosted internet-of-things web services.

.. toctree::

    Adafruit IO <https://docs.circuitpython.org/projects/adafruitio/en/latest/>
    Amazon AWS IoT <https://docs.circuitpython.org/projects/aws_iot/en/latest/>
    Azure IoT <https://docs.circuitpython.org/projects/azureiot/en/latest/>
    Google Cloud IoT Core <https://docs.circuitpython.org/projects/gc_iot_core/en/latest/>
    Hue Lights <https://docs.circuitpython.org/projects/hue/en/latest/>
    LIFX Lights <https://docs.circuitpython.org/projects/lifx/en/latest/>

Internet/Internet-of-Things Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for interfacing with the internet, including IoT protocols.

.. toctree::

    Fake Requests <https://docs.circuitpython.org/projects/fakerequests/en/latest/>
    HTTP Server <https://docs.circuitpython.org/projects/httpserver/en/latest/>
    JSON Web Token (JWT) <https://docs.circuitpython.org/projects/jwt/en/latest/>
    MiniMQTT <https://docs.circuitpython.org/projects/minimqtt/en/latest/>
    NTP (Network time Protocol) <https://docs.circuitpython.org/projects/ntp/en/latest/>
    Requests <https://docs.circuitpython.org/projects/requests/en/latest/>
    OAuth2.0 <https://docs.circuitpython.org/projects/oauth2/en/latest/>

Bluetooth Low Energy Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for Bluetooth Low Energy (BLE).

.. toctree::

    Bluefruit LE Connect App <https://docs.circuitpython.org/projects/bluefruitconnect/en/latest/>
    BLE Base Library <https://docs.circuitpython.org/projects/ble/en/latest/>
    BLE Adafruit Services <https://docs.circuitpython.org/projects/ble_adafruit/en/latest/>
    BLE Apple Media Service <https://docs.circuitpython.org/projects/ble_apple_media/en/latest/>
    BLE Apple Notification Center Service <https://docs.circuitpython.org/projects/ble_apple_notification_center/en/latest/>
    BLE Location Beacons <https://docs.circuitpython.org/projects/ble_beacon/en/latest/>
    BLE BerryMed Pulse Oximeter Service <https://docs.circuitpython.org/projects/ble_berrymed_pulse_oximeter/en/latest/>
    BLE BroadcastNet <https://docs.circuitpython.org/projects/ble_broadcastnet/en/latest/>
    BLE Cycling Speed and Cadence <https://docs.circuitpython.org/projects/ble_cycling_speed_and_cadence/en/latest/>
    BLE Eddystone Beacon <https://docs.circuitpython.org/projects/ble_eddystone/en/latest/>
    BLE File Transfer <https://docs.circuitpython.org/projects/ble_file_transfer/en/latest/>
    BLE Heart Rate <https://docs.circuitpython.org/projects/ble_heart_rate/en/latest/>
    BLE iBBQ <https://docs.circuitpython.org/projects/ble_ibbq/en/latest/>
    BLE LYWSD03MMC (Xiaomi Mijia) <https://docs.circuitpython.org/projects/ble_lywsd03mmc/en/latest/>
    BLE Magic Light <https://docs.circuitpython.org/projects/ble_magic_light/en/latest/>
    BLE MIDI <https://docs.circuitpython.org/projects/ble_midi/en/latest/>
    BLE Radio <https://docs.circuitpython.org/projects/ble_radio/en/latest/>


LoRa Wireless Helpers
^^^^^^^^^^^^^^^^^^^^^

Helpers for wireless communication via LoRa.

.. toctree::

    TinyLoRa TTN Helper (LoRaWAN) <https://docs.circuitpython.org/projects/tinylora/en/latest/>

Cryptography Helpers
^^^^^^^^^^^^^^^^^^^^^

Helpers for secure communication.

.. toctree::

    RSA <https://docs.circuitpython.org/projects/rsa/en/latest/>

CPython-module Helpers
^^^^^^^^^^^^^^^^^^^^^^^

Pure-Python implementations of standard CPython libraries. Some of these
modules may have a CircuitPython Core API implementation too.

.. toctree::

    asyncio <https://docs.circuitpython.org/projects/asyncio/en/latest/>
    binascii <https://docs.circuitpython.org/projects/binascii/en/latest/>
    datetime <https://docs.circuitpython.org/projects/datetime/en/latest/>
    IterTools <https://docs.circuitpython.org/projects/itertools/en/latest/>
    Logging  <https://docs.circuitpython.org/projects/logging/en/latest/>
    hashlib <https://docs.circuitpython.org/projects/hashlib/en/latest/>

Audio Helpers
^^^^^^^^^^^^^^^

Music, noisemakers, and more.

.. toctree::

    MIDI <https://docs.circuitpython.org/projects/midi/en/latest/>
    Ring Tone Text Transfer Language (RTTTL) <https://docs.circuitpython.org/projects/rtttl/en/latest/>
    Waveform Generation <https://docs.circuitpython.org/projects/waveform/en/latest/>
    Wave file I/O <https://docs.circuitpython.org/projects/wave/en/latest/>

Miscellaneous Helpers
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

    AVR programming <https://docs.circuitpython.org/projects/avrprog/en/latest/>
    BitbangIO <https://docs.circuitpython.org/projects/bitbangio/en/latest/>
    Board Test Suite <https://docs.circuitpython.org/projects/boardtest/en/latest/>
    Colorsys <https://docs.circuitpython.org/projects/colorsys/en/latest/>
    Debouncer <https://docs.circuitpython.org/projects/debouncer/en/latest/>
    Debug I2C <https://docs.circuitpython.org/projects/debug_i2c/en/latest/>
    Ducky <https://docs.circuitpython.org/projects/ducky/en/latest/>
    InfraRed Remote <https://docs.circuitpython.org/projects/irremote/en/latest/>
    Mini ESP Tool (ESP chips loader) <https://docs.circuitpython.org/projects/miniesptool/en/latest/>
    NeoKey <https://docs.circuitpython.org/projects/neokey/en/latest/>
    OneWire <https://docs.circuitpython.org/projects/onewire/en/latest/>
    Pastebin services <https://docs.circuitpython.org/projects/pastebin/en/latest/>
    PIOASM converter for RP2040 boards <https://docs.circuitpython.org/projects/pioasm/en/latest/>
    Radial Controller <https://docs.circuitpython.org/projects/radial-controller/en/latest/>
    SD Card <https://docs.circuitpython.org/projects/sd/en/latest/>
    SimpleIO <https://docs.circuitpython.org/projects/simpleio/en/latest/>
    SimpleMath <https://docs.circuitpython.org/projects/simplemath/en/latest/>
    Test Repo <https://docs.circuitpython.org/projects/testrepo/en/latest/>
    USB HID - Human Interface Device (Keyboard and Mouse) <https://docs.circuitpython.org/projects/hid/en/latest/>
    Ticks <https://docs.circuitpython.org/projects/ticks/en/latest/>

Blinky
--------

Multi-color LED drivers.

.. toctree::

    DotStar <https://docs.circuitpython.org/projects/dotstar/en/latest/>
    NeoPixel <https://docs.circuitpython.org/projects/neopixel/en/latest/>
    NeoPixel SPI <https://docs.circuitpython.org/projects/neopixel_spi/en/latest/>
    NeoPxl8 <https://docs.circuitpython.org/projects/neopxl8/en/latest/>
    Pixie <https://docs.circuitpython.org/projects/pixie/en/latest/>
    RGB LED <https://docs.circuitpython.org/projects/rgbled/en/latest/>
    WS2801 <https://docs.circuitpython.org/projects/ws2801/en/latest/>

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

    HX8357 (displayio) <https://docs.circuitpython.org/projects/hx8357/en/latest/>
    ILI9341 and ILI9340 (displayio) <https://docs.circuitpython.org/projects/ili9341/en/latest/>
    ST7735 (displayio) <https://docs.circuitpython.org/projects/st7735/en/latest/>
    ST7735R (displayio) <https://docs.circuitpython.org/projects/st7735r/en/latest/>
    ST7789 (displayio) <https://docs.circuitpython.org/projects/st7789/en/latest/>
    RGB Displays (framebuf) <https://docs.circuitpython.org/projects/rgb_display/en/latest/>

OLED
^^^^^^^^^^^^^^^

.. toctree::

    SH1106 OLED (displayio) <https://docs.circuitpython.org/projects/displayio_sh1106/en/latest/>
    SH1107 OLED (displayio) <https://docs.circuitpython.org/projects/displayio-sh1107/en/latest/>
    SSD1305 OLED (displayio) <https://docs.circuitpython.org/projects/displayio_ssd1305/en/latest/>
    SSD1305 OLED (framebuf) <https://docs.circuitpython.org/projects/ssd1305/en/latest/>
    SSD1306 OLED (displayio) <https://docs.circuitpython.org/projects/displayio_ssd1306/en/latest/>
    SSD1306 OLED (framebuf) <https://docs.circuitpython.org/projects/ssd1306/en/latest/>
    SSD1322 OLED (displayio) <https://docs.circuitpython.org/projects/ssd1322/en/latest/>
    SSD1325 OLED (displayio) <https://docs.circuitpython.org/projects/ssd1325/en/latest/>
    SSD1327 OLED (displayio) <https://docs.circuitpython.org/projects/ssd1327/en/latest/>
    SSD1331 OLED (displayio) <https://docs.circuitpython.org/projects/ssd1331/en/latest/>
    SSD1351 OLED (displayio) <https://docs.circuitpython.org/projects/ssd1351/en/latest/>

E-Paper / E-Ink
^^^^^^^^^^^^^^^

.. toctree::

    ACeP7In (displayio) <https://docs.circuitpython.org/projects/acep7in/en/latest/>
    E-Paper Display (framebuf) <https://docs.circuitpython.org/projects/epd/en/latest/>
    IL0373 (displayio) <https://docs.circuitpython.org/projects/il0373/en/latest/>
    IL0398 (displayio) <https://docs.circuitpython.org/projects/il0398/en/latest/>
    IL91874 (displayio) <https://docs.circuitpython.org/projects/il91874/en/latest/>
    SPD1656 (displayio) <https://docs.circuitpython.org/projects/spd1656/en/latest/>
    SSD1608 (displayio) <https://docs.circuitpython.org/projects/ssd1608/en/latest/>
    SSD1675 (displayio) <https://docs.circuitpython.org/projects/ssd1675/en/latest/>
    SSD1680 (displayio) <https://docs.circuitpython.org/projects/ssd1680/en/latest/>
    SSD1681 (displayio) <https://docs.circuitpython.org/projects/ssd1681/en/latest/>
    UC8151D (displayio) <https://docs.circuitpython.org/projects/uc8151d/en/latest/>

Other
^^^^^^^^^^^^^^^

.. toctree::

    Character LCD <https://docs.circuitpython.org/projects/charlcd/en/latest/>
    HT16K33 LED Matrices and Segment Displays <https://docs.circuitpython.org/projects/ht16k33/en/latest/>
    IS31FL3731 Charlieplexed LED Matrix <https://docs.circuitpython.org/projects/is31fl3731/en/latest/>
    IS31FL3741 RGB LED Matrix driver <https://docs.circuitpython.org/projects/is31fl3741/en/latest/>
    MAX7219 LED Matrix <https://docs.circuitpython.org/projects/max7219/en/latest/>
    Nokia PCD8544 Display <https://docs.circuitpython.org/projects/pcd8544/en/latest/>
    RA8875 40-Pin Display Driver <https://docs.circuitpython.org/projects/ra8875/en/latest/>
    Sharp Memory Display <https://docs.circuitpython.org/projects/sharpmemorydisplay/en/latest/>
    ST7565 Graphic Displays <https://docs.circuitpython.org/projects/st7565/en/latest/>
    TSC2007 Resistive Touch Screen Driver <https://docs.circuitpython.org/projects/tsc2007/en/latest/>

Real-time clocks
-----------------

Chips that keep current calendar time with a backup battery. The current date and time is available
through ``datetime``.

.. toctree::

    DS1307 Real-time Clock (5V RTC Breakout) <https://docs.circuitpython.org/projects/ds1307/en/latest/>
    DS3231 Real-time Clock (Precision RTC) <https://docs.circuitpython.org/projects/ds3231/en/latest/>
    PCF8523 Real-time Clock (Adalogger RTC) <https://docs.circuitpython.org/projects/pcf8523/en/latest/>
    PCF8563 Real-time Clock <https://docs.circuitpython.org/projects/pcf8563/en/latest/>

Motion Sensors
----------------

Motion relating sensing including ``acceleration``, ``magnetic``, ``gyro``, and ``orientation``.

.. toctree::

    ADXL34x 3 Axis Accelerometer <https://docs.circuitpython.org/projects/adxl34x/en/latest/>
    ADXL37x 3 Axis Accelerometer <https://docs.circuitpython.org/projects/adxl37x/en/latest/>
    BNO055 Accelerometer, Magnetometer, Gyroscope and Absolution Orientation <https://docs.circuitpython.org/projects/bno055/en/latest/>
    BNO08X  9 Axis Sensor Fusion IMU <https://docs.circuitpython.org/projects/bno08x/en/latest/>
    BNO08X_RVC Simple UART Heading Library <https://docs.circuitpython.org/projects/bno08x_rvc/en/latest/>
    FXAS21002C Gyroscope <https://docs.circuitpython.org/projects/fxas21002c/en/latest/>
    FXOS8700 Accelerometer <https://docs.circuitpython.org/projects/fxos8700/en/latest/>
    GPS Global Position <https://docs.circuitpython.org/projects/gps/en/latest/>
    ICM20X Wide-range 6-DoF Accelerometer and Gyro Family <https://docs.circuitpython.org/projects/icm20x/en/latest/>
    L3GD20 3-Axis Gyroscope <https://docs.circuitpython.org/projects/l3gd20/en/latest/>
    LIS2MDL 3-Axis Magnetometer <https://docs.circuitpython.org/projects/lis2mdl/en/latest/>
    LIS331HH and H3LIS331 3-Axis Accelerometers <https://docs.circuitpython.org/projects/lis331/en/latest/>
    LIS3DH Accelerometer <https://docs.circuitpython.org/projects/lis3dh/en/latest/>
    LIS3MDL 3-Axis Magnetometer <https://docs.circuitpython.org/projects/lis3mdl/en/latest/>
    LSM303 Accelerometer Only<https://docs.circuitpython.org/projects/lsm303-accel/en/latest/>
    LSM303 Accelerometer and Magnetometer <https://docs.circuitpython.org/projects/lsm303/en/latest/>
    LSM303DLH Magnetometer Only<https://docs.circuitpython.org/projects/lsm303dlh-mag/en/latest/>
    LSM6DSOX, LSM6DS33, and ISM330DHCT  Accelerometer, Gyroscope and Temperature <https://docs.circuitpython.org/projects/lsm6dsox/en/latest/>
    LSM9DS0 Accelerometer, Magnetometer, Gyroscope and Temperature <https://docs.circuitpython.org/projects/lsm9ds0/en/latest/>
    LSM9DS1 Accelerometer, Magnetometer, Gyroscope and Temperature <https://docs.circuitpython.org/projects/lsm9ds1/en/latest/>
    MLX90393 3 Axis Magnetometer <https://docs.circuitpython.org/projects/mlx90393/en/latest/>
    MLX90395 3-Axis Magnetometer <https://docs.circuitpython.org/projects/mlx90395/en/latest/>
    MMA8451 3 Axis Accelerometer <https://docs.circuitpython.org/projects/mma8451/en/latest/>
    MMC56X3 Magnetometers <https://docs.circuitpython.org/projects/mmc56x3/en/latest/>
    MPU6050 Accelerometer, Gyroscope, and Temperature Sensor <https://docs.circuitpython.org/projects/mpu6050/en/latest/>
    MSA301 3 Axis Accelerometer <https://docs.circuitpython.org/projects/msa301/en/latest/>
    TLV493D 3 Axis Magnetometer <https://docs.circuitpython.org/projects/tlv493d/en/latest/>

Environmental Sensors
----------------------

Sense attributes of the environment including ``temperature``, ``relative_humidity``, ``pressure``,
equivalent carbon dioxide (``eco2`` / ``eCO2``), and total volatile organic compounds (``tvoc`` /
``TVOC``).

.. toctree::


    ADT7410 High Accuracy Temperature Sensor <https://docs.circuitpython.org/projects/adt7410/en/latest/>
    AGS02MA Gas Sensor <https://docs.circuitpython.org/projects/ags02ma/en/latest/>
    AHTx0 Tempertaure and Humidity Sensor <https://docs.circuitpython.org/projects/ahtx0/en/latest/>
    AM2320 Temperature and Humidity <https://docs.circuitpython.org/projects/am2320/en/latest/>
    BME280 Temperature, Humidity and Pressure <https://docs.circuitpython.org/projects/bme280/en/latest/>
    BME680 Temperature, Humidity, Pressure and Gas <https://docs.circuitpython.org/projects/bme680/en/latest/>
    BMP280 Barometric Pressure and Altitude <https://docs.circuitpython.org/projects/bmp280/en/latest/>
    BMP3xx Barometric Pressure and Altimeter <https://docs.circuitpython.org/projects/bmp3xx/en/latest/>
    CCS811 Air Quality <https://docs.circuitpython.org/projects/ccs811/en/latest/>
    DHT Temperature and Humidity <https://docs.circuitpython.org/projects/dht/en/latest/>
    DPS310 Precision Barometric Pressure / Altitude Sensor <https://docs.circuitpython.org/projects/dps310/en/latest/>
    DS18x20 Temperature <https://docs.circuitpython.org/projects/ds18x20/en/latest/>
    ENS160 (ScioSense) digital multi-gas sensor <https://docs.circuitpython.org/projects/ens160/en/latest/>
    HTS221 Temperature and Humidity Sensor <https://docs.circuitpython.org/projects/hts221/en/latest/>
    HTU21D Temperature and Humidity <https://docs.circuitpython.org/projects/htu21d/en/latest/>
    HTU31D Temperature and Humidity <https://docs.circuitpython.org/projects/htu31d/en/latest/>
    LPS2X Family of Barometric Pressure, Temperature Sensors <https://docs.circuitpython.org/projects/lps2x/en/latest/>
    LPS35HW Water Resistant Barometric Pressure, Temperature <https://docs.circuitpython.org/projects/lps35hw/en/latest/>
    SGP40 Air Quality Sensor <https://docs.circuitpython.org/projects/sgp40/en/latest/>
    MAX31855 Thermocouple Amplifier, Temperature <https://docs.circuitpython.org/projects/max31855/en/latest/>
    MAX31856 Thermocouple Amplifier, Temperature <https://docs.circuitpython.org/projects/max31856/en/latest/>
    MAX31865 Thermocouple Amplifier, Temperature <https://docs.circuitpython.org/projects/max31865/en/latest/>
    MCP9600 Thermocouple Amplifier <https://docs.circuitpython.org/projects/mcp9600/en/latest/>
    MCP9808 Temperature <https://docs.circuitpython.org/projects/mcp9808/en/latest/>
    MLX90614 Contactless Temperature <https://docs.circuitpython.org/projects/mlx90614/en/latest/>
    MPL115A2 Barometric Pressure, Temperature <https://docs.circuitpython.org/projects/mpl115a2/en/latest/>
    MPL3115A2 Barometric Pressure, Altitude and Temperature Sensor <https://docs.circuitpython.org/projects/mpl3115a2/en/latest/>
    MPRLS Ported Absolute Pressure <https://docs.circuitpython.org/projects/mprls/en/latest/>
    MS8607 Pressure, Temperature, Humidity <https://docs.circuitpython.org/projects/ms8607/en/latest/>
    PCT2075 Temperature Sensor <https://docs.circuitpython.org/projects/pct2075/en/latest/>
    PM25 Air Quality Sensor <https://docs.circuitpython.org/projects/pm25/en/latest/>
    SCD30 CO2, Temperature, and Humidity Sensor <https://docs.circuitpython.org/projects/scd30/en/latest/>
    SCD4x Temperature and Humidity Sensor <https://docs.circuitpython.org/projects/scd4x/en/latest/>
    SGP30 Air Quality <https://docs.circuitpython.org/projects/sgp30/en/latest/>
    SHT31-D Temperature and Humidity <https://docs.circuitpython.org/projects/sht31d/en/latest/>
    SHT4x Temperature and Humidity <https://docs.circuitpython.org/projects/sht4x/en/latest/>
    SHTC3 Temperature and Humidity <https://docs.circuitpython.org/projects/shtc3/en/latest/>
    Si7021 Temperature and Humidity <https://docs.circuitpython.org/projects/si7021/en/latest/>
    TC74 Digital Temperature Sensor <https://docs.circuitpython.org/projects/tc74/en/latest/>
    TMP006 Contactless IR Thermopile Sensor <https://docs.circuitpython.org/projects/tmp006/en/latest/>
    TMP007 Contactless Temperature <https://docs.circuitpython.org/projects/tmp007/en/latest/>
    TMP117 High-Precision Temperature Sensor <https://docs.circuitpython.org/projects/tmp117/en/latest/>
    Thermistor Temperature <https://docs.circuitpython.org/projects/thermistor/en/latest/>

Light Sensors
---------------

These sensors detect light related attributes such as ``color``, ``light`` (unit-less), and
``lux`` (light in SI lux).

.. toctree::

    APDS9960 Proximity, Light, RGB, and Gesture <https://docs.circuitpython.org/projects/apds9960/en/latest/>
    AS726x Color Spectrum Sensor <https://docs.circuitpython.org/projects/as726x/en/latest/>
    AS7341 11-Channel Multi-Spectral Digital Sensor <https://docs.circuitpython.org/projects/as7341/en/latest/>
    BH1750 Ambient Light <https://docs.circuitpython.org/projects/bh1750/en/latest/>
    GUVx I2C UV Light Sensors <https://docs.circuitpython.org/projects/guvx-i2c/en/latest/>
    LTR329 LTR303 Light Sensors <https://docs.circuitpython.org/projects/ltr329-ltr303/en/latest/>
    LTR390 Ambient Light and UV Sensor <https://docs.circuitpython.org/projects/ltr390/en/latest/>
    TCS34725 Color Sensor <https://docs.circuitpython.org/projects/tcs34725/en/latest/>
    TSL2561 Light Sensor <https://docs.circuitpython.org/projects/tsl2561/en/latest/>
    TSL2591 High Dynamic Range Light Sensor <https://docs.circuitpython.org/projects/tsl2591/en/latest/>
    VCNL4010 Proximity and Light <https://docs.circuitpython.org/projects/vcnl4010/en/latest/>
    VCNL4040 Proximity and Light <https://docs.circuitpython.org/projects/vcnl4040/en/latest/>
    VEML6070 UV Index <https://docs.circuitpython.org/projects/veml6070/en/latest/>
    VEML6075 UV Index <https://docs.circuitpython.org/projects/veml6075/en/latest/>
    VEML7700 High Accuracy Ambient Light Sensor <https://docs.circuitpython.org/projects/veml7700/en/latest/>
    SI1145 Digital UV Index IR Visible Light Sensor <https://docs.circuitpython.org/projects/si1145/en/latest/>

Distance Sensors
------------------

These sensors measure the ``distance`` to another object and may also measure light level (``light`` and ``lux``).

.. toctree::

    Garmin LIDARLite I2C <https://docs.circuitpython.org/projects/lidarlite/en/latest/>
    HC-SR04 Ultrasonic Range Sensors <https://docs.circuitpython.org/projects/hcsr04/en/latest/>
    Slamtech RPLidar <https://docs.circuitpython.org/projects/rplidar/en/latest/>
    TFmini IR Time of Flight ~30cm - 12m <https://docs.circuitpython.org/projects/tfmini/en/latest/>
    US-100 Ultrasonic Distance Sensor <https://docs.circuitpython.org/projects/us100/en/latest/>
    VL6180x 5 - 100 mm <https://docs.circuitpython.org/projects/vl6180x/en/latest/>
    VL53L0x ~30 - 1000 mm <https://docs.circuitpython.org/projects/vl53l0x/en/latest/>
    VL53L1X ~30 - 4000 mm <https://docs.circuitpython.org/projects/vl53l1x/en/latest/>
    VL53L4CD Time of Flight <https://docs.circuitpython.org/projects/vl53l4cd/en/latest/>

Radio
--------

These chips communicate to others over radio.

.. toctree::

    Adafruit Bluefruit LE SPI Friend <https://docs.circuitpython.org/projects/bluefruitspi/en/latest/>
    AirLift Co-Processor Manager <https://docs.circuitpython.org/projects/airlift/en/latest/>
    ESP WiFi Co-Processor using AT Commands <https://docs.circuitpython.org/projects/esp-atcontrol/en/latest/>
    ESP32 WiFi Co-Processor over SPI <https://docs.circuitpython.org/projects/esp32spi/en/latest/>
    RFM9x LoRa <https://docs.circuitpython.org/projects/rfm9x/en/latest/>
    RFM69 Packet Radio <https://docs.circuitpython.org/projects/rfm69/en/latest/>
    PN532 NFC/RFID <https://docs.circuitpython.org/projects/pn532/en/latest/>

IO Expansion
--------------

These provide functionality similar to ``analogio``, ``digitalio``, ``pulseio``, and ``touchio``.

.. toctree::

    ADS1x15 Analog-to-Digital Converter  <https://docs.circuitpython.org/projects/ads1x15/en/latest/>
    Adafruit SeeSaw <https://docs.circuitpython.org/projects/seesaw/en/latest/>
    AW9523 GPIO expander and LED driver <https://docs.circuitpython.org/projects/aw9523/en/latest/>
    Crickit Robotics Boards <https://docs.circuitpython.org/projects/crickit/en/latest/>
    DS2413 OneWire GPIO Expander <https://docs.circuitpython.org/projects/ds2413/en/latest/>
    FocalTech Capacitive Touch <https://docs.circuitpython.org/projects/focaltouch/en/latest/>
    MCP2515 CAN bus controller <https://docs.circuitpython.org/projects/mcp2515/en/latest/>
    MCP230xx GPIO Expander <https://docs.circuitpython.org/projects/mcp230xx/en/latest/>
    MCP3xxx SPI ADC <https://docs.circuitpython.org/projects/mcp3xxx/en/latest/>
    MCP4725 Digital-to-Analog Converter <https://docs.circuitpython.org/projects/mcp4725/en/latest/>
    MCP4728 4-Channel, 12-bit Digital-to-Analog Converter <https://docs.circuitpython.org/projects/mcp4728/en/latest/>
    MPR121 Capacitive Touch Sensor <https://docs.circuitpython.org/projects/mpr121/en/latest/>
    NAU7802 24-Bit ADC <https://docs.circuitpython.org/projects/nau7802/en/latest/>
    PCA9685 16 x 12-bit PWM Driver <https://docs.circuitpython.org/projects/pca9685/en/latest/>
    PCF8574 GPIO Expander <https://docs.circuitpython.org/projects/pcf8574/en/latest/>
    PCF8575 GPIO Expander <https://docs.circuitpython.org/projects/pcf8575/en/latest/>
    PCF8591 ADC + DAC Combo <https://docs.circuitpython.org/projects/pcf8591/en/latest/>
    TCA8418 I2C Keyboard Multiplexor <https://docs.circuitpython.org/projects/tca8418/en/latest/>
    TCA9548 I2C Multiplexer <https://docs.circuitpython.org/projects/tca9548a/en/latest/>
    TLA202X 12-bit I2C DAC <https://docs.circuitpython.org/projects/tla202x/en/latest/>
    TLC5947 24 x 12-bit PWM Driver <https://docs.circuitpython.org/projects/tlc5947/en/latest/>
    TLC59711 12 x 16-bit PWM Driver <https://docs.circuitpython.org/projects/tlc59711/en/latest/>

Miscellaneous
----------------

.. toctree::

    24LC32 EEPROM <https://docs.circuitpython.org/projects/24lc32/en/latest/>
    74HC595 Shift Register <https://docs.circuitpython.org/projects/74hc595/en/latest/>
    ATECCx08 Cryptographic Co-Processor <https://docs.circuitpython.org/projects/atecc/en/latest/>
    AMG88xx Grid-Eye IR Camera <https://docs.circuitpython.org/projects/amg88xx/en/latest/>
    BD3491FS Audio Processor  <https://docs.circuitpython.org/projects/bd3491fs/en/latest/>
    CAP1188 8-Key Capacitive Touch <https://docs.circuitpython.org/projects/cap1188/en/latest/>
    DRV2605 Haptic Motor Controller <https://docs.circuitpython.org/projects/drv2605/en/latest/>
    DS1841 I2C Logarithmic Potentiometer <https://docs.circuitpython.org/projects/ds1841/en/latest/>
    DS3502 I2C Potentiometer <https://docs.circuitpython.org/projects/ds3502/en/latest/>
    Dymo Scale <https://docs.circuitpython.org/projects/dymoscale/en/latest/>
    Fingerprint Sensor <https://docs.circuitpython.org/projects/fingerprint/en/latest/>
    Floppy <https://docs.circuitpython.org/projects/floppy/en/latest/>
    FONA Cellular Module <https://docs.circuitpython.org/projects/fona/en/latest/>
    FRAM Non-Volatile Memory <https://docs.circuitpython.org/projects/fram/en/latest/>
    Gizmo <https://docs.circuitpython.org/projects/gizmo/en/latest/>
    INA219 High Side Current <https://docs.circuitpython.org/projects/ina219/en/latest/>
    INA260 Current and Power Monitor <https://docs.circuitpython.org/projects/ina260/en/latest/>
    LC709203F Fuel Gauge and Battery Monitor <https://docs.circuitpython.org/projects/lc709203f/en/latest/>
    Matrix Keypad <https://docs.circuitpython.org/projects/matrixkeypad/en/latest/>
    MAX1704x Fuel Gauge <https://docs.circuitpython.org/projects/max1704x/en/latest/>
    MAX9744 Audio Amplifier  <https://docs.circuitpython.org/projects/max9744/en/latest/>
    MLX90640 Thermal Camera <https://docs.circuitpython.org/projects/mlx90640/en/latest/>
    NeoTrellis 4x4 Keypad <https://docs.circuitpython.org/projects/neotrellis/en/latest/>
    NeoTrellis M4 4x8 Keypad <https://docs.circuitpython.org/projects/trellism4/en/latest/>
    Nunchuk <https://docs.circuitpython.org/projects/nunchuk/en/latest/>
    OV2640 Camera <https://docs.circuitpython.org/projects/ov2640/en/latest/>
    OV5640 Camera <https://docs.circuitpython.org/projects/ov5640/en/latest/>
    OV7670 Camera <https://docs.circuitpython.org/projects/ov7670/en/latest/>
    Pixelbuf <https://docs.circuitpython.org/projects/pixelbuf/en/latest/>
    RockBlock Iridium Satellite Modem <https://docs.circuitpython.org/projects/rockblock/en/latest/>
    Si4713 Stereo FM Transmitter <https://docs.circuitpython.org/projects/si4713/en/latest/>
    Si5351 Clock Generator <https://docs.circuitpython.org/projects/si5351/en/latest/>
    STMPE610 Resistive Touchscreen <https://docs.circuitpython.org/projects/stmpe610/en/latest/>
    Touchscreen 4-Wire Resistive <https://docs.circuitpython.org/projects/touchscreen/en/latest/>
    TPA2016 Audio Amplifier with AGC <https://docs.circuitpython.org/projects/tpa2016/en/latest/>
    Trellis 4x4 Keypad <https://docs.circuitpython.org/projects/trellis/en/latest/>
    TT21100 Capacitive Touchscreen Driver <https://docs.circuitpython.org/projects/tt21100/en/latest/>
    VC0706 TTL Camera <https://docs.circuitpython.org/projects/vc0706/en/latest/>
    VS1053 Audio Codec <https://docs.circuitpython.org/projects/vs1053/en/latest/>
    Wii Classic <https://docs.circuitpython.org/projects/wii_classic/en/latest/>
    Wiznet5k Ethernet Module <https://docs.circuitpython.org/projects/wiznet5k/en/latest/>
