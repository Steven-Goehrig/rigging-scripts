import mgear.shifter.custom_step as cstp
import pymel.core as pm


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

        #Remove default global control shape
        #Otherwise the animator could be confused about which "world" control their other controls are in the space of.
        control = self.mgear_run.global_ctl
        pm.delete(control.getShape())

        #Control geo visibility with screen protector controls
        #Get Assets
        top_ctl = self.component("protector_top_C0").ctl
        bottom_ctl = self.component("protector_bottom_C0").ctl
        screenUp = pm.PyNode('ScreenProtector_Up_GEO')
        screenDown = pm.PyNode('ScreenProtector_Down_GEO')
        #Make and connect attributes
        pm.addAttr(top_ctl, ln='geoVis', type='bool', k=1, dv=True)
        pm.connectAttr(top_ctl.geoVis, screenUp.visibility)
        pm.addAttr(bottom_ctl, ln='geoVis', type='bool', k=1, dv=True)
        pm.connectAttr(bottom_ctl.geoVis, screenDown.visibility)

        #Create left arm switch
        #Get Assets
        lSwitch = self.component('arm_settings_L0').ctl
        lFlap_ctl = self.component('arm_flap_L0').ctl
        lFlap_geo = pm.PyNode('ClosedHand_L_GEO')
        lArm_ctl = pm.PyNode('body_C0_0_cnx|arm_L0_root')
        lArm_geo = ['ArmConnection_L_GEO', 'UpperArm_L_GEO', 'MidScrew_L_GEO', 'MidScrew_s1_L_GEO', 'MidScrew_s2_L_GEO', 'LowerArm_L_GEO', 'WristScrew_L_GEO', 'WristScrew_s1_L_GEO', 'WristScrew_s2_L_GEO', 'FingerConnection_L_GEO', 'Thumb_L_GEO', 'Fingers_L_GEO']
        #Make and connect attributes
        pm.addAttr(lSwitch, ln='armSwitch', type='float', k=1, min=0, max=1, dv=.5)
        #Flap
        pm.select(lFlap_ctl)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv = .9, v = True)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv = 1, v = False)
        pm.select(lFlap_geo)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv = .9, v = True)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv = 1, v = False)
        pm.select('arm_flap_L0_0_jnt')
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=.9, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=1, v=False)
        #Arm
        pm.select(lArm_ctl)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=.1, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=0, v=False)
        pm.select('arm_L0_0_jnt')
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=.1, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=0, v=False)
        for geo in lArm_geo:
            pm.select(geo)
            pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=.1, v=True)
            pm.setDrivenKeyframe(at='visibility', cd=lSwitch + '.armSwitch', dv=0, v=False)

        #Create right arm switch
        #Get Assets
        rSwitch = self.component('arm_settings_R0').ctl
        rFlap_ctl = self.component('arm_flap_R0').ctl
        rFlap_geo = pm.PyNode('ClosedHand_R_GEO')
        rArm_ctl = pm.PyNode('body_C0_0_cnx|arm_R0_root')
        rArm_geo = ['ArmConnection_R_GEO', 'UpperArm_R_GEO', 'MidScrew_R_GEO', 'MidScrew_s1_R_GEO', 'MidScrew_s2_R_GEO', 'LowerArm_R_GEO', 'WristScrew_R_GEO', 'WristScrew_s1_R_GEO', 'WristScrew_s2_R_GEO', 'FingerConnection_R_GEO', 'Thumb_R_GEO', 'Fingers_R_GEO']
        #Make and connect attributes
        pm.addAttr(rSwitch, ln='armSwitch', type='float', k=1, min=0, max=1, dv=.5)
        #Flap
        pm.select(rFlap_ctl)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.9, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=1, v=False)
        pm.select(rFlap_geo)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.9, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=1, v=False)
        pm.select('arm_flap_R0_0_jnt')
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.9, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=1, v=False)
        #Arm
        pm.select(rArm_ctl)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.1, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=0, v=False)
        pm.select('arm_R0_0_jnt')
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.1, v=True)
        pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=0, v=False)
        for geo in rArm_geo:
            pm.select(geo)
            pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=.1, v=True)
            pm.setDrivenKeyframe(at='visibility', cd=rSwitch + '.armSwitch', dv=0, v=False)

        #Constrain inner wheel
        pm.parentConstraint(self.component('inner_wheel_C1').ctl, 'Wheel_inside_GEO', mo=True)
        pm.pointConstraint(self.component('inner_wheel_C1').ctl, 'DO_NOT_TOUCH', mo=True)

        #Corner snap
        pm.addAttr(self.component('protector_top_C0').ctl, ln='cornerSnap', type='float', k=1, min=0, max=1, dv=0)
        #Point contrain
        pm.pointConstraint(self.component('protector_top_mid_low_C0').ctl, self.component('protector_top_mid_high_C0').ctl, w=0)
        pm.pointConstraint(self.component('protector_top_left_C0').ctl, self.component('protector_top_mid_high_C0').ctl, w=0)
        #Set driven keys
        pm.select('protector_top_mid_high_C0_ctl_pointConstraint1')
        pm.setDrivenKeyframe(at='protector_top_mid_low_C0_ctlW0', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=0, v=0)
        pm.setDrivenKeyframe(at='protector_top_mid_low_C0_ctlW0', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=1, v=1)
        pm.select('protector_top_mid_high_C0_ctl_pointConstraint1')
        pm.setDrivenKeyframe(at='protector_top_left_C0_ctlW1', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=0, v=0)
        pm.setDrivenKeyframe(at='protector_top_left_C0_ctlW1', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=1, v=1)
        pm.select(self.component('protector_top_mid_high_C0').ctl)
        pm.setDrivenKeyframe(at='visibility', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=1, v=False)
        pm.setDrivenKeyframe(at='visibility', cd=self.component('protector_top_C0').ctl + '.cornerSnap', dv=.9, v=True)
        #Center snap
        pm.addAttr(self.component('protector_top_C0').ctl, ln='centerSnap', type='float', k=1, min=0, max=1, dv=0)
        #Point contrain
        pm.pointConstraint(self.component('protector_top_right_C0').ctl, self.component('protector_top_mid_low_C0').ctl, w=0)
        pm.pointConstraint(self.component('protector_top_left_C0').ctl, self.component('protector_top_mid_low_C0').ctl, w=0)
        #Set driven keys
        pm.select('protector_top_mid_low_C0_ctl_pointConstraint1')
        pm.setDrivenKeyframe(at='protector_top_right_C0_ctlW0', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=0, v=0)
        pm.setDrivenKeyframe(at='protector_top_right_C0_ctlW0', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=1, v=1)
        pm.select('protector_top_mid_low_C0_ctl_pointConstraint1')
        pm.setDrivenKeyframe(at='protector_top_left_C0_ctlW1', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=0, v=0)
        pm.setDrivenKeyframe(at='protector_top_left_C0_ctlW1', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=1, v=1)
        pm.select(self.component('protector_top_mid_low_C0').ctl)
        pm.setDrivenKeyframe(at='visibility', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=1, v=False)
        pm.setDrivenKeyframe(at='visibility', cd=self.component('protector_top_C0').ctl + '.centerSnap', dv=.9, v=True)

        #Re-Parent Controls
        pm.parent('body_C0_0_cnx|head_C0_root', 'body_C0_fk2_ctl')
        pm.parent('body_C0_0_cnx|name_tag_C0_root', 'body_C0_fk1_ctl')
        pm.parent('body_C0_0_cnx|arm_R0_root', 'body_C0_fk1_ctl')
        pm.parent('body_C0_0_cnx|arm_L0_root', 'body_C0_fk1_ctl')
        pm.parent('body_C0_0_cnx|arm_flap_L0_root', 'body_C0_fk1_ctl')
        pm.parent('body_C0_0_cnx|arm_flap_R0_root', 'body_C0_fk1_ctl')

        return