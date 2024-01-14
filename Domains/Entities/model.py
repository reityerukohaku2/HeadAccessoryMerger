from enum import auto, Enum
from armature import Armature


class ModelType(Enum):
    """モデルの種類
    """
    
    HUMANOID = auto()
    """人型
    """
    
    ACCESSORY = auto()
    """アクセサリ
    """


class Model:
    """モデル
    """

    model_id:int
    """モデルID
    """
    
    model_type:ModelType
    """モデルの種類
    """
    
    armature:Armature
    """アーマチュア
    """
    
    parent_id:int
    """親のモデルID
    """