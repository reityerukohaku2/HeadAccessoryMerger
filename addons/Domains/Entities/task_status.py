from status import Status
from model import Model
from model_type import ModelType

class TaskStatus():
    """タスクステータス管理
    """
    
    _status:Status
    """ステータス
    """
    
    _humanoid_model:Model = None
    """人モデル
    """
    
    _accessory_model:Model = None
    """アクセサリモデル
    """
    
    def get_status(self) -> Status:
        """ステータスのゲッター

        Returns:
            Status: ステータス
        """
        return self._status
    

    def set_humanoid(self, model:Model):
        """人モデルのセッター

        Args:
            model (Model): モデル

        Raises:
            ValueError: HUMANOIDではないModelが渡された場合に発生
        """
        
        # モデルの種類をチェックして、正しい場合にモデルセット
        if model.get_model_type() is ModelType.HUMANOID:
            self._humanoid_model = model
            self._change_status()
        else:
            raise ValueError("HUMANOIDではないModelが渡されました")


    def set_accessory(self, model:Model):
        """アクセサリモデルのセッター

        Args:
            model (Model): モデル

        Raises:
            ValueError: ACCESSORYではないModelが渡された場合に発生
        """
        
        # モデルの種類をチェックして、正しい場合にモデルセット
        if model.get_model_type() is ModelType.ACCESSORY:
            self._accessory_model = model
            self._change_status()
        else:
            raise ValueError("ACCESSORYではないModelが渡されました")

    def _change_status(self):
        """状況に応じてステータスを変更する
        """
        
        if self._status is Status.WAITING_FOR_MODEL_SUBMIT:
            # 人モデルとアクセサリモデルの双方が設定されていれば
            # 実行待ち状態に移行する
            if self._humanoid_model is not None and self._accessory_model is not None:
                self._status = Status.WAITING_FOR_EXECUTION
                return
        elif self._status is Status.WAITING_FOR_EXECUTION:
            return
        elif self._status is Status.MERGING:
            return
        elif self._status is Status.WEIGHT_PAINTING:
            return
        else:
            return