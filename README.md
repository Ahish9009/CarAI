# CarAI

## Metadata

 1. **Circuit**

	- To enable detection of the obstacles(anything that is not the road), we allow for only the road to be of black color. Everything else(except the car) shall be treated as an obstacle. Using this, we can create the contour for the road which will be very useful

 2. **Car**
	
	- Accelerator pedal and break(negative accelerator) is controlled using the up and down keys, while steering wheel is controlled using L/R arrow keys 
	- Maximum steering angle of the car is 60 degrees
	- Direction of car will use normal cartesian system(angles measured from positive X-axis)
	- Only the steering angle will be relative to the direction the car is moving in( Positive steering angle means car is turning to the right, and negative means car is turning to the left )
	- Maximum acceleration of the car is 4(dont know units, pixels/s^2?)
	- Assume car decelerates at 1 pps(pixels/s^2) when no acceleration is applied

3. **Data Collection**

	- Draw out 5 lines from the car: 2 horizontal, 1 vertical, 2 diagonal
	- Measure the distance to the nearest obstacle
	- Features to be used:
		1. Left Horizontal line
		2. Right Horizontal line
		3. Vertical line
		4. Left diagonal line
		5. Right diagonal line
		6. Speed
		7. Direction(?)
	- When ready to start collecting data(ie. car is in the right position), press c to enable data collection
	- Use 'c' to toggle the collection of data
	- Once you are done collecting data for the session, close the pygame session, and the new data collected will be appended automatically	

## Plan

- (**Done**) Deploy a method to get the necessary parameters for training
- (***In Progress***) Collect data by driving the car yourself, and record what you do
- Train a model using the data you have, and then test

## Issues

- (**Fixed**) Gradient for car's general movement is too steep
- (**Fixed**) Car turning animation isn't smooth possibly because car is positioned using top left corner of the car image 	
