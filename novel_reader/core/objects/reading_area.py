import tkinter as tk
from typing import Optional, List
from core.interfaces.reader_interface import IReader

class ReadingArea(IReader):
    """阅读区域实现类"""
    
    def __init__(self, parent: Optional[tk.Toplevel] = None):
        self.parent = parent
        self.window = tk.Toplevel(parent) if parent else tk.Tk()
        self.window.title("阅读区域")
        self.window.geometry("600x400")
        self.window.attributes("-alpha", 1.0)
        self.window.attributes("-topmost", True)
        
        # 初始化界面
        self.init_ui()
        
    def init_ui(self):
        """初始化阅读区域界面"""
        # 文本显示区域
        self.text_area = tk.Text(
            self.window,
            wrap="word",
            font=("宋体", 12),
            spacing1=5,
            spacing2=5,
            spacing3=5
        )
        self.text_area.pack(expand=True, fill="both")
        
        # 滚动条
        scrollbar = tk.Scrollbar(self.text_area)
        scrollbar.pack(side="right", fill="y")
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)
        
    def set_transparency(self, value: float) -> None:
        """设置透明度"""
        self.window.attributes("-alpha", value)
        
    def toggle_visibility(self) -> None:
        """切换可见性"""
        if self.window.state() == "normal":
            self.window.withdraw()
        else:
            self.window.deiconify()
            
    def toggle_topmost(self) -> None:
        """切换置顶状态"""
        current = self.window.attributes("-topmost")
        self.window.attributes("-topmost", not current)
        
    # IReader接口实现
    def open_file(self, file_path: str) -> bool:
        """打开文件"""
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                content = f.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", content)
            return True
        except Exception as e:
            print(f"打开文件失败：{e}")
            return False
            
    def get_content(self) -> str:
        """获取当前内容"""
        return self.text_area.get("1.0", "end-1c")
        
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
