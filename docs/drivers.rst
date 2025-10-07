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

    BusDevice Library (adafruit_busdevice) <https://docs.circuitpython.org/projects/busdevice/en/latest/>
    Register Library (adafruit_register) <https://docs.circuitpython.org/projects/register/en/latest/>

Board-specific Helpers
----------------------

These libraries tie lower-level libraries together to provide an easy, out-of-box experience for
specific boards.

.. toctree::

    Adafruit CircuitPlayground (adafruit_circuitplayground) <https://docs.circuitpython.org/projects/circuitplayground/en/latest/>
    Adafruit CLUE (adafruit_clue) <https://docs.circuitpython.org/projects/clue/en/latest/>
    Adafruit ESP32S2TFT (adafruit_esp32s2tft) <https://docs.circuitpython.org/projects/esp32s2tft/en/latest/>
    Adafruit FeatherWings (adafruit_featherwing) <https://docs.circuitpython.org/projects/featherwing/en/latest/>
    Adafruit FunHouse (adafruit_funhouse) <https://docs.circuitpython.org/projects/funhouse/en/latest/>
    Adafruit MacroPad (adafruit_macropad) <https://docs.circuitpython.org/projects/macropad/en/latest/>
    Adafruit MagTag (adafruit_magtag) <https://docs.circuitpython.org/projects/magtag/en/latest/>
    Adafruit MONSTER M4SK (adafruit_monsterm4sk) <https://docs.circuitpython.org/projects/monsterm4sk/en/latest/>
    Adafruit PortalBase (adafruit_portalbase) <https://docs.circuitpython.org/projects/portalbase/en/latest/>
    Adafruit PyCamera (adafruit_pycamera) <https://docs.circuitpython.org/projects/pycamera/en/latest/>
    Adafruit PyPortal (adafruit_pyportal) <https://docs.circuitpython.org/projects/pyportal/en/latest/>
    Adafruit Qualia S3 (adafruit_qualia) <https://docs.circuitpython.org/projects/qualia/en/latest/>
    PyBadger (PyBadge and PyGamer) (adafruit_pybadger) <https://docs.circuitpython.org/projects/pybadger/en/latest/>
    MatrixPortal (Metro M4 Airlift + RGB Shield) (adafruit_matrixportal) <https://docs.circuitpython.org/projects/matrixportal/en/latest/>

Helper Libraries
-----------------

These libraries build on top of the low level APIs to simplify common tasks.

LED Helpers
^^^^^^^^^^^^

Helpers for animating LEDs.

.. toctree::

    Fancy LED (similar to FastLED) (adafruit_fancyled) <https://docs.circuitpython.org/projects/fancyled/en/latest/>
    LED Animation (adafruit_led-animation) <https://docs.circuitpython.org/projects/led-animation/en/latest/>
    PixelMap (adafruit_pixelmap) <https://docs.circuitpython.org/projects/pixelmap/en/latest/>

User Interface and GFX Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for building graphical interfaces using the displayio core module and framebuf code module (framebuf is deprecated).

.. toctree::

    Anchored Group (adafruit_anchored_group) <https://docs.circuitpython.org/projects/anchored_group/en/latest/>
    Anchored TileGrid (adafruit_anchored_tilegrid) <https://docs.circuitpython.org/projects/anchored_tilegrid/en/latest/>
    Cursor Control (adafruit_cursorcontrol) <https://docs.circuitpython.org/projects/cursorcontrol/en/latest/>
    Bitmap Font (adafruit_bitmap-font) <https://docs.circuitpython.org/projects/bitmap-font/en/latest/>
    Bitmap Saver (adafruit_bitmapsaver) <https://docs.circuitpython.org/projects/bitmapsaver/en/latest/>
    Display AnalogClock (adafruit_display_analogclock) <https://docs.circuitpython.org/projects/display-analogclock/en/latest/>
    Display Button (adafruit_display-button) <https://docs.circuitpython.org/projects/display-button/en/latest//>
    Display Emoji Text (adafruit_display_emoji_text) <https://docs.circuitpython.org/projects/display_emoji_text/en/latest/>
    Display Notification (adafruit_display_notification) <https://docs.circuitpython.org/projects/display_notification/en/latest/>
    Display Shapes (adafruit_display-shapes) <https://docs.circuitpython.org/projects/display-shapes/en/latest/>
    Display Text (adafruit_display_text) <https://docs.circuitpython.org/projects/display_text/en/latest/>
    Framebuf Module (adafruit_framebuf) <https://docs.circuitpython.org/projects/framebuf/en/latest/>
    GFX (framebuf) (adafruit_gfx) <https://docs.circuitpython.org/projects/gfx/en/latest/>
    Image Load (adafruit_imageload) <https://docs.circuitpython.org/projects/imageload/en/latest/>
    miniQR Non-hardware QR code generator (adafruit_miniqr) <https://docs.circuitpython.org/projects/miniqr/en/latest/>
    Pixel Framebuf Module (adafruit_pixel_framebuf) <https://docs.circuitpython.org/projects/pixel_framebuf/en/latest/>
    ProgressBar (adafruit_progressbar) <https://docs.circuitpython.org/projects/progressbar/en/latest/>
    PYOA (adafruit_pyoa) <https://docs.circuitpython.org/projects/pyoa/en/latest/>
    Slideshow (adafruit_slideshow) <https://docs.circuitpython.org/projects/slideshow/en/latest/>
    Simple Text Display (adafruit_simple-text-display) <https://docs.circuitpython.org/projects/simple-text-display/en/latest/>
    Turtle Graphics (adafruit_turtle) <https://docs.circuitpython.org/projects/turtle/en/latest/>
    WSGI (adafruit_wsgi) <https://docs.circuitpython.org/projects/wsgi/en/latest/>
    DisplayIO Layout (adafruit_displayio-layout) <https://docs.circuitpython.org/projects/displayio-layout/en/latest/>
    Dash Display (adafruit_dash_display) <https://docs.circuitpython.org/projects/dash_display/en/latest/>

Motor Helpers
^^^^^^^^^^^^^^

Helpers for driving motors, servos, and steppers.

.. toctree::

    DC Motor and Servo (adafruit_motor) <https://docs.circuitpython.org/projects/motor/en/latest/>
    EMC2101 Fan Controller and Temperature monitor (adafruit_emc2101) <https://docs.circuitpython.org/projects/emc2101/en/latest/>
    MotorKit (adafruit_motorkit) <https://docs.circuitpython.org/projects/motorkit/en/latest/>
    ServoKit (adafruit_servokit) <https://docs.circuitpython.org/projects/servokit/en/latest/>
    STSPIN Stepper Motor Helper (adafruit_stspin) <https://docs.circuitpython.org/projects/stspin/en/latest/>

