import tkinter as tk
from typing import Optional, List
from core.interfaces.reader_interface import IReader
from core.events.event_manager import EventManager

class MainInterface(IReader):
    """主界面类"""
    
    def __init__(self):
        self.window = tk.Tk()
        
    def set_transparency(self, value: float) -> None:
        """设置窗口透明度"""
        self.window.attributes('-alpha', value)
        
    def toggle_topmost(self, topmost: bool) -> None:
        """切换窗口置顶状态"""
        self.window.attributes('-topmost', topmost)
        
    def toggle_visibility(self, visible: bool) -> None:
        """切换窗口可见性"""
        if visible:
            self.window.deiconify()
        else:
            self.window.withdraw()
        self.window.title("小说阅读器")
        self.window.geometry("800x600")
        
        # 初始化事件管理器
        self.event_manager = EventManager(self, None)
        
        # 初始化界面
        self.init_ui()
        
    def init_ui(self):
        """初始化主界面"""
        # 菜单栏
        self.menu_bar = tk.Menu(self.window)
        
        # 文件菜单
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="打开", command=self._on_open_file)
        file_menu.add_command(label="退出", command=self.window.quit)
        self.menu_bar.add_cascade(label="文件", menu=file_menu)
        
        # 阅读菜单
        read_menu = tk.Menu(self.menu_bar, tearoff=0)
        read_menu.add_command(label="开始阅读", command=self._on_start_reading)
        read_menu.add_command(label="暂停阅读", command=self._on_pause_reading)
        read_menu.add_command(label="恢复阅读", command=self._on_resume_reading)
        self.menu_bar.add_cascade(label="阅读", menu=read_menu)
        
        self.window.config(menu=self.menu_bar)
        
    def _on_open_file(self):
        """处理打开文件事件"""
        # TODO: 实现文件选择对话框
        file_path = "example.txt"  # 临时示例路径
        self.event_manager.trigger_event(
            "file_opened",
            file_path
        )
        
    def _on_start_reading(self):
        """处理开始阅读事件"""
        self.event_manager.trigger_event("reading_started")
        
    def _on_pause_reading(self):
        """处理暂停阅读事件"""
        self.event_manager.trigger_event("reading_paused")
        
    def _on_resume_reading(self):
        """处理恢复阅读事件"""
        self.event_manager.trigger_event("reading_resumed")
        
    # IReader接口实现
    def open_file(self, file_path: str) -> bool:
        """打开文件"""
        # TODO: 实现文件打开逻辑
        return True
        
    def get_content(self) -> str:
        """获取当前内容"""
        # TODO: 实现内容获取逻辑
        return ""
        
    def save_progress(self) -> None:
        """保存阅读进度"""
        # TODO: 实现进度保存逻辑
        pass
        
    def load_progress(self) -> int:
        """加载阅读进度"""
        # TODO: 实现进度加载逻辑
        return 0
        
    def get_file_history(self) -> List[str]:
        """获取文件历史记录"""
        # TODO: 实现历史记录获取逻辑
        return []
        
    def run(self):
        """运行主循环"""
        self.window.mainloop()
