import mgear.shifter.custom_step as cstp
import pymel.core as pm
from mgear.rigbits.facial_rigger import brow_rigger


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

        '''Remove default global control shape'''
        #Otherwise the animator could be confused about which "world" control their other controls are in the space of.
        control = self.mgear_run.global_ctl
        pm.delete(control.getShape())

        '''Remove leafParent control shape'''
        #LeafParent is only for space switching purposes
        control = self.component("leafParent_C0").ctl
        pm.delete(control.getShape())

        '''Reparent arm controls'''
        pm.parent(pm.PyNode('base_C0_0_cnx|arm_L0_root'), pm.PyNode('base_C0_fk2_ctl'))
        pm.parent(pm.PyNode('base_C0_0_cnx|arm_R0_root'), pm.PyNode('base_C0_fk2_ctl'))

        '''Reparent lower lip control'''
        pm.parent(pm.PyNode('base_C0_0_cnx|lowerLip_C0_root'), pm.PyNode('base_C0_fk2_ctl'))

        '''Build Lips'''
        brow_rigger.rig_from_file(
            r"C:/Users/sgoehrig/Documents/maya/projects/jennifern/data/rigConfigs/upperLip.brows")
        brow_rigger.rig_from_file(
            r"C:/Users/sgoehrig/Documents/maya/projects/jennifern/data/rigConfigs/lowerLip.brows")

        return
