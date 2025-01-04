pior de fazer a analise das vulnerabilidades pois nao tem interface grafica por padrao (poderiamos ter instalado mas a ideia era fazer a analise e comparacao de acordo com as ferramentas do jeito que instalamos, sem ajustes)


todas as vulnerabilidades de Hard-coded password e Password found in a hardcoded URL sao falso positivo, total de 99 nessa categoria
4 vulnerabilidades reportadas no arquivo apps/reaction/public/fonts/FontAwesome.otf, todas falso positivo
6 vulnerabilidades reais

portanto das 109 vulnerabilidadesm apenas 6 sao reais, todo resto (103) sao falso positivo
mas importante destacar, as vulnerabilidades de Hard-coded password e Password found in a hardcoded URL sao falso positivo devido a natureza da aplicacao, que eh uma aplicacao que devemos personalizar para fazer o seu uso, porem o sonarcloud e o semgrep nao reportaram esses pontos como vulnerabiliadde, apenas em 1 caso o sonar reportou uma credencial de exemplo do redis como vulnerabilidade