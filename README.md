# Description
A collection of scripts I made for character rigging in Maya.

# Scripts

[Matrix Constraint](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/matrixConstraint.py): Constrains the destination node to the source node. Written with PyMEL and OpenMaya.

FKIK Switch: Automates the creation of the necessary connections for the result skeleton of a biped to be driven by both Forward Kinematic and Inverse Kinematic systems. Written with PyMEL.

[Left Arm IK Stretch](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/L_arm_IKStretch.py): Automates the creation of the necessary connections for the IK system to squash and stretch. Written with Cmds.

[Left Foot Smart Roll](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/L_foot_smartRoll.py): Automates various elements of a foot roll in order to assist with the animation of walk cycles. Written with Cmds.

[Limb Matching](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/limbMatching.mel): Creates a UI tool for matching the translation and orientation of FK limbs to IK limbs and vice versa in order to enable seamless animations when switching between systems. Written in MEL.

# Aim Constraint

These gifs display an aim constraint component I scripted using the tools established within the modular rigging system used at Respawn Entertainment on *Apex Legends*. Given the proprietary nature of the tools, I cannot share the code. But these gifs should give an idea of how it functions. The first gif shows the component being created from scratch and creating a new bone. The second gif demonstrates that it also works when you select a pre-existing bone before excuting the script.

![Alt Text](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/aimConstraint_respawn_01.gif)

![Alt Text](https://github.com/Steven-Goehrig/rigging-scripts/blob/main/aimConstraint_respawn_02.gif)
