from ting_file_management.file_management import txt_importer


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
    """Aqui irá sua implementação"""


def file_metadata(instance, position):
    """Aqui irá sua implementação"""
