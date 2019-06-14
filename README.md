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

	- Draw out 9 lines from the car: 2 horizontal, 1 vertical, 2 diagonal
	- Measure the distance to the nearest obstacle
	- Features to be used:
		1. Left Horizontal line
		2. Right Horizontal line
		3. Vertical line
		4. Left diagonal line
		5. Right diagonal line
		6. Left 67.25 line
		7. Right 67.25 line
		8. Left 22.25 line
		9. Right 22.25 line
		10. Speed
		11. Direction
	- When ready to start collecting data(ie. car is in the right position), press 'c' to enable data collection
	- Use 'c' to toggle the collection of data
	- Once you are done collecting data for the session, close the pygame session, and the new data collected will be appended automatically	

4. **Models**

	- The model currently chosen can be activated/deactivated using the 'a' key
	- Hybrid models are models that combine the values found in different models to produce a better model
	- Currently, linear regression using 5, 7 and 11 features has been tested out.
	- The best performing model is the **11 features hybrid2** model.

5. **Reinforcement Learning**

	- Initialize **m** cars with random weights
	- Set up a reward system that gives each car's performance reward points based on:
		1. **Distance/amount of the track** it covers(not sure how to implement this without manual intervention) (d)
		2. **Time** taken to do so(?)(t)
	- Based on the above, a rough formula could be (d/t)
	- Select the best **n** cars, ie. the ones with the most points
	- Use these n cars weights to create mn cars having slight variants of the weights(changing the weights randomly up to a maximum of ẟ of the parent car
	- Hopefully, this will lead to a car that can manuever around all the circuits
	- Drawback: The entire process seems pretty random, especially the learning out of a parent car, there is essentially nothing the new car 'learns' from it's parent car, ie. the new car just changes the parent car by a bit **hoping** that it becomes better


## Plan

- (**Done**) Deploy a method to get the necessary parameters for training
- (**Done**) Collect data by driving the car yourself, and record what you do
- (***In Progress***) Train a model using the data you have, and then test
	1. (**Done**) Linear Regression
	2. Logistic Regression
	3. (**Done**) Neural Network(TensorFlow)

## Issues

- (**Fixed**) Gradient for car's general movement is too steep
- (**Fixed**) Car turning animation isn't smooth possibly because car is positioned using top left corner of the car image 	
