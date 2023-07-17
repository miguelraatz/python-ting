from ting_file_management.file_management import txt_importer
import sys


def process(path_file, instance):
    lines_data = txt_importer(path_file)
    new_instance = {
        "nome_do_arquivo": path_file,
        "qtd_linhas": len(lines_data),
        "linhas_do_arquivo": lines_data,
    }
    if new_instance in instance._data:
        return None
    instance.enqueue(new_instance)
    print(new_instance)


def remove(instance):
    if instance.is_empty():
        print('Não há elementos')
    else:
        file_removed = instance.dequeue()
        path_file = file_removed["nome_do_arquivo"]
        print(f'Arquivo {path_file} removido com sucesso')


def file_metadata(instance, position):
    try:
        search_queue = instance.search(position)
        print(search_queue)
    except IndexError:
        print('Posição inválida', file=sys.stderr)
