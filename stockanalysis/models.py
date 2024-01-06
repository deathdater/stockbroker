from django.db import models
from stockmaster.models import FilterStocks
from stockanalysis.fetch_trading_metrics import screener_login,get_roce

# Create your models here.
RETURN_ON_CAPITAL_EMPLOYED=(('0.0','less than 5 percent'),('1.0','5 to 10 percent'),('2.0','10 to 15 percent'),('3.0','15 to 20 percent'),('4.0','greater than 20 percent'))
EARNING_PER_SHARE=(('0.0','No'),('1.0','Yes'))
FREE_CASH_FLOW=(('0.0','No'),('1.0','Yes'))
INTEREST_COVERAGE_RATIO=(('0.0','No'),('0.5','greater than 4'),('1.0','greater than 10'))
NET_PROFIT_MARGIN=(('-1.0','less than 5 percent'),('-0.5','5 to 10 percent'),('1.0','10 to 15 percent'),('2.0','15 to 20 percent'),('3.0','greater than 20 percent'))
DIVIDENDS=(('0.0','No'),('1.0','Yes'))
GOVERNMENT_REGULTN_RISK=(('0.0','No'),('-1.0','Yes'))
R_AND_D_RISK=(('0.0','No'),('-1.0','Yes'))
KEY_PERSON_RISK=(('0.0','No'),('-1.0','Yes'))

class QualityAnalysisScoring(models.Model):
    '''
    R		Return on Capital Emplyoed		ROCE for last 5 Years			
    E		Earnings Per Share		Is EPS increasing for the past 5 years?			
    F		Free Cash Flow		Is FCF positive for the past 5 years?			
    I		Interest Coverage Ratio		What is the Interest Covergae Ratio for the last year?			
    N		Net Profit Margin		Average Net Profit Margin for the past 5 years			
    E		Economic Moats		1. Brand Loyalty 2.Cost Efficiency Advantage 3.Webbing Advantage 4.Cost of shifting Product			
    D		Dividends		Has the company given dividends for the past 5 year?			
                                
    GR		Govertment Regulations		Can Govt. regulations majorly affect the company's profits? 			
    R&D		Research & Development		Does the company need constant R&D to keep their business going?			
    KP		Key Person		Does the long term proftability of the company depend on few key people?			
    Moats
    # Brand Loyalty
    # Cost Efficiency Advantage
    # Webbing
    # Stikiness(cost of shifting product)
    '''
    stock_industry=models.CharField(max_length=50,blank=True,null=True,verbose_name=("Stock Industry"))
    stock_desc=models.TextField(null=True,blank=True)
    filtered_security_object=models.ForeignKey(FilterStocks, verbose_name=("Filter Stock"), on_delete=models.CASCADE)
    last_update_date=models.DateField(auto_now=True)
    return_on_capital_employed=models.CharField(max_length=10,choices=RETURN_ON_CAPITAL_EMPLOYED)
    earning_per_share=models.CharField(max_length=10,choices=EARNING_PER_SHARE)
    free_cash_flow=models.CharField(max_length=10,choices=FREE_CASH_FLOW)
    interest_coverage_ratio=models.CharField(max_length=10,choices=INTEREST_COVERAGE_RATIO)
    net_profit_margin=models.CharField(max_length=10,choices=NET_PROFIT_MARGIN)
    dividends=models.CharField(max_length=10,choices=DIVIDENDS)
    government_regulations_risk=models.CharField(max_length=10,choices=GOVERNMENT_REGULTN_RISK)
    research_and_development_risk=models.CharField(max_length=10,choices=R_AND_D_RISK)
    key_person_risk=models.CharField(max_length=10,choices=KEY_PERSON_RISK)
    brand_loyalty_advantage=models.BooleanField(default=False)
    cost_efficiency_advantage=models.BooleanField(default=False)
    webbing_advantage=models.BooleanField(default=False)
    stickiness_advantage=models.BooleanField(default=False)
    number_of_moats=models.FloatField(default=0.0)
    qualitative_score=models.FloatField(default=0.0)
    
    def save(self):
        print('saving quality scoreß')
        moats=1
        if(self.brand_loyalty_advantage):
            moats+=1
        if(self.cost_efficiency_advantage):
            moats+=1
        if(self.webbing_advantage):
            moats+=1
        if(self.stickiness_advantage):
            moats+=1
        if(moats>4):
            self.number_of_moats=4
        else:
            self.number_of_moats=moats
        print(moats)
        self.qualitative_score=(float(self.return_on_capital_employed)+float(self.earning_per_share)+float(self.free_cash_flow)+float(self.interest_coverage_ratio)+float(self.net_profit_margin)+float(self.dividends)+float(self.government_regulations_risk)+float(self.research_and_development_risk)+float(self.key_person_risk)+float(self.number_of_moats))
        print(self.qualitative_score)
        # self.save()
        super(QualityAnalysisScoring,self).save()

    def __str__(self):
        # self.__save__()
        # session=screener_login()
        # get_roce('EICHERMOT',session)
        return self.filtered_security_object.symbol+'_'+self.filtered_security_object.security+' Quality Score:'+str(self.qualitative_score)
    

SIGNAL_CHOICES=(('Buy','BUY'),('No Signal','No Signal'))
class StockTrendSignals(models.Model):
    stock_symbol=models.CharField(max_length=100)
    stock_name=models.CharField(max_length=100)
    bullish_engulfing_signal=models.CharField(max_length=15,choices=SIGNAL_CHOICES)
    bullish_harami_signal=models.CharField(max_length=15,choices=SIGNAL_CHOICES)
    piercing_pattern_signal=models.CharField(max_length=15,choices=SIGNAL_CHOICES)
    morning_star_signal=models.CharField(max_length=15,choices=SIGNAL_CHOICES)
    last_updated=models.DateField(auto_now=True)

    def __str__(self):
        signal='No Signal'
        if self.bullish_engulfing_signal=='Buy' or self.bullish_harami_signal=='Buy' or self.piercing_pattern_signal =='Buy' or self.morning_star_signal=='Buy':
            signal='BUY'

        return self.stock_symbol+'_Signal:'+signal

    def __unicode__(self):
        if self.bullish_engulfing_signal=='Buy' or self.bullish_harami_signal=='Buy' or self.piercing_pattern_signal =='Buy' or self.morning_star_signal=='Buy':
            signal='BUY'

        return self.stock_symbol+'_Signal:'+signal