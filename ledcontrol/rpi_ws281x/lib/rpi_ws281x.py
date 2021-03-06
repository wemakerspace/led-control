# This file was automatically generated by SWIG (http://www.swig.org).
# Version 3.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info >= (2, 7, 0):
    def swig_import_helper():
        import importlib
        pkg = __name__.rpartition('.')[0]
        mname = '.'.join((pkg, '_rpi_ws281x')).lstrip('.')
        try:
            return importlib.import_module(mname)
        except ImportError:
            return importlib.import_module('_rpi_ws281x')
    _rpi_ws281x = swig_import_helper()
    del swig_import_helper
elif _swig_python_version_info >= (2, 6, 0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_rpi_ws281x', [dirname(__file__)])
        except ImportError:
            import _rpi_ws281x
            return _rpi_ws281x
        try:
            _mod = imp.load_module('_rpi_ws281x', fp, pathname, description)
        finally:
            if fp is not None:
                fp.close()
        return _mod
    _rpi_ws281x = swig_import_helper()
    del swig_import_helper
else:
    import _rpi_ws281x
del _swig_python_version_info

try:
    _swig_property = property
except NameError:
    pass  # Python < 2.2 doesn't have 'property'.

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_setattr_nondynamic(self, class_type, name, value, static=1):
    if (name == "thisown"):
        return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name, None)
    if method:
        return method(self, value)
    if (not static):
        if _newclass:
            object.__setattr__(self, name, value)
        else:
            self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)


def _swig_setattr(self, class_type, name, value):
    return _swig_setattr_nondynamic(self, class_type, name, value, 0)


def _swig_getattr(self, class_type, name):
    if (name == "thisown"):
        return self.this.own()
    method = class_type.__swig_getmethods__.get(name, None)
    if method:
        return method(self)
    raise AttributeError("'%s' object has no attribute '%s'" % (class_type.__name__, name))


def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except __builtin__.Exception:
    class _object:
        pass
    _newclass = 0

