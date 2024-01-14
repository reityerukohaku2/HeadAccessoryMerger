from enum import auto, Enum
from armature import Armature

"""モデルの種類
"""
class ModelType(Enum):
    HUMANOID = auto()
    ACCESSORY = auto()

"""モデル
"""
class Model:
    """モデルID
    """
    model_id:int
    
    """モデルの種類
    """
    model_type:ModelType
    
    """アーマチュア
    """
    armature:Armature
    
    """親のモデルID
    """
    parent_id:int