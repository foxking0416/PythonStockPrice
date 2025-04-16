import unittest
from PySide6.QtWidgets import QApplication
from StockPriceMainWindow import (
    MainWindow, TradingType, TradingPriceType, TradingFeeType,
    DividendValueType, CapitalReductionType, TradingData,
    TradingCost, TransferType, TransferData
)

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def create_window(self, trading_file):
        return MainWindow(
            True,
            f'UnitTestData\\{trading_file}',
            'UnitTestData\\UISetting.config',
            'UnitTestData\\StockNumber.txt',
            'UnitTestData\\SuspendStockNumber.txt',
            'UnitTestData\\StockPrice.txt'
        )

    def assert_data_loaded_and_verified(self, data_dict, stock_number, expected_cost, expected_inventory):
        self.assertTrue(data_dict, "交易資料為空，無法測試")
        found = False
        for account_key, stock_dict in data_dict.items():
            for stock_num, records in stock_dict.items():
                if stock_num == stock_number:
                    found = True
                    last = records[-1]
                    self.assertEqual(last[TradingData.ACCUMULATED_COST_NON_SAVE], expected_cost)
                    self.assertEqual(last[TradingData.ACCUMULATED_QUANTITY_NON_SAVE], expected_inventory)
        self.assertTrue(found, f"未找到股票編號 {stock_number} 的資料")

    def test_window_title(self):
        self.window = self.create_window('TradingDataUnitTest.json')
        self.assertEqual(self.window.windowTitle(), "股票交易紀錄")
        self.window.close()

    def test_window_visible(self):
        self.window = self.create_window('TradingDataUnitTest.json')
        self.window.show()
        self.assertTrue(self.window.isVisible())
        self.window.close()

    def test_current_inventory(self):
        self.window = self.create_window('TradingDataUnitTest.json')
        self.assertEqual(self.window.ui.qtTabWidget.count(), 2)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '1216', 1942311, 30000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '0056', 1584469, 100000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '00679B', 13998309, 500000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '6505', 1256841, 20000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2535', 4901428, 400000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 55691180, 5458985)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2884', 11514031, 525958)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2887', 11163223, 919826)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '5410', 431634, 103000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '5864', 4376129, 214194)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '5706', -6550227, 0)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '9933', 556472, 120000)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '00916', -2446753, 0)
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '00893', -4422255, 0)
        self.window.close()

    def test_add_new_tab(self):
        self.window = self.create_window('TradingDataUnitTest.json')
        str_tab_name = self.window.add_new_tab_and_table()
        self.window.dict_all_account_all_stock_trading_data[str_tab_name] = {}
        self.window.dict_all_account_ui_state[str_tab_name] = {
            "discount_checkbox": True,
            "discount_value": 0.6,
            "insurance_checkbox": False,
            "regular_buy_trading_price_type": TradingPriceType.PER_SHARE,
            "regular_buy_trading_fee_type": TradingFeeType.VARIABLE,
            "regular_buy_trading_fee_minimum": 1,
            "regular_buy_trading_fee_constant": 1
        }
        self.window.dict_all_account_general_data[str_tab_name] = {
            "minimum_common_trading_fee": 20,
            "minimum_odd_trading_fee": 1,
            "dividend_transfer_fee": {}
        }
        self.window.dict_all_account_cash_transfer_data[str_tab_name] = []
        self.assertEqual(self.window.ui.qtTabWidget.count(), 3)

    def test_current_inventory1(self):
        self.window = self.create_window('TradingDataUnitTest_匯費10_最低手續費20_不扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9251865, 1285472)
        self.window.close()

    def test_current_inventory2(self):
        self.window = self.create_window('TradingDataUnitTest_匯費10_最低手續費20_扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9326671, 1285472)
        self.window.close()

    def test_current_inventory3(self):
        self.window = self.create_window('TradingDataUnitTest_匯費5_最低手續費20_不扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9251840, 1285472)
        self.window.close()

    def test_current_inventory4(self):
        self.window = self.create_window('TradingDataUnitTest_匯費5_最低手續費20_不扣補充保費_自訂每股股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9008555, 1100000)
        self.window.close()

    def test_current_inventory5(self):
        self.window = self.create_window('TradingDataUnitTest_匯費5_最低手續費20_不扣補充保費_自訂總股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9998555, 1010000)
        self.window.close()

    def test_current_inventory6(self):
        self.window = self.create_window('TradingDataUnitTest_最低手續費0.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 10008, 1000)
        self.window.close()

    def test_current_inventory7(self):
        self.window = self.create_window('TradingDataUnitTest_最低手續費15.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 10015, 1000)
        self.window.close()

    def test_current_inventory8(self):
        self.window = self.create_window('TradingDataUnitTest_匯費5_最低手續費20_扣補充保費_自訂總股利_自訂補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 90590, 20000)
        self.window.close()

    def test_current_inventory9(self):
        self.window = self.create_window('TradingDataUnitTest_手動輸入股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9008560, 1100000)
        self.window.close()

    def test_current_inventory10(self):
        self.window = self.create_window('TradingDataUnitTest_手動輸入加自動帶入股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 8176203, 1414019)
        self.window.close()

if __name__ == "__main__":
    unittest.main()
