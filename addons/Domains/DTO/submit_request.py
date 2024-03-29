from Entities.model import Model
from Entities.task_status import TaskStatus
from Entities.execution_button import ExecutionButton

class SubmitRequest:
    """モデル登録リクエスト
    """

    _model:Model
    """モデル
    """
    
    _task_status:TaskStatus
    """タスクステータス
    """
    
    _execution_button:ExecutionButton
    """実行ボタン
    """
    
    def __init__(self, model:Model, task_status:TaskStatus, execution_button:ExecutionButton) -> None:
        self._model = model
        self._task_status = task_status
        self._execution_button = execution_button
    
    def get_model(self) -> Model:
        """モデルのゲッター

        Returns:
            Model: モデル
        """
        return self._model
    
    def get_task_status(self) -> TaskStatus:
        """タスクステータスのゲッター

        Returns:
            TaskStatus: タスクステータス
        """
        return self._task_status
    
    def get_execution_button(self) -> ExecutionButton:
        """実行ボタンのゲッター

        Returns:
            ExecutionButton: 実行ボタン
        """
        return self._execution_button