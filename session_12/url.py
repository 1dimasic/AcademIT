def get_server_name(url):
    server_name_start_index = url.find('://') + 3
    server_name_end_index = url.find('/', server_name_start_index)

    if server_name_end_index == -1:
        return url[server_name_start_index:]

    return url[server_name_start_index: server_name_end_index]


url_address = 'https://someservername/abcd/dfdf.htm?dfdf=dfdf'
server_name = get_server_name(url_address)
print(f'Имя сервера - {server_name}')
