import json

def app_run() : 
    data = {}
    data['key'] = 'value'
    return json.dumps(data)

if __name__ == '__main__':
	print app_run()