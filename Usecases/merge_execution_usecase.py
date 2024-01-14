from abc import ABC, abstractmethod

class IMergeExecutionUseCase(ABC):
    """
    マージ実行ユースケース
    """
    
    @abstractmethod
    def execute_merge(self):
        """マージ実行
        """
        pass
