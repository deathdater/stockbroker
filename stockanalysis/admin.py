from django.contrib import admin
from .models import QualityAnalysisScoring,StockTrendSignals
from stockmaster.models import BhavLastTenDays
from stockanalysis import fetch_trading_metrics as ft
import datetime as dt
from .tradingpatterns import *
import pandas as pd

NIFTY_FIVE_Hundred=['3MINDIA','ABB','POWERINDIA','ACC','AIAENG','APLAPOLLO','AUBANK','AARTIDRUGS','AARTIIND','AAVAS','ABBOTINDIA','ADANIENT','ADANIGREEN','ADANIPORTS','ATGL','ADANITRANS','ABCAPITAL','ABFRL','AEGISCHEM','AFFLE','AJANTPHARM','AKZOINDIA','ALEMBICLTD','APLLTD','ALKEM','ALKYLAMINE','ALOKINDS','AMARAJABAT','AMBER','AMBUJACEM','ANGELBRKG','APOLLOHOSP','APOLLOTYRE','ASAHIINDIA','ASHOKLEY','ASHOKA','ASIANPAINT','ASTERDM','ASTRAZEN','ASTRAL','ATUL','AUROPHARMA','AVANTIFEED','DMART','AXISBANK','BASF','BEML','BSE','BAJAJ-AUTO','BAJAJCON','BAJAJELEC','BAJFINANCE','BAJAJFINSV','BAJAJHLDNG','BALAMINES','BALKRISIND','BALMLAWRIE','BALRAMCHIN','BANDHANBNK','BANKBARODA','BANKINDIA','MAHABANK','BATAINDIA','BAYERCROP','BERGEPAINT','BDL','BEL','BHARATFORG','BHEL','BPCL','BHARATRAS','BHARTIARTL','BIOCON','BIRLACORPN','BSOFT','BLISSGVS','BLUEDART','BLUESTARCO','BBTC','BOSCHLTD','BRIGADE','BRITANNIA','BURGERKING','CCL','CESC','CRISIL','CSBBANK','CADILAHC','CANFINHOME','CANBK','CAPLIPOINT','CGCL','CARBORUNIV','CASTROLIND','CEATLTD','CENTRALBK','CDSL','CENTURYPLY','CENTURYTEX','CERA','CHALET','CHAMBLFERT','CHOLAHLDNG','CHOLAFIN','CIPLA','CUB','COALINDIA','COCHINSHIP','COFORGE','COLPAL','CAMS','CONCOR','COROMANDEL','CROMPTON','CUMMINSIND','CYIENT','DCBBANK','DCMSHRIRAM','DLF','DABUR','DALBHARAT','DEEPAKNTR','DELTACORP','DHANI','DHANUKA','DISHTV','DCAL','DIVISLAB','DIXON','LALPATHLAB','DRREDDY','EIDPARRY','EIHOTEL','EPL','EDELWEISS','EICHERMOT','ELGIEQUIP','EMAMILTD','ENGINERSIN','EQUITAS','ERIS','ESCORTS','EXIDEIND','FDC','FEDERALBNK','FINEORG','FINCABLES','FINPIPE','FSL','FORTIS','FCONSUMER','FRETAIL','GAIL','GEPIL','GMMPFAUDLR','GMRINFRA','GALAXYSURF','GRSE','GARFIBRES','GICRE','GILLETTE','GLAND','GLAXO','GLENMARK','GODFRYPHLP','GODREJAGRO','GODREJCP','GODREJIND','GODREJPROP','GRANULES','GRAPHITE','GRASIM','GESHIP','GREAVESCOT','GRINDWELL','GUJALKALI','GAEL','FLUOROCHEM','GUJGASLTD','GNFC','GPPL','GSFC','GSPL','GULFOILLUB','HEG','HCLTECH','HDFCAMC','HDFCBANK','HDFCLIFE','HFCL','HAPPSTMNDS','HATSUN','HAVELLS','HEIDELBERG','HEMIPROP','HEROMOTOCO','HSCL','HINDALCO','HAL','HINDCOPPER','HINDPETRO','HINDUNILVR','HINDZINC','HONAUT','HUDCO','HDFC','HUHTAMAKI','ICICIBANK','ICICIGI','ICICIPRULI','ISEC','IDBI','IDFCFIRSTB','IDFC','IFBIND','IIFL','IIFLWAM','IOLCP','IRB','IRCON','ITC','ITI','INDIACEM','IBULHSGFIN','IBREALEST','INDIAMART','INDIANB','IEX','INDHOTEL','IOC','IOB','IRCTC','ICIL','INDOCO','IGL','INDUSINDBK','INFIBEAM','NAUKRI','INFY','INGERRAND','INOXLEISUR','INTELLECT','INDIGO','IPCALAB','JBCHEPHARM','JKCEMENT','JKLAKSHMI','JKPAPER','JKTYRE','JMFINANCIL','JSWENERGY','JSWSTEEL','JTEKTINDIA','JAMNAAUTO','JINDALSAW','JSLHISAR','JSL','JINDALSTEL','JCHAC','JUBLFOOD','JUSTDIAL','JYOTHYLAB','KPRMILL','KEI','KNRCON','KPITTECH','KRBL','KSB','KAJARIACER','KALPATPOWR','KANSAINER','KARURVYSYA','KSCL','KEC','KOTAKBANK','L&TFH','LICHSGFIN','LAOPALA','LAXMIMACH','LT','LAURUSLABS','LEMONTREE','LINDEINDIA','LUPIN','LUXIND','MASFIN','MMTC','MOIL','MRF','MGL','MAHSCOOTER','MAHSEAMLES','M&MFIN','M&M','MAHINDCIE','MHRIL','MAHLOG','MANAPPURAM','MRPL','MARICO','MARUTI','MFSL','MAXHEALTH','MAZDOCK','METROPOLIS','MINDTREE','MINDACORP','MINDAIND','MIDHANI','MOTILALOFS','MPHASIS','MCX','MUTHOOTFIN','NATCOPHARM','NBCC','NCC','NESCO','NHPC','NLCINDIA','NMDC','NOCIL','NTPC','NH','NATIONALUM','NFL','NAVINFLUOR','NESTLEIND','NETWORK18','NILKAMAL','NAM-INDIA','OBEROIRLTY','ONGC','OIL','OFSS','ORIENTELEC','PIIND','PNCINFRA','PVR','PAGEIND','PERSISTENT','PETRONET','PFIZER','PHILIPCARB','PHOENIXLTD','PIDILITIND','PEL','POLYMED','POLYCAB','POLYPLEX','PFC','POWERGRID','PRESTIGE','PRINCEPIPE','PRSMJOHNSN','PGHL','PGHH','PNB','QUESS','RECLTD','RHIM','RITES','RADICO','RVNL','RAIN','RAJESHEXPO','RALLIS','RCF','RATNAMANI','RAYMOND','REDINGTON','RELAXO','RELIANCE','RESPONIND','ROSSARI','ROUTE','SBICARD','SBILIFE','SIS','SJVN','SKFINDIA','SRF','SANOFI','SCHAEFFLER','SCHNEIDER','SEQUENT','SHARDACROP','SFL','SHILPAMED','SCI','SHOPERSTOP','SHREECEM','SHRIRAMCIT','SRTRANSFIN','SIEMENS','SOBHA','SOLARINDS','SOLARA','SONATSOFTW','SPANDANA','SPICEJET','STARCEMENT','SBIN','SAIL','STLTECH','STAR','SUDARSCHEM','SUMICHEM','SPARC','SUNPHARMA','SUNTV','SUNCLAYLTD','SUNDARMFIN','SUNDRMFAST','SUNTECK','SUPRAJIT','SUPREMEIND','SUPPETRO','SUZLON','SWANENERGY','SYMPHONY','SYNGENE','TCIEXP','TTKPRESTIG','TV18BRDCST','TVSMOTOR','TANLA','TATACHEM','TATACOFFEE','TATACOMM','TCS','TATACONSUM','TATAELXSI','TATAINVEST','TATAMTRDVR','TATAMOTORS','TATAPOWER','TATASTEEL','TEAMLEASE','TECHM','NIACL','RAMCOCEM','THERMAX','THYROCARE','TIMKEN','TITAN','TORNTPHARM','TORNTPOWER','TRENT','TRIDENT','TRITURBINE','TIINDIA','UCOBANK','UFLEX','UPL','UJJIVAN','UJJIVANSFB','ULTRACEMCO','UNIONBANK','UBL','MCDOWELL-N','VGUARD','VMART','VIPIND','VSTIND','VAIBHAVGBL','VAKRANGEE','VTL','VEDL','VENKEYS','VINATIORGA','IDEA','VOLTAS','WABCOINDIA','WELCORP','WELSPUNIND','WESTLIFE','WHIRLPOOL','WIPRO','WOCKPHARMA','YESBANK','ZEEL','ZENSARTECH','ZYDUSWELL','ECLERX',]
# Register your models here.
def clear_data(request,modeladmin,queryset):
    stock_data=StockTrendSignals.objects.all().delete()
    # stock_data.save()

