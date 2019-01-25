from Base.base import Base
import Page


class SearchSmsPage(Base):

    # 继承父类的方法
    def __init__(self, driver):
        Base.__init__(self, driver)