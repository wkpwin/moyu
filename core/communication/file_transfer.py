from core.events.event_bus import EventBus

class FileTransfer:
    def __init__(self, event_bus: EventBus):
        self.event_bus = event_bus
        self._register_handlers()

    def _register_handlers(self):
        """注册事件处理器"""
        self.event_bus.register('file_selected', self.handle_file_selected)

    def handle_file_selected(self, file_path: str):
        """处理文件选择事件"""
        try:
            content = self._read_file(file_path)
            self.event_bus.emit('file_content_loaded', content)
        except Exception as e:
            self.event_bus.emit('file_load_error', str(e))

    def _read_file(self, file_path: str) -> str:
        """读取文件内容"""
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
