# Backup histórico do site do Dr. Felippe Tsujinaka

| Controle do documento | Informação |
|---|---|
| Responsável | Juan Lourenço, SP3 Company |
| Versão | 1.0 |
| Histórico | 25/11/2026 · Captura inicial do site público |
| Origem | [fgtortodontia.com.br](https://fgtortodontia.com.br/) |

## Capturas

Foram arquivadas 35 páginas públicas, incluindo a home, as páginas institucionais, o blog, os nove artigos, a listagem de casos, dez casos tratados e os arquivos de tags. Cada rota tem uma captura PNG de altura integral em desktop (1440 px) e em celular (390 px). O inventário cruza o sitemap do WordPress com a navegação interna do site. O navegador carregou as mídias que o tema adia até a rolagem e capturou os mapas incorporados na posição em que aparecem na página.

- [Home completa em desktop](capturas/desktop/inicio.png)
- [Home completa em celular](capturas/mobile/inicio.png)
- [Índice de capturas por página](CAPTURAS.md)

## Conteúdo do backup

| Pasta | Conteúdo |
|---|---|
| `fonte/` | HTML servido pelo site para cada rota |
| `paginas/` | Arquivos MHTML compactados com os recursos capturados pelo navegador |
| `wordpress-publico/` | Exportação da API pública com posts, páginas, termos e 78 registros de mídia visíveis |
| `uploads/` | 293 arquivos públicos, incluindo imagens, vídeos e variantes de tamanho |
| `recursos/` | Folhas de estilo, scripts, fontes e imagens coletados durante a navegação |
| `inventario/` | Sitemaps, mapa de páginas, verificação das capturas e relação de recursos |

## Abrir uma página arquivada

No diretório do repositório, rode `python3 ferramentas/extrair-pagina.py inicio --destino /tmp/fgt-backup` e abra o arquivo `/tmp/fgt-backup/inicio.mhtml` no Chrome ou Edge. Para outras páginas, consulte o identificador no [índice](CAPTURAS.md). As capturas PNG preservam a referência visual da data. As imagens que o navegador não conseguiu renderizar estão listadas em `inventario/capturas.json`, no campo `broken` de cada resolução.

Este acervo registra o conteúdo público disponível na data da captura. Uma restauração completa do WordPress exigiria o banco de dados do servidor, código-fonte instalado dos temas e plugins, além da configuração da hospedagem. Dados enviados por formulários, credenciais e dados administrativos estão fora deste backup. O acervo é mantido pela SP3 Company.
