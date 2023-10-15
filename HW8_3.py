params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
param_strings = [f"{key}={value}" for key, value in params.items()]
result_link = initial_str + '&'.join(param_strings)
print(result_link)
