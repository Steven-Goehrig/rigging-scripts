import mgear.shifter.custom_step as cstp
from maya import mel


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
        self.name = "import_shapes_carl"

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
        mel.eval('source "C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/SHAPES/setup/carl_geo_arms_blendShape.mel";')
        mel.eval('source "C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/SHAPES/setup/carl_geo_pants_blendShape.mel";')
        mel.eval('source "C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/SHAPES/setup/carl_geo_shirt_blendShape.mel";')
        mel.eval('source "C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/SHAPES/setup/carl_geo_tie_blendShape.mel";')
        mel.eval('source "C:/Users/steve/OneDrive/Documents/maya/projects/Bulbank/data/SHAPES/setup/carl_geo_vest_blendShape.mel";')

        return