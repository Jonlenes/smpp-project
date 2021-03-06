from abc import ABC, abstractmethod
from time import time
from src.problem import Result

class BaseOptimizer(ABC):
    """Abstract class for Optimizers"""

    def __init__(self):
        pass

    def solve(self, smbpp, timeout, seed, verbose, **kwargs) -> Result:
        """Abstract method to optimize.
        """
        start_time = time()
        result = self._solve(smbpp, timeout, seed, verbose, **kwargs)
        result['time'] = time() - start_time
        result['is_valid'] = smbpp.validate_current_solution()
        return result
    
    @abstractmethod
    def _solve(self, smbpp, timeout, seed, verbose, **kwargs):
        """Abstract method to optimize.
        """
        raise NotImplementedError