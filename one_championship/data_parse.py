import sys
import pandas as pd
import json
import jsonschema
from jsonschema import validate

dataSchema=''

def read_schema(path):
    global dataSchema
    with open(path) as f:
        dataSchema=json.loads(f.read())
    return dataSchema

def validate_json(jsonData,dataSchema):
    try:
        validate(instance=jsonData,schema=dataSchema)
    except jsonschema.exceptions.ValidationError as err:
        return False
    return True

def process_df(df):
    df['Floor Access DateTime']=pd.to_datetime(df['Floor Access DateTime'])
    return df

def read_data(path):
    try:
        df=pd.read_csv(path)
        df=process_df(df)
    except FileNotFoundError:
        print("File path does not exist. Please check the file path.")
        return
    return df

def validator(json_list):
    for i in json_list:
        isValid=validate_json(i,dataSchema)
        if not isValid:
            json_list.remove(i)
    return json_list

def write_data(valid_list):
    for i in valid_list:
        print(i)

def convert_json(df):
    if not df.empty:
        out=df.to_json(orient='records',date_format='iso')
        out=json.loads(out)
        valid_json_list=validator(out)
        write_data(valid_json_list)
    else:
        write_data([])

if __name__ == '__main__':
    if(len(sys.argv)==3):
        file_path=sys.argv[1]
        schema_path=sys.argv[2]
        dataSchema=read_schema(schema_path)
        df=read_data(file_path)
        convert_json(df)

    else:
        print('Please enter the right arguments')
