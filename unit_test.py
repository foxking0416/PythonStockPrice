import unittest
from PySide6.QtWidgets import QApplication
from StockPriceMainWindow import MainWindow  # 假設你的主程式檔名是 main.py

class TestMainWindow( unittest.TestCase ):
    @classmethod
    def setUpClass(cls):
        """創建 QApplication 以便測試"""
        cls.app = QApplication([])

    def setUp(self):
        """在每個測試方法之前執行"""
        self.window = MainWindow( False)

    def tearDown(self):
        """在每個測試方法之後執行"""
        self.window.close()

    @classmethod
    def tearDownClass(cls):
        """清理 QApplication"""
        cls.app.quit()

    def test_window_title(self):
        """測試主窗口標題是否正確"""
        self.assertEqual(self.window.windowTitle(), "MainWindow")

    def test_window_visible(self):
        """測試主窗口是否可見"""
        self.window.show()
        self.assertTrue(self.window.isVisible())



if __name__ == "__main__":
    unittest.main()