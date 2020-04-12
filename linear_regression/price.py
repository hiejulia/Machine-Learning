# price
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
def cost(theta_0, theta_1, xs, ys):
    distance = 0
    for x,y in zip(xs, ys):
        predicted_value = theta_0 + theta_1 * x
        distance = distance + abs(y - predicted_value)
    return distance/len(xs)
areas = [1000, 2000, 4000]
prices = [200000, 250000, 300000]
theta_0 = 0
testno = 200
costs = [cost(theta_0, theta_1, areas, prices) for theta_1 in np.arange(testno)]
plt.plot(np.arange(testno), costs)



# Numpy
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
xi = np.array([1000, 2000, 4000])
y = [200000, 250000, 300000]
A = np.array([ xi, np.ones(len(xi))])
w = np.linalg.lstsq(A.T,y)[0]
line = w[0]*xi+w[1] # regression line
print("Numpy solution: %s" % w)
plt.plot(xi, line, 'b-', xi, y, 'o')


#SciPy
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
xi = np.array([1000, 2000, 4000])
y = [200000, 250000, 300000]
A = np.array([ xi, np.ones(len(xi))])
slope, intercept, r_value, p_value, std_err = stats.linregress(xi,y)
line = slope*xi+intercept
print(slope, intercept)
plt.plot(xi,line,'b-',xi,y,'x')

# scikit-learn
from sklearn import linear_model
regr = linear_model.LinearRegression()
xi = np.array([1000, 2000, 4000])
y = [200000, 250000, 300000]
regr.fit(xi.reshape(-1, 1), y)
print(regr.coef_, regr.intercept_) # [ 32.14285714] 175000.0


# price of house
from sklearn import linear_model
regr = linear_model.LinearRegression()
xi = np.array([1000, 2000, 4000])
y = [200000, 250000, 300000]
regr.fit(xi.reshape(-1, 1), y)
print(regr.coef_, regr.intercept_)  # [ 32.14285714] 175000.0
print(regr.predict(3000))  # 271428.57142857


## example 
# Linear regression
