# How the drone subsystems work

The flight controller (FC) is the small real-time computer that estimates aircraft attitude and commands the motors. The Raspberry Pi is a separate general-purpose computer intended for perception and higher-level information. They do not run the same firmware, and neither replaces the receiver or ESC.

## Control and power paths

```text
Pilot sticks
    |
RadioMaster T8L -- ExpressLRS radio link --> receiver
                                             |
                                       CRSF serial data
                                             |
                        IMUs + barometer --> FC2
                                             |
                                    four DShot300 signals
                                             |
Battery --> protected power distribution --> custom ESC --> four motors
                    |
                    +--> qualified regulator --> FC POWER1 and receiver
                    |
                    +--> separate qualified regulator --> Pi 5
                                                          | camera
                                                          | LiDAR
                                                          | AI HAT+
                                  planned MAVLink data <--> FC2
```

This is a logical diagram, not a pin-location or approved power-distribution drawing. The two regulated branches must not be assumed to be the same physical BEC or connected positive outputs. The exact received assembly needs identification.

## Terms the new team must know

| Term | Meaning in this project |
|---|---|
| FC2 | The later physical FC test article used in the working sessions, not the product name V2 |
| V2 | The flight-controller design publication; not a guarantee that every fabricated board is good |
| ArduPilot / ArduCopter | Autopilot software; ArduCopter 4.7.1 runs on FC2 |
| Mission Planner | Laptop ground station used to view telemetry, configure parameters and request tests |
| Parameter export | Saved settings, sensor IDs and calibration, not the firmware binary |
| Bootloader | Small program that enables application loading; separate from the Copter application |
| IMU | Accelerometer and gyro; measures acceleration and angular rate, not geographic position |
| Barometer | Pressure sensor used for height estimation, not a GPS or compass |
| GNSS / GPS | External geographic position source; none was installed in the reported final assembly |
| Magnetometer | Compass sensor; none fitted/connected in the recorded setup |
| ELRS | ExpressLRS radio protocol between transmitter and receiver |
| CRSF | Serial protocol between the receiver and FC, separate from the radio air link |
| UART | TX/RX serial interface; TX of one device normally connects to RX of the other |
| DShot300 | Digital motor-command signalling from FC to ESC; not servo pulse-width calibration |
| ESC | Electronic speed controller driving three-phase brushless motors |
| BEC | Voltage regulator; a 5 A rating is available capacity, not constant delivered current |
| MAVLink | Telemetry/control message protocol between FC, ground station and planned Pi link |
| GND | Electrical return/reference; not a power supply by itself |
| BCM GPIO | Raspberry Pi signal numbering, different from physical header positions |

## Arming is not throttle

An arm request asks the FC to permit motor operation after checks. With the aircraft armed, motors can rotate at idle while throttle is still low. Throttle then requests collective motor demand; roll, pitch and yaw request aircraft motion that the FC mixes across motors. Do not map each joystick directly to a motor.

In the final profile, **RC6 does nothing**, and arming/disarming uses the throttle/yaw stick gesture. The earlier shoulder-button configuration was superseded because the control was momentary. Read [controls](07-controls-and-calibration.md) before attempting any request.

## What manual mode does not provide

Stabilize is attitude stabilization with pilot throttle control. It is not GPS position hold, automatic altitude hold or return-home. Camera object detection and a range sensor alone do not provide a qualified localization/navigation solution. Motor rotation on a bench does not show that the control axes, thrust, tuning or failsafes are correct for flight.

The FC must continue to stabilize and handle pilot safety if the Pi crashes, loses power or stops sending data. Initial companion commissioning is telemetry-only, not autonomous command authority.
