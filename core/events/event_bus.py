from typing import Callable, Dict, List
from .event_types import EventTypes

class EventBus:
    """事件总线实现"""
    def __init__(self):
        self._handlers: Dict[str, List[Callable]] = {}

    def register(self, event_type: str, handler: Callable):
        """注册事件处理器"""
        if event_type not in self._handlers:
            self._handlers[event_type] = []
        self._handlers[event_type].append(handler)

    def emit(self, event_type: str, *args, **kwargs):
        """触发事件"""
        if event_type in self._handlers:
            for handler in self._handlers[event_type]:
                try:
                    handler(*args, **kwargs)
                except Exception as e:
                    print(f"Error handling event {event_type}: {str(e)}")

    def unregister(self, event_type: str, handler: Callable):
        """注销事件处理器"""
        if event_type in self._handlers:
            self._handlers[event_type] = [
                h for h in self._handlers[event_type] if h != handler
            ]
