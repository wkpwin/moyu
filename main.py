from core.events.event_bus import EventBus
from core.objects.main_interface import MainInterface
from core.objects.reading_area import ReadingArea
from core.objects.floating_ball import FloatingBall
from core.communication.file_transfer import FileTransfer

def main():
    # 初始化事件总线
    event_bus = EventBus()
    
    # 初始化文件传输模块
    file_transfer = FileTransfer(event_bus)
    
    # 初始化主界面
    main_interface = MainInterface(event_bus)
    
    # 初始化阅读区域
    reading_area = ReadingArea(event_bus)
    
    # 初始化悬浮球
    floating_ball = FloatingBall(event_bus)
    
    # 启动主界面
    main_interface.run()

if __name__ == "__main__":
    main()
