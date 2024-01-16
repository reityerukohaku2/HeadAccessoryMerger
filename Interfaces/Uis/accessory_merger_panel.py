import bpy

class AccessoryMergerPanel(bpy.types.Panel):
    """HeadAccessoryMergerパネル"""
    bl_idname = "object.head_accessory_merger"
    bl_label = "AccessoryMerger"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"

    def draw(self, context):
        self.layout.label(text="AccessoryMerger")