Internet of Things Web Service Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for connecting with hosted and self-hosted internet-of-things web services.

.. toctree::

    Adafruit IO (adafruit_adafruitio) <https://docs.circuitpython.org/projects/adafruitio/en/latest/>
    Amazon AWS IoT (adafruit_aws_iot) <https://docs.circuitpython.org/projects/aws_iot/en/latest/>
    Azure IoT (adafruit_azureiot) <https://docs.circuitpython.org/projects/azureiot/en/latest/>
    Google Cloud IoT Core (adafruit_gc_iot_core) <https://docs.circuitpython.org/projects/gc_iot_core/en/latest/>
    Hue Lights (adafruit_hue) <https://docs.circuitpython.org/projects/hue/en/latest/>
    LIFX Lights (adafruit_lifx) <https://docs.circuitpython.org/projects/lifx/en/latest/>

Internet/Internet-of-Things Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for interfacing with the internet, including IoT protocols.

.. toctree::

    Connection Manager (adafruit_connectionmanager) <https://docs.circuitpython.org/projects/connectionmanager/en/latest/>
    Fake Requests (adafruit_fakerequests) <https://docs.circuitpython.org/projects/fakerequests/en/latest/>
    HTTP Server (adafruit_httpserver) <https://docs.circuitpython.org/projects/httpserver/en/latest/>
    JSON Stream (adafruit_json_stream) <https://docs.circuitpython.org/projects/json_stream/en/latest/>
    JSON Web Token (JWT) (adafruit_jwt) <https://docs.circuitpython.org/projects/jwt/en/latest/>
    MiniMQTT (adafruit_minimqtt) <https://docs.circuitpython.org/projects/minimqtt/en/latest/>
    NTP (Network time Protocol) (adafruit_ntp) <https://docs.circuitpython.org/projects/ntp/en/latest/>
    Requests (adafruit_requests) <https://docs.circuitpython.org/projects/requests/en/latest/>
    OAuth2.0 (adafruit_oauth2) <https://docs.circuitpython.org/projects/oauth2/en/latest/>
    Template Engine (adafruit_templateengine) <https://docs.circuitpython.org/projects/templateengine/en/latest/>

Bluetooth Low Energy Helpers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Helpers for Bluetooth Low Energy (BLE).

.. toctree::

    Bluefruit LE Connect App (adafruit_bluefruitconnect) <https://docs.circuitpython.org/projects/bluefruitconnect/en/latest/>
    BLE Base Library (adafruit_ble) <https://docs.circuitpython.org/projects/ble/en/latest/>
    BLE Adafruit Services (adafruit_ble_adafruit) <https://docs.circuitpython.org/projects/ble_adafruit/en/latest/>
    BLE Apple Media Service (adafruit_ble_apple_media) <https://docs.circuitpython.org/projects/ble_apple_media/en/latest/>
    BLE Apple Notification Center Service (adafruit_ble_apple_notification_center) <https://docs.circuitpython.org/projects/ble_apple_notification_center/en/latest/>
    BLE Location Beacons (adafruit_ble_beacon) <https://docs.circuitpython.org/projects/ble_beacon/en/latest/>
    BLE BerryMed Pulse Oximeter Service (adafruit_ble_berrymed_pulse_oximeter) <https://docs.circuitpython.org/projects/ble_berrymed_pulse_oximeter/en/latest/>
    BLE BroadcastNet (adafruit_ble_broadcastnet) <https://docs.circuitpython.org/projects/ble_broadcastnet/en/latest/>
    BLE Cycling Speed and Cadence (adafruit_ble_cycling_speed_and_cadence) <https://docs.circuitpython.org/projects/ble_cycling_speed_and_cadence/en/latest/>
    BLE Eddystone Beacon (adafruit_ble_eddystone) <https://docs.circuitpython.org/projects/ble_eddystone/en/latest/>
    BLE File Transfer (adafruit_ble_file_transfer) <https://docs.circuitpython.org/projects/ble_file_transfer/en/latest/>
    BLE Heart Rate (adafruit_ble_heart_rate) <https://docs.circuitpython.org/projects/ble_heart_rate/en/latest/>
    BLE iBBQ (adafruit_ble_ibbq) <https://docs.circuitpython.org/projects/ble_ibbq/en/latest/>
    BLE LYWSD03MMC (Xiaomi Mijia) (adafruit_ble_lywsd03mmc) <https://docs.circuitpython.org/projects/ble_lywsd03mmc/en/latest/>
    BLE Magic Light (adafruit_ble_magic_light) <https://docs.circuitpython.org/projects/ble_magic_light/en/latest/>
    BLE MIDI (adafruit_ble_midi) <https://docs.circuitpython.org/projects/ble_midi/en/latest/>
    BLE Radio (adafruit_ble_radio) <https://docs.circuitpython.org/projects/ble_radio/en/latest/>


LoRa Wireless Helpers
^^^^^^^^^^^^^^^^^^^^^

Helpers for wireless communication via LoRa.

.. toctree::

    TinyLoRa TTN Helper (LoRaWAN) (adafruit_tinylora) <https://docs.circuitpython.org/projects/tinylora/en/latest/>

Cryptography Helpers
^^^^^^^^^^^^^^^^^^^^^

Helpers for secure communication.

.. toctree::

    RSA (adafruit_rsa) <https://docs.circuitpython.org/projects/rsa/en/latest/>

CPython-module Helpers
^^^^^^^^^^^^^^^^^^^^^^^

Pure-Python implementations of standard CPython libraries. Some of these
modules may have a CircuitPython Core API implementation too.

.. toctree::

    asyncio (asyncio) <https://docs.circuitpython.org/projects/asyncio/en/latest/>
    binascii (adafruit_binascii) <https://docs.circuitpython.org/projects/binascii/en/latest/>
    datetime (adafruit_datetime) <https://docs.circuitpython.org/projects/datetime/en/latest/>
    IterTools (adafruit_itertools) <https://docs.circuitpython.org/projects/itertools/en/latest/>
    pathlib (adafruit_pathlib) <https://docs.circuitpython.org/projects/pathlib/en/latest/>
    Logging  (adafruit_logging) <https://docs.circuitpython.org/projects/logging/en/latest/>
    hashlib (adafruit_hashlib) <https://docs.circuitpython.org/projects/hashlib/en/latest/>

Audio Helpers
^^^^^^^^^^^^^^^

Music, noisemakers, and more.

.. toctree::

    MIDI (adafruit_midi) <https://docs.circuitpython.org/projects/midi/en/latest/>
    Ring Tone Text Transfer Language (RTTTL) (adafruit_rtttl) <https://docs.circuitpython.org/projects/rtttl/en/latest/>
    Waveform Generation (adafruit_waveform) <https://docs.circuitpython.org/projects/waveform/en/latest/>
    Wave file I/O (adafruit_wave) <https://docs.circuitpython.org/projects/wave/en/latest/>

