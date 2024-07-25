def add_item(list, item):
    list.append(item)
    print(f'{item} foi adicionado ao sistema.')

def search_item_index(list, item):
    if item in list:
        return list.index(item)
    else:
        return -1

def search_item_for(list, item):
    for i, value in enumerate(list):
        if value == item:
            return i
    return -1

def delete_item(list, item, method='index'):
    if method == 'index':
        index = search_item_index(list, item)
    else:
        index = seach_item_for(list, item)
    
    if index != -1:
        del list[index]
        print(f'{item} foi deletado do sistema.')
    else: 
        print(f'{item} não foi encontrado no sistema.')

def update_item(list, old_item, new_item, method='index'):
    if method == 'index':
        index = search_item_index(list, old_item)
    else:
        index = search_item_for(list, old_item)
    
    if index != -1:
        list[index] = new_item
        print(f'{old_item} foi atualizado para {new_item}.')
    else:
        print(f'{old_item} não foi encontrado no sistema.')