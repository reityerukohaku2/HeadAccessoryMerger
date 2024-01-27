from abc import ABC, abstractmethod
from Domains.DTO.submit_request import SubmitRequest

"""
モデル登録ユースケース
"""
class IModelSubmitUseCase(ABC):

    @abstractmethod
    def submit(self, submit_request: SubmitRequest):
        """モデル登録

        Args:
            submit_request (SubmitRequest): モデル登録リクエスト
        """
        pass
