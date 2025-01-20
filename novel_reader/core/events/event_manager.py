from typing import Any
from core.events.event_bus import EventBus
from core.events.event_handlers import EventHandlers
from core.events.event_types import EventType

class EventManager:
    """事件管理器"""
    
    def __init__(self):
        self.event_bus = EventBus()
        self.event_handlers = EventHandlers()
        self._register_handlers()
        
    def _register_handlers(self) -> None:
        """注册事件处理函数"""
        # 文件相关事件
        self.event_bus.register_event(
            EventType.FILE_OPENED.value,
            self.event_handlers.handle_file_opened
        )
        
        # 进度相关事件
        self.event_bus.register_event(
            EventType.PROGRESS_UPDATED.value,
            self.event_handlers.handle_progress_updated
        )
        
        # 界面相关事件
        self.event_bus.register_event(
            EventType.WINDOW_TOGGLED.value,
            self.event_handlers.handle_window_toggled
        )
        self.event_bus.register_event(
            EventType.TRANSPARENCY_CHANGED.value,
            self.event_handlers.handle_transparency_changed
        )
        
        # 阅读相关事件
        self.event_bus.register_event(
            EventType.READING_STARTED.value,
            self.event_handlers.handle_reading_started
        )
        self.event_bus.register_event(
            EventType.READING_PAUSED.value,
            self.event_handlers.handle_reading_paused
        )
        self.event_bus.register_event(
            EventType.READING_RESUMED.value,
            self.event_handlers.handle_reading_resumed
        )
        self.event_bus.register_event(
            EventType.READING_FINISHED.value,
            self.event_handlers.handle_reading_finished
        )
        
    def trigger_event(self, event_type: str, *args: Any, **kwargs: Any) -> None:
        """触发事件"""
        self.event_bus.trigger_event(event_type, *args, **kwargs)
        
    def has_event(self, event_type: str) -> bool:
        """检查是否存在指定类型的事件处理函数"""
        return self.event_bus.has_event(event_type)
