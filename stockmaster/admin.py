from django.contrib import admin
from django.contrib.admin import ModelAdmin
from stockmaster.models import BhavcopyMasterPR,FilterStocks,BhavLastTenDays,BhavLastFiftyDays,BhavLastHundredDays,BhavLastFullYear
from stockanalysis.models import QualityAnalysisScoring
import os
import datetime as dt
from django.contrib import messages

# Register your models here.


def clear_data(request,modeladmin,queryset):
    stock_data=BhavLastTenDays.objects.all().delete()
def load_pd_data(request,modeladmin,queryset):
    pd_files=[]
    for files in os.walk('./data/downloads/PR/PdExtract/'):
        print(files[2].remove('.DS_Store'))
        # pd_files.append(files)
        for file in files[2]:
            f=open('./data/downloads/PR/PdExtract/'+str(file),'r',encoding='cp437')
            year='20'+file[6:8]
            month=file[4:6]
            day=file[2:4]
            mkt=False
            is_index=False
            is_nifty_fifty=False
            is_nifty_next_fifty=False
            # print(year,month,day)
            file_date=dt.date(year=int(year),month=int(month),day=int(day))
            for line in f.readlines():
                data=line.split(',')
                print(data)
                if data[3]!='SECURITY' and data[3]!='':
                    print(data[15])
                    fiftytwo_week_low=data[15].replace('\n','')
                    print(fiftytwo_week_low)
                    
                    if data[0].strip()=='Y':
                        mkt=True
                    if data[11].strip()=='Y':
                        is_index=True
                    else:
                        is_index=False
                    if data[3]=='NIFTY 50 Sec':
                        is_nifty_fifty=True
                    if data[3]=='NIFTY Next 50 Sec':
                        is_nifty_next_fifty=True
                    if data[3]=='COMPULSORY ROLLING STOCKS':
                        is_nifty_fifty=False
                        is_nifty_next_fifty=False
                    if data[3]!=' ' and data[14]!=' ':
                        if data[2]==' ':
                            data[2]=data[3].strip()
                        bhavcopy_pr=BhavcopyMasterPR(
                            mkt_date=file_date,
                            mkt=bool(mkt),
                            series=data[1].strip(),
                            symbol=data[2].strip(),
                            security=data[3].strip(),
                            prev_close_price=float(data[4].strip()),
                            open_price=float(data[5].strip()),
                            high_price=float(data[6].strip()),
                            low_price=float(data[7].strip()),
                            close_price=float(data[8].strip()),
                            net_trade_value=float(data[9].strip()),
                            net_trade_qty=float(data[10].strip()),
                            is_index=bool(is_index),
                            corp_index=data[12].strip(),
                            trades=float(data[13].strip()),
                            fiftytwo_week_high=float(data[14].strip()),
                            fiftytwo_week_low=float(fiftytwo_week_low),
                            is_nifty_fifty=bool(is_nifty_fifty),
                            is_nifty_next_fifty=bool(is_nifty_next_fifty))
                        bhavcopy_pr.save()
                # break
    messages.success(request,'Bhavcopy updated')

