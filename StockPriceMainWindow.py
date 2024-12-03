import sys
import datetime
from QtStockPriceMainWindow import Ui_MainWindow  # 導入轉換後的 UI 類
from QtStockPriceEditDialog import Ui_Dialog
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from enum import Enum

# 要把.ui檔變成.py
# cd D:\_2.code\PythonStockPrice
# pyside6-uic QtStockPriceEditDialog.ui -o QtStockPriceEditDialog.py
# pyside6-uic QtStockPriceMainWindow.ui -o QtStockPriceMainWindow.py

class TradingType( Enum ):
    BUY = 0
    SELL = 1

class TradingData( Enum ):
    TRADING_DATE = 0
    TRADING_TYPE = 1 # 0:買進, 1:賣出
    TRADING_PRICE = 2
    TRADING_COUNT = 3
    TRADING_DISCOUNT = 4



class TradingDataDialog( QDialog ):
    def __init__( self, b_discount, f_discount_value, b_extra_insurance, parent = None ):
        super().__init__( parent )

        self.ui = Ui_Dialog()
        self.ui.setupUi( self )

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

        if float( self.ui.qtTotalCostLineEdit.text() ) != 0:
            self.dict_trading_data[ TradingData.TRADING_DATE ] = self.ui.qtDateEdit.date().toString( "yyyy-MM-dd" )
            if self.ui.qtBuyRadioButton.isChecked():
                self.dict_trading_data[ TradingData.TRADING_TYPE ] = TradingType.BUY
            else:
                self.dict_trading_data[ TradingData.TRADING_TYPE ] = TradingType.SELL

            self.dict_trading_data[ TradingData.TRADING_PRICE ] = self.ui.qtPriceDoubleSpinBox.value()
            if self.ui.qtCommonTradeRadioButton.isChecked():
                self.dict_trading_data[ TradingData.TRADING_COUNT ] = self.ui.qtCommonTradeCountSpinBox.value() * 1000
            else:
                self.dict_trading_data[ TradingData.TRADING_COUNT ] = self.ui.qtOddTradeCountSpinBox.value()

            if self.ui.qtDiscountCheckBox.isChecked():
                self.dict_trading_data[ TradingData.TRADING_DISCOUNT ] = self.ui.qtDiscountRateDoubleSpinBox.value() / 10
            else:
                self.dict_trading_data[ TradingData.TRADING_DISCOUNT ] = 1

            self.accept()
        else:
            self.reject()
    
    def cancel( self ):
        print("cancel")
        self.reject()

    def on_trading_type_changed( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            self.ui.qtCommonTradeCountSpinBox.setEnabled( True )
            self.ui.qtOddTradeCountSpinBox.setEnabled( False )
        else:
            self.ui.qtCommonTradeCountSpinBox.setEnabled( False )
            self.ui.qtOddTradeCountSpinBox.setEnabled( True )

        self.compute_cost()

    def compute_cost( self ):
        if self.ui.qtCommonTradeRadioButton.isChecked():
            f_trade_count = self.ui.qtCommonTradeCountSpinBox.value() * 1000
        else:
            f_trade_count = self.ui.qtOddTradeCountSpinBox.value()
        
        f_trade_value = self.ui.qtPriceDoubleSpinBox.value() * f_trade_count
        self.ui.qtTradingValueLineEdit.setText( str( f_trade_value ) )

        if self.ui.qtDiscountCheckBox.isChecked():
            f_discount_value = self.ui.qtDiscountRateDoubleSpinBox.value() / 10
        else:
            f_discount_value = 1

        f_trade_fee = int( f_trade_value * 0.001425 * f_discount_value )
        self.ui.qtFeeLineEdit.setText( str( f_trade_fee ) )

        if self.ui.qtBuyRadioButton.isChecked():
            f_trade_tax = 0
            f_total_value = f_trade_value + f_trade_fee
        else:
            f_trade_tax = int( f_trade_value * 0.003 )
            f_total_value = f_trade_value - f_trade_fee - f_trade_tax
        self.ui.qtTaxLineEdit.setText( str( f_trade_tax ) )
        self.ui.qtTotalCostLineEdit.setText( str( f_total_value ) )


class MainWindow( QMainWindow ):
    def __init__(self):
        super( MainWindow, self ).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )  # 設置 UI

        self.ui.qtDiscountCheckBox.stateChanged.connect( self.on_discount_check_box_state_changed )
        self.ui.qtAddTradingDataPushButton.clicked.connect( self.on_add_new_data_push_button_clicked )
        self.ui.qtDeleteDataPushButton.clicked.connect( self.on_delete_data_push_button_clicked )
        self.ui.qtEditDataPushButton.clicked.connect( self.on_edit_data_push_button_clicked )


    def on_discount_check_box_state_changed( self, state ):
        if state == 2:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( True )
        else:
            self.ui.qtDiscountRateDoubleSpinBox.setEnabled( False )

    def on_add_new_data_push_button_clicked( self ):
        dialog = TradingDataDialog( self.ui.qtDiscountCheckBox.isChecked(), self.ui.qtDiscountRateDoubleSpinBox.value(), self.ui.qtExtraInsuranceFeeCheckBox.isChecked(), self )

        if dialog.exec():
            dict_trading_data = dialog.dict_trading_data
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