class Univariate():
    
    def QualQuan(dataset):
        quan=[]
        qual=[]
        for ColumnName in dataset.columns:    
            if(dataset[ColumnName].dtype=='O'):
                qual.append(ColumnName)
            else:
                quan.append(ColumnName)
        return quan,qual #we can return more than one variable based on our result
    
    def freqTable(columnName,dataset):
        freqTable = pd.DataFrame(columns=["Unique_Value","Frequency","Relative_Frequency","Cumsum"])
        freqTable["Unique_Value"]=dataset[columnName].value_counts().index
        freqTable["Frequency"]=dataset[columnName].value_counts().values
        freqTable["Relative_Frequency"]=(freqTable["Frequency"]/103)
        freqTable["Cumsum"]=freqTable["Relative_Frequency"].cumsum()
        return freqTable
    
    def Univariate(dataset,quan):
        descrip=pd.DataFrame(index="Mean","Median","Mode","Q1:25%","Q2:50%","Q3:75%","99%","Q4:100%",
                                   "IQR","1.5rule","Lesser","Greater","Min","Max"], columns=quan)
        for columnName in quan:
            descrip[columnName]["Mean"]=dataset[columnName].mean()
            descrip[columnName]["Median"]=dataset[columnName].median()
            descrip[columnName]["Mode"]=dataset[columnName].mode()[0]
            descrip[columnName]["Q1:25%"]=dataset.describe()[columnName]["25%"]
            descrip[columnName]["Q2:50%"]=dataset.describe()[columnName]["50%"]
            descrip[columnName]["Q3:75%"]=dataset.describe()[columnName]["75%"]
            descrip[columnName]["99%"]=np.percentile(dataset[columnName],99)
            descrip[columnName]["Q4:100%"]=dataset.describe()[columnName]["max"]
            descrip[columnName]["IQR"]=descrip[columnName]["Q3:75%"]-descrip[columnName]["Q1:25%"]
            descrip[columnName]["1.5rule"]=1.5*descrip[columnName]["IQR"]
            descrip[columnName]["Lesser"]=descrip[columnName]["Q1:25%"]-descrip[columnName]["1.5rule"]
            descrip[columnName]["Greater"]=descrip[columnName]["Q3:75%"]+descrip[columnName]["1.5rule"]
            descrip[columnName]["Min"]=dataset[columnName].min()
            descrip[columnName]["Max"]=dataset[columnName].max()
        return descrip   
    
    def OutlierColumnName(quan):
        for columnName in quan:
            if(descrip[columnName]["Min"]<descrip[columnName]["Lesser"]):
                lesser.append(columnName)
            if(descrip[columnName]["Max"]>descrip[columnName]["Greater"]):
                greater.append(columnName)  
        return lesser,greater  
    
    def ReplacingOutlier(lesser,greater):
        for columnName in lesser:
            dataset[columnName][dataset[columnName]<descrip[columnName]["Lesser"]]=descrip[columnName]["Lesser"]
        for columnName in greater:
            dataset[columnName][dataset[columnName]>descrip[columnName]["Greater"]]=descrip[columnName]["Greater"]
        return dataset   