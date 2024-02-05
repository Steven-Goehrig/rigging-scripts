import mgear.shifter.custom_step as cstp
import pymel.core as pm
from mgear.rigbits.facial_rigger import eye_rigger, lips_rigger


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

        return