import pandas as pd
from zipfile import ZipFile
# Needed to remove some annoying warning.
pd.plotting.register_matplotlib_converters(explicit=True)

# Specifying the zip file name for the Crypto Data set
fileName = "E:\\Users\\YGLM\\Development\\data\\all.zip"
  
def LoadCryptoData(fileName):
    # opening the zip file in READ mode 
    with ZipFile(fileName, 'r') as zip: 
        files = zip.namelist()
        allCryptoData = {}
        for curFile in files:
        # Read each file and extract data
            cryptoDataFrame = pd.read_csv(zip.open(curFile))
            ccyCode = curFile.split(".")[0]
            allCryptoData[ccyCode] = cryptoDataFrame
    return(allCryptoData)

# allCryptoData now contains a dictionary of dataframes.
# The dictionary is indexed by the crpyto currency name.
# The dataframe for the crypto currency contains whatever was in the .csv for that currency.
#
# Ex. in all.zip there is a file called btc.csv.  
# This data is stored in a dataframe accesed using allCryptoData["btc"]
allCryptoData = LoadCryptoData(fileName)
ethDataSet = allCryptoData["eth"]
ethDataSet.set_index("date", inplace=True)
btcDataSet = allCryptoData["btc"]
btcDataSet.set_index("date", inplace=True)
ltcDataSet = allCryptoData["ltc"]
ltcDataSet.set_index("date", inplace=True)

# Extract out interesting data and combine into a new dataset
#d1 = ethDataSet.loc[:, 'date' ]
p1 = ethDataSet.loc[:, ["PriceUSD", "TxCnt"]]
#d2 = btcDataSet.loc[:, 'date' ]
p2 = btcDataSet.loc[:, ["PriceUSD", "TxCnt"]]
p3 = ltcDataSet.loc[:, ["PriceUSD", "TxCnt"]]

merged = pd.merge(p1,p2,left_on="date", right_on="date", suffixes=('_eth', '_btc'))
print(merged)
merged = pd.merge(merged, p3, left_on="date", right_on="date", suffixes=('', '_ltc'))

print(merged.corr(method ='pearson'))