def load_pd_today_data(request,modeladmin,queryset):
    pd_files=[]
    for files in os.walk('./data/downloads/PR/PdExtract/'):
        print(files[2].remove('.DS_Store'))
        # pd_files.append(files)
        # for file in files[2]:
        today_date=dt.datetime.today()
        
        while (today_date.weekday()>4) :
            today_date=(today_date-dt.timedelta(days=1))
            
        today_date_str=today_date.strftime('%d%m%y')    
        today_filename='Pd'+today_date_str+'.csv'
        if (today_filename in files[2]):
            file=today_filename
            f=open('./data/downloads/PR/PdExtract/'+str(file),'r',encoding='cp437')
            year='20'+file[6:8]
            month=file[4:6]
            day=file[2:4]
            mkt=False
            is_index=False
            is_nifty_fifty=False
            is_nifty_next_fifty=False
            # print(year,month,day)
            file_date=dt.date(year=int(year),month=int(month),day=int(day))
            for line in f.readlines():
                data=line.split(',')
                print(data)
                if data[3]!='SECURITY' and data[3]!='':
                    print(data[15])
                    fiftytwo_week_low=data[15].replace('\n','')
                    print(fiftytwo_week_low)
                    
                    if data[0].strip()=='Y':
                        mkt=True
                    if data[11].strip()=='Y':
                        is_index=True
                    else:
                        is_index=False
                    if data[3]=='NIFTY 50 Sec':
                        is_nifty_fifty=True
                    if data[3]=='NIFTY Next 50 Sec':
                        is_nifty_next_fifty=True
                    if data[3]=='COMPULSORY ROLLING STOCKS':
                        is_nifty_fifty=False
                        is_nifty_next_fifty=False
                    if data[3]!=' ' and data[14]!=' ':
                        if data[2]==' ':
                            data[2]=data[3].strip()
                        bhavcopy_pr=BhavcopyMasterPR(
                            mkt_date=file_date,
                            mkt=bool(mkt),
                            series=data[1].strip(),
                            symbol=data[2].strip(),
                            security=data[3].strip(),
                            prev_close_price=float(data[4].strip()),
                            open_price=float(data[5].strip()),
                            high_price=float(data[6].strip()),
                            low_price=float(data[7].strip()),
                            close_price=float(data[8].strip()),
                            net_trade_value=float(data[9].strip()),
                            net_trade_qty=float(data[10].strip()),
                            is_index=bool(is_index),
                            corp_index=data[12].strip(),
                            trades=float(data[13].strip()),
                            fiftytwo_week_high=float(data[14].strip()),
                            fiftytwo_week_low=float(fiftytwo_week_low),
                            is_nifty_fifty=bool(is_nifty_fifty),
                            is_nifty_next_fifty=bool(is_nifty_next_fifty))
                        bhavcopy_pr.save()
                # break
    # messages.success(request,"Today's Bhavcopy updated")

def get_stock_tip(request,modeladmin,queryset):
    
    pass


def update_filter_stocks(request,modeladmin,queryset):
    for stock in queryset:
        latest_market_date=stock.mkt_date
    filtered_equity=BhavcopyMasterPR.objects.filter(mkt_date=latest_market_date,close_price__gte=100.0,close_price__lte=3000.0).exclude(is_nifty_fifty=False,is_nifty_next_fifty=False)
    for stock in filtered_equity:
        filtered_stock=FilterStocks.objects.create(
            mkt_date=stock.mkt_date,
            mkt=stock.mkt,
            series=stock.series,
            symbol=stock.symbol,
            security=stock.security,
            prev_close_price=stock.prev_close_price,
            open_price=stock.open_price,
            high_price=stock.high_price,
            low_price=stock.low_price,
            close_price=stock.close_price,
            net_trade_value=stock.net_trade_value,
            net_trade_qty=stock.net_trade_qty,
            is_index=stock.is_index,
            corp_index=stock.corp_index,
            trades=stock.trades,
            fiftytwo_week_high=stock.fiftytwo_week_high,
            fiftytwo_week_low=stock.fiftytwo_week_low,
            is_nifty_fifty=stock.is_nifty_fifty,
            is_nifty_next_fifty=stock.is_nifty_next_fifty,
            stock_investment_status_check='Failed',
            stock_correction=(stock.fiftytwo_week_high-stock.close_price)/(stock.fiftytwo_week_high))
        filtered_stock.save()
        quality_stocks=QualityAnalysisScoring.objects.all()
        if(filtered_stock not in quality_stocks):
            new_quality_stock=QualityAnalysisScoring(
                stock_industry='DEFAULT INDUSTRY',
                filtered_security_object=filtered_stock,
                return_on_capital_employed='less than 5 percent',
                earning_per_share='No',
                free_cash_flow='No',
                interest_coverage_ratio='No',
                net_profit_margin='less than 5 percent',
                dividends='No',
                government_regulations_risk='No',
                research_and_development_risk='No',
                key_person_risk='No')
            new_quality_stock.save()

        print(stock.security+','+str(stock.close_price),end='\n')
