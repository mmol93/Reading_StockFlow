import EWY
import VIX
import USA_index_future
import Estate_price
import Unemployed
import AbroadTrading
import DollarIndex
from datetime import datetime
import ThreeMain_USA_Flow
import SectorCheck

print("실시 날짜: " + str(datetime.now().strftime("%Y/%m/%d, %H:%M")))

# 미국 주요지수
ThreeMain_USA_Flow.three_main_Flow()

# 미국 선물지수
USA_index_future.indexOfFuture()

# 미국 주요섹터(현재 기준: 1.3)
SectorCheck.sectorCheck()

# 변동성 지수
VIX.VIX_Graph()

# 한국 지수
EWY.EWY_Graph()

# 미국 주택가격 지수
Estate_price.estate_price()

# 미국 실업수당 지수
Unemployed.unemployment()

# 한국 경상수지 지수
AbroadTrading.tradingGraph()

# 미국 달러 인덱스 지수
DollarIndex.dollarIndex()

