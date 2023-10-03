# L_foot_smartRoll.py

'''
This script assumes you already have a basic foot rig as well as
IK handles and foot locators (heel, ball, and toe) in the proper
hierarchy beneath the L_foot_CTRL.
The L_foot_CTRL should have three custom attributes: Roll,
bendLimitAngle, and toeStraightAngle (Defaults: 0, 45, 70).
'''

import maya.cmds as cmds

### Limit Heel_LOC's rotX to negative when Roll attr is negative.
cmds.shadingNode('clamp', au=True, n='L_heel_rotClamp')
cmds.connectAttr('L_foot_CTRL.roll', 'L_heel_rotClamp.inputR')
cmds.setAttr('L_heel_rotClamp.minR', -90)
cmds.connectAttr('L_heel_rotClamp.outputR', 'L_heel_LOC.rotateX')

### Limit Toe_LOC's rotX to bendLimitAngle and toeStraightAngle.
cmds.shadingNode('clamp', au=True, n='L_foot_bendToStraightClamp')
cmds.connectAttr('L_foot_CTRL.roll', 'L_foot_bendToStraightClamp.inputR')
cmds.connectAttr('L_foot_CTRL.bendLimitAngle', 'L_foot_bendToStraightClamp.minR')
cmds.connectAttr('L_foot_CTRL.toeStraightAngle', 'L_foot_bendToStraightClamp.maxR')

### Convert Roll Value to a Percentage of the difference between bendLimitAngle and toeStraightAngle.
cmds.shadingNode('setRange', au=True, n='L_foot_bendToStraightPercent')
cmds.connectAttr('L_foot_bendToStraightClamp.minR', 'L_foot_bendToStraightPercent.oldMinX')
cmds.connectAttr('L_foot_bendToStraightClamp.maxR', 'L_foot_bendToStraightPercent.oldMaxX')
cmds.setAttr('L_foot_bendToStraightPercent.maxX', 1)
cmds.connectAttr('L_foot_bendToStraightClamp.inputR', 'L_foot_bendToStraightPercent.valueX')

### Multiply Percentage by Roll Value and Limit Toe_LOC's rotX.
cmds.shadingNode('multiplyDivide', au=True, n='L_foot_roll_MULT')
cmds.connectAttr('L_foot_bendToStraightPercent.outValueX', 'L_foot_roll_MULT.input1X')
cmds.connectAttr('L_foot_bendToStraightClamp.inputR', 'L_foot_roll_MULT.input2X')
cmds.connectAttr('L_foot_roll_MULT.outputX', 'L_toe_LOC.rotateX')

### Limit Ball_LOC's rotX to positive when Roll attr is positive. Invert rotation after bendLimitAngle.
cmds.shadingNode('clamp', au=True, n='L_ball_zeroToBendClamp')
cmds.connectAttr('L_foot_CTRL.roll', 'L_ball_zeroToBendClamp.inputR')
cmds.connectAttr('L_foot_CTRL.bendLimitAngle', 'L_ball_zeroToBendClamp.maxR')
cmds.shadingNode('setRange', au=True, n='L_ball_zeroToBendPercent')
cmds.connectAttr('L_ball_zeroToBendClamp.minR', 'L_ball_zeroToBendPercent.oldMinX')
cmds.connectAttr('L_ball_zeroToBendClamp.maxR', 'L_ball_zeroToBendPercent.oldMaxX')
cmds.setAttr('L_ball_zeroToBendPercent.maxX', 1)
cmds.connectAttr('L_ball_zeroToBendClamp.inputR', 'L_ball_zeroToBendPercent.valueX')
cmds.shadingNode('plusMinusAverage', au=True, n='L_foot_invertPercentage')
cmds.setAttr('L_foot_invertPercentage.input1D[0]', 1)
cmds.setAttr('L_foot_invertPercentage.input1D[1]', 1)
cmds.connectAttr('L_foot_bendToStraightPercent.outValueX', 'L_foot_invertPercentage.input1D[1]')
cmds.setAttr('L_foot_invertPercentage.operation', 2)
cmds.shadingNode('multiplyDivide', au=True, n='L_ball_percent_MULT')
cmds.connectAttr('L_ball_zeroToBendPercent.outValueX', 'L_ball_percent_MULT.input1X')
cmds.connectAttr('L_foot_invertPercentage.output1D', 'L_ball_percent_MULT.input2X')
cmds.shadingNode('multiplyDivide', au=True, n='L_ball_roll_MULT')
cmds.connectAttr('L_ball_percent_MULT.outputX', 'L_ball_roll_MULT.input1X')
cmds.connectAttr('L_foot_CTRL.roll', 'L_ball_roll_MULT.input2X')
cmds.connectAttr('L_ball_roll_MULT.outputX', 'L_ball_LOC.rotateX')