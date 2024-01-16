import bpy
from .Interfaces.Uis.accessory_merger_panel import AccessoryMergerPanel

bl_info = {
    "name": "Head Accessory Merger",
    "blender": (2, 80, 0),
    "category": "Object",
}

def register():
    bpy.utils.register_class(AccessoryMergerPanel)

def unregister():
    bpy.utils.unregister_class(AccessoryMergerPanel)

if __name__ == "__main__":
    register()