WS2811_TARGET_FREQ = _rpi_ws281x.WS2811_TARGET_FREQ
SK6812_STRIP_RGBW = _rpi_ws281x.SK6812_STRIP_RGBW
SK6812_STRIP_RBGW = _rpi_ws281x.SK6812_STRIP_RBGW
SK6812_STRIP_GRBW = _rpi_ws281x.SK6812_STRIP_GRBW
SK6812_STRIP_GBRW = _rpi_ws281x.SK6812_STRIP_GBRW
SK6812_STRIP_BRGW = _rpi_ws281x.SK6812_STRIP_BRGW
SK6812_STRIP_BGRW = _rpi_ws281x.SK6812_STRIP_BGRW
SK6812_SHIFT_WMASK = _rpi_ws281x.SK6812_SHIFT_WMASK
WS2811_STRIP_RGB = _rpi_ws281x.WS2811_STRIP_RGB
WS2811_STRIP_RBG = _rpi_ws281x.WS2811_STRIP_RBG
WS2811_STRIP_GRB = _rpi_ws281x.WS2811_STRIP_GRB
WS2811_STRIP_GBR = _rpi_ws281x.WS2811_STRIP_GBR
WS2811_STRIP_BRG = _rpi_ws281x.WS2811_STRIP_BRG
WS2811_STRIP_BGR = _rpi_ws281x.WS2811_STRIP_BGR
WS2812_STRIP = _rpi_ws281x.WS2812_STRIP
SK6812_STRIP = _rpi_ws281x.SK6812_STRIP
SK6812W_STRIP = _rpi_ws281x.SK6812W_STRIP
class ws2811_channel_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ws2811_channel_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ws2811_channel_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["gpionum"] = _rpi_ws281x.ws2811_channel_t_gpionum_set
    __swig_getmethods__["gpionum"] = _rpi_ws281x.ws2811_channel_t_gpionum_get
    if _newclass:
        gpionum = _swig_property(_rpi_ws281x.ws2811_channel_t_gpionum_get, _rpi_ws281x.ws2811_channel_t_gpionum_set)
    __swig_setmethods__["invert"] = _rpi_ws281x.ws2811_channel_t_invert_set
    __swig_getmethods__["invert"] = _rpi_ws281x.ws2811_channel_t_invert_get
    if _newclass:
        invert = _swig_property(_rpi_ws281x.ws2811_channel_t_invert_get, _rpi_ws281x.ws2811_channel_t_invert_set)
    __swig_setmethods__["count"] = _rpi_ws281x.ws2811_channel_t_count_set
    __swig_getmethods__["count"] = _rpi_ws281x.ws2811_channel_t_count_get
    if _newclass:
        count = _swig_property(_rpi_ws281x.ws2811_channel_t_count_get, _rpi_ws281x.ws2811_channel_t_count_set)
    __swig_setmethods__["strip_type"] = _rpi_ws281x.ws2811_channel_t_strip_type_set
    __swig_getmethods__["strip_type"] = _rpi_ws281x.ws2811_channel_t_strip_type_get
    if _newclass:
        strip_type = _swig_property(_rpi_ws281x.ws2811_channel_t_strip_type_get, _rpi_ws281x.ws2811_channel_t_strip_type_set)
    __swig_setmethods__["leds"] = _rpi_ws281x.ws2811_channel_t_leds_set
    __swig_getmethods__["leds"] = _rpi_ws281x.ws2811_channel_t_leds_get
    if _newclass:
        leds = _swig_property(_rpi_ws281x.ws2811_channel_t_leds_get, _rpi_ws281x.ws2811_channel_t_leds_set)
    __swig_setmethods__["brightness"] = _rpi_ws281x.ws2811_channel_t_brightness_set
    __swig_getmethods__["brightness"] = _rpi_ws281x.ws2811_channel_t_brightness_get
    if _newclass:
        brightness = _swig_property(_rpi_ws281x.ws2811_channel_t_brightness_get, _rpi_ws281x.ws2811_channel_t_brightness_set)
    __swig_setmethods__["wshift"] = _rpi_ws281x.ws2811_channel_t_wshift_set
    __swig_getmethods__["wshift"] = _rpi_ws281x.ws2811_channel_t_wshift_get
    if _newclass:
        wshift = _swig_property(_rpi_ws281x.ws2811_channel_t_wshift_get, _rpi_ws281x.ws2811_channel_t_wshift_set)
    __swig_setmethods__["rshift"] = _rpi_ws281x.ws2811_channel_t_rshift_set
    __swig_getmethods__["rshift"] = _rpi_ws281x.ws2811_channel_t_rshift_get
    if _newclass:
        rshift = _swig_property(_rpi_ws281x.ws2811_channel_t_rshift_get, _rpi_ws281x.ws2811_channel_t_rshift_set)
    __swig_setmethods__["gshift"] = _rpi_ws281x.ws2811_channel_t_gshift_set
    __swig_getmethods__["gshift"] = _rpi_ws281x.ws2811_channel_t_gshift_get
    if _newclass:
        gshift = _swig_property(_rpi_ws281x.ws2811_channel_t_gshift_get, _rpi_ws281x.ws2811_channel_t_gshift_set)
    __swig_setmethods__["bshift"] = _rpi_ws281x.ws2811_channel_t_bshift_set
    __swig_getmethods__["bshift"] = _rpi_ws281x.ws2811_channel_t_bshift_get
    if _newclass:
        bshift = _swig_property(_rpi_ws281x.ws2811_channel_t_bshift_get, _rpi_ws281x.ws2811_channel_t_bshift_set)
    __swig_setmethods__["gamma"] = _rpi_ws281x.ws2811_channel_t_gamma_set
    __swig_getmethods__["gamma"] = _rpi_ws281x.ws2811_channel_t_gamma_get
    if _newclass:
        gamma = _swig_property(_rpi_ws281x.ws2811_channel_t_gamma_get, _rpi_ws281x.ws2811_channel_t_gamma_set)

    def __init__(self):
        this = _rpi_ws281x.new_ws2811_channel_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_channel_t
    __del__ = lambda self: None
