import pandas


result = pandas.read_csv('D:/EducationalProjects/03_Python/HomeWork/07_HomeWork/contact.csv', encoding='ANSI')
print(result)

# 1.регистр при вводе
# 2.писать ошибку при удалении несуществующего


# df = pandas.read_csv('D:/EducationalProjects/03_Python/HomeWork/07_HomeWork/contact.csv', encoding='utf8')
# df.apply(lambda x: pandas.lib.infer_dtype(x.values))
# print(df)