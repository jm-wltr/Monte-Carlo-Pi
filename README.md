# Monte-Carlo-Pi
Approximate pi with Monte Carlo algorithm and generate graphs.

The way this works is by randomly generating a lot of 2D points from (-1,-1) to (1,1) (the total area of the surface where the points can land is then 4) and
checking if they fall inside the unit circle. Since the unit circle radius is 1, its area is pi. Therefore, the probability that a points lands inside the circle
is pi/4. Knowing the number of random points that indeed landed inside the circle, dividing it by the number of points we generated, and multiplying the result 
by 4 gives us an approximation of the value of pi.

"monte_carlo_graph.py", calculates pi and generates a graph showing how each the number of generated points relates to the accuracy of our approximation. We will
see that as the number of samples increases, the results from all of our calculations slowly converge to pi. You can change the number of times we perform the
calculation to show in the graph by changing the value of the variable "reps" (at the beginning of the code). You can also change the maximum number of samples
for each repetition by changing the value of the variable "samples", which is expressesed as the log10 of the desired number. It uses a logaritmic scale for this
in order to plot less points while maintaining the graph more or less the same. However, in the final graph, both axis are in linear scale. Finally, the code also
prints the final approximation of pi in the console. It is the mean of the results of all the calculations.

"monte_carlo.py" uses a slightly simpler version of the algorithm used in "monte_carlo_graph.py" because it doesn't generate graphs. Instead, it just runs 
indefinitely calculating pi over and over and adding its result to the text file "pi.txt", so that we don't lose the progress of calculating pi with larger
and larger samples of randomly generated points. It also shows a progress bar for each calculation, in order to see how it is going.

Finally, the repository also has a folder (named "images") with images of graphs I have generated using "monte_carlo_graph.py".