ws2811_channel_t_swigregister = _rpi_ws281x.ws2811_channel_t_swigregister
ws2811_channel_t_swigregister(ws2811_channel_t)

class ws2811_t(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ws2811_t, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ws2811_t, name)
    __repr__ = _swig_repr
    __swig_setmethods__["render_wait_time"] = _rpi_ws281x.ws2811_t_render_wait_time_set
    __swig_getmethods__["render_wait_time"] = _rpi_ws281x.ws2811_t_render_wait_time_get
    if _newclass:
        render_wait_time = _swig_property(_rpi_ws281x.ws2811_t_render_wait_time_get, _rpi_ws281x.ws2811_t_render_wait_time_set)
    __swig_setmethods__["device"] = _rpi_ws281x.ws2811_t_device_set
    __swig_getmethods__["device"] = _rpi_ws281x.ws2811_t_device_get
    if _newclass:
        device = _swig_property(_rpi_ws281x.ws2811_t_device_get, _rpi_ws281x.ws2811_t_device_set)
    __swig_setmethods__["rpi_hw"] = _rpi_ws281x.ws2811_t_rpi_hw_set
    __swig_getmethods__["rpi_hw"] = _rpi_ws281x.ws2811_t_rpi_hw_get
    if _newclass:
        rpi_hw = _swig_property(_rpi_ws281x.ws2811_t_rpi_hw_get, _rpi_ws281x.ws2811_t_rpi_hw_set)
    __swig_setmethods__["freq"] = _rpi_ws281x.ws2811_t_freq_set
    __swig_getmethods__["freq"] = _rpi_ws281x.ws2811_t_freq_get
    if _newclass:
        freq = _swig_property(_rpi_ws281x.ws2811_t_freq_get, _rpi_ws281x.ws2811_t_freq_set)
    __swig_setmethods__["dmanum"] = _rpi_ws281x.ws2811_t_dmanum_set
    __swig_getmethods__["dmanum"] = _rpi_ws281x.ws2811_t_dmanum_get
    if _newclass:
        dmanum = _swig_property(_rpi_ws281x.ws2811_t_dmanum_get, _rpi_ws281x.ws2811_t_dmanum_set)
    __swig_setmethods__["channel"] = _rpi_ws281x.ws2811_t_channel_set
    __swig_getmethods__["channel"] = _rpi_ws281x.ws2811_t_channel_get
    if _newclass:
        channel = _swig_property(_rpi_ws281x.ws2811_t_channel_get, _rpi_ws281x.ws2811_t_channel_set)

    def __init__(self):
        this = _rpi_ws281x.new_ws2811_t()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_ws2811_t
    __del__ = lambda self: None
ws2811_t_swigregister = _rpi_ws281x.ws2811_t_swigregister
ws2811_t_swigregister(ws2811_t)