Miscellaneous Helpers
^^^^^^^^^^^^^^^^^^^^^^^

.. toctree::

    AVR programming (adafruit_avrprog) <https://docs.circuitpython.org/projects/avrprog/en/latest/>
    BitbangIO (adafruit_bitbangio) <https://docs.circuitpython.org/projects/bitbangio/en/latest/>
    Board Test Suite (adafruit_boardtest) <https://docs.circuitpython.org/projects/boardtest/en/latest/>
    Colorsys (colorsys) <https://docs.circuitpython.org/projects/colorsys/en/latest/>
    Color Terminal (color_terminal) <https://docs.circuitpython.org/projects/color_terminal/en/latest/>
    Dang (dang) <https://docs.circuitpython.org/projects/dang/en/latest/>
    Debouncer (adafruit_debouncer) <https://docs.circuitpython.org/projects/debouncer/en/latest/>
    Debug I2C (adafruit_debug_i2c) <https://docs.circuitpython.org/projects/debug_i2c/en/latest/>
    Ducky (adafruit_ducky) <https://docs.circuitpython.org/projects/ducky/en/latest/>
    InfraRed Remote (adafruit_irremote) <https://docs.circuitpython.org/projects/irremote/en/latest/>
    Mini ESP Tool (ESP chips loader) (adafruit_miniesptool) <https://docs.circuitpython.org/projects/miniesptool/en/latest/>
    NeoKey (adafruit_neokey) <https://docs.circuitpython.org/projects/neokey/en/latest/>
    OneWire (adafruit_onewire) <https://docs.circuitpython.org/projects/onewire/en/latest/>
    Pastebin services (adafruit_pastebin) <https://docs.circuitpython.org/projects/pastebin/en/latest/>
    PIOASM converter for RP2 boards (adafruit_pioasm) <https://docs.circuitpython.org/projects/pioasm/en/latest/>
    PIO UART (adafruit_pio_uart) <https://docs.circuitpython.org/projects/pio_uart/en/latest/>
    Prompt Toolkit (adafruit_prompt_toolkit) <https://docs.circuitpython.org/projects/prompt_toolkit/en/latest/>
    Radial Controller (adafruit_radial-controller) <https://docs.circuitpython.org/projects/radial-controller/en/latest/>
    SD Card (adafruit_sd) <https://docs.circuitpython.org/projects/sd/en/latest/>
    SimpleIO (simpleio) <https://docs.circuitpython.org/projects/simpleio/en/latest/>
    SimpleMath (adafruit_simplemath) <https://docs.circuitpython.org/projects/simplemath/en/latest/>
    Test Repo (adafruit_testrepo) <https://docs.circuitpython.org/projects/testrepo/en/latest/>
    USB HID - Human Interface Device (Keyboard and Mouse) (adafruit_hid) <https://docs.circuitpython.org/projects/hid/en/latest/>
    USB Host Descriptors (adafruit_usb-host-descriptors) <https://docs.circuitpython.org/projects/usb-host-descriptors/en/latest/>
    USB Host Mass Storage (adafruit_usb-host-mass-storage) <https://docs.circuitpython.org/projects/usb-host-mass-storage/en/latest/>
    USB Host MIDI (adafruit_usb-host-midi) <https://docs.circuitpython.org/projects/usb-host-midi/en/latest/>
    Ticks (adafruit_ticks) <https://docs.circuitpython.org/projects/ticks/en/latest/>

Blinky
--------

Multi-color LED drivers.

.. toctree::

    DotStar (adafruit_dotstar) <https://docs.circuitpython.org/projects/dotstar/en/latest/>
    NeoPixel (neopixel) <https://docs.circuitpython.org/projects/neopixel/en/latest/>
    NeoPixel SPI (neopixel_spi) <https://docs.circuitpython.org/projects/neopixel_spi/en/latest/>
    NeoPxl8 (adafruit_neopxl8) <https://docs.circuitpython.org/projects/neopxl8/en/latest/>
    Pixie (adafruit_pixie) <https://docs.circuitpython.org/projects/pixie/en/latest/>
    RGB LED (adafruit_rgbled) <https://docs.circuitpython.org/projects/rgbled/en/latest/>
    TM1814 (adafruit_tm1814) <https://docs.circuitpython.org/projects/tm1814/en/latest/>
    WS2801 (adafruit_ws2801) <https://docs.circuitpython.org/projects/ws2801/en/latest/>

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

    GC9A01A (displayio) (adafruit_gc9a01a) <https://docs.circuitpython.org/projects/gc9a01a/en/latest/>
    HX8357 (displayio) (adafruit_hx8357) <https://docs.circuitpython.org/projects/hx8357/en/latest/>
    ILI9341 and ILI9340 (displayio) (adafruit_ili9341) <https://docs.circuitpython.org/projects/ili9341/en/latest/>
    ST7735 (displayio) (adafruit_st7735) <https://docs.circuitpython.org/projects/st7735/en/latest/>
    ST7735R (displayio) (adafruit_st7735r) <https://docs.circuitpython.org/projects/st7735r/en/latest/>
    ST7789 (displayio) (adafruit_st7789) <https://docs.circuitpython.org/projects/st7789/en/latest/>
    RGB Displays (framebuf) (adafruit_rgb_display) <https://docs.circuitpython.org/projects/rgb_display/en/latest/>

OLED
^^^^^^^^^^^^^^^

.. toctree::

    SH1106 OLED (displayio) (adafruit_displayio_sh1106) <https://docs.circuitpython.org/projects/displayio_sh1106/en/latest/>
    SH1107 OLED (displayio) (adafruit_displayio-sh1107) <https://docs.circuitpython.org/projects/displayio-sh1107/en/latest/>
    SSD1305 OLED (displayio) (adafruit_displayio_ssd1305) <https://docs.circuitpython.org/projects/displayio_ssd1305/en/latest/>
    SSD1305 OLED (framebuf) (adafruit_ssd1305) <https://docs.circuitpython.org/projects/ssd1305/en/latest/>
    SSD1306 OLED (displayio) (adafruit_displayio_ssd1306) <https://docs.circuitpython.org/projects/displayio_ssd1306/en/latest/>
    SSD1306 OLED (framebuf) (adafruit_ssd1306) <https://docs.circuitpython.org/projects/ssd1306/en/latest/>
    SSD1322 OLED (displayio) (adafruit_ssd1322) <https://docs.circuitpython.org/projects/ssd1322/en/latest/>
    SSD1325 OLED (displayio) (adafruit_ssd1325) <https://docs.circuitpython.org/projects/ssd1325/en/latest/>
    SSD1327 OLED (displayio) (adafruit_ssd1327) <https://docs.circuitpython.org/projects/ssd1327/en/latest/>
    SSD1331 OLED (displayio) (adafruit_ssd1331) <https://docs.circuitpython.org/projects/ssd1331/en/latest/>
    SSD1351 OLED (displayio) (adafruit_ssd1351) <https://docs.circuitpython.org/projects/ssd1351/en/latest/>

