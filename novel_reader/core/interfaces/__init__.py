# 接口模块初始化文件
from .reader_interface import IReader
from .event_interface import IEvent, IEventHandler

__all__ = ['IReader', 'IEventHandler']
