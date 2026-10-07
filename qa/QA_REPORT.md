# QA da prévia FRESTA

Revisão em 07/10/2026. Navegador local da sessão, subdiretório `/fresta-site/`. Não houve publicação ou conclusão de reserva.

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

`git diff --check` foi executado sem erro; como o projeto é novo e está sem staging, também foi realizada verificação direta de espaços finais e marcadores de conflito nos arquivos textuais autorais da entrega. As duas licenças OFL de terceiros foram preservadas integralmente e excluídas desse critério de formatação. Não houve commit ou push.

Limites: validação HTML própria, sem certificação W3C; sem leitor de tela, aparelhos físicos ou auditoria multibrowser; preferência de movimento reduzido aplicada via CSS de teste, não OS; Lighthouse não disponível; nenhuma métrica de campo inventada. As evidências externas confirmam destinos e documentos, não a vigência operacional do restaurante em outubro de 2026.
