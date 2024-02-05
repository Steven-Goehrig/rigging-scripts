import mgear.shifter.custom_step as cstp
from mgear.core import skin
import os
import pymel.core as pm

class CustomShifterStep(cstp.customShifterMainStep):
    def __init__(self):
        self.name = "import_geoProxy_carl"

    def run(self, stepDict):
        self.import_geometry()

        try:
            pm.select("guide")
        except:
            pass

    def import_geometry(self):
        path = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-1])

        pm.importFile(os.path.join(path, "scenes", "carl_geo.ma"))