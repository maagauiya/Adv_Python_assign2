import parserwithsel
scrapper=parserwithsel
print('Enter the name of the cryptocurrency you want to see the latest news:')
name_of_coin=str(input())
scrapper.get_datar(name_of_coin)
