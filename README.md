# Cal-Packs
Our Cal Hacks 6.0 Project
# Inspiration
After getting a nice big Costco sized bag of Dinosaur Chicken Nuggets, a hungry group of Berkeley students wanted to bake them. Unfortunately, they were constraint by the size of the baking tray, and really wished they had a way to optimize the max number of Dino-nuggets that can fit on the tray. Thus, Dino Pack was born, a way to tackle the classic packing problem in 2-d and ensure that the maximum number of nuggets are put onto our limited tray space.

# What it does
Dino-Pack is built from the ground up completely. The first portion fo the program serves to turn ASCII image files into an output display, as well as into a matrix representation for manipulation through our packing algorithm. The second portion involves of two packing algorithms, BOGO pack and rectangular pack, that serve to find the ideal configuration for packing.

What you can do is input a variety of different shapes you want to pack, and the constraint of the space you want to pack it onto. An ASCII representation of the shape can be used and using either BOGO pack or rectangular pack, the program will output an image showcasing an efficient pack. You can also compare the algorithms with information on how many objects you fit, and the amount of free space that was filled up.

# How we built it
The program is completely built from very basic Python libraries, with linear algebra knowledge. We represented the images as matrixes, which we can apply various linear transformations to, and write functions to put find the optimal pack.

The imaging portion of the project was built using PIL (python imaging library), which allowed us to take our very abstract representations of the shapes and output an actual display image.

# Challenges we ran into
Everything from the this project was built up from very bare bones elements, meaning we had to conceptualize and execute everything ourselves. We had to learn and understand the math behind the algorithms we had to apply, as well as run through the issues of implementing them through code. In addition, We tried packing in very complex (dinosaur) shapes, that required a lot of tweeking and working to make sure that our algorithm will pack them correctly.

# Accomplishments that we're proud of
Coming in with a relatively silly idea, but actually creating a solution to it. Of course, there is a lot that can be improved on in terms of the interface, algorithm, and coding. Creating Dino Pack out of nothing was a very rewarding experience, and really tested our understanding of fundamental programming skills.

# What we learned
We learned about the many issues and challenges that go into creating your own algorithm, which is in and of itself mathematically involved. In addition, trying to implement those faced many coding challenges, and involved ensuring abstraction throughout the project so that all parts can work together.

# What's next for Dino Pack
The problem that Dino Pack seeks to solve is not just for chicken nuggets. Packing problems can be used to find the ideal configuration of designs on a sheet to conserve material while laser cutting or vinyl cutting. It can also be used to find the optimal ways to store various items. Going forward, Dino Pack can see it's interface improved, going from simply displaying simple black and white images to a full fledged GUI, with inputs for desired shape, size, and dimensions. In addition, our algorithms can be improved as well, to take into account more cases and complex shapes.