def load_pd_ten_day_data(request,modeladmin,queryset):
    pd_files=[]
    for files in os.walk('./data/downloads/PR/PdExtract/'):
        print(files[2].remove('.DS_Store'))
        # pd_files.append(files)
        # for file in files[2]:
        date_list=[]
        today_date=dt.datetime.today()
        last_date=today_date-dt.timedelta(days=10)
        while last_date.weekday()>4:
            last_date=last_date-dt.timedelta(days=1)
        new_date=last_date
        while new_date<=today_date:
            # print('in loop')
            while new_date.weekday()>4:
                new_date=new_date+dt.timedelta(days=1)
                print('inner loop')
            print('new date: ',new_date)
            print('new date: ',last_date)
            date_list.append(new_date)
            new_date=new_date+dt.timedelta(days=1)
        print(date_list)


        # while (today_date.weekday()>4) :
        #     today_date=(today_date-dt.timedelta(days=1))
        for myday in date_list:  
            today_date_str=myday.strftime('%d%m%y')    
            today_filename='Pd'+today_date_str+'.csv'
            if (today_filename in files[2]):
                file=today_filename
                f=open('./data/downloads/PR/PdExtract/'+str(file),'r',encoding='cp437')
                year='20'+file[6:8]
                month=file[4:6]
                day=file[2:4]
                mkt=False
                is_index=False
                is_nifty_fifty=False
                is_nifty_next_fifty=False
                # print(year,month,day)
                file_date=dt.date(year=int(year),month=int(month),day=int(day))
                for line in f.readlines():
                    data=line.split(',')
                    print(data)
                    if data[3]!='SECURITY' and data[3]!='':
                        print(data[15])
                        fiftytwo_week_low=data[15].replace('\n','')
                        print(fiftytwo_week_low)
                        
                        if data[0].strip()=='Y':
                            mkt=True
                        if data[11].strip()=='Y':
                            is_index=True
                        else:
                            is_index=False
                        if data[3]=='NIFTY 50 Sec':
                            is_nifty_fifty=True
                        if data[3]=='NIFTY Next 50 Sec':
                            is_nifty_next_fifty=True
                        if data[3]=='COMPULSORY ROLLING STOCKS':
                            is_nifty_fifty=False
                            is_nifty_next_fifty=False
                        if data[3]!=' ' and data[14]!=' ':
                            if data[2]==' ':
                                data[2]=data[3].strip()
                            if data[1].strip()=='EQ':
                                bhavcopy_pr=BhavLastTenDays(
                                    mkt_date=file_date,
                                    mkt=bool(mkt),
                                    series=data[1].strip(),
                                    symbol=data[2].strip(),
                                    security=data[3].strip(),
                                    prev_close_price=float(data[4].strip()),
                                    open_price=float(data[5].strip()),
                                    high_price=float(data[6].strip()),
                                    low_price=float(data[7].strip()),
                                    close_price=float(data[8].strip()),
                                    net_trade_value=float(data[9].strip()),
                                    net_trade_qty=float(data[10].strip()),
                                    is_index=bool(is_index),
                                    corp_index=data[12].strip(),
                                    trades=float(data[13].strip()),
                                    fiftytwo_week_high=float(data[14].strip()),
                                    fiftytwo_week_low=float(fiftytwo_week_low),
                                    is_nifty_fifty=bool(is_nifty_fifty),
                                    is_nifty_next_fifty=bool(is_nifty_next_fifty))
                                bhavcopy_pr.save()




class BhavCopyLoaderAdmin(admin.ModelAdmin):
    actions=[load_pd_data,load_pd_today_data,update_filter_stocks]
    list_display=[]
    search_fields=[]

class BhavCopyTenLoadedAdmin(admin.ModelAdmin):
    actions=[load_pd_ten_day_data,clear_data]
    list_display=['mkt_date','symbol','close_price','fiftytwo_week_high','is_nifty_fifty','is_nifty_next_fifty']
    search_fields=['security','symbol']
    list_filter=['mkt_date','is_nifty_fifty','is_nifty_next_fifty']
admin.site.register(BhavcopyMasterPR,BhavCopyLoaderAdmin)
admin.site.register(FilterStocks)
admin.site.register(BhavLastTenDays,BhavCopyTenLoadedAdmin)
admin.site.register(BhavLastFiftyDays)
admin.site.register(BhavLastHundredDays)
admin.site.register(BhavLastFullYear)