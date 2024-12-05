import json
import os
import sys
import datetime
from QtStockPriceMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
from QtStockPriceEditDialog import Ui_Dialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6.QtGui import QStandardItemModel, QStandardItem, QIcon
from PySide6.QtCore import Qt, QModelIndex
from enum import Enum

# 要把.ui檔變成.py
# cd D:\_2.code\PythonStockPrice
# pyside6-uic QtStockPriceEditDialog.ui -o QtStockPriceEditDialog.py
# pyside6-uic QtStockPriceMainWindow.ui -o QtStockPriceMainWindow.py

class TradingType( Enum ):
    TEMPLATE = 0
    BUY = 1
    SELL = 2

class TradingData( Enum ):
    STOCK_NUMBER = 0
    TRADING_DATE = 1
    TRADING_TYPE = 2 # 0:買進, 1:賣出
    TRADING_PRICE = 3
    TRADING_COUNT = 4
    TRADING_FEE_DISCOUNT = 5

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

    def generate_trading_data( str_stock_number, str_trading_date, e_trading_type, f_trading_price, n_trading_count, f_trading_fee_discount ):
        dict_trading_data = {}
        dict_trading_data[ TradingData.STOCK_NUMBER ] = str_stock_number
        dict_trading_data[ TradingData.TRADING_DATE ] = str_trading_date
        dict_trading_data[ TradingData.TRADING_TYPE ] = e_trading_type
        dict_trading_data[ TradingData.TRADING_PRICE ] = f_trading_price
        dict_trading_data[ TradingData.TRADING_COUNT ] = n_trading_count
        dict_trading_data[ TradingData.TRADING_FEE_DISCOUNT ] = f_trading_fee_discount
        return dict_trading_data

