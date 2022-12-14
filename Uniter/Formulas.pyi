from typing import overload
from Uniter.Uniter import Unit
from Uniter.Units import *

@overload
def average_speed(distance: None = ..., speed: Speed = ..., time: Time = ...) -> Length: ...

@overload
def average_speed(distance: Length = ..., speed: None = ..., time: Time = ...) -> Speed: ...

@overload
def average_speed(distance: Length = ..., speed: Speed = ..., time: None = ...) -> Time: ...

def average_speed(distance: Length | None = ..., speed: Speed | None = ..., time: Time | None = ...) -> Unit: ...

@overload
def cylinder_surface(radius: None = ..., height: Length = ..., surface: Area = ...) -> Length: ...

@overload
def cylinder_surface(radius: Length = ..., height: None = ..., surface: Area = ...) -> Length: ...

@overload
def cylinder_surface(radius: Length = ..., height: Length = ..., surface: None = ...) -> Area: ...

def cylinder_surface(radius: Length | None = ..., height: Length | None = ..., surface: Area | None = ...) -> Unit: ...

@overload
def cylinder_volume(radius: None = ..., height: Length = ..., volume: Volume = ...) -> Length: ...

@overload
def cylinder_volume(radius: Length = ..., height: None = ..., volume: Volume = ...) -> Length: ...

@overload
def cylinder_volume(radius: Length = ..., height: Length = ..., volume: None = ...) -> Volume: ...

def cylinder_volume(radius: Length | None = ..., height: Length | None = ..., volume: Volume | None = ...) -> Unit: ...

@overload
def ohms_law(electric_current: None = ..., voltage: Voltage = ..., resistance: Resistance = ...) -> Electric_Current: ...

@overload
def ohms_law(electric_current: Electric_Current = ..., voltage: None = ..., resistance: Resistance = ...) -> Voltage: ...

@overload
def ohms_law(electric_current: Electric_Current = ..., voltage: Voltage = ..., resistance: None = ...) -> Resistance: ...

def ohms_law(electric_current: Electric_Current | None = ..., voltage: Voltage | None = ..., resistance: Resistance | None = ...) -> Unit: ...

@overload
def sphere_volume(radius: None = ..., volume: Volume = ...) -> Length: ...

@overload
def sphere_volume(radius: Length = ..., volume: None = ...) -> Volume: ...

def sphere_volume(radius: Length | None = ..., volume: Volume | None = ...) -> Unit: ...

