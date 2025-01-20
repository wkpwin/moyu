from typing import Dict, List, Callable, Any
from core.interfaces.event_interface import IEventHandler

class EventBus(IEventHandler):
    """事件总线实现类"""
    
    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}
        
    def register_event(self, event_type: str, handler: Callable) -> None:
        """注册事件处理函数"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)
        
    def unregister_event(self, event_type: str, handler: Callable) -> None:
        """注销事件处理函数"""
        if event_type in self._handlers:
            self._handlers[event_type] = [
                h for h in self._handlers[event_type] if h != handler
            ]
            
    def trigger_event(self, event_type: str, *args: Any, **kwargs: Any) -> None:
        """触发事件"""
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                try:
                    handler(*args, **kwargs)
                except Exception as e:
                    print(f"事件处理出错：{e}")
                    
    def has_event(self, event_type: str) -> bool:
        """检查是否存在指定类型的事件处理函数"""
        return event_type in self._handlers and len(self._handlers[event_type]) > 0

    # IEventHandler接口实现
    def handle_file_opened(self, file_path: str) -> None:
        """处理文件打开事件"""
        self.trigger_event("file_opened", file_path)
        
    def handle_progress_updated(self, progress: int) -> None:
        """处理进度更新事件"""
        self.trigger_event("progress_updated", progress)
        
    def handle_reading_finished(self) -> None:
        """处理阅读完成事件"""
        self.trigger_event("reading_finished")
        
    def handle_reading_paused(self) -> None:
        """处理阅读暂停事件"""
        self.trigger_event("reading_paused")
        
    def handle_reading_resumed(self) -> None:
        """处理阅读恢复事件"""
        self.trigger_event("reading_resumed")
        
    def handle_reading_started(self) -> None:
        """处理阅读开始事件"""
        self.trigger_event("reading_started")
        
    def handle_transparency_changed(self, value: float) -> None:
        """处理透明度改变事件"""
        self.trigger_event("transparency_changed", value)
        
    def handle_window_toggled(self, visible: bool) -> None:
        """处理窗口切换事件"""
        self.trigger_event("window_toggled", visible)
