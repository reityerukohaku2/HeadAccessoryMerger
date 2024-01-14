from enum import Enum, auto

class Status(Enum):
    """ステータス"""
    
    WAITING_FOR_MODEL_SUBMIT = auto()
    """モデルの登録待ち
    """
    
    WAITING_FOR_EXECUTION = auto()
    """実行待ち
    """
    
    MERGING = auto()
    """マージ中
    """
    
    WEIGHT_PAINTING = auto()
    """ウェイトペイント中
    """
    
    COMPLETE = auto()
    """完了
    """