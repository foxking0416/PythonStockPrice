import foxinfo_share_utility.share_api as share_api
from bs4 import BeautifulSoup
import json
import re

class Download():

    @staticmethod
    def download_company_stock_number():
        tds = []
        # 上市公司股票代碼
        companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=2"
        try:
            res = share_api.send_get_request( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )

            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td" )]
                if len( data ) == 7 and ( data[ 5 ] == 'ESVUFR' or 
                                          data[ 5 ] == 'ESVTFR' or
                                          data[ 5 ] == 'CEOGBU' or
                                          data[ 5 ] == 'CEOGCU' or
                                          data[ 5 ] == 'CEOGDU' or 
                                          data[ 5 ] == 'CEOGEU' or 
                                          data[ 5 ] == 'CEOGMU' or
                                          data[ 5 ] == 'CEOJBU' or 
                                          data[ 5 ] == 'CEOJEU' or
                                          data[ 5 ] == 'CEOJLU' or
                                          data[ 5 ] == 'CEOIBU' or
                                          data[ 5 ] == 'CEOIEU' or
                                          data[ 5 ] == 'CEOIRU' or
                                          data[ 5 ] == 'EPNRAR' or 
                                          data[ 5 ] == 'EPNRQR' or
                                          data[ 5 ] == 'EPRRQR' or
                                          data[ 5 ] == 'EPNNFB' or
                                          data[ 5 ] == 'EPRRAR' or 
                                          data[ 5 ] == 'EPNCAR' or 
                                          data[ 5 ] == 'EFNRAR' or 
                                          data[ 5 ] == 'EPNTAR' or 
                                          data[ 5 ] == 'EPRNAR' or 
                                          data[ 5 ] == 'EPNRFR' ): 
                    b_ETF = False if data[ 5 ] == 'ESVUFR' else True
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip(), b_ETF ]
                        tds.append( modified_data_after_strip )
        except Exception as e:
            pass                

        # 上櫃公司股票代碼
        companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=4"
        try:
            res = share_api.send_get_request( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )
            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td") ]
                if len( data ) == 7 and ( data[ 5 ] == 'ESVUFR' or 
                                            data[ 5 ] == 'CEOGBU' or
                                            data[ 5 ] == 'CEOGEU' or 
                                            data[ 5 ] == 'CEOJBU' or 
                                            data[ 5 ] == 'CEOIBU' or
                                            data[ 5 ] == 'CEOIEU' or
                                            data[ 5 ] == 'CEOIRU' or
                                            data[ 5 ] == 'EPNRAR'  ): 
                    b_ETF = False if data[ 5 ] == 'ESVUFR' else True
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip(), b_ETF ]
                        tds.append( modified_data_after_strip )
        except Exception as e:
            pass

        # 興櫃公司股票代碼
        companyNymUrl = "https://isin.twse.com.tw/isin/C_public.jsp?strMode=5"
        try:
            res = share_api.send_get_request( companyNymUrl )
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )
            for raw in tr:
                data = [ td.get_text() for td in raw.findAll("td") ]
                if len( data ) == 7 and data[ 5 ] == 'ESVUFR': 
                    if '\u3000' in data[ 0 ]:
                        modified_data = data[ 0 ].split("\u3000")
                        modified_data_after_strip = [ modified_data[ 0 ].strip(), modified_data[ 1 ].strip(), False ]
                        tds.append( modified_data_after_strip )
        except Exception as e:
            pass
        
        return tds
    
    @staticmethod
    def download_suspend_company_stock_number():
        tds = []
        companyNymUrl = "https://www.twse.com.tw/rwd/zh/company/suspendListing"
        try:
            res = share_api.send_get_request( companyNymUrl )
            json_data = res.json()
            if "data" in json_data:
                for item in json_data["data"]:
                    modified_data_after_strip = [ item[ 2 ].strip(), item[ 1 ].strip(), False, item[ 0 ].strip() ]
                    tds.append( modified_data_after_strip )
        except Exception as e:
            pass

        return tds
    
    @staticmethod
    def download_listed_stock_price_by_date( str_date ):
        all_stock_price = []
        # 上市公司股價從證交所取得
        # https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=20240912&type=ALLBUT0999&response=json&_=1726121461234
        url = 'https://www.twse.com.tw/rwd/zh/afterTrading/MI_INDEX?date=' + str_date + '&type=ALLBUT0999&response=json&_=1726121461234'
        try:
            res = share_api.send_get_request( url )
            soup = BeautifulSoup( res.content, 'html.parser' )

            json_str = soup.get_text()
            json_data = json.loads(json_str)
            if 'tables' in json_data:
                for item in json_data['tables']:
                    if 'title' in item:
                        if '每日收盤行情' in item['title']:
                            for data in item['data']:
                                #index 0 證券代號    "0050",
                                #index 1 證券名稱    "元大台灣50",
                                #index 2 成交股數    "16,337,565",
                                #index 3 成交筆數    "15,442",
                                #index 4 成交金額    "2,900,529,886",
                                #index 5 開盤價      "176.10",
                                #index 6 最高價      "178.65",
                                #index 7 最低價      "176.10",
                                #index 8 收盤價      "178.30",
                                #index 9 漲跌(+/-)   "<p style= color:red>+<\u002fp>",
                                #index 10 漲跌價差    "6.45",
                                #index 11 最後揭示買價 "178.20",
                                #index 12 最後揭示買量 "5",
                                #index 13 最後揭示賣價 "178.30",
                                #index 14 最後揭示賣量 "103",
                                #index 15 本益比 

                                list_stock_price = [ data[ 0 ], data[ 1 ], data[ 8 ].replace( ',', '' ) ] 
                                all_stock_price.append( list_stock_price )
        except Exception as e:
            pass
        return all_stock_price

    @staticmethod
    def download_OTC_stock_price_by_date( str_date ):
        all_stock_price = []
        # 上櫃公司股價從櫃買中心取得
        # https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes?date=2024%2F12%2F09&id=&response=html
        formatted_date = f"{str_date[:4]}%2F{str_date[4:6]}%2F{str_date[6:]}"
        url = 'https://www.tpex.org.tw/www/zh-tw/afterTrading/dailyQuotes?date=' + formatted_date + '&id=&response=html'
        try:
            res = share_api.send_get_request( url )
            
            soup = BeautifulSoup( res.text, "lxml" )
            tr = soup.findAll( 'tr' )
            for raw in tr:
                if not raw.find( 'th' ):
                    td_elements = raw.findAll( "td" )
                    if len( td_elements ) == 19:
                        # index 0 證券代號	
                        # index 1 證券名稱	
                        # index 2 收盤	
                        # index 3 漲跌	
                        # index 4 開盤
                        # index 5 最高	
                        # index 6 最低
                        # index 7 均價	
                        # index 8 成交股數
                        # index 9 成交金額(元)
                        # index 10 成交筆數	
                        # index 11 最後買價	
                        # index 12 最後買量(千股)	2020/4/29 開始才有這筆資訊
                        # index 13 最後賣價	
                        # index 14 最後賣量(千股)   2020/4/29 開始才有這筆資訊
                        # index 15 發行股數	次日
                        # index 16 參考價	次日
                        # index 17 漲停價	次日
                        # index 18 跌停價
                        str_stock_number = td_elements[ 0 ].get_text().strip()
                        str_stock_name = td_elements[ 1 ].get_text().strip()
                        str_stock_price = td_elements[ 2 ].get_text().strip()
                        list_stock_price = [ str_stock_number, str_stock_name, str_stock_price.replace( ',', '' ) ] 
                        all_stock_price.append( list_stock_price )
        except Exception as e:
            pass 
        return all_stock_price   

    @staticmethod
    def download_ROTC_stock_price_by_date( str_date ):
        all_stock_price = []
        formatted_date = f"{str_date[:4]}/{str_date[4:6]}/{str_date[6:]}"
        url = "https://www.tpex.org.tw/www/zh-tw/emerging/des010"
        payload = {
            'date': formatted_date
        }
        try:
            res = share_api.send_post_request( url, payload )
            soup = BeautifulSoup( res.text, "lxml" )
            json_str = soup.get_text()
            json_data = json.loads(json_str)
            if 'tables' in json_data:
                for item in json_data['tables']:
                    if 'data' in item:
                        for data in item['data']:
                            #index 0 證券代號       "1260",
                            #index 1 證券名稱       "富味鄉",
                            #index 2 最後最佳報買價  "23.00",
                            #index 3 最後最佳報賣價  "23.55",
                            #index 4 日均價         "23.50",
                            #index 5 前日均價       "23.54",
                            #index 6 漲跌           "-0.04",
                            #index 7 漲跌幅         "-0.17",
                            #index 8 最高           "23.65",
                            #index 9 最低           "23.45",
                            #index 10 最後          "23.55",
                            #index 11 成交量        "4074",
                            #index 12 成交金額      "95742",
                            #index 13 筆數          "5",
                            #index 14 發行股數      "102098182",
                            #index 15 上市櫃進度日期 
                            #index 16 上市櫃進度 
                            list_stock_price = [ data[ 0 ], data[ 1 ], data[ 4 ].replace( ',', '' ) ] 
                            all_stock_price.append( list_stock_price )
        except Exception as e:
                pass
        return all_stock_price
    
    @staticmethod
    def download_general_company_dividend_by_year( n_year ):
        general_company_dividend = []
        url = 'https://mopsov.twse.com.tw/mops/web/ajax_t108sb27'

        payload = {
            # 'TYPEK': 'sii' if e_company_type2 == CompanyType2.LISTED else 'otc',
            'encodeURIComponent': '1',
            'firstin': '1',
            'off': '1',
            'step': '1',
            'year': str(n_year)
        }

        try:
            for n_type in range( 3 ):
                if n_type == 0:
                    payload[ 'TYPEK' ] = 'sii'
                elif n_type == 1:
                    payload[ 'TYPEK' ] = 'otc'
                else:
                    payload[ 'TYPEK' ] = 'rotc'
                res = share_api.send_post_request( url, payload )

                soup = BeautifulSoup( res.text, "lxml" )
                tr = soup.findAll( 'tr' )
                for raw in tr:
                    if not raw.find( 'th' ):
                        data = []
                        td_elements = raw.findAll( "td" )
                        if n_year >= 94 and n_year < 105:
                            if len( td_elements ) == 23:
                                # [0]公司代號
                                # [1]公司名稱	
                                # [2]股利所屬年度	
                                # [3]權利分派基準日	
                                # [4]股票股利_盈餘轉增資配股(元/股)
                                # [5]股票股利_法定盈餘公積、資本公積轉增資配股(元/股)
                                # [6]股票股利_除權交易日
                                # X [7]配股總股數(股)
                                # X [8]配股總金額(元)
                                # X [9]配股總股數佔盈餘配股總股數之比例(%)
                                # X [10]員工紅利配股率
                                # [11]現金股利_盈餘分配之股東現金股利(元/股)
                                # [12]現金股利_法定盈餘公積、資本公積發放之現金(元/股)
                                # [13]現金股利_除息交易日
                                # [14]現金股利_現金股利發放日
                                # X [15]員工紅利總金額(元)
                                # [16]現金增資總股數(股)	
                                # [17]現金增資認股比率(%)	
                                # [18]現金增資認購價(元/股)		
                                # X [19]董監酬勞(元)
                                # [20]公告日期
                                # [21]公告時間
                                # [22]普通股每股面額
                                for index, td in enumerate( td_elements ):
                                    text = td.get_text().strip()
                                    if index == 4 or index == 5 or index == 11 or index == 12 or index == 17 or index == 18:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = float( text.replace( ',', '' ) ) 
                                            data.append( number )
                                        if index == 12:
                                            data.append( 0 ) # 為了跟後續的格式有一致性，因為105年之後的表格有「現金股利_特別股配發現金股利(元/股)」，但因為現在沒有，所以直接補0
                                    elif index == 16:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = int( text.replace( ',', '' ) ) 
                                            data.append( number )
                                    elif index == 7 or index == 8 or index == 9 or index == 10 or index == 15 or index == 19:
                                        continue
                                    else:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( '--' )
                                        else:
                                            data.append( text )

                                general_company_dividend.append( data )
                        elif n_year >= 105 and n_year < 108:
                            if len( td_elements ) == 18:
                                # [0]公司代號,
                                # [1]公司名稱,
                                # [2]股利所屬期間,
                                # [3]權利分派基準日,
                                # [4]股票股利_盈餘轉增資配股(元/股),
                                # [5]股票股利_法定盈餘公積、資本公積轉增資配股(元/股),                        
                                # [6]股票股利_除權交易日,
                                # [7]現金股利_盈餘分配之股東現金股利(元/股),
                                # [8]現金股利_法定盈餘公積、資本公積發放之現金(元/股),
                                # [9]現金股利_特別股配發現金股利(元/股),                        
                                # [10]現金股利_除息交易日,
                                # [11]現金股利_現金股利發放日,
                                # [12]現金增資總股數(股),
                                # [13]現金增資認股比率(%),
                                # [14]現金增資認購價(元/股),                        
                                # [15]公告日期,
                                # [16]公告時間,
                                # [17]普通股每股面額
                                for index, td in enumerate( td_elements ):
                                    text = td.get_text().strip()
                                    if index == 4 or index == 5 or index == 7 or index == 8 or index == 9 or index == 13 or index == 14:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = float( text.replace( ',', '' ) ) 
                                            data.append( number )
                                    elif index == 12:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = int( text.replace( ',', '' ) ) 
                                            data.append( number )
                                    else:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( '--' )
                                        else:
                                            data.append( text )

                                general_company_dividend.append( data )
                        elif n_year >= 108:
                            if len( td_elements ) == 19:
                                # [0]公司代號,
                                # [1]公司名稱,
                                # [2]股利所屬期間,
                                # [3]權利分派基準日,
                                # [4]股票股利_盈餘轉增資配股(元/股),
                                # [5]股票股利_法定盈餘公積、資本公積轉增資配股(元/股),                        
                                # [6]股票股利_除權交易日,
                                # [7]現金股利_盈餘分配之股東現金股利(元/股),
                                # [8]現金股利_法定盈餘公積、資本公積發放之現金(元/股),
                                # [9]現金股利_特別股配發現金股利(元/股),                        
                                # [10]現金股利_除息交易日,
                                # [11]現金股利_現金股利發放日,
                                # [12]現金增資總股數(股),
                                # [13]現金增資認股比率(%),
                                # [14]現金增資認購價(元/股),                        
                                # [15]參加分派總股數,
                                # [16]公告日期,
                                # [17]公告時間,
                                # [18]普通股每股面額
                                for index, td in enumerate( td_elements ):
                                    text = td.get_text().strip()
                                    if index == 4 or index == 5 or index == 7 or index == 8 or index == 9 or index == 13 or index == 14:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = float( text.replace( ',', '' ) ) 
                                            data.append( number )
                                    elif index == 12:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( 0 )
                                        else:
                                            number = int( text.replace( ',', '' ) ) 
                                            data.append( number )
                                    elif index == 15:
                                        continue
                                    else:
                                        if text == '\xa0' or text == ''  or text == '-' or text == '--':
                                            data.append( '--' )
                                        else:
                                            data.append( text )

                                general_company_dividend.append( data )
        except Exception as e:
            print(f"Final error: {e}")
        return general_company_dividend

    @staticmethod
    def download_listed_etf_dividend_by_year( n_year ):
        return_json_value = None
        url = "https://www.twse.com.tw/rwd/zh/ETF/etfDiv?stkNo=&startDate=" + str( n_year ) + "0101&endDate=" + str( n_year ) + "0101&response=json&_=1734754779791"
        try:
            res = share_api.send_get_request( url )
            return_json_value = json.loads( res.text )
        except Exception as e:
            print(f"Final error: {e}")

        return return_json_value

    @staticmethod
    def download_OTC_etf_dividend_by_year( n_year ):
        return_json_value = None
        url = 'https://www.tpex.org.tw/www/zh-tw/bulletin/exDailyQ'

        if n_year < 1990:
            n_year += 1911
        # POST 請求的數據
        payload = {
            'startDate': str( n_year ) + '/01/01',
            'endDate': str( n_year ) + '/12/31',
            'response': 'json'
        }

        try:
            res = share_api.send_post_request( url, payload )
            return_json_value = json.loads( res.text )
        except Exception as e:
            print(f"Final error: {e}")

        return return_json_value
    
    @staticmethod
    def download_listed_stock_split_by_year( n_start_year, n_end_year ): #上市公司 分割、反分割
        return_json_value = None
        # https://www.twse.com.tw/rwd/zh/change/TWTB8U?startDate=20240101&endDate=20241231&response=json&_=1745546342137
        url = "https://www.twse.com.tw/rwd/zh/change/TWTB8U?startDate=" + str( n_start_year ) + "0101&endDate=" + str( n_end_year ) + "1231&response=json&_=1745546342137"
        try:
            res = share_api.send_get_request( url )
            return_json_value = json.loads( res.text )
        except Exception as e:
            print(f"Final error: {e}")

        return return_json_value
    
    @staticmethod
    def download_OTC_and_ROTC_stock_split_merge(): #上櫃、興櫃公司 分割、反分割
        results = []
        url = "https://www.tpex.org.tw/zh-tw/mainboard/listed/flexible-face-value.html"
        try:
            res = share_api.send_get_request( url )
            res.encoding = 'utf-8'  # 設定正確編碼
            soup = BeautifulSoup( res.text, "lxml" )
            table = soup.find("table", class_="infotable align_c")
            for row in table.find_all("tr")[1:]:
                cols = row.find_all("td")
                if len(cols) == 8:
                    stock_code = cols[2].get_text(strip=True)
                    change_date = cols[5].get_text(strip=True)
                    face_value = cols[6].get_text(strip=True)
                elif len(cols) == 7:
                    stock_code = cols[1].get_text(strip=True)
                    change_date = cols[4].get_text(strip=True)
                    face_value = cols[5].get_text(strip=True)
                if '-' != change_date and change_date.count('.') >= 2 and change_date.count('.') % 2 == 0:
                    dates = re.findall(r'\d{3}\.\d{2}\.\d{2}', change_date)
                    values = re.findall(r"新台幣.*?元", face_value)
                    if len( dates ) == len( values ):
                        for i in range( len( dates ) ):
                            change_date = dates[ i ]
                            face_value = values[ i ]
                            results.append( [ stock_code, change_date, face_value ] )
        except Exception as e:
            print(f"Final error: {e}")

        return results

    @staticmethod
    def download_listed_etf_split_merge_by_year( n_start_year, n_end_year ): #上市 etf 分割、反分割
        # https://www.twse.com.tw/rwd/zh/split/TWTCAU?startDate=20240101&endDate=20250219&response=json&_=1745559156488
        return_json_value = None
        url = "https://www.twse.com.tw/rwd/zh/split/TWTCAU?startDate=" + str( n_start_year ) + "0101&endDate=" + str( n_end_year ) + "1231&response=json&_=1745559156488"
        try:
            res = share_api.send_get_request( url )
            return_json_value = json.loads( res.text )
        except Exception as e:
            print(f"Final error: {e}")

        return return_json_value['data']

    @staticmethod
    def download_OTC_etf_split_merge_by_year(): #上櫃 etf 分割
        # 上櫃的 etf 尚未有任何分割 反分割的資料
        pass

    @staticmethod
    def download_listed_company_capital_reduction_by_year( n_start_year, n_end_year ): #上市公司 減資
        # https://www.twse.com.tw/rwd/zh/reducation/TWTAUU?startDate=20110101&endDate=20250425&response=json&_=1745560741649
        return_json_value = []
        url = "https://www.twse.com.tw/rwd/zh/reducation/TWTAUU?startDate=" + str( n_start_year ) + "0101&endDate=" + str( n_end_year ) + "1231&response=json&_=1745560741649"
        try:
            res = share_api.send_get_request( url )
            json_value_from_request = json.loads( res.text )
        except Exception as e:
            print(f"Final error: {e}")

        for per_data in json_value_from_request['data']:
            # per_reduction_url = "https://www.twse.com.tw/zh/announcement/reduction/twtavu-detail.html?" + per_data[10].replace( ' ', '' )
            list_number_and_date = per_data[10].replace( ' ', '' ).split( ',' )
            per_reduction_url = "https://www.twse.com.tw/rwd/zh/reducation/TWTAVUDetail?STK_NO=" + list_number_and_date[ 0 ] + "&FILE_DATE=" + list_number_and_date[ 1 ] + "&response=json&_=1745569612993"
            try:
                res = share_api.send_get_request( per_reduction_url )
                json_value_per_reduction_from_request = json.loads( res.text )
                per_data.append( json_value_per_reduction_from_request['data'][ 0 ][ 3 ] )
                per_data.append( json_value_per_reduction_from_request['data'][ 0 ][ 4 ] )
                return_json_value.append( per_data )
            except Exception as e:
                print(f"Final error: {e}")

        return return_json_value
    
    @staticmethod
    def download_OTC_company_capital_reduction_by_year( n_start_year, n_end_year ): #上櫃公司 減資
        return_json_value = []
        url = "https://www.tpex.org.tw/www/zh-tw/bulletin/revivt?startDate=" + str( n_start_year ) + "%2F01%2F01&endDate=" + str( n_end_year ) + "%2F12%2F31&id="
        try:
            res = share_api.send_get_request( url )
            json_value_from_request = json.loads( res.text )
            for per_data in json_value_from_request['tables'][0]['data']:
                soup = BeautifulSoup(per_data[10], "html.parser")

                target_th = soup.find("th", string="每壹仟股換發新股票:")
                if target_th:
                    value_td = target_th.find_next_sibling("td")
                    if value_td:
                        result = value_td.get_text(strip=True)
                        clean_text = result.replace('\xa0', '').replace('股', '').strip()
                        per_data[10] = clean_text
                        return_json_value.append( per_data )
        except Exception as e:
            print(f"Final error: {e}")

        return return_json_value