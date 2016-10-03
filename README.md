# python_UR5_ikSolver
Closed form IK solver for UR5

## Dependencies:
numpy

## class function members:
  - setJointWeights(joint weights{python list}): assign weights for each joint with a python list that contains 6 elements  
  - setJointLimits(joint_minimum{numerical_value}, joint_maximum{numerical_value}): set joint limit parameters for all joint.  
  - solveIK(target_transformation{numpy 4x4 array} ): returns up to 8 joint configuration in numpy array with dimension (number_of_solutions x 6). If there is no solution, returns None  
  - findClosestIK (target_transformation{numpy 4x4 array}, current_joint{python list/ numpy array containing 6 elements} ): returns closest IK solution from the current joint. The closest value depends on joint weights and the solution itself. If there is no solution, returns None  

## usage:
See test.py
