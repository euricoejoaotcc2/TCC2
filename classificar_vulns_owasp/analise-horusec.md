# Classificação das Vulnerabilidades Horusec

## **A02:2021 Falhas Criptográficas** e **A07:2021 Falha de Identificação e Autenticação**
### Vulnerabilidades relacionadas a credenciais hardcoded:
- **Total**: 98 vulnerabilidades
- **Identificadores**: `vuln02 - vuln27`, `vuln29 - vuln99`

---

## **A02:2021 Falhas Criptográficas**
### Vulnerabilidades relacionadas a senhas em URLs hardcoded:
- **Total**: 3 vulnerabilidades
- **Identificadores**: `vuln01`, `vuln28`, `vuln65`

---

## **A07:2021 Falha de Identificação e Autenticação**
### Vulnerabilidades relacionadas a Client IDs, Secrets e Tokens expostos:
- **Total**: 4 vulnerabilidades
- **Identificadores**: `vuln100`, `vuln101`, `vuln102`, `vuln103`

---

## **A05:2021 Security Misconfiguration**
### Vulnerabilidades relacionadas à configuração incorreta de CORS:
- **Total**: 3 vulnerabilidades
- **Identificadores**: `vuln107`, `vuln108`, `vuln109`

### Vulnerabilidade relacionada a configuração incorreta no Dockerfile:
- **Total**: 1 vulnerabilidade
- **Identificador**: `vuln106`

---

## **A06:2021 Vulnerable and Outdated Components**
### Vulnerabilidades relacionadas a uso de geradores de números previsíveis:
- **Total**: 2 vulnerabilidades
- **Identificadores**: `vuln104`, `vuln105`

---

# Resumo Geral
- **A02:2021 Falhas Criptográficas**: 101 vulnerabilidades (credenciais hardcoded + senhas em URLs).
- **A07:2021 Falha de Identificação e Autenticação**: 102 vulnerabilidades (inclui sobreposição com A02).
- **A05:2021 Security Misconfiguration**: 4 vulnerabilidades.
- **A06:2021 Vulnerable and Outdated Components**: 2 vulnerabilidades.


ATENCAO:
Horusec faz mencao ao Top 10 da Owasp em alguns casos
por exemplo: "details": "(1/1) * Possible vulnerability detected: Having a permissive Cross-Origin Resource Sharing policy
Same origin policy in browsers prevents, by default and for security-reasons, a javascript frontend to perform a cross-origin HTTP request to a resource that has a different origin (domain, protocol, or port) from its own. The requested target can append additional HTTP headers in response, called CORS, that act like directives for the browser and change the access control policy / relax the same origin policy. The Access-Control-Allow-Origin header should be set only for a trusted origin and for specific resources. For more information checkout the OWASP A6:2017 (https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html) advisory."
