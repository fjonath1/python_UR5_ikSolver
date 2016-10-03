from inverseKinematicsUR5 import InverseKinematicsUR5, transformRobotParameter
import numpy as np
from math import pi

theta0 = [0.6,0.2,0.5,1.2,0.1,-0.1]
theta = [0.7,0.3,0.2,1.0,0.5,0.1]
gd = transformRobotParameter(theta)
print gd
joint_weights = [6,5,4,3,2,1]
ik = InverseKinematicsUR5()
ik.setJointWeights(joint_weights)
ik.setJointLimits(-pi, pi)
# print ik.solveIK(gd)
print ik.findClosestIK(gd,theta0)