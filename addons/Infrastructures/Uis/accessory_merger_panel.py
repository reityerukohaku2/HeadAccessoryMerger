import bpy
from ...Controller.model_controller import ModelController

class AccessoryMergerPanel(bpy.types.Panel):
    """HeadAccessoryMergerパネル"""
    bl_idname = "accessory_merger_panel"
    bl_label = "AccessoryMerger"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Operator"

    def __init__(self):
        bpy.types.Scene.humanoid = bpy.props.StringProperty()
        bpy.types.Scene.accessory = bpy.props.StringProperty()

    def draw(self, context):
        layout = self.layout
        
        # オブジェクト選択メニューを作成
        layout.prop_search(context.scene, "humanoid", context.scene, "objects", text="人型モデル")
        layout.prop_search(context.scene, "accessory", context.scene, "objects", text="アクセサリー")
        
        ModelController.PostSubmitRequest()

