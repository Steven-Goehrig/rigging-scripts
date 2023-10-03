# L_arm_IKStretch.py

'''
Start with a left arm joint chain (positive X).
Each joint labeled according to the convention L_[jointname]_IK_JNT.
It should have a RPSolver IK Handle and a measure distance node from beginning to end.
The distanceDimension node should be labeled L_arm_IK_length.
The L_arm_IK_lengthEnd_LOC should be placed under the IK arm control alongside the IK Handle.
'''

import maya.cmds as cmds

driver = 'L_arm_IK_lengthShape.distance'
leftUpperArmLength = cmds.getAttr('L_foreArm_IK_JNT.translateX')
leftForeArmLength = cmds.getAttr('L_hand_IK_JNT.translateX')
sumLength = leftUpperArmLength + leftForeArmLength

# Set first upper arm key at default max arm length. Ensures elbow bend beneath this value.
cmds.setDrivenKeyframe('L_foreArm_IK_JNT', cd=driver, dv=sumLength, at='translateX', v=leftUpperArmLength, itt='clamped', ott='clamped')

# Set second upper arm key at twice max arm length. Set post infinity of the second key to linear for infinite stretch.
cmds.setDrivenKeyframe('L_foreArm_IK_JNT', cd=driver, dv=sumLength*2, at='translateX', v=leftUpperArmLength*2, itt='clamped', ott='clamped')
cmds.selectKey('L_foreArm_IK_JNT', index=(1,1), at='translateX')
cmds.setInfinity(poi='linear')

# Set first forearm key at default max arm length. Ensures elbow bend beneath this value.
cmds.setDrivenKeyframe('L_hand_IK_JNT', cd=driver, dv=sumLength, at='translateX', v=leftForeArmLength, itt='clamped', ott='clamped')

# Set second forearm key at twice max arm length. Set post infinity of the second key to linear for infinite stretch.
cmds.setDrivenKeyframe('L_hand_IK_JNT', cd=driver, dv=sumLength*2, at='translateX', v=leftForeArmLength*2, itt='clamped', ott='clamped')
cmds.selectKey('L_hand_IK_JNT', index=(1,1), at='translateX')
cmds.setInfinity(poi='linear')
