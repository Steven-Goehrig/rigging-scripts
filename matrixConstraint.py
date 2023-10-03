from maya.api import OpenMaya as om2
import pymel.core as pm

def matrixConstraint(source, destination, mo=False, t=True, r=True):
    """
    Constrains the destination node to the source node.
     
    Args:
        source(str): A source node name.
        destination(str): A destination node name.
        mo(bool): Whether to maintain the current offset.
        t(bool): Whether to constrain translation.
        r(bool): Whether to constrain rotation.
    """
    
    #Create multMatrix node that will add up the constraining matrices.
    multNode = pm.shadingNode('multMatrix', au=True)
    #Create and Connect decomposeMatrix node that will plug into destination's transform.
    decompNode = pm.createNode('decomposeMatrix')
    pm.connectAttr(multNode.matrixSum, decompNode.inputMatrix)
    
    #If Maintaining Offset, Connect offset matrix to the MultMatrix Node.
    if mo:
        #Get offset transform.
        srcMatrix = pm.PyNode(source).getMatrix(worldSpace=True)
        dstMatrix = pm.PyNode(destination).getMatrix(worldSpace=True)
        offsetMatrix = dstMatrix * srcMatrix.inverse()
        offsetTransform = om2.MTransformationMatrix(om2.MMatrix(offsetMatrix))
        
        #Create and Set values for the offset node.
        offsetNode = pm.createNode('composeMatrix')
        offsetNode.inputTranslate.set(*offsetTransform.translation(4))
        offsetNode.inputRotate.set(*offsetTransform.rotation(asQuaternion=False))
        
        #Connect to multMatrix.
        pm.connectAttr(offsetNode.outputMatrix, multNode.matrixIn[0])
        
    #Connect source's World Matrix and destination's Parent Inverse to multNode.
    pm.connectAttr(pm.PyNode(source).worldMatrix[0], multNode.matrixIn[1])
    pm.connectAttr(pm.PyNode(destination).parentInverseMatrix, multNode.matrixIn[2])
    #Plug decomposeMatrix's output tranform into destination's transform. Adjust for translation or rotation only.
    if t:
        pm.connectAttr(decompNode.outputTranslate, pm.PyNode(destination).translate)
    if r:
        pm.connectAttr(decompNode.outputRotate, pm.PyNode(destination).rotate)
    
matrixConstraint('srcChild', 'dstChild', mo=True)
