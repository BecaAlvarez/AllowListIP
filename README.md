# AllowListIP

Este repositório contém um script em Python desenvolvido para fins **educacionais**, como parte dos meus estudos de **Python aplicado à cibersegurança**.

O objetivo principal é atualizar periodicamente um arquivo com a lista de endereços IP autorizados a acessar conteúdo restrito dentro de uma rede interna. Essa autorização é baseada em funcionários que lidam com registros sensíveis de pacientes.

---

## 🧠 Objetivo Educacional

Este projeto tem como objetivo ajudar no aprendizado prático de Python voltado para cibersegurança, incluindo:

✅ Manipulação de arquivos com open(), .readlines() e .strip()

✅ Uso de funções, listas e condicionais

✅ Importação e uso da biblioteca os (os.path.join, os.path.dirname)

✅ Automações típicas de listas, whitelists e blacklists de IP

✅ Prática com leitura e filtragem de dados sensíveis

## 🔍 O que o script faz?

O script:

- Lê uma lista de permissões (`allow_list.txt`) contendo usuários e seus endereços IP autorizados.
- Lê uma lista de remoção (`remove_list.txt`) com IPs que devem ser revogados.
- Verifica se algum IP da lista de permissões também aparece na lista de remoção.
- Remove automaticamente essas entradas.
- Mostra no console:
  - A lista original
  - Os usuários removidos
  - A lista atualizada (IPs válidos)

---
## 🚧 Status do Projeto

✅ Concluído para finalidade educacional e prática inicial.<br>

## ✅ Melhorias Futuras (ideias)

- Melhoria na arquitetura do código e implementação de práticas de segurança
  
- Salvar a nova lista atualizada diretamente em arquivo

- Gerar logs de auditoria

- Usar scheduler (cron ou Task Scheduler) para atualização automática

- Interface CLI ou Web simples

## ⚠️ Aviso

Este projeto não deve ser usado diretamente em ambientes de produção sem testes adicionais e ajustes de segurança. Ele foi criado para fins de aprendizado em Python e automação de tarefas de cibersegurança.


![Python](https://img.shields.io/badge/python-3.9+-blue?logo=python)
![Status](https://img.shields.io/badge/status-educacional-orange)
![License](https://img.shields.io/badge/license-MIT-green)
