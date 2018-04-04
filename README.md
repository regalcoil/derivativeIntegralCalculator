# derivativeIntegralCalculator
Python, Single-Variable Calculus

Open the command-line terminal of your preference.

While in the correct directory (derivativeIntegralCalculator), enter the command `python3 derivInteg.py` to start the calculator.

The system will begin by asking you for the exponent on the leading element of the equation. If you accidentally enter an exponent that is too large, the application is programmed to account for this error. Simply enter `0` when it asks for the coefficient on any element with an exponent larger than the leading element. However, this does NOT work the other way around. If the entry is too small, you will have to restart the program for user entry. The best way to get around this issue is to make sure every input is correct.

After the equation is created, the command-line will print out the equation in this format:

ƒ(x) = ax^n + ... + bx^2 + cx + intercept

Next, you will be prompted as to whether or not you would like to calculate the derivative or the integral of the equation; either one will require input as to whether you would like to calculate the derivative/integral in numerical (definite) or variable (indefinite) terms. Numerical answers will also display the variable answer.

For numerical derivatives, simply enter a value for x. The answer is reported as either an INT or FLOAT without unit specification.
Derivative answers include both the first and second derivative: ƒ'(x) = dx f''(x) = ddx.

For numerical integrals, enter a lower range and upper range for x. The answer is reported as either an INT or FLOAT in terms of units^2.
Variable integrals are reported as ∫ƒ(x) = ax^n + ... + bx^2 + mx + interceptProxy WHERE interceptProxy always equals 'c'.

After the calculation is reported, if you would like to switch between derivative and integral enter `switch`; if you would like to reenter an equation from scratch enter `restart`.

Thank you for using this application. Message me at christopherbiemer@gmail.com with any questions or recommendations for updates in functionality.