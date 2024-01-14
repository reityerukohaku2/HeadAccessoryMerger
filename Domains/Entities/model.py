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

    _model_id:int
    """モデルID
    """
    
    _model_type:ModelType
    """モデルの種類
    """
    
    _armature:Armature
    """アーマチュア
    """
    
    _parent_id:int
    """親のモデルID
    """