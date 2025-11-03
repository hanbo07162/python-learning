#数据的排序和去重
'''
通过sort_values方法对数据进行排序
语法
DataFrame.sort_values(
    by,  排序列名（字符串或列表） 必填
    axis=0/1  排序轴0=行，1=列 默认0
    ascending=True/False  升序或降序 默认True
    inplace=False  是否在原数据上修改，默认False
)
'''
import pandas as pd
book=pd.read_excel(r"D:\practicePython\.venv\book1.xlsx")
print(book)
#按单列排序

book.sort_values(
    by="单价",
    ascending=False,
    inplace=True
)
print(book)

#按多列排序

book.sort_values(
    by=["总价","单价"],
    ascending=[True,False],
    inplace=True
)
print(book)

#对于重复数据的处理
'''

DataFrame.drop_duplicates(
    subset=None,  指定列进行重复数据的判断，默认所有列
    keep='first'  保留重复数据的哪一条，默认first /last/False
    inplace=False  是否在原数据上修改，默认False
)
'''
book.drop_duplicates(
    subset='name',
    inplace=True
)
print(book)


#数据的筛选与过滤
'''
条件筛选
将符合条件的数据筛选出来，
分为
单条件筛选

多条件筛选


'''
datas=[
    {'name':"xiao","hight":"215",'weight':"182"},
    {'name':"sda","hight":"152",'weight':"172"},
    {'name':"ds","hight":"212",'weight':"162"},
    {'name':"dde","hight":"123",'weight':"152"},
    {'name':"ww","hight":"154",'weight':"142"},
    {'name':"dfg","hight":"187",'weight':"142"},
    {'name':"dsds","hight":"181",'weight':"123"},
    {'name':"sda","hight":"165",'weight':"100"},
]
df=pd.DataFrame(datas)
print(df)
df1=df[df['hight']>'170']
print(df1)
#还可以利用query进行筛选
df1=df.query("'150'<hight<'170'")
print(df1)
#还可以使用isin函数 选出具有特定值的记录
df1=df[df['hight'].isin(['123','154'])]
print(df1)
#多条件筛选 使用运算符& 比如筛选身高大于170，并且体重大于160的人
df1=df[(df['hight']>'170')&(df['weight']>'160')]
print(df1)

#那么如何排除某些特定的行呢，首先将要排除的列选择出来，删去要排除的数值，在利用isin
ex_list=list(df['hight'])
ex_list.remove('215')
ex_list.remove('212')
df1=df[df.hight.isin(ex_list)]
print(df1)

#索引筛选 使用iloc 
#选择第一行第一列
print(df)
print(df.loc[0,'hight'])
#选择第123行，第一第二列
print(df.loc[[0,1,2],['hight','weight']])
#切片操作选择特定的行
print(df[1:5])
#使用iloc不必输入列名称而使用列
#选择123行，1，2列
print(df.iloc[0:3,1:3])