E-Paper / E-Ink
^^^^^^^^^^^^^^^

.. toctree::

    ACeP7In (displayio) (adafruit_acep7in) <https://docs.circuitpython.org/projects/acep7in/en/latest/>
    E-Paper Display (framebuf) (adafruit_epd) <https://docs.circuitpython.org/projects/epd/en/latest/>
    EK79686 (displayio) (adafruit_ek79686) <https://docs.circuitpython.org/projects/ek79686/en/latest/>
    IL0373 (displayio) (adafruit_il0373) <https://docs.circuitpython.org/projects/il0373/en/latest/>
    IL0398 (displayio) (adafruit_il0398) <https://docs.circuitpython.org/projects/il0398/en/latest/>
    IL91874 (displayio) (adafruit_il91874) <https://docs.circuitpython.org/projects/il91874/en/latest/>
    JD79661 (displayio) (adafruit_jd79661) <https://docs.circuitpython.org/projects/jd79661/en/latest/>
    JD79667 (displayio) (adafruit_jd79667) <https://docs.circuitpython.org/projects/jd79667/en/latest/>
    SPD1656 (displayio) (adafruit_spd1656) <https://docs.circuitpython.org/projects/spd1656/en/latest/>
    SSD1608 (displayio) (adafruit_ssd1608) <https://docs.circuitpython.org/projects/ssd1608/en/latest/>
    SSD1675 (displayio) (adafruit_ssd1675) <https://docs.circuitpython.org/projects/ssd1675/en/latest/>
    SSD1680 (displayio) (adafruit_ssd1680) <https://docs.circuitpython.org/projects/ssd1680/en/latest/>
    SSD1681 (displayio) (adafruit_ssd1681) <https://docs.circuitpython.org/projects/ssd1681/en/latest/>
    UC8151D (displayio) (adafruit_uc8151d) <https://docs.circuitpython.org/projects/uc8151d/en/latest/>
    UC8179 (displayio) (adafruit_uc8179) <https://docs.circuitpython.org/projects/uc8179/en/latest/>
    UC8253 (displayio) (adafruit_uc8253) <https://docs.circuitpython.org/projects/uc8253/en/latest/>

Other
^^^^^^^^^^^^^^^

.. toctree::

    Character LCD (adafruit_charlcd) <https://docs.circuitpython.org/projects/charlcd/en/latest/>
    FT5336 Capacitive Touch Screen Driver (adafruit_ft5336) <https://docs.circuitpython.org/projects/ft5336/en/latest/>
    HT16K33 LED Matrices and Segment Displays (adafruit_ht16k33) <https://docs.circuitpython.org/projects/ht16k33/en/latest/>
    IS31FL3731 Charlieplexed LED Matrix (adafruit_is31fl3731) <https://docs.circuitpython.org/projects/is31fl3731/en/latest/>
    IS31FL3741 RGB LED Matrix driver (adafruit_is31fl3741) <https://docs.circuitpython.org/projects/is31fl3741/en/latest/>
    MAX7219 LED Matrix (adafruit_max7219) <https://docs.circuitpython.org/projects/max7219/en/latest/>
    Nokia PCD8544 Display (adafruit_pcd8544) <https://docs.circuitpython.org/projects/pcd8544/en/latest/>
    RA8875 40-Pin Display Driver (adafruit_ra8875) <https://docs.circuitpython.org/projects/ra8875/en/latest/>
    Sharp Memory Display (adafruit_sharpmemorydisplay) <https://docs.circuitpython.org/projects/sharpmemorydisplay/en/latest/>
    ST7565 Graphic Displays (adafruit_st7565) <https://docs.circuitpython.org/projects/st7565/en/latest/>
    TSC2007 Resistive Touch Screen Driver (adafruit_tsc2007) <https://docs.circuitpython.org/projects/tsc2007/en/latest/>

Real-time clocks
-----------------

Chips that keep current calendar time with a backup battery. The current date and time is available
through ``datetime``.

.. toctree::

    DS1307 Real-time Clock (5V RTC Breakout) (adafruit_ds1307) <https://docs.circuitpython.org/projects/ds1307/en/latest/>
    DS3231 Real-time Clock (Precision RTC) (adafruit_ds3231) <https://docs.circuitpython.org/projects/ds3231/en/latest/>
    PCF8523 Real-time Clock (Adalogger RTC) (adafruit_pcf8523) <https://docs.circuitpython.org/projects/pcf8523/en/latest/>
    PCF8563 Real-time Clock (adafruit_pcf8563) <https://docs.circuitpython.org/projects/pcf8563/en/latest/>

Motion Sensors
----------------

Motion relating sensing including ``acceleration``, ``magnetic``, ``gyro``, and ``orientation``.

