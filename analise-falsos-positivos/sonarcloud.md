a unica vulnerabilidade reportada como security é falso positivo
esta no arquivo packages/api-core/src/config.js que é um arquivo de configuracao
e sao credenciais de exemplo para rodar localmente

as 6 vulnerabiliddes reportadas como security hotspot da categoria Encryption of Sensitive Data sao falsos positivos, as urls usadas sao de exemplo, nao as que serao usadas em producao

a security hotspot Omitting --ignore-scripts can lead to the execution of shell scripts. Make sure it is safe here. vai ser consideradad como valida, pelo fato de ser uma recomendacao, e realemten a falta de --ignore-scripts pode ser um problema de seguraca em alguns casos, nesse caso eh no uso de um pacote globalmente utilizaod e fortemente auditado, portanto com riscos muito menores. mas mesmo assim consideraremos como valida

portanto a unica vulnerabilidade da categorai Security eh falso positivo
6 vulnerabilidades da categoria Encryption of Sensitive Data tambem sao falsos positivos

como mencionado anteriormente, o sonar reportou 3 vulnerabilidades na categoria de security, porem ao detalhar so aparece uma, consideraremos essa quantidade real para calculos,

total de 16 vulnerabilidades reportadas (fusao entre hotspots e security) com 7 falsos positivos (1 security + 6 de hotspots)


analise facil de ser feita, interface grafica muito boa, com muitos detalhes sobre as vulnerabilidades, referencia para estudo, explicacao do risco, indicacao de como corrigir, onde esta a vuln no codigo, possivel rastrear a vulnerabilidade durante o ciclo de vida dela no codigo
a melhor ferramenta testada para fazer a verificacao de falsos positivos, devido a quantidade de informacao disponibilizada para auxiliar
ADICIONAR FOTO QUE ESTA NA IMAGES