def load_all_stocks(request,modeladmin,queryset):
    mkt_date=BhavLastTenDays.objects.last().mkt_date-dt.timedelta(days=0)
    print(str(mkt_date))
    stockdata=BhavLastTenDays.objects.filter(mkt_date=mkt_date,open_price__gt=100.0,is_index=False,series='EQ')
    print(len(stockdata))
    for stock in stockdata:
        stock_trend=StockTrendSignals(stock_symbol=stock.symbol,stock_name=stock.security,bullish_engulfing_signal='No Signal',bullish_harami_signal='No Signal',piercing_pattern_signal='No Signal',morning_star_signal='No Signal')
        stock_trend.save()
# checking for head &shoulder pattern
def check_head_n_shoulder(request,modeladmin,queryset):
    
    for stock in queryset:
        symbol=stock.stock_symbol
        stockdata = BhavLastTenDays.objects.filter(symbol=symbol).order_by('mkt_date')[:10]
        open_prices=[]
        high_prices=[]
        low_prices=[]
        close_prices=[]
        prev_close_prices=[]
        movement_range=[]
        mkt_dates=[]
        # Adding volume data for OHLCV Data
        volumes=[]
        if len(stockdata)>6:
            for day in range(7):
                # print(stockdata[day].mkt_date)
                mkt_dates.append(stockdata[day].mkt_date)
                open_prices.append(stockdata[day].open_price)
                high_prices.append(stockdata[day].high_price)
                low_prices.append(stockdata[day].low_price)
                close_prices.append(stockdata[day].close_price)
                prev_close_prices.append(stockdata[day].prev_close_price)
                movement_range.append(abs(open_prices[day]-close_prices[day]))
                volumes.append(stockdata[day].net_trade_qty)
            average_movement=sum(movement_range)/len(movement_range)
            date_rng=pd.date_range(start=str(mkt_dates[0]),end=str(mkt_dates[-1]),freq='D')
            data={'date':date_rng[:7]}
            #    data['Date']=mkt_dates
            data['Open']=open_prices
            data['High']=high_prices
            data['Low']=low_prices
            data['Close']=close_prices
            data['Volume']= volumes
            df = pd.DataFrame(data)
            # print(df)
            df_new=detect_head_shoulder(df)
            if(df_new[df_new['head_shoulder_pattern'].any=='Head and Shoulder']):
                print('HAS HEAD & SHOULDERS  '+symbol)
                print(df_new['head_shoulder_pattern'])

    
        

    
