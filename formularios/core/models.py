from django.db import models

SEXO_CHOICES = (
    ('masculino', 'Masculino'),
    ('feminino', 'Feminino'),
)

BIRTH_YEAR_CHOICES = (
    ('1980', '1980'),
    ('1981', '1981'),
    ('1982', '1982'),
    ('1983', '1983'),
    ('1984', '1984'),
)

FAVORITE_COLORS_CHOICES = (
    ('az', 'Azul'),
    ('vd', 'Verde'),
    ('pt', 'Preto'),
)

class Client(models.Model):
    name=models.CharField(max_length=200)
    birth_year=models.DateField()
    birth_year1=models.CharField(max_length=4, choices=BIRTH_YEAR_CHOICES)
    favorite_colors=models.CharField(max_length=2, choices=FAVORITE_COLORS_CHOICES)

    def __str__(self):
        return self.name

class Cliente(models.Model):
    nome = models.CharField(max_length=250)
    cpf = models.CharField(max_length=15)
    sexo = models.CharField(max_length=10, choices = SEXO_CHOICES)
    fone = models.CharField(max_length=15)
    email = models.EmailField(verbose_name='e-mail')
    endereco = models.CharField(max_length=300)
    
    def __str__(self):
        return self.nome

class Fornecedor(models.Model):
    nome = models.CharField(max_length=250, error_messages={'required':'Obrigatório o preenchimento do nome!'})
    cnpj = models.CharField(max_length=15)
    fone = models.CharField(max_length=15)
    email = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = 'fornecedor'
        verbose_name_plural = 'fornecedores'

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Agenda(models.Model):
    descricao = models.CharField(max_length=200, verbose_name='descrição')
    cliente = models.ForeignKey(Cliente, on_delete = models.CASCADE)
    dataInicial = models.DateTimeField('data inicial')
    dataFinal = models.DateTimeField('data final')

    def __str__(self):
        return '{} - {} - {}'.format(self.dataInicial, self.cliente, self.descricao)