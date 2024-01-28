from ...Domains.Entities.model import Model
from abc import ABC, abstractmethod

class IModelRepository(ABC):
    """モデル用リポジトリ

    Args:
        ABC (_type_): _description_
    """
    @abstractmethod
    def update(self, model: Model):
        """モデルの追加

        Args:
            model (Model): モデル
        """
        pass