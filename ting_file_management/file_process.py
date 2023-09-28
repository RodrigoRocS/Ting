import sys
from ting_file_management.file_management import txt_importer


def process(path_file, instance):
    found = False

    for i in range(len(instance)):
        if instance.search(i)["nome_do_arquivo"] == path_file:
            found = True
            break

    if not found:
        file = txt_importer(path_file)
        file_info = {
            "nome_do_arquivo": path_file,
            "qtd_linhas": len(file),
            "linhas_do_arquivo": file,
        }
        instance.enqueue(file_info)
        sys.stdout.write(str(file_info))

    return found


def remove(instance):
    if len(instance) == 0:
        sys.stdout.write("Não há elementos\n")
    else:
        removed_file = instance.dequeue()
        sys.stdout.write(
            f"Arquivo {removed_file['nome_do_arquivo']} removido com sucesso\n"
        )


def file_metadata(instance, position):
    try:
        file_info = instance.search(position)
        sys.stdout.write(str(file_info) + '\n')
    except IndexError:
        sys.stderr.write("Posição inválida\n")
