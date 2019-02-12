# fourier triangle

This is a project by Craig Best and Tristan Trim. Our objective is to learn about, and show off how the fourier series works. To that end, we have developed some code to generate graphical representations of a the fourier series for generating a triagle wave. But first some theory.

A fourier series is made up of the sum of sine and cosine waves. A different series of waves summed together will give you any arbitrary waveform. In our example, we are generating a triangle wave. This is done with the following series:

INSERT MATH HERE?!?

To visualize how this works, we wrote three programs making use of the python programming language and the packages numpy, matplotlib, and scipy. The first program, 'triangle.py' computes and plots the fourier series for a triangle wave, iteratively adding more terms. The second program, 'animated-triangle.py' was a combination of the original program, and an example matplotlib program. Finally the program 'waveform.py' goes deeper into the math, calculating the fourier coefficients, and graphing the function, as in 'triangle.py'.

Throughout the programs you can get a sense of how the iterative process of adding terms of the forier series converges towards the given function, which in this case, is a triangle wave.


