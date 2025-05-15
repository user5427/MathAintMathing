import unittest
import math
import numpy as np
from scipy.stats import t, chi2
import sys
import os
from T12.math3 import Q, x

# Import the module using absolute import
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestMath3(unittest.TestCase):
    
    def test_mean_calculation(self):
        """Test that the mean is calculated correctly"""
        expected_mean = sum(x) / len(x)
        self.assertAlmostEqual(expected_mean, 17.8, places=1)
        
    def test_std_calculation(self):
        """Test that the standard deviation is calculated correctly"""
        mean = sum(x) / len(x)
        expected_std = math.sqrt(sum([(i - mean) ** 2 for i in x]) / (len(x) - 1))
        self.assertAlmostEqual(expected_std, 2.49, places=2)
        
    def test_confidence_interval_for_mean(self):
        """Test the confidence interval for mean"""
        mean = sum(x) / len(x)
        std_dev = math.sqrt(sum([(i - mean) ** 2 for i in x]) / (len(x) - 1))
        t_value = t.ppf(Q, len(x) - 1)
        
        expected_lower = mean - t_value * std_dev / math.sqrt(len(x))
        expected_upper = mean + t_value * std_dev / math.sqrt(len(x))
        
        self.assertAlmostEqual(expected_lower, 16.52, places=2)
        self.assertAlmostEqual(expected_upper, 19.08, places=2)
        
    def test_confidence_interval_for_variance(self):
        """Test the confidence interval for variance"""
        mean = sum(x) / len(x)
        std_dev = math.sqrt(sum([(i - mean) ** 2 for i in x]) / (len(x) - 1))
        variance = std_dev ** 2
        
        chi2_upper = chi2.ppf(Q, len(x) - 1)
        chi2_lower = chi2.ppf(1 - Q, len(x) - 1)
        
        expected_lower = (len(x) - 1) * variance / chi2_upper
        expected_upper = (len(x) - 1) * variance / chi2_lower
        
        self.assertAlmostEqual(expected_lower, 2.92, places=2)
        self.assertAlmostEqual(expected_upper, 11.71, places=2)
        
    def test_valid_confidence_level(self):
        """Test that Q is a valid confidence level value"""
        self.assertTrue(0 < Q < 1)
        
    def test_sample_size(self):
        """Test that the sample size is sufficient for t-distribution"""
        self.assertTrue(len(x) > 1)


if __name__ == "__main__":
    unittest.main()