.. toctree::

    ADXL34x 3 Axis Accelerometer (adafruit_adxl34x) <https://docs.circuitpython.org/projects/adxl34x/en/latest/>
    ADXL37x 3 Axis Accelerometer (adafruit_adxl37x) <https://docs.circuitpython.org/projects/adxl37x/en/latest/>
    AS5600 Magnetic Angle Sensor (adafruit_as5600) <https://docs.circuitpython.org/projects/as5600/en/latest/>
    BNO055 Accelerometer, Magnetometer, Gyroscope and Absolution Orientation (adafruit_bno055) <https://docs.circuitpython.org/projects/bno055/en/latest/>
    BNO08X  9 Axis Sensor Fusion IMU (adafruit_bno08x) <https://docs.circuitpython.org/projects/bno08x/en/latest/>
    BNO08X_RVC Simple UART Heading Library (adafruit_bno08x_rvc) <https://docs.circuitpython.org/projects/bno08x_rvc/en/latest/>
    FXAS21002C Gyroscope (adafruit_fxas21002c) <https://docs.circuitpython.org/projects/fxas21002c/en/latest/>
    FXOS8700 Accelerometer (adafruit_fxos8700) <https://docs.circuitpython.org/projects/fxos8700/en/latest/>
    GPS Global Position (adafruit_gps) <https://docs.circuitpython.org/projects/gps/en/latest/>
    ICM20X Wide-range 6-DoF Accelerometer and Gyro Family (adafruit_icm20x) <https://docs.circuitpython.org/projects/icm20x/en/latest/>
    L3GD20 3-Axis Gyroscope (adafruit_l3gd20) <https://docs.circuitpython.org/projects/l3gd20/en/latest/>
    LIS2MDL 3-Axis Magnetometer (adafruit_lis2mdl) <https://docs.circuitpython.org/projects/lis2mdl/en/latest/>
    LIS331HH and H3LIS331 3-Axis Accelerometers (adafruit_lis331) <https://docs.circuitpython.org/projects/lis331/en/latest/>
    LIS3DH Accelerometer (adafruit_lis3dh) <https://docs.circuitpython.org/projects/lis3dh/en/latest/>
    LIS3MDL 3-Axis Magnetometer (adafruit_lis3mdl) <https://docs.circuitpython.org/projects/lis3mdl/en/latest/>
    LSM303 Accelerometer Onl (adafruit_lsm303-accel)y<https://docs.circuitpython.org/projects/lsm303-accel/en/latest/>
    LSM303 Accelerometer and Magnetometer (adafruit_lsm303) <https://docs.circuitpython.org/projects/lsm303/en/latest/>
    LSM303DLH Magnetometer Onl (adafruit_lsm303dlh-mag)y<https://docs.circuitpython.org/projects/lsm303dlh-mag/en/latest/>
    LSM6DSOX, LSM6DS33, and ISM330DHCT  Accelerometer, Gyroscope and Temperature (adafruit_lsm6dsox) <https://docs.circuitpython.org/projects/lsm6dsox/en/latest/>
    LSM9DS0 Accelerometer, Magnetometer, Gyroscope and Temperature (adafruit_lsm9ds0) <https://docs.circuitpython.org/projects/lsm9ds0/en/latest/>
    LSM9DS1 Accelerometer, Magnetometer, Gyroscope and Temperature (adafruit_lsm9ds1) <https://docs.circuitpython.org/projects/lsm9ds1/en/latest/>
    MLX90393 3 Axis Magnetometer (adafruit_mlx90393) <https://docs.circuitpython.org/projects/mlx90393/en/latest/>
    MLX90395 3-Axis Magnetometer (adafruit_mlx90395) <https://docs.circuitpython.org/projects/mlx90395/en/latest/>
    MMA8451 3 Axis Accelerometer (adafruit_mma8451) <https://docs.circuitpython.org/projects/mma8451/en/latest/>
    MMC56X3 Magnetometers (adafruit_mmc56x3) <https://docs.circuitpython.org/projects/mmc56x3/en/latest/>
    MPU6050 Accelerometer, Gyroscope, and Temperature Sensor (adafruit_mpu6050) <https://docs.circuitpython.org/projects/mpu6050/en/latest/>
    MSA301 3 Axis Accelerometer (adafruit_msa301) <https://docs.circuitpython.org/projects/msa301/en/latest/>
    TLV493D 3 Axis Magnetometer (adafruit_tlv493d) <https://docs.circuitpython.org/projects/tlv493d/en/latest/>

Environmental Sensors
----------------------

Sense attributes of the environment including ``temperature``, ``relative_humidity``, ``pressure``,
equivalent carbon dioxide (``eco2`` / ``eCO2``), and total volatile organic compounds (``tvoc`` /
``TVOC``).

.. toctree::


    ADT7410 High Accuracy Temperature Sensor (adafruit_adt7410) <https://docs.circuitpython.org/projects/adt7410/en/latest/>
    AGS02MA Gas Sensor (adafruit_ags02ma) <https://docs.circuitpython.org/projects/ags02ma/en/latest/>
    AHTx0 Tempertaure and Humidity Sensor (adafruit_ahtx0) <https://docs.circuitpython.org/projects/ahtx0/en/latest/>
    AM2320 Temperature and Humidity (adafruit_am2320) <https://docs.circuitpython.org/projects/am2320/en/latest/>
    BME280 Temperature, Humidity and Pressure (adafruit_bme280) <https://docs.circuitpython.org/projects/bme280/en/latest/>
    BME680 Temperature, Humidity, Pressure and Gas (adafruit_bme680) <https://docs.circuitpython.org/projects/bme680/en/latest/>
    BMP280 Barometric Pressure and Altitude (adafruit_bmp280) <https://docs.circuitpython.org/projects/bmp280/en/latest/>
    BMP3xx Barometric Pressure and Altimeter (adafruit_bmp3xx) <https://docs.circuitpython.org/projects/bmp3xx/en/latest/>
    BMP5xx Barometric Pressure and Altimeter (adafruit_bmp5xx) <https://docs.circuitpython.org/projects/bmp5xx/en/latest/>
    CCS811 Air Quality (adafruit_ccs811) <https://docs.circuitpython.org/projects/ccs811/en/latest/>
    DHT Temperature and Humidity (adafruit_dht) <https://docs.circuitpython.org/projects/dht/en/latest/>
    DPS310 Precision Barometric Pressure / Altitude Sensor (adafruit_dps310) <https://docs.circuitpython.org/projects/dps310/en/latest/>
    DS18x20 Temperature (adafruit_ds18x20) <https://docs.circuitpython.org/projects/ds18x20/en/latest/>
    ENS160 (ScioSense) digital multi-gas sensor (adafruit_ens160) <https://docs.circuitpython.org/projects/ens160/en/latest/>
    HDC302x Temperature and Humidity Sensor (adafruit_hdc302x) <https://docs.circuitpython.org/projects/hdc302x/en/latest/>
    HTS221 Temperature and Humidity Sensor (adafruit_hts221) <https://docs.circuitpython.org/projects/hts221/en/latest/>
    HTU21D Temperature and Humidity (adafruit_htu21d) <https://docs.circuitpython.org/projects/htu21d/en/latest/>
    HTU31D Temperature and Humidity (adafruit_htu31d) <https://docs.circuitpython.org/projects/htu31d/en/latest/>
    LPS2X Family of Barometric Pressure, Temperature Sensors (adafruit_lps2x) <https://docs.circuitpython.org/projects/lps2x/en/latest/>
    LPS28 Pressure Sensor (adafruit_lps28) <https://docs.circuitpython.org/projects/lps28/en/latest/>
    LPS35HW Water Resistant Barometric Pressure, Temperature (adafruit_lps35hw) <https://docs.circuitpython.org/projects/lps35hw/en/latest/>
    SGP40 Air Quality Sensor (adafruit_sgp40) <https://docs.circuitpython.org/projects/sgp40/en/latest/>
    MAX31855 Thermocouple Amplifier, Temperature (adafruit_max31855) <https://docs.circuitpython.org/projects/max31855/en/latest/>
    MAX31856 Thermocouple Amplifier, Temperature (adafruit_max31856) <https://docs.circuitpython.org/projects/max31856/en/latest/>
    MAX31865 Thermocouple Amplifier, Temperature (adafruit_max31865) <https://docs.circuitpython.org/projects/max31865/en/latest/>
    MCP9600 Thermocouple Amplifier (adafruit_mcp9600) <https://docs.circuitpython.org/projects/mcp9600/en/latest/>
    MCP9808 Temperature (adafruit_mcp9808) <https://docs.circuitpython.org/projects/mcp9808/en/latest/>
    MLX90614 Contactless Temperature (adafruit_mlx90614) <https://docs.circuitpython.org/projects/mlx90614/en/latest/>
    MLX90632 FIR Remote Thermal Temperature Sensor (adafruit_mlx90632) <https://docs.circuitpython.org/projects/mlx90632/en/latest/>
    MPL115A2 Barometric Pressure, Temperature (adafruit_mpl115a2) <https://docs.circuitpython.org/projects/mpl115a2/en/latest/>
    MPL3115A2 Barometric Pressure, Altitude and Temperature Sensor (adafruit_mpl3115a2) <https://docs.circuitpython.org/projects/mpl3115a2/en/latest/>
    MPRLS Ported Absolute Pressure (adafruit_mprls) <https://docs.circuitpython.org/projects/mprls/en/latest/>
    MS8607 Pressure, Temperature, Humidity (adafruit_ms8607) <https://docs.circuitpython.org/projects/ms8607/en/latest/>
    PCT2075 Temperature Sensor (adafruit_pct2075) <https://docs.circuitpython.org/projects/pct2075/en/latest/>
    PM25 Air Quality Sensor (adafruit_pm25) <https://docs.circuitpython.org/projects/pm25/en/latest/>
    SCD30 CO2, Temperature, and Humidity Sensor (adafruit_scd30) <https://docs.circuitpython.org/projects/scd30/en/latest/>
    SCD4x Temperature and Humidity Sensor (adafruit_scd4x) <https://docs.circuitpython.org/projects/scd4x/en/latest/>
    SEN6x Environmental Sensor (adafruit_sen6x) <https://docs.circuitpython.org/projects/sen6x/en/latest/>
    SGP30 Air Quality (adafruit_sgp30) <https://docs.circuitpython.org/projects/sgp30/en/latest/>
    SHT31-D Temperature and Humidity (adafruit_sht31d) <https://docs.circuitpython.org/projects/sht31d/en/latest/>
    SHT4x Temperature and Humidity (adafruit_sht4x) <https://docs.circuitpython.org/projects/sht4x/en/latest/>
    SHTC3 Temperature and Humidity (adafruit_shtc3) <https://docs.circuitpython.org/projects/shtc3/en/latest/>
    Si7021 Temperature and Humidity (adafruit_si7021) <https://docs.circuitpython.org/projects/si7021/en/latest/>
    SPA06-003 Temperature and Pressure (adafruit_spa06_003) <https://docs.circuitpython.org/projects/spa06_003/en/latest/>
    TC74 Digital Temperature Sensor (adafruit_tc74) <https://docs.circuitpython.org/projects/tc74/en/latest/>
    TMP006 Contactless IR Thermopile Sensor (adafruit_tmp006) <https://docs.circuitpython.org/projects/tmp006/en/latest/>
    TMP007 Contactless Temperature (adafruit_tmp007) <https://docs.circuitpython.org/projects/tmp007/en/latest/>
    TMP117 High-Precision Temperature Sensor (adafruit_tmp117) <https://docs.circuitpython.org/projects/tmp117/en/latest/>
    Thermistor Temperature (adafruit_thermistor) <https://docs.circuitpython.org/projects/thermistor/en/latest/>

