import unittest
from PySide6.QtWidgets import QApplication
from StockPriceMainWindow import MainWindow  # 假設你的主程式檔名是 main.py

class TestMainWindow( unittest.TestCase ):
    @classmethod
    def setUpClass(cls):
        """創建 QApplication 以便測試"""
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        """清理 QApplication"""
        cls.app.quit()

    def test_window_title(self):
        """測試主窗口標題是否正確"""
        self.window = MainWindow( False, 'TradingDataUnitTest.json' )
        self.assertEqual( self.window.windowTitle(), "MainWindow" )
        self.window.close()

    def test_window_visible(self):
        """測試主窗口是否可見"""
        self.window = MainWindow( False, 'TradingDataUnitTest.json' )
        self.window.show()
        self.assertTrue( self.window.isVisible() )
        self.window.close()

    def test_tab_widget_count(self):
        self.window = MainWindow( False, 'TradingDataUnitTest.json' )
        self.assertEqual( self.window.ui.qtTabWidget.count(), 3 )
        self.window.close()



if __name__ == "__main__":
    unittest.main()