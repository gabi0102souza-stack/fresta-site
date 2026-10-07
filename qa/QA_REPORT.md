# QA da prévia FRESTA

Revisão local em 07/10/2026, antes da publicação. Navegador da sessão, subdiretório `/fresta-site/`. Não houve conclusão de reserva ou contato com o restaurante.

| Verificação | Resultado |
| --- | --- |
| Estrutura HTML | Validador local: nesting, 1 H1, 11 IDs únicos, 29 referências, fragmentos, arquivos CSS e noindex corretos. |
| JavaScript | `node --check dist/main.js` passou. |
| Assets por HTTP | 10 requisições, todas 200, incluindo favicon, OG e fontes. WOFF2 com assinatura válida; OG 1200 × 630. |
| 360, 390, 430, 768, 1440 | Nenhum overflow horizontal, imagem quebrada ou fragmento inexistente. Screenshots finais salvos. |
| Menu mobile | Abre, anuncia estado, fecha por Escape e devolve foco; âncora fecha o menu e transfere foco à seção. |
| Reserva contextual | Barra aparece quando o CTA do hero sai da tela; desaparece ao alcançar a visita. |
| Teclado | Skip link alcançado por Tab, com outline visível; menu/Escape/âncora verificados. |
| Clipboard | Clique exibiu “Endereço copiado”; status acessível e fallback estão implementados. |
| Sem JavaScript | Rota local removeu o script. Navegação permaneceu visível, 22 links disponíveis e sem overflow em 390 px. |
| Movimento reduzido | Regras CSS aplicadas por rota de teste: animação none, transição 0s e scroll auto. Sem emulação da preferência do sistema. |
| Contraste | Cinco pares principais entre 4,68:1 e 12,00:1. |
| Console | Nenhum erro ou aviso retornado no registro da revisão final. |
| Destinos externos | WhatsApp abre o número vinculado no Linktree; titularidade não confirmada. Hub e três fontes de imprensa consultados. Maps é busca por endereço; perfil Business não confirmado. Instagram divergente foi retirado do site. |

Evidências: [larguras](responsive-results.json), [HTTP](http-results.json), [contraste](contrast-results.json), [hero final](hero-final.png), [sem JS](no-js-390.png) e capturas `responsive-*.png`.

Antes do primeiro commit, `git diff --cached --check` passou para os arquivos autorais. As duas licenças OFL de terceiros foram preservadas integralmente e excluídas desse critério de formatação. O projeto foi enviado ao GitHub após autorização do usuário; nenhuma credencial foi salva nos arquivos.

Limites: validação HTML própria, sem certificação W3C; sem leitor de tela, aparelhos físicos ou auditoria multibrowser; preferência de movimento reduzido aplicada via CSS de teste, não OS; Lighthouse não disponível; nenhuma métrica de campo inventada. As evidências externas confirmam destinos e documentos, não a vigência operacional do restaurante em outubro de 2026.

## Publicação externa

Publicação autorizada e concluída em **07/10/2026** no endereço **https://gabi0102souza-stack.github.io/fresta-site/**.

- [GitHub Actions](https://github.com/gabi0102souza-stack/fresta-site/actions/runs/37613715652): `completed / success`, commit de site `946f4feed4ca97684cfa7f5c13c4123141e41d6e`.
- Dez requisições públicas por HTTPS, sem credenciais: todas 200. Fontes WOFF2 e OG com dimensões válidas. [Resultados](public-http-results.json).
- Versão pública aberta e verificada visualmente no navegador da sessão; nenhum erro ou aviso de console registrado. [Screenshot](public-preview.png).
- O link público funciona sem o servidor local e pode ser compartilhado. Nenhuma mensagem foi enviada ao restaurante.