Light Sensors
---------------

These sensors detect light related attributes such as ``color``, ``light`` (unit-less), and
``lux`` (light in SI lux).

.. toctree::

    APDS9960 Proximity, Light, RGB, and Gesture (adafruit_apds9960) <https://docs.circuitpython.org/projects/apds9960/en/latest/>
    AS726x Color Spectrum Sensor (adafruit_as726x) <https://docs.circuitpython.org/projects/as726x/en/latest/>
    AS7341 11-Channel Multi-Spectral Digital Sensor (adafruit_as7341) <https://docs.circuitpython.org/projects/as7341/en/latest/>
    BH1750 Ambient Light (adafruit_bh1750) <https://docs.circuitpython.org/projects/bh1750/en/latest/>
    GUVx I2C UV Light Sensors (adafruit_guvx-i2c) <https://docs.circuitpython.org/projects/guvx-i2c/en/latest/>
    LTR329 LTR303 Light Sensors (adafruit_ltr329-ltr303) <https://docs.circuitpython.org/projects/ltr329-ltr303/en/latest/>
    LTR390 Ambient Light and UV Sensor (adafruit_ltr390) <https://docs.circuitpython.org/projects/ltr390/en/latest/>
    OPT4048 Tri-Stimulus XYZ Color and Lux Sensor <https://docs.circuitpython.org/projects/opt4048/en/latest/>
    TCS34725 Color Sensor (adafruit_tcs34725) <https://docs.circuitpython.org/projects/tcs34725/en/latest/>
    TSL2561 Light Sensor (adafruit_tsl2561) <https://docs.circuitpython.org/projects/tsl2561/en/latest/>
    TSL2591 High Dynamic Range Light Sensor (adafruit_tsl2591) <https://docs.circuitpython.org/projects/tsl2591/en/latest/>
    VCNL4010 Proximity and Light (adafruit_vcnl4010) <https://docs.circuitpython.org/projects/vcnl4010/en/latest/>
    VCNL4020 Proximity and Light (adafruit_vcnl4020) <https://docs.circuitpython.org/projects/vcnl4020/en/latest/>
    VCNL4040 Proximity and Light (adafruit_vcnl4040) <https://docs.circuitpython.org/projects/vcnl4040/en/latest/>
    VCNL4200 Proximity and Light (adafruit_vcnl4200) <https://docs.circuitpython.org/projects/vcnl4200/en/latest/>
    VEML6070 UV Index (adafruit_veml6070) <https://docs.circuitpython.org/projects/veml6070/en/latest/>
    VEML6075 UV Index (adafruit_veml6075) <https://docs.circuitpython.org/projects/veml6075/en/latest/>
    VEML7700 High Accuracy Ambient Light Sensor (adafruit_veml7700) <https://docs.circuitpython.org/projects/veml7700/en/latest/>
    SI1145 Digital UV Index IR Visible Light Sensor (adafruit_si1145) <https://docs.circuitpython.org/projects/si1145/en/latest/>

Distance Sensors
------------------

These sensors measure the ``distance`` to another object and may also measure light level (``light`` and ``lux``).

