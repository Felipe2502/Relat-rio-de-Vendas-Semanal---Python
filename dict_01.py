vendas_semana = [1500, 2000, 800, 3500, 1200]
total_vendas = sum(vendas_semana)
quantidade_dias = ["Segunda", "Terça", "Quarta", "Quinta", "Sexta"]

media_diaria = total_vendas / len(quantidade_dias)

melhor_venda = max(vendas_semana)
pior_venda = min(vendas_semana)

print("-" * 40)
print("RELATÓRIO DE VENDAS SEMANAL")
print("-" * 40)
print(f"1. Total de vendas na semana: R${total_vendas:,.2f}")
print(f"2. Média de vendas diária: R${media_diaria:,.2f}")
print(f"3.Destaques do período:")
print(f" - Melhor dia de vendas: R${melhor_venda:,.2f}")
print(f" - Pior dia de vendas: R${pior_venda:,.2f}")
print("-"*40)