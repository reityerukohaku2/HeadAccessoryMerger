import bpy
from .Interfaces.Uis.accessory_merger_panel import *

bl_info = {
    "name": "Head Accessory Merger",
    "blender": (2, 80, 0),
    "category": "Object",
}

# def launch_debug_server():
    
#     ptvsd_path = "c:/users/fujimoto.rei22/appdata/local/packages/pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0/localcache/local-packages/python310/site-packages"
#     import sys
#     sys.path.append(ptvsd_path)
#     import ptvsd

#     # デバッグサーバの立ち上げ
#     # IPアドレス0.0.0.0（ローカルホスト）、ポート5678として立ち上げる
#     ptvsd.enable_attach(address=("0.0.0.0", 5678))

#     # Visual Studio Codeからのデバッグリクエストを待ち受ける
#     ptvsd.wait_for_attach()

def register():
    bpy.utils.register_class(AccessoryMergerPanel)
    # launch_debug_server()
    
def unregister():
    bpy.utils.unregister_class(AccessoryMergerPanel)

if __name__ == "__main__":
    register()