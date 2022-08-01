
import math
from matplotlib import pyplot
from Generaldistribution import Distribution

class Binomial(Distribution):
    """ Binomial distribution class for calculating and 
    visualizing a Binomial distribution.
    
    Attributes:
        mean (float) representing the mean value of the distribution
        stdev (float) representing the standard deviation of the distribution
        data_list (list of floats) a list of floats to be extracted from the data file
        p (float) representing the probability of an event occurring
                
    """
  
    def __init__(self, positive_probability = 0.5, trials = 10): 
        self.p = positive_probability
        self.n = trials
        Distribution.__init__(self, self.calculate_mean(), self.calculate_stdev())
    
    def calculate_mean(self):
        """Function to calculate the mean from p and n
        
        Args: 
            None
        
        Returns: 
            float: mean of the data set
    
        """
        return self.n * self.p 

    def calculate_stdev(self):
        """Function to calculate the standard deviation from p and n.
        
        Args: 
            None
        
        Returns: 
            float: standard deviation of the data set
    
        """
        return math.sqrt(self.n * self.p * (1 - self.p))

    def replace_stats_with_data(self):
        """Function to calculate p and n from the data set. The function updates the p and n variables of the object.
        
        Args: 
            None
        
        Returns: 
            float: the p value
            float: the n value
    
        """
        self. n = len(self.data)
        self.p = 1.0 * sum(self.data)/self.n
        self.mean = self.calculate_mean()
        self.stdev = self.calculate_stdev()
        return self.p, self.n
    
    def plot_bar(self):
        """Function to output a histogram of the instance variable data using 
        matplotlib pyplot library.
        
        Args:
            None
            
        Returns:
            None
        """
        x = [0, 1]
        positive_count = sum(self.data)
        negative_count = len(self.data) - positive_count
        y = [negative_count, positive_count]
        pyplot.bar(x, y)
        pyplot.title('histogram of data')
        pyplot.xlabel('outcome')
        pyplot.ylabel('count')
    
    def pdf(self, k):
        """Probability density function calculator for the binomial distribution.
        
        Args:
            k (float): point for calculating the probability density function
            
        
        Returns:
            float: probability density function output
        """
        binomial_coeff = math.factorial(self.n)/(math.factorial(k) * math.factorial(self.n - k))
        return  binomial_coeff * pow(self.p, k) * pow(1 - self.p, self.n - k)
        

    def plot_bar_pdf(self):
        """Function to plot the pdf of the binomial distribution
        
        Args:
            None
        
        Returns:
            list: x values for the pdf plot
            list: y values for the pdf plot
            
        """
        x = [i for i in range(self.n + 1)]
        y = [self.pdf(k) for k in x]
        pyplot.bar(x,y)

    def __add__(self, other):                    
        """Function to add together two Binomial distributions with equal p
        
        Args:
            other (Binomial): Binomial instance
            
        Returns:
            Binomial: Binomial distribution
            
        """
        
        try:
            assert self.p == other.p, 'p values are not equal'
        except AssertionError as error:
            raise
       
        return Binomial(other.p, self.n + other.n) 

    def __repr__(self):
        """Function to output the characteristics of the Binomial instance
        
        Args:
            None
        
        Returns:
            string: characteristics of the Binomial object
        
        """
        return 'mean %f, standard deviation %f, p %f, n %d' % (self.mean, self.stdev, self.p, self.n)
