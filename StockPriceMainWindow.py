import requests
from bs4 import BeautifulSoup
import json
import os
import sys
import datetime
from QtStockPriceMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
from QtStockTradingEditDialog import Ui_Dialog as Ui_StockTradingDialog
from QtStockDividendEditDialog import Ui_Dialog as Ui_StockDividendDialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog, QButtonGroup, QMessageBox
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtCore import Qt, QModelIndex
from openpyxl import Workbook
from enum import Enum

# 要把.ui檔變成.py
# cd D:\_2.code\PythonStockPrice
# pyside6-uic QtStockPriceMainWindow.ui -o QtStockPriceMainWindow.py
# pyside6-uic QtStockTradingEditDialog.ui -o QtStockTradingEditDialog.py
# pyside6-uic QtStockDividendEditDialog.ui -o QtStockDividendEditDialog.py

g_list_trading_data_table_vertical_header = ['交易日', '交易種類', '交易價格', '交易股數', '交易金額', '手續費', 
                                             '交易稅', '補充保費', '單筆總成本', '累計總成本', '庫存股數', '均價',
                                             '編輯', '刪除' ]
g_list_stock_list_table_vertical_header = [ '庫存股數', '總成本', '平均成本', '今日股價', '刪除' ]
g_current_dir = os.path.dirname(__file__)
edit_icon_file_path = os.path.join( g_current_dir, 'icon\\Edit.svg' ) 
edit_icon = QIcon( edit_icon_file_path ) 
delete_icon_file_path = os.path.join( g_current_dir, 'icon\\Delete.svg' ) 
delete_icon = QIcon( delete_icon_file_path ) 
trading_data_json_file_path = os.path.join( g_current_dir, 'TradingData.json' )


class TradingType( Enum ):
    TEMPLATE = 0
    BUY = 1
    SELL = 2
    DIVIDEND = 3
    CAPITAL_REDUCTION = 4

class TradingData( Enum ):
    STOCK_NUMBER = 0
    TRADING_DATE = 1
    TRADING_TYPE = 2 # 0:買進, 1:賣出
    TRADING_PRICE = 3
    TRADING_COUNT = 4
    TRADING_FEE_DISCOUNT = 5
    STOCK_DIVIDEND = 6
    CASH_DIVIDEND = 7

class TradingCost( Enum ):
    TRADING_VALUE = 0
    TRADING_FEE = 1
    TRADING_TAX = 2
    TRADING_INSURANCE = 3
    TRADING_TOTAL_COST = 4

class Utility():
    def compute_cost( e_trading_type, f_trading_price, n_trading_count, f_trading_fee_discount, b_extra_insurance, b_daying_trading ):

        n_trading_value = int( f_trading_price * n_trading_count )
        n_trading_fee = int( n_trading_value * 0.001425 * f_trading_fee_discount )
        if n_trading_fee < 20:
            n_trading_fee = 20
        if e_trading_type == TradingType.SELL:
            if b_daying_trading:
                n_trading_tax = int( n_trading_value * 0.0015 )
            else:
                n_trading_tax = int( n_trading_value * 0.003 )
        else:
            n_trading_tax = 0

        dict_result = {}
        dict_result[ TradingCost.TRADING_VALUE ] = n_trading_value
        dict_result[ TradingCost.TRADING_FEE ] = n_trading_fee
        dict_result[ TradingCost.TRADING_TAX ] = n_trading_tax
        dict_result[ TradingCost.TRADING_INSURANCE ] = 0
        dict_result[ TradingCost.TRADING_TOTAL_COST ] = n_trading_value + n_trading_fee + n_trading_tax
        return dict_result

    def generate_trading_data( str_stock_number,            #股票代碼
                               str_trading_date,            #交易日期
                               e_trading_type,              #交易種類
                               f_trading_price,             #交易價格
                               n_trading_count,             #交易股數
                               f_trading_fee_discount,      #手續費折扣
                               f_stock_dividend_per_share,  #每股股票股利
                               f_cash_dividend_per_share ): #每股現金股利
        dict_trading_data = {}
        dict_trading_data[ TradingData.STOCK_NUMBER ] = str_stock_number
        dict_trading_data[ TradingData.TRADING_DATE ] = str_trading_date
        dict_trading_data[ TradingData.TRADING_TYPE ] = e_trading_type
        dict_trading_data[ TradingData.TRADING_PRICE ] = f_trading_price
        dict_trading_data[ TradingData.TRADING_COUNT ] = n_trading_count
        dict_trading_data[ TradingData.TRADING_FEE_DISCOUNT ] = f_trading_fee_discount
        dict_trading_data[ TradingData.STOCK_DIVIDEND ] = f_stock_dividend_per_share
        dict_trading_data[ TradingData.CASH_DIVIDEND ] = f_cash_dividend_per_share
        return dict_trading_data