.. toctree::

    Garmin LIDARLite I2C (adafruit_lidarlite) <https://docs.circuitpython.org/projects/lidarlite/en/latest/>
    HC-SR04 Ultrasonic Range Sensors (adafruit_hcsr04) <https://docs.circuitpython.org/projects/hcsr04/en/latest/>
    Slamtech RPLidar (adafruit_rplidar) <https://docs.circuitpython.org/projects/rplidar/en/latest/>
    TFmini IR Time of Flight ~30cm - 12m (adafruit_tfmini) <https://docs.circuitpython.org/projects/tfmini/en/latest/>
    US-100 Ultrasonic Distance Sensor (adafruit_us100) <https://docs.circuitpython.org/projects/us100/en/latest/>
    VL6180x 5 - 100 mm (adafruit_vl6180x) <https://docs.circuitpython.org/projects/vl6180x/en/latest/>
    VL53L0x ~30 - 1000 mm (adafruit_vl53l0x) <https://docs.circuitpython.org/projects/vl53l0x/en/latest/>
    VL53L1X ~30 - 4000 mm (adafruit_vl53l1x) <https://docs.circuitpython.org/projects/vl53l1x/en/latest/>
    VL53L4CD Time of Flight (adafruit_vl53l4cd) <https://docs.circuitpython.org/projects/vl53l4cd/en/latest/>

Radio
--------

These chips communicate to others over radio.

.. toctree::

    Adafruit Bluefruit LE SPI Friend (adafruit_bluefruitspi) <https://docs.circuitpython.org/projects/bluefruitspi/en/latest/>
    AirLift Co-Processor Manager (adafruit_airlift) <https://docs.circuitpython.org/projects/airlift/en/latest/>
    ESP WiFi Co-Processor using AT Commands (adafruit_esp-atcontrol) <https://docs.circuitpython.org/projects/esp-atcontrol/en/latest/>
    ESP32 WiFi Co-Processor over SPI (adafruit_esp32spi) <https://docs.circuitpython.org/projects/esp32spi/en/latest/>
    RFM LoRa & Packet Radio (adafruit_rfm) <https://docs.circuitpython.org/projects/rfm/en/latest/>
    RFM9x LoRa (adafruit_rfm9x) <https://docs.circuitpython.org/projects/rfm9x/en/latest/>
    RFM69 Packet Radio (adafruit_rfm69) <https://docs.circuitpython.org/projects/rfm69/en/latest/>
    PN532 NFC/RFID (adafruit_pn532) <https://docs.circuitpython.org/projects/pn532/en/latest/>

IO Expansion
--------------

These provide functionality similar to ``analogio``, ``digitalio``, ``pulseio``, and ``touchio``.

.. toctree::

    AD569x 16-bit DAC (adafruit_ad569x) <https://docs.circuitpython.org/projects/ad569x/en/latest/>
    Adafruit SeeSaw (adafruit_seesaw) <https://docs.circuitpython.org/projects/seesaw/en/latest/>
    ADG72x Analog Matrix Switches (adafruit_adg72x) <https://docs.circuitpython.org/projects/adg72x/en/latest/>
    ADS1x15 Analog-to-Digital Converter  (adafruit_ads1x15) <https://docs.circuitpython.org/projects/ads1x15/en/latest/>
    ADS7830 8-Channel 8-Bit ADC (adafruit_ads7830) <https://docs.circuitpython.org/projects/ads7830/en/latest/>
    AW9523 GPIO expander and LED driver (adafruit_aw9523) <https://docs.circuitpython.org/projects/aw9523/en/latest/>
    Crickit Robotics Boards (adafruit_crickit) <https://docs.circuitpython.org/projects/crickit/en/latest/>
    CST8XX Capacitive Touch (adafruit_cst8xx) <https://docs.circuitpython.org/projects/cst8xx/en/latest/>
    DACx578 8 x Channel 12-Bit DAC (adafruit_dacx578) <https://docs.circuitpython.org/projects/dacx578/en/latest/>
    DS2413 OneWire GPIO Expander (adafruit_ds2413) <https://docs.circuitpython.org/projects/ds2413/en/latest/>
    FocalTech Capacitive Touch (adafruit_focaltouch) <https://docs.circuitpython.org/projects/focaltouch/en/latest/>
    HX711 24-bit ADC (adafruit_hx711) <https://docs.circuitpython.org/projects/hx711/en/latest/>
    MCP2515 CAN bus controller (adafruit_mcp2515) <https://docs.circuitpython.org/projects/mcp2515/en/latest/>
    MCP230xx GPIO Expander (adafruit_mcp230xx) <https://docs.circuitpython.org/projects/mcp230xx/en/latest/>
    MCP3xxx SPI ADC (adafruit_mcp3xxx) <https://docs.circuitpython.org/projects/mcp3xxx/en/latest/>
    MCP3421 18-bit ADC (adafruit_mcp3421) <https://docs.circuitpython.org/projects/mcp3421/en/latest/>
    MCP4725 Digital-to-Analog Converter (adafruit_mcp4725) <https://docs.circuitpython.org/projects/mcp4725/en/latest/>
    MCP4728 4-Channel, 12-bit Digital-to-Analog Converter (adafruit_mcp4728) <https://docs.circuitpython.org/projects/mcp4728/en/latest/>
    MPR121 Capacitive Touch Sensor (adafruit_mpr121) <https://docs.circuitpython.org/projects/mpr121/en/latest/>
    NAU7802 24-Bit ADC (cedargrove_nau7802) <https://docs.circuitpython.org/projects/nau7802/en/latest/>
    PCA9554 GPIO Expander (adafruit_pca9554) <https://docs.circuitpython.org/projects/pca9554/en/latest/>
    PCA9685 16 x 12-bit PWM Driver (adafruit_pca9685) <https://docs.circuitpython.org/projects/pca9685/en/latest/>
    PCF8574 GPIO Expander (adafruit_pcf8574) <https://docs.circuitpython.org/projects/pcf8574/en/latest/>
    PCF8575 GPIO Expander (adafruit_pcf8575) <https://docs.circuitpython.org/projects/pcf8575/en/latest/>
    PCF8591 ADC + DAC Combo (adafruit_pcf8591) <https://docs.circuitpython.org/projects/pcf8591/en/latest/>
    TCA8418 I2C Keyboard Multiplexor (adafruit_tca8418) <https://docs.circuitpython.org/projects/tca8418/en/latest/>
    TCA9548 I2C Multiplexer (adafruit_tca9548a) <https://docs.circuitpython.org/projects/tca9548a/en/latest/>
    TLA202X 12-bit I2C DAC (adafruit_tla202x) <https://docs.circuitpython.org/projects/tla202x/en/latest/>
    TLC5947 24 x 12-bit PWM Driver (adafruit_tlc5947) <https://docs.circuitpython.org/projects/tlc5947/en/latest/>
    TLC59711 12 x 16-bit PWM Driver (adafruit_tlc59711) <https://docs.circuitpython.org/projects/tlc59711/en/latest/>

Miscellaneous
----------------

