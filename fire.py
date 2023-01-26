from datetime import datetime 
import re
import pdb

def func_input(data):
    data_list = re.sub("[|]|'| ", "",data)
    data_list = data_list.split(',')
    print(data_list)
    pdb.set_trace()

    json_send(data_list)
    

    
def json_send(data) : 
    print( "\"m2m:cin\": { \n    \"cnf\":\"application/json\",\n    \"con\":{" )
    print( "\"time\": \"", datetime.now().strftime('%Y-%m-%d %H:%M:%S'),"\"")
    print( "        \"CO2\": ", round(float(data[3])),",")
    print( "        \"TVOC\": ", round(float(data[4])),",")
    print( "        \"temperature\": ", round(float(data[1]),1),",")
    print( "        \"humidity\": ", round(float(data[2])))


if __name__  == '__main__':
    #data = []
    str_data = "'fire_0001', '21.66', '41.03', '400.00', '0.00'"
    result = func_input(str_data)
