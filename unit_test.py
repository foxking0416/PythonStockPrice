import unittest
from StockPriceMainWindow import StockTradingEditDialog  # 加在原 import 區塊
from PySide6.QtWidgets import QApplication, QDialog, QTableView
from PySide6.QtCore import Qt
from StockPriceMainWindow import (
    MainWindow, TradingType, TradingPriceType, TradingFeeType,
    DividendValueType, CapitalReductionType, TradingData,
    TradingCost, TransferType, TransferData
)

class TestStockTradingEditDialog(unittest.TestCase):
    def setUp(self):
        self.dialog = StockTradingEditDialog(
            str_stock_number="2330",
            str_stock_name="台積電",
            b_etf=False,
            b_discount=True,
            f_discount_value=0.6,
            n_minimum_common_trading_fee=20,
            n_minimum_odd_trading_fee=1
        )

    def test_dialog_accepts_input_and_returns_data(self):
        # 模擬設定資料
        self.dialog.setup_trading_type(TradingType.BUY)
        self.dialog.setup_trading_count(1000)
        self.dialog.setup_trading_price(500)
        self.dialog.setup_trading_discount(0.6)
        self.dialog.setup_daying_trading(False)

        # 點擊「確認」
        self.dialog.ui.qtOkPushButton.click()

        self.assertEqual(self.dialog.result(), QDialog.Accepted)
        data = self.dialog.dict_trading_data
        self.assertEqual(data[TradingData.TRADING_TYPE], TradingType.BUY)
        self.assertEqual(data[TradingData.PER_SHARE_TRADING_PRICE], 500)
        self.assertEqual(data[TradingData.TRADING_QUANTITY], 1000)
        self.assertAlmostEqual(data[TradingData.TRADING_FEE_DISCOUNT], 0.6)

    def test_dialog_reject_should_not_have_data(self):
        self.dialog.ui.qtCancelPushButton.click()
        self.assertEqual(self.dialog.result(), QDialog.Rejected)
        self.assertEqual(self.dialog.dict_trading_data, {})

