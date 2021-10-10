import parserwithsel
scrapper=parserwithsel
name_of_coin=str(input())
print('Enter the name of the cryptocurrency you want to see the latest news:')
scrapper.get_datar(name_of_coin)
