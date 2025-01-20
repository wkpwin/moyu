from core.objects.main_interface import MainInterface
from core.objects.reading_area import ReadingArea
from core.objects.floating_ball import FloatingBall
from core.events.event_manager import EventManager

def main():
    # 初始化主界面
    main_interface = MainInterface()
    
    # 初始化阅读区域
    reading_area = ReadingArea(main_interface.window)
    
    # 初始化悬浮球
    floating_ball = FloatingBall(main_interface.window)
    
    # 初始化事件管理器
    event_manager = EventManager()
    
    # 注册组件到事件处理器
    event_manager.event_handlers.register_components(
        main_interface,
        reading_area
    )
    
    # 运行主界面
    main_interface.run()

if __name__ == "__main__":
    main()
