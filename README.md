# CarAI

## Metadata

 1. Circuit

	- To enable detection of the obstacles(anything that is not the road), we allow for only the road to be of black color. Everything else(except the car) shall be treated as an obstacle. Using this, we can create the contour for the road which will be very useful

 2. Car
	
	- Maximum steering angle of the car is 60 degrees
	- Direction of car will use normal cartesian system(angles measured from positive X-axis)
	- Only the steering angle will be relative to the direction the car is moving in( Positive steering angle means car is turning to the right, and negative means car is turning to the left )
	- Maximum acceleration of the car is 4(dont know units, pixels/s^2?)
	- Assume car decelerates at 1 pps(pixels per second) when no acceleration is applied
