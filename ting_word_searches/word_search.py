def exists_word(word, instance):
    queue = instance.get_data()
    ocorrencias = []
    for dict in queue:
        arquivo = dict["nome_do_arquivo"]
        lines_data = dict["linhas_do_arquivo"]

        for index, line in enumerate(lines_data):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1})
    if len(ocorrencias) == 0:
        return []

    return [{"palavra": word, "arquivo": arquivo, "ocorrencias": ocorrencias}]


def search_by_word(word, instance):
    queue = instance.get_data()
    ocorrencias = []
    for dict in queue:
        arquivo = dict["nome_do_arquivo"]
        lines_data = dict["linhas_do_arquivo"]

        for index, line in enumerate(lines_data):
            if word.lower() in line.lower():
                ocorrencias.append({"linha": index + 1, "conteudo": line})
    if len(ocorrencias) == 0:
        return []

    return [{"palavra": word, "arquivo": arquivo, "ocorrencias": ocorrencias}]
