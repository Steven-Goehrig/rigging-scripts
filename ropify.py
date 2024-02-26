import mgear.shifter.custom_step as cstp
import pymel.core as pm
from mgear.rigbits.rope import rope


class CustomShifterStep(cstp.customShifterMainStep):
    """Turns the standard chain_spring_01 component into a tail by adding a layer of rope joints.
    """

    def setup(self):
        """
        Setting the name property makes the custom step accessible
        in later steps.

        i.e: Running  self.custom_step("ropify")  from steps ran after
             this one, will grant this step.
        """
        self.name = "ropify"

    def run(self):
        """Run method.

            i.e:  self.mgear_run.global_ctl
                gets the global_ctl from shifter rig build base

            i.e:  self.component("control_C0").ctl
                gets the ctl from shifter component called control_C0

            i.e:  self.custom_step("otherCustomStepName").ctlMesh
                gets the ctlMesh from a previous custom step called
                "otherCustomStepName"

        Returns:
            None: None
        """

        '''Create Curves'''

        # Get joint positions for CVs
        joints = pm.ls("leafTweak*", typ='joint')
        joints.sort()
        listNum = int(len(joints) / 7)
        jointsList = []
        for num in range(1, listNum + 1):
            begin = num * 7 - 7
            end = num * 7
            jointsList.append(joints[begin:end])

        #Create Ropes for each leaf
        ctlNum = 0
        for list in jointsList:
            jnt_positions = []
            for joint in list:
                jnt_positions.append(pm.xform(joint, q=True, t=True, ws=True))

            #Create Control Curve
            ctl_curve = pm.curve(n="ctl_crv_" + str(ctlNum), p=jnt_positions)

            #Create Up Vector Cure
            leafDir = pm.datatypes.Vector(pm.datatypes.Point(jnt_positions[0]) - pm.datatypes.Point(jnt_positions[-1]))
            worldUpv = pm.datatypes.Vector(0,1,0)
            upvDir = leafDir.cross(worldUpv).normal()
            upv_curve = pm.curve(n="upv_crv_" + str(ctlNum), p=jnt_positions)
            pm.xform(upv_curve, r=True, t=100*upvDir)

            #Bind Control Curve
            pm.skinCluster(joints, ctl_curve, tsb=True, bm=0, sm=0, mi=1)

            #Create Rope
            pm.select(ctl_curve)
            pm.select(upv_curve, add=True)
            rope(DEF_nb=24, ropeName="leafRope", keepRatio=True)

            #Increment ctlNum
            ctlNum += 1

            #Move curves under rig hierarchy
            pm.parent(ctl_curve, pm.PyNode('rig|setup'))
            pm.parent(upv_curve, pm.PyNode('rig|setup'))
            pm.setAttr(ctl_curve.visibility, 0)
            pm.setAttr(upv_curve.visibility, 0)

        # Move rope root nodes under rig hierarchy
        ropeRoots = pm.ls("leafRope_root*", typ='transform')
        for ropeRoot in ropeRoots:
            if pm.listRelatives(ropeRoot, p=True) == []:
                pm.parent(ropeRoot, pm.PyNode('rig|setup'))

        return