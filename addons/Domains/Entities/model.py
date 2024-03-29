from armature import Armature
from model_type import ModelType

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
    
    def get_model_type(self) -> ModelType:
        """モデルタイプのゲッター

        Returns:
            ModelType: モデルの種類
        """
        return self._model_type