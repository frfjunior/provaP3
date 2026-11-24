import pytest
from datetime import date
from .models import Produtor, Lote

@pytest.fixture
def produtor():
    return Produtor.objects.create(nome="Ana", cidade="Olimpia", cpf_cnpj="12345678901")

@pytest.mark.django_db
def test_total(produtor):
    lote = Lote.objects.create(
        variedade="Pera",
        caixas=10,
        preco_caixa="50.00",
        data=date(2026, 11, 23),
        produtor=produtor,
    )
    assert lote.total == 10 * lote.preco_caixa

@pytest.mark.django_db
def test_filtro_variedade(client, produtor):
    Lote.objects.create(variedade="Pera", caixas=10, preco_caixa="50.00", data=date(2026, 11, 23), produtor=produtor)
    Lote.objects.create(variedade="Lima", caixas=4, preco_caixa="40.00", data=date(2026, 11, 23), produtor=produtor)
    resp = client.get("/lotes/?variedade=Pera")
    texto = resp.content.decode()
    assert resp.status_code == 200
    assert "Pera" in texto
    assert "Lima" not in texto

@pytest.mark.django_db
def test_api_post(client, produtor):
    resp = client.post(
        "/api/lotes/",
        {
            "variedade": "Pera",
            "caixas": 10,
            "preco_caixa": "50.00",
            "data": "2026-11-23",
            "produtor": produtor.id,
        },
        content_type="application/json",
    )
    assert resp.status_code == 201

@pytest.mark.django_db
def test_api_post_invalido(client, produtor):
    resp = client.post(
        "/api/lotes/",
        {
            "variedade": "Pera",
            "caixas": 0,
            "preco_caixa": "50.00",
            "data": "2026-11-23",
            "produtor": produtor.id,
        },
        content_type="application/json",
    )
    assert resp.status_code == 400