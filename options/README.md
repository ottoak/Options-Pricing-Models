## Options Models
This folder contains the files that define the classes to build the simulations. Bionmial_Models contain simple implementations of American and European put and call pricing models, with the following inputs:

S0: Initial stock price

K: Strike Price

N: Number of periods

R: Interest rate

u: Proportion the stock will move up at any given node in the binomial model (proportion it will move down is 1/u
Type: call or put

BS_Binomial_Models contains variants that use parameters from the black scholes equation (and allows for dividends):

T: Time period

N: number of sub periods of [0,T] we will simulate over

s: standard deviation of the stock (volatility)

r: continous interest rate

c: dividend yield

Otherwise, both work the same. fill_praces creates the stock price lattice, and fill_values works backwards from the end to compute the fair value of the option at each node. The value at the first node is the option prive given the current stock price S0 and strike price K.
