# FRESTA WEBSITE PREVIEW

Pesquisa e revisão: **07/10/2026**, America/Sao_Paulo. Proposta com publicação no GitHub Pages autorizada posteriormente pelo usuário. Nenhum contato com o restaurante foi realizado.

## 1. RESULTADO

Site completo de uma página em português brasileiro, com HTML, CSS e JavaScript nativos. Inclui hero, cozinha, consulta do cardápio, casa, imprensa datada, visita, reserva, endereço copiável e rodapé de apresentação. Os arquivos entregues estão em `dist/`; não há build obrigatório.

Site publicado e verificado: https://gabi0102souza-stack.github.io/fresta-site/. A prévia local em http://127.0.0.1:4173/fresta-site/ serve apenas para desenvolvimento. Captura pública: [site publicado](qa/public-preview.png). Revisão e instruções: [README](README.md) e [QA_REPORT](qa/QA_REPORT.md).

O layout está finalizado com arte abstrata assumida. A falta de fotografias autorizadas não deixou blocos vazios ou imagens fictícias de pratos e salão.

## 2. CREATIVE THESIS

O vinho do símbolo real, o nome FRESTA e uma abertura de luz orientam a composição. O título amplo dá presença; o convite para almoço, a chef e a Simão Álvares 447 dão contexto concreto. A rua, a cozinha aberta e as mesas aparecem no ritmo editorial da página.

A abertura é um dispositivo desta proposta, não uma filosofia atribuída à casa. A passagem para almoço é apresentada no corpo como fato de maio de 2026, sem afirmar confirmação operacional em outubro.

No teste de substituição, trocar apenas o nome deixaria sem fundamento a combinação entre símbolo, abertura, Carol, endereço 447 e a narrativa da casa. O sistema de layout pode ser reutilizado, mas o conteúdo e sua composição foram construídos para o Fresta.

## 3. BRAND EVIDENCE