.. toctree::

    24LC32 EEPROM (adafruit_24lc32) <https://docs.circuitpython.org/projects/24lc32/en/latest/>
    74HC595 Shift Register (adafruit_74hc595) <https://docs.circuitpython.org/projects/74hc595/en/latest/>
    ATECCx08 Cryptographic Co-Processor (adafruit_atecc) <https://docs.circuitpython.org/projects/atecc/en/latest/>
    AMG88xx Grid-Eye IR Camera (adafruit_amg88xx) <https://docs.circuitpython.org/projects/amg88xx/en/latest/>
    BD3491FS Audio Processor  (adafruit_bd3491fs) <https://docs.circuitpython.org/projects/bd3491fs/en/latest/>
    CAP1188 8-Key Capacitive Touch (adafruit_cap1188) <https://docs.circuitpython.org/projects/cap1188/en/latest/>
    CH9328 UART to HID Keyboard (adafruit_ch9328) <https://docs.circuitpython.org/projects/ch9328/en/latest/>
    DRV2605 Haptic Motor Controller (adafruit_drv2605) <https://docs.circuitpython.org/projects/drv2605/en/latest/>
    DS1841 I2C Logarithmic Potentiometer (adafruit_ds1841) <https://docs.circuitpython.org/projects/ds1841/en/latest/>
    DS248x 1-Wire to I2C (adafruit_ds248x) <https://docs.circuitpython.org/projects/ds248x/en/latest/>
    DS3502 I2C Potentiometer (adafruit_ds3502) <https://docs.circuitpython.org/projects/ds3502/en/latest/>
    Dymo Scale (adafruit_dymoscale) <https://docs.circuitpython.org/projects/dymoscale/en/latest/>
    Fingerprint Sensor (adafruit_fingerprint) <https://docs.circuitpython.org/projects/fingerprint/en/latest/>
    Floppy (adafruit_floppy) <https://docs.circuitpython.org/projects/floppy/en/latest/>
    FONA Cellular Module (adafruit_fona) <https://docs.circuitpython.org/projects/fona/en/latest/>
    FRAM Non-Volatile Memory (adafruit_fram) <https://docs.circuitpython.org/projects/fram/en/latest/>
    Gizmo (adafruit_gizmo) <https://docs.circuitpython.org/projects/gizmo/en/latest/>
    HUSB238 (adafruit_husb238) <https://docs.circuitpython.org/projects/husb238/en/latest/>
    INA219 High Side Current (adafruit_ina219) <https://docs.circuitpython.org/projects/ina219/en/latest/>
    INA228 High or Low Side Power Monitor (adafruit_ina228) <https://docs.circuitpython.org/projects/ina228/en/latest/>
    INA23x Current and Power Monitor (adafruit_ina23x) <https://docs.circuitpython.org/projects/ina23x/en/latest/>
    INA260 Current and Power Monitor (adafruit_ina260) <https://docs.circuitpython.org/projects/ina260/en/latest/>
    INA3221 Three Channel Amp Power Monitor (adafruit_ina3221) <https://docs.circuitpython.org/projects/ina3221/en/latest/>
    LC709203F Fuel Gauge and Battery Monitor (adafruit_lc709203f) <https://docs.circuitpython.org/projects/lc709203f/en/latest/>
    Matrix Keypad (adafruit_matrixkeypad) <https://docs.circuitpython.org/projects/matrixkeypad/en/latest/>
    MAX1704x Fuel Gauge (adafruit_max1704x) <https://docs.circuitpython.org/projects/max1704x/en/latest/>
    MAX9744 Audio Amplifier  (adafruit_max9744) <https://docs.circuitpython.org/projects/max9744/en/latest/>
    MLX90640 Thermal Camera (adafruit_mlx90640) <https://docs.circuitpython.org/projects/mlx90640/en/latest/>
    NeoTrellis 4x4 Keypad (adafruit_neotrellis) <https://docs.circuitpython.org/projects/neotrellis/en/latest/>
    NeoTrellis M4 4x8 Keypad (adafruit_trellism4) <https://docs.circuitpython.org/projects/trellism4/en/latest/>
    Nunchuk (adafruit_nunchuk) <https://docs.circuitpython.org/projects/nunchuk/en/latest/>
    OV2640 Camera (adafruit_ov2640) <https://docs.circuitpython.org/projects/ov2640/en/latest/>
    OV5640 Camera (adafruit_ov5640) <https://docs.circuitpython.org/projects/ov5640/en/latest/>
    OV7670 Camera (adafruit_ov7670) <https://docs.circuitpython.org/projects/ov7670/en/latest/>
    PCM51xx I2S DAC (adafruit_pcm51xx) <https://docs.circuitpython.org/projects/pcm51xx/en/latest/>
    Pixelbuf (adafruit_pixelbuf) <https://docs.circuitpython.org/projects/pixelbuf/en/latest/>
    RockBlock Iridium Satellite Modem (adafruit_rockblock) <https://docs.circuitpython.org/projects/rockblock/en/latest/>
    S-35710 Low-Power Wake Up Timer (adafruit_s35710) <https://docs.circuitpython.org/projects/s35710/en/latest/>
    Si4713 Stereo FM Transmitter (adafruit_si4713) <https://docs.circuitpython.org/projects/si4713/en/latest/>
    Si5351 Clock Generator (adafruit_si5351) <https://docs.circuitpython.org/projects/si5351/en/latest/>
    STMPE610 Resistive Touchscreen (adafruit_stmpe610) <https://docs.circuitpython.org/projects/stmpe610/en/latest/>
    TLV320DAC3100 I2S DAC (adafruit_tlv320) <https://docs.circuitpython.org/projects/tlv320/en/latest/>
    Touchscreen 4-Wire Resistive (adafruit_touchscreen) <https://docs.circuitpython.org/projects/touchscreen/en/latest/>
    TPA2016 Audio Amplifier with AGC (adafruit_tpa2016) <https://docs.circuitpython.org/projects/tpa2016/en/latest/>
    Trellis 4x4 Keypad (adafruit_trellis) <https://docs.circuitpython.org/projects/trellis/en/latest/>
    TT21100 Capacitive Touchscreen Driver (adafruit_tt21100) <https://docs.circuitpython.org/projects/tt21100/en/latest/>
    VC0706 TTL Camera (adafruit_vc0706) <https://docs.circuitpython.org/projects/vc0706/en/latest/>
    VS1053 Audio Codec (adafruit_vs1053) <https://docs.circuitpython.org/projects/vs1053/en/latest/>
    Wii Classic (adafruit_wii_classic) <https://docs.circuitpython.org/projects/wii_classic/en/latest/>
    Wiznet5k Ethernet Module (adafruit_wiznet5k) <https://docs.circuitpython.org/projects/wiznet5k/en/latest/>
    WM8960 Audio Codec (adafruit_wm8960) <https://docs.circuitpython.org/projects/wm8960/en/latest/>
