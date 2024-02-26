import mgear.shifter.custom_step as cstp
import pymel.core as pm
from mgear.rigbits.facial_rigger import eye_rigger, lips_rigger, brow_rigger
from mgear.rigbits import replaceShape


class CustomShifterStep(cstp.customShifterMainStep):
    """Cleans up the Robot's controls after creation.
    """

    def setup(self):
        """
        Setting the name property makes the custom step accessible
        in later steps.

        i.e: Running  self.custom_step("cleanup_controls")  from steps ran after
             this one, will grant this step.
        """
        self.name = "cleanup_controls"

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

        """Remove default global control shape"""
        #Otherwise the animator could be confused about which "world" control their other controls are in the space of.
        control = self.mgear_run.global_ctl
        pm.delete(control.getShape())

        """Isolate Left FK Leg Control Switch"""
        # control to isolate
        isolate_ctrl = pm.PyNode('leg_L0_fk0_ctl')

        # spaces to add to isolation
        global_ctrl = pm.PyNode('local_C0_ctl')
        parent_ctrl = pm.PyNode('body_C0_ctl')

        isolate_constrain_grp = pm.PyNode('leg_L0_fk0_npo')
        isolate_constrain_grp_parent = isolate_constrain_grp.getParent()
        isolate_attr_holder = pm.PyNode('legUI_L0_ctl')

        # create extra top group for isolate constrain
        isolate_grp = pm.group(n=isolate_constrain_grp.name() + '_isolate', empty=True, world=True)
        pm.delete(pm.parentConstraint(isolate_constrain_grp_parent, isolate_grp, mo=False))

        pm.parent(isolate_constrain_grp, isolate_grp)
        pm.parent(isolate_grp, isolate_constrain_grp_parent)

        # add orientConstraint
        con = pm.parentConstraint(global_ctrl, parent_ctrl, isolate_grp, mo=True, weight=0,
                                  skipTranslate=['x', 'y', 'z'])
        con.interpType.set(2)

        # add attribute for switching spaces
        pm.addAttr(isolate_attr_holder, type='float', min=0, max=1, dv=1, longName='isolate_fk_rotation', keyable=True)

        # connect attr to constraint target weights
        isolate_attr_holder.isolate_fk_rotation >> con.getWeightAliasList()[0]

        rev_node = pm.createNode('reverse')
        isolate_attr_holder.isolate_fk_rotation >> rev_node.inputX
        rev_node.outputX >> con.getWeightAliasList()[1]


        """Isolate Right FK Leg Control Switch"""
        # control to isolate
        isolate_ctrl = pm.PyNode('leg_R0_fk0_ctl')

        # spaces to add to isolation
        global_ctrl = pm.PyNode('local_C0_ctl')
        parent_ctrl = pm.PyNode('body_C0_ctl')

        isolate_constrain_grp = pm.PyNode('leg_R0_fk0_npo')
        isolate_constrain_grp_parent = isolate_constrain_grp.getParent()
        isolate_attr_holder = pm.PyNode('legUI_R0_ctl')

        # create extra top group for isolate constrain
        isolate_grp = pm.group(n=isolate_constrain_grp.name() + '_isolate', empty=True, world=True)
        pm.delete(pm.parentConstraint(isolate_constrain_grp_parent, isolate_grp, mo=False))

        pm.parent(isolate_constrain_grp, isolate_grp)
        pm.parent(isolate_grp, isolate_constrain_grp_parent)

        # add orientConstraint
        con = pm.parentConstraint(global_ctrl, parent_ctrl, isolate_grp, mo=True, weight=0,
                                  skipTranslate=['x', 'y', 'z'])
        con.interpType.set(2)

        # add attribute for switching spaces
        pm.addAttr(isolate_attr_holder, type='float', min=0, max=1, dv=1, longName='isolate_fk_rotation', keyable=True)

        # connect attr to constraint target weights
        isolate_attr_holder.isolate_fk_rotation >> con.getWeightAliasList()[0]

        rev_node = pm.createNode('reverse')
        isolate_attr_holder.isolate_fk_rotation >> rev_node.inputX
        rev_node.outputX >> con.getWeightAliasList()[1]

        """Isolate Left FK Arm Control Switch"""
        # control to isolate
        isolate_ctrl = pm.PyNode('arm_L0_fk0_ctl')

        # spaces to add to isolation
        global_ctrl = pm.PyNode('local_C0_ctl')
        parent_ctrl = pm.PyNode('shoulder_L0_orbit_ctl')

        isolate_constrain_grp = pm.PyNode('arm_L0_fk0_npo')
        isolate_constrain_grp_parent = isolate_constrain_grp.getParent()
        isolate_attr_holder = pm.PyNode('armUI_L0_ctl')

        # create extra top group for isolate constrain
        isolate_grp = pm.group(n=isolate_constrain_grp.name() + '_isolate', empty=True, world=True)
        pm.delete(pm.parentConstraint(isolate_constrain_grp_parent, isolate_grp, mo=False))

        pm.parent(isolate_constrain_grp, isolate_grp)
        pm.parent(isolate_grp, isolate_constrain_grp_parent)

        # add orientConstraint
        con = pm.parentConstraint(global_ctrl, parent_ctrl, isolate_grp, mo=True, weight=0,
                                  skipTranslate=['x', 'y', 'z'])
        con.interpType.set(2)

        # add attribute for switching spaces
        pm.addAttr(isolate_attr_holder, type='float', min=0, max=1, dv=0, longName='isolate_fk_rotation', keyable=True)

        # connect attr to constraint target weights
        isolate_attr_holder.isolate_fk_rotation >> con.getWeightAliasList()[0]

        rev_node = pm.createNode('reverse')
        isolate_attr_holder.isolate_fk_rotation >> rev_node.inputX
        rev_node.outputX >> con.getWeightAliasList()[1]


        """Isolate Right FK Arm Control Switch"""
        # control to isolate
        isolate_ctrl = pm.PyNode('arm_R0_fk0_ctl')

        # spaces to add to isolation
        global_ctrl = pm.PyNode('local_C0_ctl')
        parent_ctrl = pm.PyNode('shoulder_R0_orbit_ctl')

        isolate_constrain_grp = pm.PyNode('arm_R0_fk0_npo')
        isolate_constrain_grp_parent = isolate_constrain_grp.getParent()
        isolate_attr_holder = pm.PyNode('armUI_R0_ctl')

        # create extra top group for isolate constrain
        isolate_grp = pm.group(n=isolate_constrain_grp.name() + '_isolate', empty=True, world=True)
        pm.delete(pm.parentConstraint(isolate_constrain_grp_parent, isolate_grp, mo=False))

        pm.parent(isolate_constrain_grp, isolate_grp)
        pm.parent(isolate_grp, isolate_constrain_grp_parent)

        # add orientConstraint
        con = pm.parentConstraint(global_ctrl, parent_ctrl, isolate_grp, mo=True, weight=0,
                                  skipTranslate=['x', 'y', 'z'])
        con.interpType.set(2)

        # add attribute for switching spaces
        pm.addAttr(isolate_attr_holder, type='float', min=0, max=1, dv=0, longName='isolate_fk_rotation', keyable=True)

        # connect attr to constraint target weights
        isolate_attr_holder.isolate_fk_rotation >> con.getWeightAliasList()[0]

        rev_node = pm.createNode('reverse')
        isolate_attr_holder.isolate_fk_rotation >> rev_node.inputX
        rev_node.outputX >> con.getWeightAliasList()[1]

        '''Build Eyes'''
        eye_rigger.rig_from_file(r"C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/rigConfigs/carl_L.eyes")
        eye_rigger.rig_from_file(r"C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/rigConfigs/carl_R.eyes")

        '''Build Lips'''
        lips_rigger.rig_from_file(r"C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/rigConfigs/carl.lips")

        '''Build Brows'''
        brow_rigger.rig_from_file(r"C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/rigConfigs/carl_L.brows")
        brow_rigger.rig_from_file(r"C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/rigConfigs/carl_R.brows")
        #Move brow shapes outside of brow
        browBuffers = pm.ls('brow*' + '*controlBuffer')
        for browBuffer in browBuffers:
            if browBuffer == pm.PyNode('brow_L0_ctl_controlBuffer') or browBuffer == pm.PyNode(
                    'brow_R0_ctl_controlBuffer'):
                browBuffers.remove(browBuffer)
        for browBuffer in browBuffers:
            pm.select(browBuffer)
            pm.select(pm.PyNode(browBuffer.nodeName().replace('_controlBuffer', '')), add=True)
            replaceShape()

        '''Control teeth visibility with jaw control'''
        #Get Assets
        jaw_ctl = pm.PyNode('mouth_C0_jaw_ctl')
        top_ctl = pm.PyNode('mouth_C0_teethup_ctl')
        bottom_ctl = pm.PyNode('mouth_C0_teethlow_ctl')
        topTeeth = pm.PyNode('Teeth_Upper_GEO')
        topGum = pm.PyNode('Gum_Upper_GEO')
        bottomTeeth = pm.PyNode('Teeth_Lower_GEO')
        bottomGum = pm.PyNode('Gum_Lower_GEO')
        bigTeeth = pm.PyNode('BigTeeth_GEO')
        bigTeethCtl = pm.PyNode('bigTeeth_C0_ctl')

        #Make and connect attributes
        pm.addAttr(jaw_ctl, ln='teeth_vis', type='bool', k=1, dv=True)
        pm.connectAttr(jaw_ctl.teeth_vis, top_ctl.visibility)
        pm.connectAttr(jaw_ctl.teeth_vis, topTeeth.visibility)
        pm.connectAttr(jaw_ctl.teeth_vis, topGum.visibility)
        pm.connectAttr(jaw_ctl.teeth_vis, bottom_ctl.visibility)
        pm.connectAttr(jaw_ctl.teeth_vis, bottomTeeth.visibility)
        pm.connectAttr(jaw_ctl.teeth_vis, bottomGum.visibility)

        inv_teeth_vis = pm.shadingNode('reverse', au=1)
        pm.connectAttr(jaw_ctl.teeth_vis, inv_teeth_vis.inputX)
        pm.connectAttr(inv_teeth_vis.outputX, bigTeeth.visibility)
        pm.setAttr(bigTeethCtl.visibility, lock=0)
        pm.connectAttr(inv_teeth_vis.outputX, bigTeethCtl.visibility)

        '''Set limits on eye rotation'''
        pm.transformLimits('eye_L0_eye_jnt', erx=(-15, 20), ery=(-5, 35), rx=(-15, 20), ry=(-5, 35))
        pm.transformLimits('eye_R0_eye_jnt', erx=(-15, 20), ery=(-35, 5), rx=(-15, 20), ry=(-35, 5))

        '''Set default jaw sensitivity'''
        pm.setAttr('faceUI_C0_ctl.mouth_siderot', 2)
        pm.setAttr('faceUI_C0_ctl.mouth_vertrot', 2)

        '''Mouth Master Control'''
        jawCtl = pm.PyNode('mouth_C0_jaw_ctl')
        #Group mouth control parents
        con_grp = pm.group(pm.PyNode('mouth_C0_liplow_npo'))
        lowCon = pm.parentConstraint(pm.PyNode('mouthMaster_C0_ctl'), con_grp, mo=True, w=0)
        con_grp = pm.group(pm.PyNode('mouth_C0_lipup_npo'))
        upCon = pm.parentConstraint(pm.PyNode('mouthMaster_C0_ctl'), con_grp, mo=True, w=0)
        #Create and connect switch on jaw
        pm.addAttr(pm.PyNode('mouth_C0_jaw_ctl'), type='float', min=0, max=1, dv=0, longName='mouthMasterSwitch', keyable=True)
        jawCtl.mouthMasterSwitch >> upCon.getWeightAliasList()[0]
        jawCtl.mouthMasterSwitch >> lowCon.getWeightAliasList()[0]
        pm.setAttr('mouthMaster_C0_ctl.visibility', k=True, lock=False)
        jawCtl.mouthMasterSwitch >> 'mouthMaster_C0_ctl.visibility'

        '''Mouth Shapes'''
        pm.addAttr(pm.PyNode('mouth_C0_jaw_ctl'), type='float', min=0, max=1, dv=0, longName='puffCheecks',
                   keyable=True)
        pm.addAttr(pm.PyNode('mouth_C0_jaw_ctl'), type='float', min=0, max=1, dv=0, longName='puckerLips',
                   keyable=True)

        return