class TestMainWindow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.app = QApplication([])

    @classmethod
    def tearDownClass(cls):
        cls.app.quit()

    def create_window(self, trading_file, ui_setting_file = "UISetting.config", stock_price_file = "StockPrice.txt"):
        return MainWindow(
            True,
            f'UnitTestData\\{trading_file}',
            f'UnitTestData\\{ui_setting_file}',
            'UnitTestData\\StockNumber.txt',
            'UnitTestData\\SuspendStockNumber.txt',
            f'UnitTestData\\{stock_price_file}',
            'UnitTestData\\PreStockPrice.txt',
            'UnitTestData\\StockDividendPositionDate.json'
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

    def assert_data_loaded_and_verified2(self, data_dict, stock_number, expected_cost, expected_inventory):
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
        self.window = self.create_window('TradingDataUnitTest_#1_匯費10_最低手續費20_不扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9251865, 1285472)
        self.window.close()

    def test_current_inventory2(self):
        self.window = self.create_window('TradingDataUnitTest_#2_匯費10_最低手續費20_扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9326671, 1285472)
        self.window.close()

    def test_current_inventory3(self):
        self.window = self.create_window('TradingDataUnitTest_#3_匯費5_最低手續費20_不扣補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9251840, 1285472)
        self.window.close()

    def test_current_inventory4(self):
        self.window = self.create_window('TradingDataUnitTest_#4_匯費5_最低手續費20_不扣補充保費_自訂每股股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9008555, 1100000)
        self.window.close()

    def test_current_inventory5(self):
        self.window = self.create_window('TradingDataUnitTest_#5_匯費5_最低手續費20_不扣補充保費_自訂總股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9998555, 1010000)
        self.window.close()

    def test_current_inventory6(self):
        self.window = self.create_window('TradingDataUnitTest_#6_最低手續費0.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 10008, 1000)
        self.window.close()

    def test_current_inventory7(self):
        self.window = self.create_window('TradingDataUnitTest_#7_最低手續費15.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 10015, 1000)
        self.window.close()

    def test_current_inventory8(self):
        self.window = self.create_window('TradingDataUnitTest_#8_匯費5_最低手續費20_扣補充保費_自訂總股利_自訂補充保費.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 90590, 20000)
        self.window.close()

    def test_current_inventory9(self):
        self.window = self.create_window('TradingDataUnitTest_#9_手動輸入股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 9008560, 1100000)
        self.window.close()

    def test_current_inventory10(self):
        self.window = self.create_window('TradingDataUnitTest_#10_手動輸入加自動帶入股利.json')
        self.assert_data_loaded_and_verified(self.window.dict_all_account_all_stock_trading_data, '2834', 8176203, 1414019)
        self.window.close()

    def test_current_inventory11(self): #測試自訂欄位
        self.window = self.create_window('TradingDataUnitTest_#11_已實現未實現.json', "UISetting.config", "StockPrice_20250416.txt")

        # 刷新 QTableView 的資料
        self.window.refresh_stock_list_table( clear_table = True )

        # 抓出第一個 tab 的 QTableView 與 model
        first_tab_widget = self.window.ui.qtTabWidget.widget( 0 )
        qt_table_view = first_tab_widget.findChild( QTableView, "StockListTableView" )
        qt_model = qt_table_view.model()
        header_labels = [ qt_model.headerData(i, Qt.Horizontal) for i in range(qt_model.columnCount()) ]
        
        self.assertEqual( header_labels[ 0 ], '股票代碼及名稱')
        self.assertEqual( header_labels[ 1 ], '04/16 收盤價')
        self.assertEqual( header_labels[ 2 ], '庫存股數')
        self.assertEqual( header_labels[ 3 ], '市值')
        self.assertEqual( header_labels[ 4 ], '現股成本')
        self.assertEqual( header_labels[ 5 ], '未實現損益')
        self.assertEqual( header_labels[ 6 ], '未實現報酬率')
        self.assertEqual( header_labels[ 7 ], '已實現損益')
        self.assertEqual( header_labels[ 8 ], '損益平衡價')
        self.assertEqual( header_labels[ 9 ], '累計成本\n(不含息)')
        self.assertEqual( header_labels[ 10 ], '累計平均成本\n(不含息)')
        self.assertEqual( header_labels[ 11 ], '累計損益\n(不含息)')
        self.assertEqual( header_labels[ 12 ], '累計手續費')
        self.assertEqual( header_labels[ 13 ], '累計交易稅')
        self.assertEqual( header_labels[ 14 ], '累計股利所得')
        self.assertEqual( header_labels[ 15 ], '平均年化報酬率')
        self.assertEqual( header_labels[ 16 ], '持股淨值比')
        self.assertEqual( header_labels[ 17 ], '自動帶入股利')
        self.assertEqual( header_labels[ 18 ], '匯出')
        self.assertEqual( header_labels[ 19 ], '刪除')
        
        self.assertEqual( qt_model.columnCount(), 20 )
        self.assertEqual( qt_model.rowCount(), 16 )

        self.assertEqual( qt_model.item(  0, 0 ).text(), "0050 元大台灣50")
        self.assertEqual( qt_model.item(  1, 0 ).text(), "0056 元大高股息")
        self.assertEqual( qt_model.item(  2, 0 ).text(), "006208 富邦台50")
        self.assertEqual( qt_model.item(  3, 0 ).text(), "00878 國泰永續高股息")
        self.assertEqual( qt_model.item(  4, 0 ).text(), "2330 台積電")
        self.assertEqual( qt_model.item(  5, 0 ).text(), "2809 京城銀")
        self.assertEqual( qt_model.item(  6, 0 ).text(), "2834 臺企銀")
        self.assertEqual( qt_model.item(  7, 0 ).text(), "2887 台新金")
        self.assertEqual( qt_model.item(  8, 0 ).text(), "2888 新光金")
        self.assertEqual( qt_model.item(  9, 0 ).text(), "2891 中信金")
        self.assertEqual( qt_model.item( 10, 0 ).text(), "4104 佳醫")
        self.assertEqual( qt_model.item( 11, 0 ).text(), "8112 至上")
        self.assertEqual( qt_model.item( 12, 0 ).text(), "1570 力肯")
        self.assertEqual( qt_model.item( 13, 0 ).text(), "3293 鈊象")
        self.assertEqual( qt_model.item( 14, 0 ).text(), "5864 致和證")
        self.assertEqual( qt_model.item( 15, 0 ).text(), "6882 甲尚")

        #庫存股數
        self.assertEqual( qt_model.item(  0, 2 ).text(), "944") #元大台灣50
        self.assertEqual( qt_model.item(  1, 2 ).text(), "4,812") #元大高股息
        self.assertEqual( qt_model.item(  2, 2 ).text(), "1,861") #富邦台50
        self.assertEqual( qt_model.item(  3, 2 ).text(), "5,961") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 2 ).text(), "100") #台積電
        self.assertEqual( qt_model.item(  5, 2 ).text(), "1,000") #京城銀
        self.assertEqual( qt_model.item(  6, 2 ).text(), "11,230") #臺企銀
        self.assertEqual( qt_model.item(  7, 2 ).text(), "25,629") #台新金
        self.assertEqual( qt_model.item(  8, 2 ).text(), "1,000") #新光金
        self.assertEqual( qt_model.item(  9, 2 ).text(), "37,501") #中信金
        self.assertEqual( qt_model.item( 10, 2 ).text(), "10,459") #佳醫
        self.assertEqual( qt_model.item( 11, 2 ).text(), "11,000") #至上
        self.assertEqual( qt_model.item( 12, 2 ).text(), "4,000") #力肯
        self.assertEqual( qt_model.item( 13, 2 ).text(), "50") #鈊象
        self.assertEqual( qt_model.item( 14, 2 ).text(), "28,323") #致和證
        self.assertEqual( qt_model.item( 15, 2 ).text(), "1,000") #甲尚

        #市值
        n_total_market_value = 0
        list_str_cost = [ "153,258", "158,074", "176,981", "119,160", "85,500", "47,600", "156,658", "406,220", "11,200", "1,415,663", "920,392", "562,100", "90,400", "40,700", "355,454", "18,000" ]
        for i in range( 16 ):
            self.assertEqual( qt_model.item( i, 3 ).text(), list_str_cost[ i ] )
            n_total_market_value += int( qt_model.item( i, 3 ).text().replace( ",", "" ) )
        self.assertEqual( n_total_market_value, 4717360 )
        self.assertEqual( qt_model.item(  0, 3 ).text(), "153,258") #元大台灣50
        self.assertEqual( qt_model.item(  1, 3 ).text(), "158,074") #元大高股息
        self.assertEqual( qt_model.item(  2, 3 ).text(), "176,981") #富邦台50
        self.assertEqual( qt_model.item(  3, 3 ).text(), "119,160") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 3 ).text(), "85,500") #台積電
        self.assertEqual( qt_model.item(  5, 3 ).text(), "47,600") #京城銀
        self.assertEqual( qt_model.item(  6, 3 ).text(), "156,658") #臺企銀
        self.assertEqual( qt_model.item(  7, 3 ).text(), "406,220") #台新金
        self.assertEqual( qt_model.item(  8, 3 ).text(), "11,200") #新光金
        self.assertEqual( qt_model.item(  9, 3 ).text(), "1,415,663") #中信金
        self.assertEqual( qt_model.item( 10, 3 ).text(), "920,392") #佳醫
        self.assertEqual( qt_model.item( 11, 3 ).text(), "562,100") #至上
        self.assertEqual( qt_model.item( 12, 3 ).text(), "90,400") #力肯
        self.assertEqual( qt_model.item( 13, 3 ).text(), "40,700") #鈊象
        self.assertEqual( qt_model.item( 14, 3 ).text(), "355,454") #致和證
        self.assertEqual( qt_model.item( 15, 3 ).text(), "18,000") #甲尚

        #現股成本
        self.assertEqual( qt_model.item(  0, 4 ).text(), "180.53") #元大台灣50
        self.assertEqual( qt_model.item(  1, 4 ).text(), "32.57") #元大高股息
        self.assertEqual( qt_model.item(  2, 4 ).text(), "109.54") #富邦台50
        self.assertEqual( qt_model.item(  3, 4 ).text(), "19.92") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 4 ).text(), "920.78") #台積電
        self.assertEqual( qt_model.item(  5, 4 ).text(), "49.89") #京城銀
        self.assertEqual( qt_model.item(  6, 4 ).text(), "14.84") #臺企銀
        self.assertEqual( qt_model.item(  7, 4 ).text(), "16.74") #台新金
        self.assertEqual( qt_model.item(  8, 4 ).text(), "12.42") #新光金
        self.assertEqual( qt_model.item(  9, 4 ).text(), "36.65") #中信金
        self.assertEqual( qt_model.item( 10, 4 ).text(), "72.32") #佳醫
        self.assertEqual( qt_model.item( 11, 4 ).text(), "67.84") #至上
        self.assertEqual( qt_model.item( 12, 4 ).text(), "35.49") #力肯
        self.assertEqual( qt_model.item( 13, 4 ).text(), "690.58") #鈊象
        self.assertEqual( qt_model.item( 14, 4 ).text(), "20.36") #致和證
        self.assertEqual( qt_model.item( 15, 4 ).text(), "24.02") #甲尚

        #未實現損益
        self.assertEqual( qt_model.item(  0, 5 ).text(), "-17,536") #元大台灣50 
        self.assertEqual( qt_model.item(  1, 5 ).text(), "956") #元大高股息
        self.assertEqual( qt_model.item(  2, 5 ).text(), "-27,309") #富邦台50
        self.assertEqual( qt_model.item(  3, 5 ).text(), "141") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 5 ).text(), "-6,955") #台積電
        self.assertEqual( qt_model.item(  5, 5 ).text(), "-2,501") #京城銀
        self.assertEqual( qt_model.item(  6, 5 ).text(), "-10,690") #臺企銀
        self.assertEqual( qt_model.item(  7, 5 ).text(), "-24,588") #台新金
        self.assertEqual( qt_model.item(  8, 5 ).text(), "-1,273") #新光金
        self.assertEqual( qt_model.item(  9, 5 ).text(), "34,850") #中信金
        self.assertEqual( qt_model.item( 10, 5 ).text(), "159,875") #佳醫
        self.assertEqual( qt_model.item( 11, 5 ).text(), "-186,618") #至上
        self.assertEqual( qt_model.item( 12, 5 ).text(), "-51,969") #力肯
        self.assertEqual( qt_model.item( 13, 5 ).text(), "5,992") #鈊象
        self.assertEqual( qt_model.item( 14, 5 ).text(), "-222,865") #致和證
        self.assertEqual( qt_model.item( 15, 5 ).text(), "-6,099") #甲尚

        #未實現報酬率
        self.assertEqual( qt_model.item(  0, 6 ).text(), "-10.29%") #元大台灣50 
        self.assertEqual( qt_model.item(  1, 6 ).text(), "0.61%") #元大高股息
        self.assertEqual( qt_model.item(  2, 6 ).text(), "-13.40%") #富邦台50
        self.assertEqual( qt_model.item(  3, 6 ).text(), "0.12%") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 6 ).text(), "-7.55%") #台積電
        self.assertEqual( qt_model.item(  5, 6 ).text(), "-5.01%") #京城銀
        self.assertEqual( qt_model.item(  6, 6 ).text(), "-6.41%") #臺企銀
        self.assertEqual( qt_model.item(  7, 6 ).text(), "-5.73%") #台新金
        self.assertEqual( qt_model.item(  8, 6 ).text(), "-10.25%") #新光金
        self.assertEqual( qt_model.item(  9, 6 ).text(), "2.54%") #中信金
        self.assertEqual( qt_model.item( 10, 6 ).text(), "21.14%") #佳醫
        self.assertEqual( qt_model.item( 11, 6 ).text(), "-25.01%") #至上
        self.assertEqual( qt_model.item( 12, 6 ).text(), "-36.61%") #力肯
        self.assertEqual( qt_model.item( 13, 6 ).text(), "17.35%") #鈊象
        self.assertEqual( qt_model.item( 14, 6 ).text(), "-38.64%") #致和證
        self.assertEqual( qt_model.item( 15, 6 ).text(), "-25.39%") #甲尚

        #已實現損益
        self.assertEqual( qt_model.item(  0, 7 ).text(), "125,719") #元大台灣50 
        self.assertEqual( qt_model.item(  1, 7 ).text(), "9,784") #元大高股息
        self.assertEqual( qt_model.item(  2, 7 ).text(), "0") #富邦台50
        self.assertEqual( qt_model.item(  3, 7 ).text(), "0") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 7 ).text(), "18,514") #台積電
        self.assertEqual( qt_model.item(  5, 7 ).text(), "0") #京城銀
        self.assertEqual( qt_model.item(  6, 7 ).text(), "-110,716") #臺企銀
        self.assertEqual( qt_model.item(  7, 7 ).text(), "245,953") #台新金
        self.assertEqual( qt_model.item(  8, 7 ).text(), "8,267") #新光金
        self.assertEqual( qt_model.item(  9, 7 ).text(), "167,307") #中信金
        self.assertEqual( qt_model.item( 10, 7 ).text(), "109,927") #佳醫
        self.assertEqual( qt_model.item( 11, 7 ).text(), "37,252") #至上
        self.assertEqual( qt_model.item( 12, 7 ).text(), "0") #力肯
        self.assertEqual( qt_model.item( 13, 7 ).text(), "33,413") #鈊象
        self.assertEqual( qt_model.item( 14, 7 ).text(), "0") #致和證
        self.assertEqual( qt_model.item( 15, 7 ).text(), "576,013") #甲尚

        #損益平衡價
        self.assertEqual( qt_model.item(  0, 8 ).text(), "181.00") #元大台灣50 
        self.assertEqual( qt_model.item(  1, 8 ).text(), "32.66") #元大高股息
        self.assertEqual( qt_model.item(  2, 8 ).text(), "109.85") #富邦台50
        self.assertEqual( qt_model.item(  3, 8 ).text(), "19.97") #國泰永續高股息
        self.assertEqual( qt_model.item(  4, 8 ).text(), "925.00") #台積電
        self.assertEqual( qt_model.item(  5, 8 ).text(), "50.20") #京城銀
        self.assertEqual( qt_model.item(  6, 8 ).text(), "14.95") #臺企銀
        self.assertEqual( qt_model.item(  7, 8 ).text(), "16.85") #台新金
        self.assertEqual( qt_model.item(  8, 8 ).text(), "12.50") #新光金
        self.assertEqual( qt_model.item(  9, 8 ).text(), "36.85") #中信金
        self.assertEqual( qt_model.item( 10, 8 ).text(), "72.70") #佳醫
        self.assertEqual( qt_model.item( 11, 8 ).text(), "68.20") #至上
        self.assertEqual( qt_model.item( 12, 8 ).text(), "35.65") #力肯
        self.assertEqual( qt_model.item( 13, 8 ).text(), "694.00") #鈊象
        self.assertEqual( qt_model.item( 14, 8 ).text(), "20.50") #致和證
        self.assertEqual( qt_model.item( 15, 8 ).text(), "24.15") #甲尚

        #累計成本(不含息)
        n_total_cost = 0
        list_str_cost = [ "44,704", "146,951", "203,862", "118,731", "73,564", "49,892", "277,372", "189,383", "4,153", "1,207,243", "667,038", "708,980", "141,970", "1,116", "636,404", "-244,993" ]
        for i in range( 16 ):
            self.assertEqual( qt_model.item( i, 9 ).text(), list_str_cost[ i ] )
            n_total_cost += int( qt_model.item( i, 9 ).text().replace( ",", "" ) )
        self.assertEqual( n_total_cost, 4226370 )

        #累計損益(不含息)
        n_total_profit = 0
        list_str_profit = [ "108,183", "10,740", "-27,309", "141", "11,559", "-2,501", "-121,406", "215,041", "6,994", "202,157", "249,282", "-149,366", "-51,969", "39,405", "-282,522", "262,914" ]  
        for i in range( 16 ):
            self.assertEqual( qt_model.item( i, 11 ).text(), list_str_profit[ i ] )
            n_total_profit += int( qt_model.item( i, 11 ).text().replace( ",", "" ) )
        self.assertEqual( n_total_profit, 471343 )

        self.window.close()

if __name__ == "__main__":
    unittest.main()
