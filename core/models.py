from django.db import models
from django.contrib.auth.models import User

class Perfil(models.Model):
    TIPO_USUARIO = [
        ('cliente', 'Cliente'),
        ('atendente', 'Atendente'),
        ('analista', 'Analista'),
        ('gestor', 'Gestor'),
        ('operacional', 'Operacional'),
        ('admin', 'Administrador'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO)

    def __str__(self):
        return f"{self.user.username} - {self.tipo}"


class Servico(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Feedback(models.Model):
    STATUS_CHOICES = [
        ('aberto', 'Aberto'),
        ('analise', 'Em análise'),
        ('respondido', 'Respondido'),
        ('concluido', 'Concluído'),
    ]

    TIPO_CHOICES = [
        ('elogio', 'Elogio'),
        ('reclamacao', 'Reclamação'),
        ('sugestao', 'Sugestão'),
    ]

    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)

    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES)
    descricao = models.TextField()

    prioridade = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='aberto')

    resposta = models.TextField(blank=True, null=True)
    anexo = models.FileField(upload_to='feedbacks/', null=True, blank=True)

    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.tipo} - {self.cliente.username}"
