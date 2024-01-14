from Usecases.model_submit_usecase import IModelSubmitUseCase
from DTO.submit_request import SubmitRequest
from Entities.model_type import ModelType
from Entities.status import Status

class ModelSubmitInteractor(IModelSubmitUseCase):
    def submit(self, request: SubmitRequest):
        """モデル登録

        Args:
            request (SubmitRequest): モデル登録リクエスト
        """
        
        model = request.get_model()
        model_type = model.get_model_type()
        task_status = request.get_task_status()
        execution_button = request.get_execution_button()
        
        # モデル登録待ち状態以外ではモデルの登録はしない
        if task_status.get_status() is not Status.WAITING_FOR_MODEL_SUBMIT:
            return
        
        # モデルの種類を判別して、ステータスにモデルをセット
        if model_type is ModelType.HUMANOID:
            task_status.set_humanoid(model)
        else:
            task_status.set_accessory(model)

        # 実行待ち状態になったら実行ボタンを有効にする
        if task_status.get_status() is Status.WAITING_FOR_EXECUTION:
            execution_button.setActive(True)