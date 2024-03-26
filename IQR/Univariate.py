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