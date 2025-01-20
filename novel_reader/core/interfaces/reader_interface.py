from abc import ABC, abstractmethod

class IReader(ABC):
    """阅读器核心功能接口"""
    
    @abstractmethod
    def open_file(self, file_path: str) -> bool:
        """打开文件并加载内容"""
        pass
    
    @abstractmethod
    def get_content(self) -> str:
        """获取当前阅读内容"""
        pass
    
    @abstractmethod
    def save_progress(self) -> None:
        """保存阅读进度"""
        pass
    
    @abstractmethod
    def load_progress(self) -> int:
        """加载阅读进度"""
        pass
    
    @abstractmethod
    def get_file_history(self) -> list:
        """获取文件历史记录"""
        pass
    
    @abstractmethod
    def set_transparency(self, value: float) -> None:
        """设置阅读区域透明度"""
        pass
    
    @abstractmethod
    def toggle_visibility(self) -> None:
        """切换阅读区域可见性"""
        pass
    
    @abstractmethod
    def toggle_topmost(self) -> None:
        """切换窗口置顶状态"""
        pass
