bl_info = {
    "name": "Head Accessory Merger",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class HeadAccessoryMerger(bpy.types.Operator):
    """HeadAccessoryMerger"""
    bl_idname = "object.head_accessory_merger"
    bl_label = "Merge Accessory into Head"
    bl_options = {'REGISTER', 'UNDO'}
    
    def execute(self, context):
        return {'FINISHED'}

# store keymaps here to access after registration
addon_keymaps = []


def register():
    bpy.utils.register_class(HeadAccessoryMerger)

def unregister():
    bpy.utils.unregister_class(HeadAccessoryMerger)

if __name__ == "__main__":
    register()