WS2811_SUCCESS = _rpi_ws281x.WS2811_SUCCESS
WS2811_ERROR_GENERIC = _rpi_ws281x.WS2811_ERROR_GENERIC
WS2811_ERROR_OUT_OF_MEMORY = _rpi_ws281x.WS2811_ERROR_OUT_OF_MEMORY
WS2811_ERROR_HW_NOT_SUPPORTED = _rpi_ws281x.WS2811_ERROR_HW_NOT_SUPPORTED
WS2811_ERROR_MEM_LOCK = _rpi_ws281x.WS2811_ERROR_MEM_LOCK
WS2811_ERROR_MMAP = _rpi_ws281x.WS2811_ERROR_MMAP
WS2811_ERROR_MAP_REGISTERS = _rpi_ws281x.WS2811_ERROR_MAP_REGISTERS
WS2811_ERROR_GPIO_INIT = _rpi_ws281x.WS2811_ERROR_GPIO_INIT
WS2811_ERROR_PWM_SETUP = _rpi_ws281x.WS2811_ERROR_PWM_SETUP
WS2811_ERROR_MAILBOX_DEVICE = _rpi_ws281x.WS2811_ERROR_MAILBOX_DEVICE
WS2811_ERROR_DMA = _rpi_ws281x.WS2811_ERROR_DMA
WS2811_ERROR_ILLEGAL_GPIO = _rpi_ws281x.WS2811_ERROR_ILLEGAL_GPIO
WS2811_ERROR_PCM_SETUP = _rpi_ws281x.WS2811_ERROR_PCM_SETUP
WS2811_ERROR_SPI_SETUP = _rpi_ws281x.WS2811_ERROR_SPI_SETUP
WS2811_ERROR_SPI_TRANSFER = _rpi_ws281x.WS2811_ERROR_SPI_TRANSFER
WS2811_RETURN_STATE_COUNT = _rpi_ws281x.WS2811_RETURN_STATE_COUNT

def ws2811_init(ws2811):
    return _rpi_ws281x.ws2811_init(ws2811)
ws2811_init = _rpi_ws281x.ws2811_init

def ws2811_fini(ws2811):
    return _rpi_ws281x.ws2811_fini(ws2811)
ws2811_fini = _rpi_ws281x.ws2811_fini

def ws2811_render(ws2811):
    return _rpi_ws281x.ws2811_render(ws2811)
ws2811_render = _rpi_ws281x.ws2811_render

def ws2811_wait(ws2811):
    return _rpi_ws281x.ws2811_wait(ws2811)
ws2811_wait = _rpi_ws281x.ws2811_wait

def ws2811_get_return_t_str(state):
    return _rpi_ws281x.ws2811_get_return_t_str(state)