class StockDividendEditDialog( QDialog ):
    def __init__( self, str_stock_number, str_stock_name, parent = None ):
        super().__init__( parent )

        self.ui = Ui_StockDividendDialog()
        self.ui.setupUi( self )

        self.ui.qtStockNumberLabel.setText( str_stock_number )
        self.ui.qtStockNameLabel.setText( str_stock_name )
        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )
        self.ui.qtDateEdit.setCalendarPopup( True )
        self.ui.qtOkButtonBox.accepted.connect( self.accept_data )
        self.ui.qtOkButtonBox.rejected.connect( self.cancel )
        self.dict_trading_data = {}

    def accept_data( self ):
        f_stock_dividend_per_share = self.ui.qtStockDividendDoubleSpinBox.value()
        f_cash_dividend_per_share = self.ui.qtCashDividendDoubleSpinBox.value()
        if f_stock_dividend_per_share != 0 or f_cash_dividend_per_share != 0:

            self.dict_trading_data = Utility.generate_trading_data( self.ui.qtStockNumberLabel.text(),                  #股票代碼
                                                                    self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" ), #交易日期
                                                                    TradingType.DIVIDEND,                               #交易種類
                                                                    0,                                                  #交易價格                         
                                                                    0,                                                  #交易股數
                                                                    1,                                                  #手續費折扣                                   
                                                                    f_stock_dividend_per_share,                         #每股股票股利
                                                                    f_cash_dividend_per_share )                         #每股現金股利
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

