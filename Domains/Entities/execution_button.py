class ExecutionButton():
    """実行ボタン
    """
    
    _is_active:bool
    """ボタンの有効状態
    """
    
    def get_active(self) -> bool:
        """ボタンの有効状態のゲッター

        Returns:
            bool: ボタンの有効状態
        """
        return self._is_active
    
    def set_active(self, active: bool):
        """ボタンの有効状態のセッター

        Args:
            active (bool): ボタンの有効状態
        """
        self._is_active = active