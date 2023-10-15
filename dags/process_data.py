from datetime import datetime

def process_record(record):
    record['ins_dt'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return record

def process_data(api_data):
    print(api_data)
    if api_data is not None:
        processed_data = [process_record(record) for record in api_data]
        return processed_data
    else:
        return None
