from abc import ABC, abstractmethod
from typing import Any

class IEvent(ABC):
    """事件接口"""
    
    @abstractmethod
    def trigger_event(self, event_type: str, *args: Any, **kwargs: Any) -> None:
        """触发事件"""
        pass
        
    @abstractmethod
    def has_event(self, event_type: str) -> bool:
        """检查是否存在指定类型的事件处理函数"""
        pass

class IEventHandler(ABC):
    """事件处理器接口"""
    
    @abstractmethod
    def handle_file_opened(self, *args: Any, **kwargs: Any) -> None:
        """处理文件打开事件"""
        pass
        
    @abstractmethod
    def handle_progress_updated(self, *args: Any, **kwargs: Any) -> None:
        """处理进度更新事件"""
        pass
        
    @abstractmethod
    def handle_window_toggled(self, *args: Any, **kwargs: Any) -> None:
        """处理窗口切换事件"""
        pass
        
    @abstractmethod
    def handle_transparency_changed(self, *args: Any, **kwargs: Any) -> None:
        """处理透明度改变事件"""
        pass
        
    @abstractmethod
    def handle_reading_started(self, *args: Any, **kwargs: Any) -> None:
        """处理开始阅读事件"""
        pass
        
    @abstractmethod
    def handle_reading_paused(self, *args: Any, **kwargs: Any) -> None:
        """处理暂停阅读事件"""
        pass
        
    @abstractmethod
    def handle_reading_resumed(self, *args: Any, **kwargs: Any) -> None:
        """处理继续阅读事件"""
        pass
        
    @abstractmethod
    def handle_reading_finished(self, *args: Any, **kwargs: Any) -> None:
        """处理完成阅读事件"""
        pass
