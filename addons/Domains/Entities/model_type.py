from enum import auto, Enum

class ModelType(Enum):
    """モデルの種類
    """
    
    HUMANOID = auto()
    """人型
    """
    
    ACCESSORY = auto()
    """アクセサリ
    """