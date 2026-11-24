from django.core.validators import MinValueValidator
from django.db import models


class Produtor(models.Model):
    nome = models.CharField(max_length=80)
    cidade = models.CharField(max_length=80)
    cpf_cnpj = models.CharField(max_length=18)

    def __str__(self):
        return self.nome


class Lote(models.Model):
    VARIEDADES = [
        ("Pera", "Pera"),
        ("Valência", "Valência"),
        ("Lima", "Lima"),
    ]
    variedade = models.CharField(max_length=20, choices=VARIEDADES)
    caixas = models.IntegerField(validators=[MinValueValidator(1)])
    preco_caixa = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0)]
    )
    data = models.DateField()
    produtor = models.ForeignKey(
        Produtor, on_delete=models.CASCADE, related_name="lotes"
    )

    def __str__(self):
        return f"{self.variedade} - {self.produtor}"

    @property
    def total(self):
        return self.caixas * self.preco_caixa