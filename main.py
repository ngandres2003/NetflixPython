import utils
import read_csv
import charts

def run():
    data = read_csv.read_csv('./NetflixOriginals.csv') 
    keys,values = utils.most_genre(data) 
    charts.generate_pie_chart(keys,values)
if __name__=='__main__':
    run()

# def run2():
#     data = read_csv.read_csv('./NetflixOriginals.csv')
#     keys,values = utils.top_3(data)
#     charts.generate_bar_chart(keys,values)
# if __name__ =='__main__':
#     run2()