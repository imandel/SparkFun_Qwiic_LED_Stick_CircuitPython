from adafruit_bus_device.i2c_device import I2CDevice

# Register addresses:
CHANGE_ADDRESS = 0xC7
CHANGE_LED_LENGTH = 0x70
WRITE_SINGLE_LED_COLOR = 0x71
WRITE_ALL_LED_COLOR = 0x72
WRITE_RED_ARRAY = 0x73
WRITE_GREEN_ARRAY = 0x74
WRITE_BLUE_ARRAY = 0x75
WRITE_SINGLE_LED_BRIGHTNESS = 0x76
WRITE_ALL_LED_BRIGHTNESS = 0x77
WRITE_ALL_LED_OFF = 0x78

_DEFAULT_ADDRESS = 0x23



class LED_Stick:
	"""I2C connected LED strip with addressable LEDs https://www.sparkfun.com/products/14783

	:param i2c_addr: I2C address of the button
	:type i2c_addr: int
	:param i2c_obj: initialized I2C object
	:type i2c_obj: adafruit_bus_device.i2c_device.I2CDevice

	"""
	__version__ = "0.0.0-auto.0"
	__repo__ = "https://github.com/FAR-Lab/CircuitPython_SparkFun_Qwiic_LED_Stick_CircuitPython.git"

	def __init__(self, i2c_obj, i2c_addr=_DEFAULT_ADDRESS):
		self.i2c = i2c_obj
		self.device = I2CDevice(i2c_obj, i2c_addr)
		self.length = 10
		self.i2c_addr = i2c_addr

	def __repr__(self):
		return f"{self.__class__.__name__}({self.i2c}, i2c_addr={hex(self.i2c_addr)})"

	def set_LED_color(self, red, green, blue, number = None):
		"""
		set the color for the whole led strip or specify the specific led number (index begins at 1)

		:param red: red value 0-255
		:type int:
		:param green: green value 0-255
		:type int:
		:param blue: blue value 0-255
		:type int:
		:param number: if none set whole array to color values otherwise set led at index starting at 1 to color 

		"""
		if number:
			self._write_register_array(WRITE_SINGLE_LED_COLOR, [number, red, green, blue])
		else:
			self._write_register_array(WRITE_ALL_LED_COLOR, [red, green, blue])

	def set_LED_brightness(self, brightness, number = None):
		"""
		set the brightness for the whole led strip or specify the led number (index starting at 1) and set the brightness

		:param brightness: brightness value 0-255
		:type int:
		:param number: if none set whole array to brightness otherwise set led at index starting at 1 to brightness 
		"""

		if number:
			self._write_register_array(WRITE_SINGLE_LED_BRIGHTNESS, [number, brightness])
		else: 
			self._write_register_array(WRITE_ALL_LED_BRIGHTNESS, [brightness])

	def change_address(self, address):
		"""
		reassign i2c address to avoid conficts. 

		:param address: new i2c address to use
		:type address: int
		"""
		self._write_register_array(CHANGE_ADDRESS, [address])
		self.i2c_addr = address

	def change_length(self, length):
		"""
		reassign the number of leds 

		:param length: change the length of your array (requires soldering on additional LEDs)
		:type length: int
		"""

		self._write_register_array(CHANGE_LED_LENGTH, [length])
		self.length = length
	
	def _write_register_array(self, register, valueArray):
		buf = bytearray(1 + len(valueArray))
		buf[0] = register
		buf[1:] = valueArray
		with self.device as dev:
			dev.write(buf)
