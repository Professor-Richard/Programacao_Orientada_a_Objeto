# Desafio

Implemente um sistema de notificações com:

- `Email`
- `SMS`
- `Push`

Regras:

1. Classe base `Notificacao` com método `enviar(mensagem: str) -> None`
2. O código principal deve enviar para uma lista de notificações
3. **Sem condicionais** para decidir o tipo

Exemplo de uso esperado:

```python
notificacoes = [Email(), SMS(), Push()]

for n in notificacoes:
    n.enviar("Sua compra foi aprovada!")
```

---