ws2811_get_return_t_str = _rpi_ws281x.ws2811_get_return_t_str
class color_hsv(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, color_hsv, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, color_hsv, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hue"] = _rpi_ws281x.color_hsv_hue_set
    __swig_getmethods__["hue"] = _rpi_ws281x.color_hsv_hue_get
    if _newclass:
        hue = _swig_property(_rpi_ws281x.color_hsv_hue_get, _rpi_ws281x.color_hsv_hue_set)
    __swig_setmethods__["h"] = _rpi_ws281x.color_hsv_h_set
    __swig_getmethods__["h"] = _rpi_ws281x.color_hsv_h_get
    if _newclass:
        h = _swig_property(_rpi_ws281x.color_hsv_h_get, _rpi_ws281x.color_hsv_h_set)
    __swig_setmethods__["saturation"] = _rpi_ws281x.color_hsv_saturation_set
    __swig_getmethods__["saturation"] = _rpi_ws281x.color_hsv_saturation_get
    if _newclass:
        saturation = _swig_property(_rpi_ws281x.color_hsv_saturation_get, _rpi_ws281x.color_hsv_saturation_set)
    __swig_setmethods__["sat"] = _rpi_ws281x.color_hsv_sat_set
    __swig_getmethods__["sat"] = _rpi_ws281x.color_hsv_sat_get
    if _newclass:
        sat = _swig_property(_rpi_ws281x.color_hsv_sat_get, _rpi_ws281x.color_hsv_sat_set)
    __swig_setmethods__["s"] = _rpi_ws281x.color_hsv_s_set
    __swig_getmethods__["s"] = _rpi_ws281x.color_hsv_s_get
    if _newclass:
        s = _swig_property(_rpi_ws281x.color_hsv_s_get, _rpi_ws281x.color_hsv_s_set)
    __swig_setmethods__["value"] = _rpi_ws281x.color_hsv_value_set
    __swig_getmethods__["value"] = _rpi_ws281x.color_hsv_value_get
    if _newclass:
        value = _swig_property(_rpi_ws281x.color_hsv_value_get, _rpi_ws281x.color_hsv_value_set)
    __swig_setmethods__["val"] = _rpi_ws281x.color_hsv_val_set
    __swig_getmethods__["val"] = _rpi_ws281x.color_hsv_val_get
    if _newclass:
        val = _swig_property(_rpi_ws281x.color_hsv_val_get, _rpi_ws281x.color_hsv_val_set)
    __swig_setmethods__["v"] = _rpi_ws281x.color_hsv_v_set
    __swig_getmethods__["v"] = _rpi_ws281x.color_hsv_v_get
    if _newclass:
        v = _swig_property(_rpi_ws281x.color_hsv_v_get, _rpi_ws281x.color_hsv_v_set)
    __swig_setmethods__["raw"] = _rpi_ws281x.color_hsv_raw_set
    __swig_getmethods__["raw"] = _rpi_ws281x.color_hsv_raw_get
    if _newclass:
        raw = _swig_property(_rpi_ws281x.color_hsv_raw_get, _rpi_ws281x.color_hsv_raw_set)

    def __init__(self):
        this = _rpi_ws281x.new_color_hsv()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_color_hsv
    __del__ = lambda self: None
color_hsv_swigregister = _rpi_ws281x.color_hsv_swigregister
color_hsv_swigregister(color_hsv)

class color_hsv_float(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, color_hsv_float, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, color_hsv_float, name)
    __repr__ = _swig_repr
    __swig_setmethods__["hue"] = _rpi_ws281x.color_hsv_float_hue_set
    __swig_getmethods__["hue"] = _rpi_ws281x.color_hsv_float_hue_get
    if _newclass:
        hue = _swig_property(_rpi_ws281x.color_hsv_float_hue_get, _rpi_ws281x.color_hsv_float_hue_set)
    __swig_setmethods__["h"] = _rpi_ws281x.color_hsv_float_h_set
    __swig_getmethods__["h"] = _rpi_ws281x.color_hsv_float_h_get
    if _newclass:
        h = _swig_property(_rpi_ws281x.color_hsv_float_h_get, _rpi_ws281x.color_hsv_float_h_set)
    __swig_setmethods__["saturation"] = _rpi_ws281x.color_hsv_float_saturation_set
    __swig_getmethods__["saturation"] = _rpi_ws281x.color_hsv_float_saturation_get
    if _newclass:
        saturation = _swig_property(_rpi_ws281x.color_hsv_float_saturation_get, _rpi_ws281x.color_hsv_float_saturation_set)
    __swig_setmethods__["sat"] = _rpi_ws281x.color_hsv_float_sat_set
    __swig_getmethods__["sat"] = _rpi_ws281x.color_hsv_float_sat_get
    if _newclass:
        sat = _swig_property(_rpi_ws281x.color_hsv_float_sat_get, _rpi_ws281x.color_hsv_float_sat_set)
    __swig_setmethods__["s"] = _rpi_ws281x.color_hsv_float_s_set
    __swig_getmethods__["s"] = _rpi_ws281x.color_hsv_float_s_get
    if _newclass:
        s = _swig_property(_rpi_ws281x.color_hsv_float_s_get, _rpi_ws281x.color_hsv_float_s_set)
    __swig_setmethods__["value"] = _rpi_ws281x.color_hsv_float_value_set
    __swig_getmethods__["value"] = _rpi_ws281x.color_hsv_float_value_get
    if _newclass:
        value = _swig_property(_rpi_ws281x.color_hsv_float_value_get, _rpi_ws281x.color_hsv_float_value_set)
    __swig_setmethods__["val"] = _rpi_ws281x.color_hsv_float_val_set
    __swig_getmethods__["val"] = _rpi_ws281x.color_hsv_float_val_get
    if _newclass:
        val = _swig_property(_rpi_ws281x.color_hsv_float_val_get, _rpi_ws281x.color_hsv_float_val_set)
    __swig_setmethods__["v"] = _rpi_ws281x.color_hsv_float_v_set
    __swig_getmethods__["v"] = _rpi_ws281x.color_hsv_float_v_get
    if _newclass:
        v = _swig_property(_rpi_ws281x.color_hsv_float_v_get, _rpi_ws281x.color_hsv_float_v_set)
    __swig_setmethods__["raw"] = _rpi_ws281x.color_hsv_float_raw_set
    __swig_getmethods__["raw"] = _rpi_ws281x.color_hsv_float_raw_get
    if _newclass:
        raw = _swig_property(_rpi_ws281x.color_hsv_float_raw_get, _rpi_ws281x.color_hsv_float_raw_set)

    def __init__(self):
        this = _rpi_ws281x.new_color_hsv_float()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_color_hsv_float
    __del__ = lambda self: None
color_hsv_float_swigregister = _rpi_ws281x.color_hsv_float_swigregister
color_hsv_float_swigregister(color_hsv_float)

class color_rgb(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, color_rgb, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, color_rgb, name)
    __repr__ = _swig_repr
    __swig_setmethods__["red"] = _rpi_ws281x.color_rgb_red_set
    __swig_getmethods__["red"] = _rpi_ws281x.color_rgb_red_get
    if _newclass:
        red = _swig_property(_rpi_ws281x.color_rgb_red_get, _rpi_ws281x.color_rgb_red_set)
    __swig_setmethods__["r"] = _rpi_ws281x.color_rgb_r_set
    __swig_getmethods__["r"] = _rpi_ws281x.color_rgb_r_get
    if _newclass:
        r = _swig_property(_rpi_ws281x.color_rgb_r_get, _rpi_ws281x.color_rgb_r_set)
    __swig_setmethods__["green"] = _rpi_ws281x.color_rgb_green_set
    __swig_getmethods__["green"] = _rpi_ws281x.color_rgb_green_get
    if _newclass:
        green = _swig_property(_rpi_ws281x.color_rgb_green_get, _rpi_ws281x.color_rgb_green_set)
    __swig_setmethods__["g"] = _rpi_ws281x.color_rgb_g_set
    __swig_getmethods__["g"] = _rpi_ws281x.color_rgb_g_get
    if _newclass:
        g = _swig_property(_rpi_ws281x.color_rgb_g_get, _rpi_ws281x.color_rgb_g_set)
    __swig_setmethods__["blue"] = _rpi_ws281x.color_rgb_blue_set
    __swig_getmethods__["blue"] = _rpi_ws281x.color_rgb_blue_get
    if _newclass:
        blue = _swig_property(_rpi_ws281x.color_rgb_blue_get, _rpi_ws281x.color_rgb_blue_set)
    __swig_setmethods__["b"] = _rpi_ws281x.color_rgb_b_set
    __swig_getmethods__["b"] = _rpi_ws281x.color_rgb_b_get
    if _newclass:
        b = _swig_property(_rpi_ws281x.color_rgb_b_get, _rpi_ws281x.color_rgb_b_set)
    __swig_setmethods__["raw"] = _rpi_ws281x.color_rgb_raw_set
    __swig_getmethods__["raw"] = _rpi_ws281x.color_rgb_raw_get
    if _newclass:
        raw = _swig_property(_rpi_ws281x.color_rgb_raw_get, _rpi_ws281x.color_rgb_raw_set)

    def __init__(self):
        this = _rpi_ws281x.new_color_rgb()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_color_rgb
    __del__ = lambda self: None
color_rgb_swigregister = _rpi_ws281x.color_rgb_swigregister
color_rgb_swigregister(color_rgb)

class color_rgb_float(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, color_rgb_float, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, color_rgb_float, name)
    __repr__ = _swig_repr
    __swig_setmethods__["red"] = _rpi_ws281x.color_rgb_float_red_set
    __swig_getmethods__["red"] = _rpi_ws281x.color_rgb_float_red_get
    if _newclass:
        red = _swig_property(_rpi_ws281x.color_rgb_float_red_get, _rpi_ws281x.color_rgb_float_red_set)
    __swig_setmethods__["r"] = _rpi_ws281x.color_rgb_float_r_set
    __swig_getmethods__["r"] = _rpi_ws281x.color_rgb_float_r_get
    if _newclass:
        r = _swig_property(_rpi_ws281x.color_rgb_float_r_get, _rpi_ws281x.color_rgb_float_r_set)
    __swig_setmethods__["green"] = _rpi_ws281x.color_rgb_float_green_set
    __swig_getmethods__["green"] = _rpi_ws281x.color_rgb_float_green_get
    if _newclass:
        green = _swig_property(_rpi_ws281x.color_rgb_float_green_get, _rpi_ws281x.color_rgb_float_green_set)
    __swig_setmethods__["g"] = _rpi_ws281x.color_rgb_float_g_set
    __swig_getmethods__["g"] = _rpi_ws281x.color_rgb_float_g_get
    if _newclass:
        g = _swig_property(_rpi_ws281x.color_rgb_float_g_get, _rpi_ws281x.color_rgb_float_g_set)
    __swig_setmethods__["blue"] = _rpi_ws281x.color_rgb_float_blue_set
    __swig_getmethods__["blue"] = _rpi_ws281x.color_rgb_float_blue_get
    if _newclass:
        blue = _swig_property(_rpi_ws281x.color_rgb_float_blue_get, _rpi_ws281x.color_rgb_float_blue_set)
    __swig_setmethods__["b"] = _rpi_ws281x.color_rgb_float_b_set
    __swig_getmethods__["b"] = _rpi_ws281x.color_rgb_float_b_get
    if _newclass:
        b = _swig_property(_rpi_ws281x.color_rgb_float_b_get, _rpi_ws281x.color_rgb_float_b_set)
    __swig_setmethods__["raw"] = _rpi_ws281x.color_rgb_float_raw_set
    __swig_getmethods__["raw"] = _rpi_ws281x.color_rgb_float_raw_get
    if _newclass:
        raw = _swig_property(_rpi_ws281x.color_rgb_float_raw_get, _rpi_ws281x.color_rgb_float_raw_set)

    def __init__(self):
        this = _rpi_ws281x.new_color_rgb_float()
        try:
            self.this.append(this)
        except __builtin__.Exception:
            self.this = this
    __swig_destroy__ = _rpi_ws281x.delete_color_rgb_float
    __del__ = lambda self: None
color_rgb_float_swigregister = _rpi_ws281x.color_rgb_float_swigregister
color_rgb_float_swigregister(color_rgb_float)


def ws2811_channel_get(ws, channelnum):
    return _rpi_ws281x.ws2811_channel_get(ws, channelnum)
ws2811_channel_get = _rpi_ws281x.ws2811_channel_get

def ws2811_led_get(channel, lednum):
    return _rpi_ws281x.ws2811_led_get(channel, lednum)
ws2811_led_get = _rpi_ws281x.ws2811_led_get

def ws2811_led_set(channel, lednum, color):
    return _rpi_ws281x.ws2811_led_set(channel, lednum, color)
ws2811_led_set = _rpi_ws281x.ws2811_led_set

def unpack_rgb(arg1):
    return _rpi_ws281x.unpack_rgb(arg1)
unpack_rgb = _rpi_ws281x.unpack_rgb

def pack_rgb(r, g, b):
    return _rpi_ws281x.pack_rgb(r, g, b)
pack_rgb = _rpi_ws281x.pack_rgb

def scale_8(a, b):
    return _rpi_ws281x.scale_8(a, b)
scale_8 = _rpi_ws281x.scale_8

def clamp(d, min, max):
    return _rpi_ws281x.clamp(d, min, max)
clamp = _rpi_ws281x.clamp

def blackbody_to_rgb(kelvin):
    return _rpi_ws281x.blackbody_to_rgb(kelvin)
blackbody_to_rgb = _rpi_ws281x.blackbody_to_rgb

def blackbody_correction_rgb(rgb, kelvin):
    return _rpi_ws281x.blackbody_correction_rgb(rgb, kelvin)
blackbody_correction_rgb = _rpi_ws281x.blackbody_correction_rgb

def render_hsv2rgb_rainbow_float(hsv, corr_rgb, saturation, brightness, gamma):
    return _rpi_ws281x.render_hsv2rgb_rainbow_float(hsv, corr_rgb, saturation, brightness, gamma)
render_hsv2rgb_rainbow_float = _rpi_ws281x.render_hsv2rgb_rainbow_float

def render_rgb_float(rgb, corr_rgb, saturation, brightness, gamma):
    return _rpi_ws281x.render_rgb_float(rgb, corr_rgb, saturation, brightness, gamma)
render_rgb_float = _rpi_ws281x.render_rgb_float

def ws2811_hsv_render_array_float(ws, channel, values, count, correction, saturation, brightness, gamma):
    return _rpi_ws281x.ws2811_hsv_render_array_float(ws, channel, values, count, correction, saturation, brightness, gamma)
ws2811_hsv_render_array_float = _rpi_ws281x.ws2811_hsv_render_array_float

def ws2811_rgb_render_array_float(ws, channel, values, count, correction, saturation, brightness, gamma):
    return _rpi_ws281x.ws2811_rgb_render_array_float(ws, channel, values, count, correction, saturation, brightness, gamma)
ws2811_rgb_render_array_float = _rpi_ws281x.ws2811_rgb_render_array_float

def wave_pulse(t, duty_cycle):
    return _rpi_ws281x.wave_pulse(t, duty_cycle)
wave_pulse = _rpi_ws281x.wave_pulse

def wave_triangle(t):
    return _rpi_ws281x.wave_triangle(t)
wave_triangle = _rpi_ws281x.wave_triangle

def wave_sine(t):
    return _rpi_ws281x.wave_sine(t)
wave_sine = _rpi_ws281x.wave_sine

def wave_cubic(t):
    return _rpi_ws281x.wave_cubic(t)
wave_cubic = _rpi_ws281x.wave_cubic

def plasma_sines(x, y, t, coeff_x, coeff_y, coeff_x_y, coeff_dist_xy):
    return _rpi_ws281x.plasma_sines(x, y, t, coeff_x, coeff_y, coeff_x_y, coeff_dist_xy)
plasma_sines = _rpi_ws281x.plasma_sines

def plasma_sines_octave(x, y, t, octaves, temporal_freq_persistence, amplitude_persistence):
    return _rpi_ws281x.plasma_sines_octave(x, y, t, octaves, temporal_freq_persistence, amplitude_persistence)
plasma_sines_octave = _rpi_ws281x.plasma_sines_octave

def fade(t):
    return _rpi_ws281x.fade(t)
fade = _rpi_ws281x.fade

def lerp(t, a, b):
    return _rpi_ws281x.lerp(t, a, b)
lerp = _rpi_ws281x.lerp

def grad(hash, x, y, z):
    return _rpi_ws281x.grad(hash, x, y, z)
grad = _rpi_ws281x.grad

def perlin_noise_3d(x, y, z):
    return _rpi_ws281x.perlin_noise_3d(x, y, z)
perlin_noise_3d = _rpi_ws281x.perlin_noise_3d
# This file is compatible with both classic and new-style classes.

cvar = _rpi_ws281x.cvar

