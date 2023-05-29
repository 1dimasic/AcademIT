def get_server_name(url):
    start_index = url.find('://') + 3
    end_index = url.find('/', start_index)

    if end_index == -1:
        return url[start_index:]

    return url[start_index:end_index]


url_address = 'https://Someservername/abcd/dfdf.htm?dfdf=dfdf'
server_name = get_server_name(url_address)
print(f'Имя сервера - {server_name}')
