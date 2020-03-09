from django.db import models

STATUS_PROJETO = (
    ('concluido', 'Concluído'),
    ('atrasado', 'Atrasado'),
    ('em_andamento', 'Em Andamento')
)

class Aluno(models.Model):
    nome = models.CharField('Nome', max_length=200)
    email = models.EmailField('E-mail')
    turma = models.CharField('Turma', max_length=10)
    ano = models.CharField('Ano', max_length=4)
    projeto = models.ForeignKey('Projeto', on_delete=models.CASCADE)

    def __str__(self):
        return '%s - %s' % (self.nome, self.projeto.titulo)


class Projeto(models.Model):
    titulo = models.CharField('Título', max_length=250)
    resumo = models.TextField('Resumo')
    documento = models.FileField('Documento', upload_to='arquivos')
    data_inicio = models.DateTimeField('Data de inicio do Projeto')
    data_fim = models.DateTimeField('Data de Entrega')
    status = models.CharField('Status do Projeto', max_length=50, choices=STATUS_PROJETO)

    def __str__(self):
        return self.titulo
