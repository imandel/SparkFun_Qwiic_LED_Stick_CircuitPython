Introduction
============

.. image:: https://readthedocs.org/projects/circuitpython-sparkfun_qwiic_led_stick_circuitpython/badge/?version=latest
    :target: https://circuitpython-sparkfun_qwiic_led_stick_circuitpython.readthedocs.io/
    :alt: Documentation Status

.. image:: https://img.shields.io/discord/327254708534116352.svg
    :target: https://adafru.it/discord
    :alt: Discord

.. image:: https://github.com/imandel/CircuitPython_SparkFun_Qwiic_LED_Stick_CircuitPython/workflows/Build%20CI/badge.svg
    :target: https://github.com/imandel/CircuitPython_SparkFun_Qwiic_LED_Stick_CircuitPython/actions
    :alt: Build Status

.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

CircuitPython librabry for the Sparkfun Qwiic LED Stick


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Bus Device <https://github.com/adafruit/Adafruit_CircuitPython_BusDevice>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_.

Installing from PyPI
=====================
.. note:: This library is not available on PyPI yet. Install documentation is included
   as a standard element. Stay tuned for PyPI availability!

   .. code-block:: shell
    pip install git+https://github.com/imandel/SparkFun_Qwiic_LED_Stick_CircuitPython.git


..    If the library is not planned for PyPI, remove the entire 'Installing from PyPI' section.

.. On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
.. PyPI <https://pypi.org/project/adafruit-circuitpython-sparkfun_qwiic_led_stick_circuitpython/>`_. To install for current user:

.. .. code-block:: shell

..     pip3 install adafruit-circuitpython-sparkfun-qwiic-led-stick-circuitpython

.. To install system-wide (this may be required in some cases):

.. .. code-block:: shell

..     sudo pip3 install adafruit-circuitpython-sparkfun-qwiic-led-stick-circuitpython

.. To install in a virtual environment in your current project:

.. .. code-block:: shell

..     mkdir project-name && cd project-name
..     python3 -m venv .env
..     source .env/bin/activate
..     pip3 install adafruit-circuitpython-sparkfun-qwiic-led-stick-circuitpython

Usage Example
=============
   .. code-block:: python
    import board
    import busio
    from adafruit_bus_device.i2c_device import I2CDevice
    from Sparkfun_Qwiic_LED_Stick_CircuitPython import LED_Stick

    i2c = busio.I2C(board.SCL, board.SDA)
    stick = LED_Stick(i2c)

    #set entire strip
    stick.set_LED_color(0,255,0)

    #set second LED
    stick.set_LED_color(255,0,0, 2).. .. 

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/imandel/CircuitPython_SparkFun_Qwiic_LED_Stick_CircuitPython/blob/master/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

Documentation
=============

For information on building library documentation, please check out `this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.