class TradingDataDialog( QDialog ):
    def __init__( self, str_stock_number, b_discount, f_discount_value, b_extra_insurance, parent = None ):
        super().__init__( parent )

        self.ui = Ui_Dialog()
        self.ui.setupUi( self )

        self.ui.qtStockNumberLabel.setText( str_stock_number )
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
            
            self.dict_trading_data = Utility.generate_trading_data( self.ui.qtStockNumberLabel.text(), self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" ), self.get_trading_type(), self.ui.qtPriceDoubleSpinBox.value(), self.get_trading_count(), self.get_trading_fee_discount() )
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
        self.stock_list_model.setHorizontalHeaderLabels( [ '股票代碼', '公司名稱', '庫存股數', '總成本', '均價' ] )
        self.ui.qtStockListTableView.setModel( self.stock_list_model )
        self.ui.qtStockListTableView.clicked.connect( lambda index: self.on_table_item_clicked( index, self.stock_list_model ) )

        self.per_stock_trading_data_model = QStandardItemModel( 0, 0 ) 
        self.per_stock_trading_data_model.setVerticalHeaderLabels( [ '交易日', '交易種類', '交易價格', '交易股數', '交易金額', '手續費', 
                                                                     '交易稅', '補充保費', '單筆總成本', '累計總成本', '庫存股數', '均價'] )
        self.ui.qtTradingDataTableView.setModel( self.per_stock_trading_data_model )
        self.ui.qtTradingDataTableView.horizontalHeader().hide()


        self.ui.qtDiscountCheckBox.stateChanged.connect( self.on_discount_check_box_state_changed )
        self.ui.qtAddTradingDataPushButton.clicked.connect( self.on_add_new_data_push_button_clicked )
        self.ui.qtAddStockPushButton.clicked.connect( self.on_add_stock_push_button_clicked )
        # self.ui.qtDeleteDataPushButton.clicked.connect( self.on_delete_data_push_button_clicked )
        # self.ui.qtEditDataPushButton.clicked.connect( self.on_edit_data_push_button_clicked )

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
            dict_trading_data = Utility.generate_trading_data( str_first_four_chars, "0001-01-01", TradingType.TEMPLATE, 0, 0, 1 )
            self.dict_all_stock_trading_data[ str_first_four_chars ] = [ dict_trading_data ]

            self.refresh_stock_list_table()
            self.func_save_trading_data()


    def on_add_new_data_push_button_clicked( self ):
        if self.str_picked_stock_number is None:
            return
        str_stock_number = self.str_picked_stock_number
        dialog = TradingDataDialog( str_stock_number, self.ui.qtDiscountCheckBox.isChecked(), self.ui.qtDiscountRateDoubleSpinBox.value(), self.ui.qtExtraInsuranceFeeCheckBox.isChecked(), self )

        if dialog.exec():
            dict_trading_data = dialog.dict_trading_data
            self.dict_all_stock_trading_data[ str_stock_number ].append( dict_trading_data )
            list_trading_data = self.dict_all_stock_trading_data[ str_stock_number ]
            sorted_list = sorted( list_trading_data, key=lambda x: ( datetime.datetime.strptime( x[ TradingData.TRADING_DATE ], "%Y-%m-%d"), x[ TradingData.TRADING_TYPE ] ) )
            self.refresh_trading_data_table( sorted_list )
            self.func_save_trading_data()

    def on_table_item_clicked( self, index: QModelIndex, table_model ):
        item = table_model.itemFromIndex( index )
        if item is not None:
            header_text = table_model.verticalHeaderItem( index.row() ).text()
            str_stock_number = header_text[:4]
            self.str_picked_stock_number = str_stock_number

            if str_stock_number in self.dict_all_stock_trading_data:
                list_trading_data = self.dict_all_stock_trading_data[ str_stock_number ]
                sorted_list = sorted( list_trading_data, key=lambda x: ( datetime.datetime.strptime( x[ TradingData.TRADING_DATE ], "%Y-%m-%d"), x[ TradingData.TRADING_TYPE ] ) )
                self.refresh_trading_data_table( sorted_list )

    def func_save_trading_data( self ):
        current_dir = os.path.dirname( __file__ )
        json_file_path = os.path.join( current_dir, 'TradingData.json' )
        
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

                export_data.append( dict_per_trading_data )


        with open( json_file_path, 'w', encoding='utf-8' ) as f:
            json.dump( export_data, f, ensure_ascii=False, indent=4 )

    def func_load_existing_trading_data( self ):
        current_dir = os.path.dirname( __file__ )
        json_file_path = os.path.join( current_dir, 'TradingData.json' )

        with open( json_file_path,'r', encoding='utf-8' ) as f:
            data = json.load( f )

        for item in data:
            if ( item[ "stock_number" ] != None and 
                 item[ "trading_date" ] != None and 
                 item[ "trading_type" ] != None and 
                 item[ "trading_price" ] != None and 
                 item[ "trading_count" ] != None and 
                 item[ "trading_fee_discount" ] != None ):

                dict_per_trading_data = Utility.generate_trading_data( item[ "stock_number" ], 
                                                                       item[ "trading_date" ], 
                                                                       TradingType( item[ "trading_type" ] ), 
                                                                       item[ "trading_price" ],
                                                                       item[ "trading_count" ], 
                                                                       item[ "trading_fee_discount" ] )

                if item[ "stock_number" ] not in self.dict_all_stock_trading_data:
                    self.dict_all_stock_trading_data[ item[ "stock_number" ] ] = [ dict_per_trading_data ]
                else:
                    self.dict_all_stock_trading_data[ item[ "stock_number" ] ].append( dict_per_trading_data )

        self.refresh_stock_list_table()

    def refresh_stock_list_table( self ):
        self.stock_list_model.clear()
        self.stock_list_model.setHorizontalHeaderLabels( ['股票代碼', '公司名稱', '庫存股數', '總成本', '均價'] )

        list_vertical_labels = []
        for index,( key, value ) in enumerate( self.dict_all_stock_trading_data.items() ):
            list_vertical_labels.append( key )
            stock_number_item = QStandardItem( key )
            # stock_name_item = QStandardItem( '公司名稱' )
            # stock_inventory_item = QStandardItem( '庫存股數' )
            # total_cost_item = QStandardItem( '總成本' )
            # average_price_item = QStandardItem( '均價' )

            # condition_item.setFlags( condition_item.flags() & ~Qt.ItemIsEditable )
            # condition_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
            self.stock_list_model.setItem( index, 0, stock_number_item )

        self.stock_list_model.setVerticalHeaderLabels( list_vertical_labels )

    def refresh_trading_data_table( self, sorted_list ):
        self.per_stock_trading_data_model.clear()
        self.per_stock_trading_data_model.setVerticalHeaderLabels( ['交易日', '交易種類', '交易價格', '交易股數', '交易金額', '手續費', 
                                                                    '交易稅', '補充保費', '單筆總成本', '累計總成本', '庫存股數', '均價'
                                                                    '', ''] )
        self.ui.qtTradingDataTableView.horizontalHeader().hide()

        n_stock_inventory = 0
        n_accumulated_total_cost = 0

        current_dir = os.path.dirname(__file__)
        edit_icon_file_path = os.path.join( current_dir, 'icon\\Edit.svg' ) 
        edit_icon = QIcon( edit_icon_file_path ) 
        delete_icon_file_path = os.path.join( current_dir, 'icon\\Delete.svg' ) 
        delete_icon = QIcon( delete_icon_file_path ) 
        
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
            else:
                n_stock_inventory -= n_trading_count
                str_trading_type = "賣出"

            list_data = [ dict_per_trading_data[ TradingData.TRADING_DATE ], # 交易日期
                          str_trading_type, # 交易種類
                          format( f_trading_price, "," ), # 交易價格
                          format( n_trading_count, "," ), # 交易股數
                          format( n_trading_value, "," ), # 交易金額
                          format( n_trading_fee, "," ), # 手續費
                          format( n_trading_tax, "," ), # 交易稅
                          format( n_trading_insurance, "," ), # 補充保費
                          format( n_per_trading_total_cost, "," ), # 單筆總成本
                          format( n_accumulated_total_cost, "," ), # 累計總成本
                          format( n_stock_inventory, "," ),
                          'XXXX' ] # 庫存股數

            for row, data in enumerate( list_data ):
                standard_item = QStandardItem( data )
                standard_item.setTextAlignment( Qt.AlignHCenter | Qt.AlignVCenter )
                edit_icon_item.setFlags( edit_icon_item.flags() & ~Qt.ItemIsEditable )
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

    def on_delete_data_push_button_clicked( self ):
        print("on_delete_data_push_button_clicked")

    def on_edit_data_push_button_clicked( self ):
        print("on_edit_data_push_button_clicked")
        # dialog = EditDialog()
        # dialog.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)  # 創建應用程式
    app.setStyle('Fusion')
    window = MainWindow()  # 創建主窗口
    window.show()  # 顯示窗口
    sys.exit(app.exec())  # 進入事件循環