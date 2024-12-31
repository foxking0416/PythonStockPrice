import unittest
from PySide6.QtWidgets import QApplication
from StockPriceMainWindow import MainWindow  # 假設你的主程式檔名是 main.py
from StockPriceMainWindow import TradingType
from StockPriceMainWindow import TradingData

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
        self.window = MainWindow( True, 
                                  'UnitTestData\\TradingDataUnitTest.json',
                                  'UnitTestData\\UISetting.config',
                                  'UnitTestData\\StockNumber.txt',
                                  'UnitTestData\\StockPrice.txt' )
        
        self.assertEqual( self.window.windowTitle(), "MainWindow" )
        self.window.close()

    def test_window_visible(self):
        """測試主窗口是否可見"""
        self.window = MainWindow( True, 
                                  'UnitTestData\\TradingDataUnitTest.json',
                                  'UnitTestData\\UISetting.config',
                                  'UnitTestData\\StockNumber.txt',
                                  'UnitTestData\\StockPrice.txt' )
        self.window.show()
        self.assertTrue( self.window.isVisible() )
        self.window.close()

    def test_current_inventory(self):
        self.window = MainWindow( True, 
                                  'UnitTestData\\TradingDataUnitTest.json',
                                  'UnitTestData\\UISetting.config',
                                  'UnitTestData\\StockNumber.txt',
                                  'UnitTestData\\StockPrice.txt' )
        self.assertEqual( self.window.ui.qtTabWidget.count(), 2 )

        for key, value_dict_per_account_all_stock_trading_data in self.window.dict_all_account_all_stock_trading_data.items():
            self.assertEqual( key, 'TabIndex0' )
            for key_stock_number, value_dict_per_stock_trading_data in value_dict_per_account_all_stock_trading_data.items():
                if key_stock_number == '1216':# 統一
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 1942311 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 30000 )
                elif key_stock_number == '0056':# 元大高股息
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 1584469 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 100000 )
                elif key_stock_number == '00679B':# 元大美債
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 13998309 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 500000 )
                elif key_stock_number == '6505':# 台塑化
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 1256841 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 20000 )
                elif key_stock_number == '2535':# 達欣工
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 4901428 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 400000 )
                elif key_stock_number == '2834':# 台企銀
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 55691180 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 5458985 )
                elif key_stock_number == '2884':# 玉山銀
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 11514031 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 525958 )
                elif key_stock_number == '2887':# 台新金
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 11163223 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 919826 )
                elif key_stock_number == '5410':# 國眾
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 431634 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 103000 )
                elif key_stock_number == '5864':# 致和證
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 4376129 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 214194 )
                elif key_stock_number == '5706':# 鳳凰
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], -6550227 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 0 )
                elif key_stock_number == '9933':# 中鼎
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], 556472 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 120000 )
                elif key_stock_number == '00916':# 國泰全球品牌50
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], -2446753 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 0 )
                elif key_stock_number == '00893':# 國泰智能車
                    dict_trading_data_last = value_dict_per_stock_trading_data[ len( value_dict_per_stock_trading_data ) - 1 ]
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_COST_NON_SAVE ], -4422255 )
                    self.assertEqual( dict_trading_data_last[ TradingData.ACCUMULATED_INVENTORY_NON_SAVE ], 0 )

        self.window.close()



if __name__ == "__main__":
        unittest.main()