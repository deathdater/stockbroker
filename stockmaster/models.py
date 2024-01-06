from django.db import models

STOCK_INVESTMENT_STATUS_CHECK=(('Passed','Passed'),('Failed','Failed'))

# Create your models here.
class BhavcopyMasterPR(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)

    def __str__(self):
        return str(self.mkt_date)+'_'+str(self.symbol)
class IndianStockMasterData(models.Model):
    stock_symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    stock_name=models.CharField(verbose_name='Name', max_length=100)
    stock_first_data_date=models.DateField(auto_now=False, auto_now_add=False)
    stock_last_data_date=models.DateField(auto_now=False, auto_now_add=False)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)
    is_nifty_five_hundred=models.BooleanField(verbose_name='Is Nifty 500',default=False)
    def __str__(self):
        return stock_name+'_From: '+str(stock_first_data_date)+'_To: '+str(stock_last_data_date)

class FilterStocks(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)
    stock_investment_status_check=models.CharField(max_length=50,default='Failed', choices=STOCK_INVESTMENT_STATUS_CHECK)
    stock_correction=models.FloatField(null=True,blank=True)

    def __str__(self):
        return str(self.security)+'_'+str(self.mkt_date)+'_'+str(self.close_price)+'_'+str(self.stock_investment_status_check)+'_Correction: '+str(self.stock_correction)

class BhavLastTenDays(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)

    def __str__(self):
        return str(self.symbol)+'_'+str(self.mkt_date)

class BhavLastFiftyDays(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)

    def __str__(self):
        return str(self.mkt_date)+'_'+str(self.symbol)

class BhavLastHundredDays(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)

    def __str__(self):
        return str(self.mkt_date)+'_'+str(self.symbol)

class BhavLastFullYear(models.Model):
    mkt_date=models.DateField(auto_now=False, auto_now_add=False)
    mkt=models.BooleanField(verbose_name='Market',default=False)
    series=models.CharField(verbose_name='Series', max_length=10)
    symbol=models.CharField(verbose_name='Symbol', max_length=50,null=False)
    security=models.CharField(verbose_name='Name', max_length=100)
    prev_close_price=models.FloatField(default=0.0)
    open_price=models.FloatField(default=0.0)
    high_price=models.FloatField(default=0.0)
    low_price=models.FloatField(default=0.0)
    close_price=models.FloatField(default=0.0)
    net_trade_value=models.FloatField(default=0.0)
    net_trade_qty=models.FloatField(default=0.0)
    is_index=models.BooleanField(verbose_name='Is Index',default=False)
    corp_index=models.CharField(verbose_name='Is Corp Index', max_length=5,blank=True,null=True)
    trades=models.FloatField(default=0.0)
    fiftytwo_week_high=models.FloatField(default=0.0)
    fiftytwo_week_low=models.FloatField(default=0.0)
    is_nifty_fifty=models.BooleanField(verbose_name='Is Nifty 50',default=False)
    is_nifty_next_fifty=models.BooleanField(verbose_name='Is Nifty Next 50',default=False)

    def __str__(self):
        return str(self.mkt_date)+'_'+str(self.symbol)