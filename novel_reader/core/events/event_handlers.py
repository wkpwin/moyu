from typing import Any
from core.events.event_types import EventType

class EventHandlers:
    """事件处理器"""
    
    def __init__(self):
        self.main_interface = None
        self.reading_area = None
        
    def register_components(self, main_interface, reading_area):
        """注册组件"""
        self.main_interface = main_interface
        self.reading_area = reading_area
        
    def handle_file_opened(self, *args: Any, **kwargs: Any) -> None:
        """处理文件打开事件"""
        if self.main_interface:
            self.main_interface.update_file_info(*args, **kwargs)
            
    def handle_progress_updated(self, *args: Any, **kwargs: Any) -> None:
        """处理进度更新事件"""
        if self.reading_area:
            self.reading_area.update_progress(*args, **kwargs)
            
    def handle_window_toggled(self, *args: Any, **kwargs: Any) -> None:
        """处理窗口切换事件"""
        if self.main_interface:
            self.main_interface.toggle_window(*args, **kwargs)
            
    def handle_transparency_changed(self, *args: Any, **kwargs: Any) -> None:
        """处理透明度改变事件"""
        if self.main_interface:
            self.main_interface.change_transparency(*args, **kwargs)
            
    def handle_reading_started(self, *args: Any, **kwargs: Any) -> None:
        """处理开始阅读事件"""
        if self.reading_area:
            self.reading_area.start_reading(*args, **kwargs)
            
    def handle_reading_paused(self, *args: Any, **kwargs: Any) -> None:
        """处理暂停阅读事件"""
        if self.reading_area:
            self.reading_area.pause_reading(*args, **kwargs)
            
    def handle_reading_resumed(self, *args: Any, **kwargs: Any) -> None:
        """处理继续阅读事件"""
        if self.reading_area:
            self.reading_area.resume_reading(*args, **kwargs)
            
    def handle_reading_finished(self, *args: Any, **kwargs: Any) -> None:
        """处理完成阅读事件"""
        if self.reading_area:
            self.reading_area.finish_reading(*args, **kwargs)