class StockTradingEditDialog( QDialog ):
    def __init__( self, str_stock_number, str_stock_name, b_discount, f_discount_value, b_extra_insurance, parent = None ):
        super().__init__( parent )

        self.ui = Ui_StockTradingDialog()
        self.ui.setupUi( self )

        self.ui.qtStockNumberLabel.setText( str_stock_number )
        self.ui.qtStockNameLabel.setText( str_stock_name )
        obj_current_date = datetime.datetime.today()
        self.ui.qtDateEdit.setDate( obj_current_date.date() )
        self.ui.qtDateEdit.setCalendarPopup( True )
        self.ui.qtDiscountCheckBox.setChecked( b_discount )
        self.ui.qtDiscountRateDoubleSpinBox.setValue( f_discount_value )

        self.ui.qtDiscountCheckBox.stateChanged.connect( self.on_discount_check_box_state_changed )
        self.ui.qtBuyRadioButton.toggled.connect( self.compute_cost )
        self.ui.qtSellRadioButton.toggled.connect( self.compute_cost )
        self.ui.qtCommonTradeRadioButton.toggled.connect( self.on_trading_type_changed )
        self.ui.qtOddTradeRadioButton.toggled.connect( self.on_trading_type_changed )
        self.ui.qtPriceDoubleSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtCommonTradeCountSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtOddTradeCountSpinBox.valueChanged.connect( self.compute_cost )
        self.ui.qtOkButtonBox.accepted.connect( self.accept_data )
        self.ui.qtOkButtonBox.rejected.connect( self.cancel )


        self.dict_trading_data = {}

    def on_discount_check_box_state_changed( self, state ):
        if state == 2:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( True )
        else:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( False )

        self.compute_cost()

    def accept_data( self ):

        if float( self.ui.qtTotalCostLineEdit.text().replace( ',', '' ) ) != 0:
            
            self.dict_trading_data = Utility.generate_trading_data( self.ui.qtStockNumberLabel.text(),                  #股票代碼
                                                                    self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" ), #交易日期
                                                                    self.get_trading_type(),                            #交易種類
                                                                    self.ui.qtPriceDoubleSpinBox.value(),               #交易價格
                                                                    self.get_trading_count(),                           #交易股數
                                                                    self.get_trading_fee_discount(),                    #手續費折扣
                                                                    0,                                                  #每股股票股利
                                                                    0 )                                                 #每股現金股利
            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        self.reject()

    def on_trading_type_changed( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            self.ui.qtCommonTradeCountSpinBox.setEnabled( True )
            self.ui.qtOddTradeCountSpinBox.setEnabled( False )
        else:
            self.ui.qtCommonTradeCountSpinBox.setEnabled( False )
            self.ui.qtOddTradeCountSpinBox.setEnabled( True )

        self.compute_cost()

    def get_trading_type( self ):
        if self.ui.qtBuyRadioButton.isChecked():
            return TradingType.BUY
        else:
            return TradingType.SELL

    def get_trading_count( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            return self.ui.qtCommonTradeCountSpinBox.value() * 1000
        else:
            return self.ui.qtOddTradeCountSpinBox.value()
        
    def get_trading_fee_discount( self ):
        if self.ui.qtDiscountCheckBox.isChecked():
            return self.ui.qtDiscountRateDoubleSpinBox.value() / 10
        else:
            return 1

    def compute_cost( self ):
        e_trading_type = self.get_trading_type()
        f_trading_price = self.ui.qtPriceDoubleSpinBox.value()
        n_trading_count = self.get_trading_count()
        f_trading_fee_discount = self.get_trading_fee_discount() 
        
        dict_result = Utility.compute_cost( e_trading_type, f_trading_price, n_trading_count, f_trading_fee_discount, True, False )

        self.ui.qtTradingValueLineEdit.setText( format( dict_result[ TradingCost.TRADING_VALUE ], ',' ) )
        self.ui.qtFeeLineEdit.setText( format( dict_result[ TradingCost.TRADING_FEE ], ',' ) )
        self.ui.qtTaxLineEdit.setText( format( dict_result[ TradingCost.TRADING_TAX ], ',' ) )
        self.ui.qtTotalCostLineEdit.setText( format( dict_result[ TradingCost.TRADING_TOTAL_COST ], ',' ) )

class MainWindow( QMainWindow ):
    def __init__(self):
        super( MainWindow, self ).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )  # 設置 UI

        self.stock_list_model = QStandardItemModel( 0, 0 )
        self.stock_list_model.setHorizontalHeaderLabels( g_list_stock_list_table_vertical_header )
        self.ui.qtStockListTableView.setModel( self.stock_list_model )
        self.ui.qtStockListTableView.clicked.connect( lambda index: self.on_stock_list_table_item_clicked( index, self.stock_list_model ) )

        self.per_stock_trading_data_model = QStandardItemModel( 0, 0 ) 
        self.per_stock_trading_data_model.setVerticalHeaderLabels( g_list_trading_data_table_vertical_header )
        self.ui.qtTradingDataTableView.setModel( self.per_stock_trading_data_model )
        self.ui.qtTradingDataTableView.horizontalHeader().hide()
        self.ui.qtTradingDataTableView.clicked.connect( lambda index: self.on_trading_data_table_item_clicked( index, self.per_stock_trading_data_model ) )

        button_group_1 = QButtonGroup(self)
        button_group_1.addButton( self.ui.qtFromNewToOldRadioButton )
        button_group_1.addButton( self.ui.qtFromOldToNewRadioButton )
        self.ui.qtFromNewToOldRadioButton.setChecked( True )

        button_group_2 = QButtonGroup(self)
        button_group_2.addButton( self.ui.qtShowAllRadioButton )
        button_group_2.addButton( self.ui.qtShow10RadioButton )
        self.ui.qtShowAllRadioButton.setChecked( True )


        self.ui.qtAddStockPushButton.clicked.connect( self.on_add_stock_push_button_clicked )
        self.ui.qtDiscountCheckBox.stateChanged.connect( self.on_discount_check_box_state_changed )

        self.ui.qtAddTradingDataPushButton.clicked.connect( self.on_add_trading_data_push_button_clicked )
        self.ui.qtAddDividendDataPushButton.clicked.connect( self.on_add_dividend_data_push_button_clicked )
        self.ui.qtAddCapitalReductionDataPushButton.clicked.connect( self.on_add_capital_reduction_data_push_button_clicked )
        self.ui.qtAddCapitalIncreaseDataPushButton.clicked.connect( self.on_add_capital_increase_data_push_button_clicked )
        # self.ui.qtDeleteDataPushButton.clicked.connect( self.on_delete_data_push_button_clicked )
        # self.ui.qtEditDataPushButton.clicked.connect( self.on_edit_data_push_button_clicked )

        self.dict_all_company_number_and_name = self.download_all_company_stock_number()

        self.str_picked_stock_number = None
        self.dict_all_stock_trading_data = {}

        self.func_load_existing_trading_data()

    def on_discount_check_box_state_changed( self, state ):
        if state == 2:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( True )
        else:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( False )

    def on_add_stock_push_button_clicked( self ):
        str_stock_input = self.ui.qtStockInputLineEdit.text()
        self.ui.qtStockInputLineEdit.clear()
        str_first_four_chars = str_stock_input[:4]
        # if str_first_four_chars not in self.dict_all_company_stock_info:
        #     b_find = False
        #     for stock_number, stock_info in self.dict_all_company_stock_info.items():
        #         stock_name = stock_info[ StockCore.ModifiedDataType.NAME ]
        #         if str_first_four_chars == stock_name:
        #             str_first_four_chars = stock_number
        #             b_find = True
        #             break
        #     if not b_find:
        #         QMessageBox.warning( self, "警告", "輸入的股票代碼不存在", QMessageBox.Ok )
        #         return
        
        if str_first_four_chars not in self.dict_all_stock_trading_data:
            dict_trading_data = Utility.generate_trading_data( str_first_four_chars, #股票代碼
                                                               "0001-01-01",         #交易日期
                                                               TradingType.TEMPLATE, #交易種類
                                                               0,                    #交易價格
                                                               0,                    #交易股數
                                                               1,                    #手續費折扣
                                                               0,                    #每股股票股利
                                                               0 )                   #每股現金股利
            self.dict_all_stock_trading_data[ str_first_four_chars ] = [ dict_trading_data ]

            self.refresh_stock_list_table()
            self.func_save_trading_data()

    def on_add_trading_data_push_button_clicked( self ):
        if self.str_picked_stock_number is None:
            return
        str_stock_number = self.str_picked_stock_number
        str_stock_name = self.dict_all_company_number_and_name[ str_stock_number ]
        dialog = StockTradingEditDialog( str_stock_number, str_stock_name, self.ui.qtDiscountCheckBox.isChecked(), self.ui.qtDiscountRateDoubleSpinBox.value(), self.ui.qtExtraInsuranceFeeCheckBox.isChecked(), self )

        if dialog.exec():
            dict_trading_data = dialog.dict_trading_data
            self.dict_all_stock_trading_data[ str_stock_number ].append( dict_trading_data )
            sorted_list = self.func_sort_single_trading_data( str_stock_number )
            self.refresh_trading_data_table( sorted_list )
            self.func_save_trading_data()

    def on_add_dividend_data_push_button_clicked( self ):
        if self.str_picked_stock_number is None:
            return
        str_stock_number = self.str_picked_stock_number
        str_stock_name = self.dict_all_company_number_and_name[ str_stock_number ]
        dialog = StockDividendEditDialog( str_stock_number, str_stock_name, self )

        if dialog.exec():
            dict_trading_data = dialog.dict_trading_data
            self.dict_all_stock_trading_data[ str_stock_number ].append( dict_trading_data )
            sorted_list = self.func_sort_single_trading_data( str_stock_number )
            self.refresh_trading_data_table( sorted_list )
            self.func_save_trading_data()

    def on_add_capital_reduction_data_push_button_clicked( self ):
        if self.str_picked_stock_number is None:
            return
        str_stock_number = self.str_picked_stock_number
        sorted_list = self.func_sort_single_trading_data( str_stock_number )
        self.refresh_trading_data_table( sorted_list )
        self.func_save_trading_data()
        pass

    def on_add_capital_increase_data_push_button_clicked( self ):
        if self.str_picked_stock_number is None:
            return
        str_stock_number = self.str_picked_stock_number
        sorted_list = self.func_sort_single_trading_data( str_stock_number )
        self.refresh_trading_data_table( sorted_list )
        self.func_save_trading_data()
        pass

    def on_delete_data_push_button_clicked( self ):
        print("on_delete_data_push_button_clicked")

    def on_edit_data_push_button_clicked( self ):
        print("on_edit_data_push_button_clicked")
        # dialog = EditDialog()
        # dialog.exec()

    def on_stock_list_table_item_clicked( self, index: QModelIndex, table_model ):
        item = table_model.itemFromIndex( index )
        if item is not None:
            n_column = index.column()  # 獲取列索引
            n_row = index.row()  # 獲取行索引
            header_text = table_model.verticalHeaderItem( index.row() ).text()
            str_stock_number = header_text[:4]
            self.str_picked_stock_number = str_stock_number
            
            if n_column == len( g_list_stock_list_table_vertical_header ) - 1:
                result = self.func_show_message_box( "警告", f"確定要刪掉『{header_text}』的所有資料嗎?" )
                if result:
                    del self.dict_all_stock_trading_data[ str_stock_number ]
                    self.refresh_stock_list_table()
                    self.per_stock_trading_data_model.clear()
                    self.func_save_trading_data()
            elif str_stock_number in self.dict_all_stock_trading_data:
                list_trading_data = self.dict_all_stock_trading_data[ str_stock_number ]
                self.refresh_trading_data_table( list_trading_data )

        self.func_update_button_status()

    def on_trading_data_table_item_clicked( self, index: QModelIndex, table_model ):
        item = table_model.itemFromIndex( index )
        if item is not None:
            n_column = index.column()  # 獲取列索引
            n_row = index.row()  # 獲取行索引
            n_index = 0
            list_trading_data = self.dict_all_stock_trading_data[ self.str_picked_stock_number ]
            if self.ui.qtFromNewToOldRadioButton.isChecked():
                n_index = n_column
            else:
                n_index = len( list_trading_data ) - n_column - 1

            if n_row == len( g_list_trading_data_table_vertical_header ) - 2: #編輯
                pass
            elif n_row == len( g_list_trading_data_table_vertical_header ) - 1: #刪除
                pass

    def func_show_message_box( self, str_title, str_message ):
        message_box = QMessageBox( self )
        message_box.setIcon( QMessageBox.Warning )  # 設置為警告圖示
        message_box.setWindowTitle( str_title )
        message_box.setText( str_message )

        # 添加自訂按鈕
        button_ok = message_box.addButton("確定", QMessageBox.AcceptRole)
        button_cancel = message_box.addButton("取消", QMessageBox.RejectRole)

        message_box.exec()

        if message_box.clickedButton() == button_ok:
            return True
        elif message_box.clickedButton() == button_cancel:
            return False

    def func_update_button_status( self ):
        if self.str_picked_stock_number is None:
            self.ui.qtAddTradingDataPushButton.setEnabled( False )
            self.ui.qtAddDividendDataPushButton.setEnabled( False )
            self.ui.qtAddCapitalReductionDataPushButton.setEnabled( False )
            self.ui.qtAddCapitalIncreaseDataPushButton.setEnabled( False )
        else:
            self.ui.qtAddTradingDataPushButton.setEnabled( True )
            self.ui.qtAddDividendDataPushButton.setEnabled( True )
            self.ui.qtAddCapitalReductionDataPushButton.setEnabled( True )
            self.ui.qtAddCapitalIncreaseDataPushButton.setEnabled( True)
        pass

    def func_sort_single_trading_data( self, str_stock_number ):
        list_trading_data = self.dict_all_stock_trading_data[ str_stock_number ]
        sorted_list = sorted( list_trading_data, key=lambda x: ( datetime.datetime.strptime( x[ TradingData.TRADING_DATE ], "%Y-%m-%d"), x[ TradingData.TRADING_TYPE ] ) )
        self.dict_all_stock_trading_data[ str_stock_number ] = sorted_list
        return sorted_list

    def func_sort_all_trading_data( self ):
        for key_stock_number, value_list_trading_data in self.dict_all_stock_trading_data.items():
            self.func_sort_single_trading_data( key_stock_number )

    def func_save_trading_data( self ):

        export_data = []
        for key, value in self.dict_all_stock_trading_data.items():
            for item in value:
                dict_per_trading_data = {}
                dict_per_trading_data[ "stock_number" ] = item[ TradingData.STOCK_NUMBER ]
                dict_per_trading_data[ "trading_date" ] = item[ TradingData.TRADING_DATE ]
                dict_per_trading_data[ "trading_type" ] = int( item[ TradingData.TRADING_TYPE ].value )
                dict_per_trading_data[ "trading_price" ] = item[ TradingData.TRADING_PRICE ]
                dict_per_trading_data[ "trading_count" ] = item[ TradingData.TRADING_COUNT ]
                dict_per_trading_data[ "trading_fee_discount" ] = item[ TradingData.TRADING_FEE_DISCOUNT ]
                dict_per_trading_data[ "stock_dividend" ] = item[ TradingData.STOCK_DIVIDEND ]
                dict_per_trading_data[ "cash_dividend" ] = item[ TradingData.CASH_DIVIDEND ]


                export_data.append( dict_per_trading_data )


        with open( trading_data_json_file_path, 'w', encoding='utf-8' ) as f:
            json.dump( export_data, f, ensure_ascii=False, indent=4 )

    def func_load_existing_trading_data( self ):

        if not os.path.exists( trading_data_json_file_path ):
            return
        with open( trading_data_json_file_path,'r', encoding='utf-8' ) as f:
            data = json.load( f )

        for item in data:
            if ( "stock_number" in item and
                 "trading_date" in item and
                 "trading_type" in item and
                 "trading_price" in item and
                 "trading_count" in item and
                 "trading_fee_discount" in item and
                 "stock_dividend" in item and
                 "cash_dividend" in item ):

                dict_per_trading_data = Utility.generate_trading_data( item[ "stock_number" ],                #股票代碼
                                                                       item[ "trading_date" ],                #交易日期
                                                                       TradingType( item[ "trading_type" ] ), #交易種類
                                                                       item[ "trading_price" ],               #交易價格
                                                                       item[ "trading_count" ],               #交易股數
                                                                       item[ "trading_fee_discount" ],        #手續費折扣
                                                                       item[ "stock_dividend" ],              #每股股票股利
                                                                       item[ "cash_dividend" ] )              #每股現金股利

                if item[ "stock_number" ] not in self.dict_all_stock_trading_data:
                    self.dict_all_stock_trading_data[ item[ "stock_number" ] ] = [ dict_per_trading_data ]
                else:
                    self.dict_all_stock_trading_data[ item[ "stock_number" ] ].append( dict_per_trading_data )

                
        self.func_sort_all_trading_data()
        self.refresh_stock_list_table()

    def refresh_stock_list_table( self ):
        self.stock_list_model.clear()
        self.stock_list_model.setHorizontalHeaderLabels( g_list_stock_list_table_vertical_header )

        list_vertical_labels = []
        for index,( key_stock_number, value ) in enumerate( self.dict_all_stock_trading_data.items() ):
            str_stock_name = self.dict_all_company_number_and_name[ key_stock_number ]
            list_vertical_labels.append( f"{key_stock_number} {str_stock_name}" )

            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            delete_icon_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )

            self.stock_list_model.setItem( index, len( g_list_stock_list_table_vertical_header ) - 1, delete_icon_item )
            # table_model.setItem( index, 0, icon_item )
            # stock_inventory_item = QStandardItem( '庫存股數' )
            # total_cost_item = QStandardItem( '總成本' )
            # average_price_item = QStandardItem( '均價' )

            # condition_item.setFlags( condition_item.flags() & ~Qt.ItemIsEditable )
            # condition_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )

        self.stock_list_model.setVerticalHeaderLabels( list_vertical_labels )

    def refresh_trading_data_table( self, sorted_list ):
        self.per_stock_trading_data_model.clear()
        self.per_stock_trading_data_model.setVerticalHeaderLabels( g_list_trading_data_table_vertical_header )
        self.ui.qtTradingDataTableView.horizontalHeader().hide()

        n_stock_inventory = 0
        n_accumulated_total_cost = 0

        index = 0
        for dict_per_trading_data in sorted_list:

            e_trading_type = dict_per_trading_data[ TradingData.TRADING_TYPE ]
            if e_trading_type == TradingType.TEMPLATE:
                continue
            f_trading_price = dict_per_trading_data[ TradingData.TRADING_PRICE ]
            n_trading_count = dict_per_trading_data[ TradingData.TRADING_COUNT ]
            f_trading_fee_discount = dict_per_trading_data[ TradingData.TRADING_FEE_DISCOUNT ]
            dict_result = Utility.compute_cost( e_trading_type, f_trading_price, n_trading_count, f_trading_fee_discount, True, False )
            n_trading_value = dict_result[ TradingCost.TRADING_VALUE ]
            n_trading_fee = dict_result[ TradingCost.TRADING_FEE ]
            n_trading_tax = dict_result[ TradingCost.TRADING_TAX ]
            n_trading_insurance = dict_result[ TradingCost.TRADING_INSURANCE ]  
            n_per_trading_total_cost = dict_result[ TradingCost.TRADING_TOTAL_COST ]

            if e_trading_type == TradingType.BUY:
                n_stock_inventory += n_trading_count
                str_trading_type = "買進"
                n_accumulated_total_cost += n_per_trading_total_cost
            elif e_trading_type == TradingType.SELL:
                n_stock_inventory -= n_trading_count
                str_trading_type = "賣出"
            elif e_trading_type == TradingType.DIVIDEND:
                str_trading_type = "股利分配"
            elif e_trading_type == TradingType.CAPITAL_REDUCTION:
                str_trading_type = "減資"

            list_data = [ dict_per_trading_data[ TradingData.TRADING_DATE ], #交易日期
                          str_trading_type,                                  #交易種類
                          format( f_trading_price, "," ),                    #交易價格
                          format( n_trading_count, "," ),                    #交易股數
                          format( n_trading_value, "," ),                    #交易金額
                          format( n_trading_fee, "," ),                      #手續費
                          format( n_trading_tax, "," ),                      #交易稅
                          format( n_trading_insurance, "," ),                #補充保費
                          format( n_per_trading_total_cost, "," ),           #單筆總成本
                          format( n_accumulated_total_cost, "," ),           #累計總成本
                          format( n_stock_inventory, "," ),                  #庫存股數
                          'XXXX' ]                                           #均價

            for row, data in enumerate( list_data ):
                standard_item = QStandardItem( data )
                standard_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
                standard_item.setFlags( standard_item.flags() & ~Qt.ItemIsEditable )
                self.per_stock_trading_data_model.setItem( row, index, standard_item ) 

            edit_icon_item = QStandardItem("")
            edit_icon_item.setIcon( edit_icon )
            edit_icon_item.setFlags( edit_icon_item.flags() & ~Qt.ItemIsEditable )
            delete_icon_item = QStandardItem("")
            delete_icon_item.setIcon( delete_icon )
            delete_icon_item.setFlags( delete_icon_item.flags() & ~Qt.ItemIsEditable )
            delete_icon_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )

            self.per_stock_trading_data_model.setItem( len( list_data ), index, edit_icon_item )
            self.per_stock_trading_data_model.setItem( len( list_data ) + 1, index, delete_icon_item )
            index += 1
            pass

    def on_export_selected_to_excell_button_clicked( self ):
        workbook = Workbook()
        worksheet = workbook.active
        # worksheet.title = str_tab_title
        
        pass

    def on_export_all_to_excell_button_clicked( self ):
        pass

    def download_all_company_stock_number( self ): 
        all_company_name_and_number = {}
        obj_current_date = datetime.datetime.today()
        str_date = obj_current_date.strftime('%Y%m%d')

        file_path = os.path.join( os.path.dirname(__file__), 'StockNumber.txt' )
        b_need_to_download = False
        if os.path.exists( file_path ):
            with open( file_path, 'r', encoding='utf-8' ) as f:
                data = f.readlines()
                for i, row in enumerate( data ):
                    if i == 0:
                        if row.strip() != str_date:
                            b_need_to_download = True
                            break
                    else:
                        ele = row.strip().split( ',' )
                        all_company_name_and_number[ ele[ 0 ] ] = ele[ 1 ]
        else:
            b_need_to_download = True

        if b_need_to_download:
            # 上市公司股票代碼
            companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
            res = requests.get( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )

            total_company_count = 0
            tds = []
            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td" )]
                if len( data ) == 7 and data[ 5 ] == 'ESVUFR': 
                    total_company_count += 1
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        if '-創' in modified_data[ 1 ]:
                            continue
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip() ]
                        tds.append( modified_data_after_strip )

            # 上櫃公司股票代碼
            companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"
            res = requests.get( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )
            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td") ]
                if len( data ) == 7 and data[ 5 ] == 'ESVUFR': 
                    total_company_count += 1
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        if '-創' in modified_data[ 1 ]:
                            continue
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip() ]
                        tds.append( modified_data_after_strip )

            # 興櫃公司股票代碼
            companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=5"
            res = requests.get( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )
            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td") ]
                if len( data ) == 7 and data[ 5 ] == 'ESVUFR': 
                    total_company_count += 1
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        if '-創' in modified_data[ 1 ]:
                            continue
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip() ]
                        tds.append( modified_data_after_strip )

            if len( tds ) == 0:
                return
            
            # 確保目錄存在，若不存在則遞歸創建
            os.makedirs( os.path.dirname( file_path ), exist_ok = True )
            with open( file_path, 'w', encoding='utf-8' ) as f:
                f.write( str_date + '\n' )
                for row in tds:
                    f.write( str( row[ 0 ] ) + ',' + str( row[ 1 ] ) + '\n' )
                    all_company_name_and_number[ row[ 0 ] ] = row[ 1 ]

        return all_company_name_and_number
    
if __name__ == "__main__":
    app = QApplication(sys.argv)  # 創建應用程式
    app.setStyle('Fusion')
    window = MainWindow()  # 創建主窗口
    window.show()  # 顯示窗口
    sys.exit(app.exec())  # 進入事件循環