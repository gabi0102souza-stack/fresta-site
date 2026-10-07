# FRESTA · prévia de site

Site estático em português brasileiro, feito para apresentar uma proposta ao Fresta, em Pinheiros. HTML, CSS e JavaScript nativos; fontes e imagens locais; nenhuma instalação ou etapa de build para hospedar.

## Abrir e revisar

```powershell
python scripts/preview.py --port 4173
```

Abra **http://127.0.0.1:4173/fresta-site/**. O servidor simula o subdiretório do GitHub Pages. Também é possível abrir `dist/index.html` diretamente; os links continuam funcionando, mas a cópia de endereço exige um contexto seguro, como localhost ou HTTPS.

## Verificações

```powershell
node --check dist/main.js
python scripts/validate.py
git diff --check
```

`qa/` contém screenshots e resultados da revisão no navegador. O validador local verifica estrutura, referências, arquivos, fragmentos e metadados; não substitui uma certificação de conformidade HTML ou WCAG.

As rotas `?qa=nojs` e `?qa=reduce` existem apenas no servidor de revisão. A primeira remove o script; a segunda aplica as regras de movimento reduzido para testar o fallback. Esses mecanismos não entram no site entregue.

## GitHub Pages

Destino preparado: `gabi0102souza-stack/fresta-site`.

1. Envie estes arquivos para a branch `main` desse repositório.
2. Em **Settings → Pages → Build and deployment**, selecione **GitHub Actions**.
3. O workflow `.github/workflows/pages.yml` verifica e publica apenas `dist/`.

URL pública configurada: https://gabi0102souza-stack.github.io/fresta-site/

Publicação no GitHub autorizada pelo usuário em 07/10/2026. A prévia pública não depende do servidor local. Todos os caminhos internos são relativos; o OG usa a URL pública acima. O workflow publica somente `dist/`; screenshots de sites de terceiros ficam na pesquisa local e foram excluídos do Git. Alterações apenas na documentação não disparam nova publicação.

## Conteúdo e identidade

- A informação sobre o almoço vem da matéria de 22/05/2026 da VEJA São Paulo. Não são publicados horários ou pratos como vigentes.
- O link de reserva foi seguido a partir do Linktree com o endereço correto. A titularidade e vigência do telefone continuam pendentes de validação da casa.
- O Instagram `@fresta.bar` apresenta informação pública divergente. Os links de acompanhamento levam ao Linktree, até resolver essa identidade.
- O símbolo é o arquivo real do avatar do Linktree, reduzido sem redesenho. O vinho foi amostrado desse arquivo. As famílias tipográficas de interface são complementares, não fontes oficiais.
- A composição de luz e a peça tipográfica são arte conceitual original. Não há fotos inventadas de pratos, fachada, salão ou pessoas.
- `noindex,nofollow`, aviso de proposta no rodapé e ausência de analytics fazem parte da entrega.

Leia `FINAL_REPORT.md`, `IMAGE_SOURCES.md` e `research/` antes de enviar a proposta. Fontes Instrument Sans e Instrument Serif: SIL Open Font License, incluída em `dist/fonts/`. A marca e o símbolo pertencem à casa; o material não implica aprovação.

## Alterar

Texto e links: `dist/index.html`. Tokens, layout e motion: `dist/styles.css`. Interações: `dist/main.js`.

O PNG social e o avatar já estão prontos. Para regenerá-los, o script opcional `scripts/make-assets.cjs` usa Sharp; ele não é necessário no GitHub Pages. A fonte vetorial do social está em `design/og-fresta.svg`.
