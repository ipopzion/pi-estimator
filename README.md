# pi-estimator
Simple demonstration of the usage of Monte Carlo Method  
_idea from https://en.wikipedia.org/wiki/Monte_Carlo_method_

# mathematical concept
Pi can be calculated through the ratio of the quadrant flushed within a square. 
Mathematically, area of quadrant = 0.25*pi*r^2, while the area of the square = r^2. 
Hence, pi = 4 * (area of quadrant) / (area of the square) 

However, the default way to calculate the area of a quadrant comes from the value of pi. To calculate the value of pi then, we will have to use a different method to calculate the area of the quadrant. 

One such method is the random generation of points on a cartesian plane. 
Through the generation of random numbers ranged 0 to 1, we can generate points with x and y coordinates distributed between 0 and 1.
Since the point has equal probability to land anywhere within a 1 by 1 box, the number of dots landing within a specific area should correspond to the size of the area. 
Given a large enough sample, the ratio of the dots within and without the quadrant will sufficiently estimate the ratio between the two areas, thereby allowing us to estimate the value of pi. 
