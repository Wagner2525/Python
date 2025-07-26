def notas(*notas, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.

    :param notas: Recebe várias notas para o cálculo.
    :param sit: (Opcional) Fala como está a situação do aluno.
    :return r: Retorna o dicionário com os resultados.
    """
    r = {}
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['média'] = sum(notas)/len(notas)
    if sit:
        if r['média'] >= 7:
            r['Situação'] = 'BOA'
        elif r['média'] == 6:
            r['Situação'] = 'ACEITAVEL'
        else:
            r['Situação'] = 'RUIM PAKAS'
    return r

# Main
resp = notas(5, 7, 10, sit=True)
print(resp)
