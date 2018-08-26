# CarND-PID-Control-Project

Self-Driving Car Engineer Nanodegree Program

---


## PID Controller


The controller adjusts the speed and steering of a car so it can drive around the track. This adjustement is done by computing the cross-track error (CTE) and analyzing three components that depend on CTE, namely:

* Proportional component 
* Integral component (to combat systematic bias)
* Differential component (to proevent zig-zagging)

See `writeup-report` for more details.


## Dependencies

* cmake >= 3.5
* All other dependencies can be installed by running:
	* install-ubuntu.sh
    

## Basic Build Instructions

1. Clone this repo.
2. Make a build directory: `mkdir build && cd build`
3. Compile: `cmake .. && make`
4. Run it: `./pid`

**NOTE:** The PID system is designed to be run against the [Udacity simulator](https://github.com/udacity/self-driving-car-sim/releases). Run PID with the simulator already running.


## Examples

Two video examples are included in `videos` folder. The folder contains a `README` file with more information.