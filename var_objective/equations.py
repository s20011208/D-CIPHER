from .differential_operator import LinearOperator, Partial
from sympy import Symbol, Function, symbols, sin
from abc import ABC, abstractmethod
import numpy as np

def get_pdes(name, parameters=None):
    
    if name == "TestEquation1":
        return TestEquation1()
    elif name == "TestEquation2":
        return TestEquation2()
    elif name == "Laplace2D":
        return Laplace2D()

class PDE(ABC):

    def __init__(self, param=None):
        pass
       
    @property
    @abstractmethod
    def name(self):
        pass
    
    @property
    @abstractmethod
    def M(self):
        pass

    @property
    @abstractmethod
    def N(self):
        pass

    @property
    @abstractmethod
    def num_conditions(self):
        pass



    @abstractmethod
    def get_expression(self):
        pass

    @abstractmethod
    def get_solution(self, boundary_functions):
        pass

    def __str__(self):
        return "\n".join([f"({L})u - {g} = 0" for L,g in self.get_expression()])


class TestEquation1(PDE):

    def __init__(self):
        super().__init__(None)
    
    @property
    def name(self):
        return "TestEquation1"

    @property
    def M(self):
        return 2

    @property
    def N(self):
        return  1

    @property
    def num_conditions(self):
        return 1
    
    def get_expression(self):
        x0,x1 = symbols('x0,x1', real=True)
        g = Function('g')
        L = LinearOperator([1.0,-1.0],[Partial([1,0]),Partial([0,1])])
        g = 0.0*x0 + 0.0*x1
        return [(L,g)]

    def get_solution(self, boundary_functions):
        if len(boundary_functions) != self.num_conditions:
            raise ValueError("Wrong number of boundary functions")
        h = boundary_functions[0]
        def func(x):
            return h(x[0] + x[1])

        return [func]
        

class TestEquation2(PDE):
    
    def __init__(self):
        super().__init__(None)
    
    @property
    def name(self):
        return "TestEquation2"

    @property
    def M(self):
        return 2

    @property
    def N(self):
        return  1

    @property
    def num_conditions(self):
        return 1
    
    def get_expression(self):
        x0,x1 = symbols('x0,x1', real=True)
        g = Function('g')
        L = LinearOperator([1.0,2.0],[Partial([1,0]),Partial([0,1])])
        g = 0.0*x0 + sin(x1)
        return [(L,g)]

    def get_solution(self, boundary_functions):
        """
            boundary_function h specifies the boundary condition u0(t,0) = h(t)
        """
        if len(boundary_functions) != self.num_conditions:
            raise ValueError("Wrong number of boundary functions")
        h = boundary_functions[0]
        def func(x):
            return -0.5 * np.cos(x[1]) + h(x[0] - x[1]/2) + 0.5

        return [func]


class Laplace2D(PDE):

    def __init__(self):
        super().__init__(None)

    @property
    def name(self):
        return "Laplace2D"

    @property
    def M(self):
        return 2

    @property
    def N(self):
        return  1

    def get_expression(self):
        x0,x1 = symbols('x0,x1', real=True)
        g = Function('g')
        L = LinearOperator([1.0,1.0],[Partial([2,0]),Partial([0,2])])
        g = 0.0*x0 + 0.0*x1
        return [(L,g)]
    
    def get_solution(self, boundary_functions):
        return super().generate_solution(boundary_functions)

        
    