def analyse_ten_day_data(request,modeladmin,queryset):
    for stock in queryset:
        symbol=stock.stock_symbol
        stockdata = BhavLastTenDays.objects.filter(symbol=symbol).order_by('mkt_date')[:10]
        open_prices=[]
        high_prices=[]
        low_prices=[]
        close_prices=[]
        prev_close_prices=[]
        movement_range=[]
        # Adding volume data for OHLCV Data
        volumes=[]
        if len(stockdata)>6:
            for day in range(7):
                print(stockdata[day].mkt_date)
                open_prices.append(stockdata[day].open_price)
                high_prices.append(stockdata[day].high_price)
                low_prices.append(stockdata[day].low_price)
                close_prices.append(stockdata[day].close_price)
                prev_close_prices.append(stockdata[day].prev_close_price)
                movement_range.append(abs(open_prices[day]-close_prices[day]))
                volumes.append[stockdata[day].net_trade_qty]
            average_movement=sum(movement_range)/len(movement_range)
            # bullish engulfing
            
            bullish_engulfing=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]<close_prices[5]) and (close_prices[6]>open_prices[5]) 
            piercing_pattern=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]<close_prices[5]) and (close_prices[4]>(abs(open_prices[3]-close_prices[3])/2))
            bullish_harami=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]>close_prices[5]) and (close_prices[4]<open_prices[3])
            morning_star=(close_prices[1]<open_prices[1]) and (close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]-open_prices[4]<0)and abs(open_prices[5]-close_prices[4])<average_movement and (close_prices[6]-open_prices[6]>0) and (close_prices[6]>(abs(open_prices[4]-close_prices[4])/2))
            if bullish_engulfing :
                stock.bullish_engulfing_signal='Buy'
            else:
                stock.bullish_engulfing_signal='No Signal'
            if piercing_pattern :
                stock.piercing_pattern_signal='Buy'
            else:
                stock.piercing_pattern_signal='No Signal'
            if bullish_harami :
                stock.bullish_harami_signal='Buy'
            else:
                stock.bullish_harami_signal='No Signal'
            
            if morning_star:
                stock.morning_star_signal='Buy'
            else:
                stock.morning_star_signal='No Signal'
            
            stock.save()
        else:
            stock.delete()
        
        # print('bullish engulfing value is: ',bullish_engulfing)

        # print(open_prices,high_prices,low_prices,close_prices,prev_close_prices,sep='\n')
        # print('average is',sum(movement_range)/len(movement_range))
