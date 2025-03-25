@echo off
chcp 65001 >nul

rd /s /q build
rd /s /q dist

echo 🔧 Uninstalling previous version...
pip uninstall -y FoxInfoShareUtility

echo 📦 Installing library in normal mode for PyInstaller...
pip install D:\_2.code\FoxInfoShareUtility   

echo 🛠️  Building executable with PyInstaller...
pyinstaller --clean ^
            --noconfirm ^
			--hidden-import "babel.numbers" ^
            --add-data "resources;./resources" ^
			--add-data "StockInventory/Dividend;./StockInventory/Dividend" ^
			--add-data "../FoxInfoShareUtility/foxinfo_share_utility/icons;foxinfo_share_utility/icons" ^
			--noconsole StockPriceMainWindow.py

echo ♻️  Reinstalling in editable mode for development...
pip install -e D:\_2.code\FoxInfoShareUtility   

xcopy /E /I /Y resources dist\StockPriceMainWindow\resources
copy /Y 教學.pdf dist\StockPriceMainWindow
rename dist\StockPriceMainWindow\StockPriceMainWindow.exe "股票交易紀錄.exe"
rd /s /q build

powershell -Command "Compress-Archive -Path 'D:\_2.code\PythonStockPrice\dist\StockPriceMainWindow\*' -DestinationPath 'D:\_2.code\PythonStockPrice\dist\股票交易記帳程式.zip' -Force"


pause