import mgear.shifter.custom_step as cstp
from mgear.core import skin
import os
import pymel.core as pm

class CustomShifterStep(cstp.customShifterMainStep):
    def __init__(self):
        self.name = "import_skinPack_carl"

    def run(selfself, stepDict):
        path = "\\".join(os.path.abspath(os.path.dirname(__file__)).split("\\")[:-2])
        skin.importSkinPack(os.path.join(path, "Bulbank", "data", "skinPacks", "carl", "carl.gSkinPack"))