def investpy_analyse_ten_day_data(request,modeladmin,queryset):
    for stock in queryset:
        symbol=stock.stock_symbol
        
        # BhavLastTenDays.objects.filter(symbol=symbol).order_by('mkt_date')[:10]
        open_prices=[]
        high_prices=[]
        low_prices=[]
        close_prices=[]
        # prev_close_prices=[]
        movement_range=[]
        try :
            if symbol in NIFTY_FIVE_Hundred and symbol != 'VBL' and symbol !='VALIANTORG':
                stockdata = ft.fetch_recent_data(symbol).tail(10)
                open_prices=stockdata['Open'][3:10]
                close_prices=stockdata['Close'][3:10]
                print(close_prices)
                high_prices=stockdata['High'][3:10]
                print(high_prices)
                low_prices=stockdata['Low'][3:10]
                print(low_prices)
                movement_range=high_prices-low_prices
                print(movement_range)
                average_movement=movement_range.mean()
                print(average_movement)
                bullish_engulfing=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]<close_prices[5]) and (close_prices[6]>open_prices[5]) 
                piercing_pattern=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]<close_prices[5]) and (close_prices[4]>(abs(open_prices[3]-close_prices[3])/2))
                bullish_harami=(close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]<open_prices[4]) and (close_prices[5]-open_prices[5]<0)and (open_prices[6]<open_prices[5])and (open_prices[6]>close_prices[5]) and (close_prices[4]<open_prices[3])
                morning_star=(close_prices[1]<open_prices[1]) and (close_prices[2]<open_prices[2]) and (close_prices[3]<open_prices[3]) and (close_prices[4]-open_prices[4]<0)and abs(open_prices[5]-close_prices[4])<average_movement and (close_prices[6]-open_prices[6]>0) and (close_prices[6]>(abs(open_prices[4]-close_prices[4])/2))
                if bullish_engulfing :
                    stock.bullish_engulfing_signal='Buy'
                else:
                    stock.bullish_engulfing_signal='No Signal'
                if piercing_pattern :
                    stock.piercing_pattern_signal='Buy'
                else:
                    stock.piercing_pattern_signal='No Signal'
                if bullish_harami :
                    stock.bullish_harami_signal='Buy'
                else:
                    stock.bullish_harami_signal='No Signal'
                
                if morning_star:
                    stock.morning_star_signal='Buy'
                else:
                    stock.morning_star_signal='No Signal'
                
                stock.save()
                
            else:
                stock.delete()
        
        except:
            print("Not Found: "+str(symbol))

        


def get_trendy_stocks(request,modeladmin,queryset):
    stocks={}
    # stocks_investpy={}
    for stock in queryset:
        # stock_data=ft.fetch_recent_data(stock.stock_symbol)

        if stock.bullish_engulfing_signal=='Buy' or stock.bullish_harami_signal=='Buy' or stock.piercing_pattern_signal =='Buy' or stock.morning_star_signal=='Buy':
            stocks[str(stock.stock_symbol)]=[]
            if stock.bullish_engulfing_signal=='Buy':
                stocks[str(stock.stock_symbol)].append('bullish_engulfing')
            if stock.bullish_harami_signal=='Buy' :
                stocks[str(stock.stock_symbol)].append('bullish_harami')
            if stock.piercing_pattern_signal =='Buy':
                stocks[str(stock.stock_symbol)].append('piercing_pattern')
            if stock.morning_star_signal=='Buy':
                stocks[str(stock.stock_symbol)].append('morning_star')
    print(stocks)



class TenDayAnalysisAdmin(admin.ModelAdmin):
    actions=[analyse_ten_day_data,load_all_stocks,get_trendy_stocks,clear_data,investpy_analyse_ten_day_data,check_head_n_shoulder]
    list_display=['stock_symbol','stock_name','bullish_engulfing_signal','bullish_harami_signal','piercing_pattern_signal','morning_star_signal']
    search_fields=['stock_symbol','stock_name']
    list_filter=('bullish_engulfing_signal','bullish_harami_signal','piercing_pattern_signal','morning_star_signal')

admin.site.register(StockTrendSignals,TenDayAnalysisAdmin)
admin.site.register(QualityAnalysisScoring)
