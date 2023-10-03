# FKIKSwitch.py

'''
This script assumes a normal human body.
Start with three overlapping and identical joint chains for a leg or arm.
Label each according to the convention [L/R]_[jointname]_[FK/IK/result]_JNT.
Also have a [L/R]_[limb]_settings_CTRL with an FKIK_blend attribute from 0 to 1.
It should be parent constrained to the [L/R]_[foot/hand]_result_JNT.
'''

import maya.cmds as cmds

'''
BEFORE EXECUTING: Going from top to bottom down each hierarchy, shift select the joints
in this order: result, FK, IK. Then shift select the settings control.
Example: If selecting the left leg joints, you would start with L_thigh_result_JNT
and end with the L_foot_IK_JNT,
'''

# Create lists.
objects = cmds.ls(orderedSelection=True)
resultJoints = objects[0:3]
FKJoints = objects[3:6]
IKJoints = objects[6:9]
blendColors = []
counter = 0
ctrl = objects[9]

#Create and name blendColors nodes.

for eachJoint in FKJoints:
    blendColors.append(cmds.shadingNode('blendColors', au=True, n=eachJoint.replace('FK_JNT', 'rot_FKIKChoice')))
    blendColors.append(cmds.shadingNode('blendColors', au=True, n=eachJoint.replace('FK_JNT', 'trans_FKIKChoice')))

# Connect IK JNT attrs to respective blendNode color1 attrs.
for eachJoint in IKJoints:
    cmds.connectAttr('%s.rotate' % (eachJoint), '%s.color1' % (blendColors[counter]))
    counter += 1
    cmds.connectAttr('%s.translate' % (eachJoint), '%s.color1' % (blendColors[counter]))
    counter += 1
    
counter = 0

# Connect FK JNT attrs to respective blendNode color2 attrs.
for eachJoint in FKJoints:
    cmds.connectAttr('%s.rotate' % (eachJoint), '%s.color2' % (blendColors[counter]))
    counter += 1
    cmds.connectAttr('%s.translate' % (eachJoint), '%s.color2' % (blendColors[counter]))
    counter += 1
    
counter = 0

# Connect blendNode output attrs to respective result JNT attrs.
for eachJoint in resultJoints:
    cmds.connectAttr('%s.output' % (blendColors[counter]), '%s.rotate' % (eachJoint))
    counter += 1
    cmds.connectAttr('%s.output' % (blendColors[counter]), '%s.translate' % (eachJoint))
    counter += 1

counter = 0

# Connect settings ctrl FK/IK Blend attr to blendNode blender attr.
for eachBlender in blendColors:
    cmds.connectAttr('%s.FKIK_blend' % (ctrl), '%s.blender' % (blendColors[counter]))
    counter += 1
 