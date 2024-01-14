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