- Símbolo circular: arquivo real do avatar do [Linktree](https://linktr.ee/fresta.bar), reduzido sem redesenho para cabeçalho e favicon.
- Vinho primário `#891f2d`: RGB dominante amostrado do JPEG original; não equivale a uma especificação oficial de cor.
- Nome, endereço e botão de reserva: encontrados nesse hub.
- Carol, primeira casa independente, cozinha aberta e relação com a calçada: documentados nas fontes editoriais, com datas e limites em [SOURCES](research/SOURCES.md).

Não foi fornecido brand book. A consulta pública do Instagram ficou limitada e revelou divergência de identidade. [BRAND_AUDIT](research/BRAND_AUDIT.md) separa evidência e decisão criativa.

## 4. INFERRED DESIGN

Instrument Sans e Instrument Serif são fontes complementares sob SIL OFL, locais em WOFF2. Não foram identificadas como fontes oficiais. Papel claro, oliva, superfícies secundárias, grid, hierarquia, arte de luz e composição tipográfica são decisões de apresentação.

O pequeno texto “fresta” no cabeçalho é provisório; FRESTA em escala grande é um título editorial. **OFFICIAL LOGO ASSET REQUIRED:** wordmark aprovado e vetor do símbolo para adoção oficial. A proposta preserva o símbolo existente.

## 5. BENCHMARK INSIGHTS

Foram abertos 16 sites oficiais de cinco regiões. The Four Horsemen permaneceu em loader, por isso sua avaliação foi registrada como incompleta. Houve inspeção mobile direta de Septime, Café Cecilia e Kiln. Não foram medidos tempos de animação, Lighthouse ou Core Web Vitals dos concorrentes.

Aplicações concretas: página útil em HTML por afinidade com Septime; dados comerciais integrados ao desenho como em Kiln e Bar Isabel; imprensa editorial como em Café Cecilia; informação acessível mesmo quando mídia falha, observada em Supernormal. Nenhuma marca, fotografia ou filosofia foi copiada.

Fontes e observações individuais: [BENCHMARKS](research/BENCHMARKS.md). Oportunidades e limites: [BENCHMARK_NEGATIVE_SPACE](research/BENCHMARK_NEGATIVE_SPACE.md).

## 6. UNIQUE INTERACTIONS

Uma única composição no hero se abre com `clip-path`, em 820 ms e `cubic-bezier(.22,.68,.08,1)`. Texto, endereço e reserva permanecem estáveis e disponíveis durante o efeito. Não há scroll hijacking ou sequência de reveals.

No celular, a reserva aparece em uma barra quando o CTA principal deixa a tela e sai quando a seção de visita aparece. Menu com `aria-expanded`, Escape e transferência de foco para a seção escolhida. Copiar endereço anuncia sucesso ou orienta a seleção manual se a API falhar. São melhorias progressivas; o conteúdo e os links existem sem JavaScript.

## 7. COPY

“Uma pausa. Um bom almoço.” foi escolhida entre três alternativas internas: frase autoral simples, sem citação ou manifesto. Chef, bairro, endereço e ação aparecem no início. “Boa cozinha. Pouca cerimônia.” traduz o caráter informal descrito pela imprensa, sem inventar práticas ou fornecedores.

O menu é uma consulta direta, sem pratos ou preços de 2025. Imprensa tem veículo e data, sem avaliações inventadas. Horários conflitantes foram omitidos. O rodapé identifica a proposta e o caráter conceitual dos visuais.

## 8. IMAGES

| Categoria | Entrega |
| --- | --- |
| REAL | Símbolo do Linktree em WebP e o mesmo arquivo em PNG de favicon. A origem está documentada; autorização para uso público oficial não foi presumida. |
| TEMPORARY | Texto auxiliar de marca e famílias de interface, sujeitos à aprovação. |
| CONCEPTUAL | `luz.svg`, peça rua/cozinha/mesa em HTML/CSS e OG original 1200 × 630. Não representam comida ou arquitetura da casa. |
| MISSING | Fotografias atuais autorizadas; wordmark e vetor oficiais. |

Não foram usadas fotos da imprensa, hotlinks, cenários gerados ou pratos inventados. [IMAGE_SOURCES](IMAGE_SOURCES.md) registra origens e condições.

## 9. FACT CHECK

**CONFIRMED:** existência do hub com nome, símbolo, endereço e link de reserva; destino de WhatsApp abre o número vinculado. A [VEJA de 22/05/2026](https://vejasp.abril.com.br/coluna/arnaldo-lorencato/comer-e-beber-fresta-abre-para-almoco/) documenta a mudança para almoço. Trajetória de Carol e ambiente foram encontrados em matérias históricas identificadas.

**CONFLICTING:** Linktree encaminha a 95590-8761; VEJA de maio informa 99662-7838. A bio parcial acessível de `@fresta.bar` mostra horários noturnos e informação insuficiente para corroborar a identidade de Pinheiros. Não se considerou login uma exigência para a pesquisa e não houve acesso à conta do usuário.

**UNVERIFIED:** titularidade e vigência do número de reserva; operação em outubro de 2026; horários, menu, preços, políticas, bebidas, música, eventos, delivery e manutenção do ambiente. Não foi encontrado site institucional independente atribuível com segurança à casa; isso não prova inexistência.

## 10. LINKS

| Destino | Resultado e decisão |
| --- | --- |
| Reserva / WhatsApp | `https://wa.me/+5511955908761`, seguido do botão Reservas do Linktree. Abriu página com o número correto; proprietário e disponibilidade continuam pendentes. Nenhuma mensagem enviada. |
| Instagram | Handle encontrado na imprensa e no hub, mas identidade atual não resolvida. Link direto retirado da proposta; acompanhamento leva ao Linktree. |
| Canais da casa | `https://linktr.ee/fresta.bar`, página aberta e endereço verificado. O hub pode conter links antigos. |
| Maps | URL de busca com Fresta + endereço completo. Não usa coordenadas inventadas. A sessão não confirmou dados de Google Business. |
| Imprensa | Páginas VEJA, UOL e CNN abertas; links têm origem real e data editorial. Nenhum conteúdo longo ou fotografia foi reproduzido. |
| Âncoras / assets | Fragmentos válidos, arquivos locais encontrados e 10 requisições HTTP com status 200 no subdiretório. |

## 11. PERFORMANCE

`dist/` soma aproximadamente **184 KB (180 KiB)**, incluindo OG e licenças. Os arquivos da página sem OG e licenças somam cerca de **114 KiB** antes de compressão HTTP. Peso de arquivos não é uma medição de tráfego real ou de tempo de carregamento.

Zero dependências de runtime, frameworks, bibliotecas de motion, vídeos, embeds, analytics e fontes remotas. Símbolo WebP de 2,6 KB; arte SVG de 2,2 KB. Fontes usam `font-display:swap`; imagens têm dimensões reservadas. Sharp é opcional apenas para regenerar assets.

Lighthouse não estava disponível no runtime verificado. Não foram atribuídos scores ou métricas LCP/CLS/INP. A estrutura foi construída para reduzir bloqueios e deslocamentos, sem certificar resultados de campo.

## 12. MOBILE

Capturas finais em `qa/responsive-{largura}.png`; valores em [responsive-results](qa/responsive-results.json).

| Largura solicitada | Área útil / scrollWidth | Resultado |
| --- | --- | --- |
| 360 px | 345 / 345 px | Sem overflow; imagens e alvos verificados; menu de toque. |
| 390 px | 375 / 375 px | Sem overflow; menu/Escape/âncora e reserva contextual testados. |
| 430 px | 415 / 415 px | Sem overflow; recorte e textos revisados. |
| 768 px | 753 / 753 px | Sem overflow; navegação exposta; grid de tablet. |
| 1440 px | 1425 / 1425 px | Sem overflow; composição editorial desktop revisada. |

A diferença de 15 px é a barra vertical do navegador da sessão. Não houve imagem quebrada ou fragmento inexistente nas cinco larguras. Conteúdo mobile tem ordem, recorte, escala e reserva próprios. Não houve teste em aparelhos físicos ou certificação multibrowser.

## 13. ACCESSIBILITY

Implementados: `lang="pt-BR"`, um H1, headings, landmarks, alt útil, skip link, foco visível, menu com estado anunciado, Escape, links com aviso de nova aba, status do clipboard e áreas de toque próximas ou superiores a 44 px. Navegação e informação permanecem utilizáveis sem JS.

Contrastes calculados nos cinco pares principais: **12,00:1; 5,16:1; 4,68:1; 7,89:1; 6,63:1**. Todos superam 4,5:1; resultados em [contrast-results](qa/contrast-results.json). Isso não constitui auditoria WCAG completa.

Sem JS, a navegação fica visível e 22 links continuam presentes. O fallback de movimento reduzido foi verificado aplicando as regras CSS por uma rota local de QA: animação `none`, transições `0s` e scroll `auto`. O navegador disponível não ofereceu emulação de preferência do sistema; a media query real está no CSS, mas não foi validada por alteração da configuração do OS. Skip link, Escape, foco e cópia foram testados; não houve auditoria com leitor de tela.

## 14. GITHUB PAGES

Funcionamento confirmado localmente em **`/fresta-site/`**: caminhos relativos e 10 requisições de página/assets com status 200, incluindo favicon, fontes e OG. O workflow `.github/workflows/pages.yml` valida o site e publica somente `dist/`, via checkout → configure → upload → deploy, com permissões de Pages e ambiente `github-pages`.

Destino preparado: `gabi0102souza-stack/fresta-site`. Os metadados sociais usam a URL futura correspondente. Se o nome da conta ou repositório mudar, ajustar essas URLs absolutas.

O usuário autorizou subir e publicar o projeto em 07/10/2026. O repositório de destino foi conferido pela conta autenticada `gabi0102souza-stack`; GitHub Pages usa o workflow. Screenshots de terceiros da pesquisa local foram excluídos do Git. A verificação externa da publicação é registrada no [QA_REPORT](qa/QA_REPORT.md).

**Deploy concluído com sucesso:** [execução 37613715652](https://github.com/gabi0102souza-stack/fresta-site/actions/runs/37613715652), commit de site `946f4fe`. Dez requisições por HTTPS sem login retornaram 200; favicon, OG e fontes válidos. A versão pública foi aberta e inspecionada visualmente no navegador, sem erros ou avisos de console registrados.

## 15. BEFORE OUTREACH

| Estado | Item |
| --- | --- |
| READY | Layout final, mobile, fontes/assets locais, HTML/CSS/JS, metadados, noindex, aviso de proposta, workflow, pesquisa e QA. |
| VERIFY | Identidade do Instagram, WhatsApp de reserva, operação atual, endereço vigente e aprovação de uso da marca. Não apresentar esses canais como verificados em outubro. |
| REPLACE | Wordmark provisório por asset aprovado para uma futura adoção oficial. Fotografias reais podem substituir a composição se a casa fornecer material autorizado. |
| OPTIONAL | Menu HTML atualizado, fotos da chef/cozinha, horários confirmados e dados estruturados após validação. Lighthouse em ambiente de publicação, leitor de tela e teste em aparelhos reais. |

Red team: o símbolo foi preservado; não existem pratos, fotos, horários, reviews ou serviços fabricados. O alerta de almoço tem referência datada. A vulnerabilidade restante é a identificação atual dos canais, apresentada aqui sem fingir resolução. A proposta permite avaliar a direção visual; uma adoção oficial exige validação da casa.

## 16. FINAL SCORE

Notas de autoavaliação **subjetivas da proposta**, não métricas de usuário ou certificações.

| Critério | Nota / 10 | Motivo |
| --- | --- | --- |
| Visual | 8,5 | Escala, contraste e ritmo consistentes, com alternativa abstrata completa. |
| Brand fidelity | 7,5 | Símbolo e vinho reais; faltam wordmark, fonte oficial, brand book e fotos autorizadas. |
| Originality | 8,5 | Abertura única, composição rua/cozinha/mesa e informações integradas ao desenho. |
| Copy | 8,5 | Direta, datada quando necessário, sem menu ou promessa inventados. |
| Authenticity | 8,0 | Evidência distinguida de invenção; ausência de fotografia documental limita reconhecimento do espaço. |
| Performance | 8,5 | Arquivos leves e nenhuma dependência de runtime; sem dados Lighthouse ou de campo. |
| Mobile | 8,5 | Cinco larguras e interações conferidas; falta validação em aparelhos físicos. |
| Commercial presentation | 8,5 | Prévia concreta e completa, com reserva e visita fáceis de localizar. |
| Readiness to send | 7,5 | Pronta para revisão como conceito; confirmar identidade e titularidade dos canais antes de envio comercial evita contato errado. |

As notas abaixo de 8 refletem dependências de evidência e assets da casa, não trabalho de implementação pendente. O site, a documentação e o QA solicitados estão entregues.
