# Classificação de Vulnerabilidades e Hotspots

## **Categorias do OWASP Top 10 (2021)**

### **A02:2021 Falhas Criptográficas**
- **Descrição da Categoria:**  
  A categoria **A02:2021-Cryptographic Failures** no OWASP Top 10 de 2021 é uma evolução do **A3:2017-Sensitive Data Exposure**. Enquanto a versão de 2017 tratava o problema de maneira ampla, como um sintoma, a nova categoria foca na **causa raiz**: falhas relacionadas à criptografia. Essas falhas podem levar à exposição de dados sensíveis ou comprometimento do sistema.  
  - **Fonte:** Documentação do OWASP: *"A02:2021 shifts up one position to #2, previously known as A3:2017-Sensitive Data Exposure, which was broad symptom rather than a root cause."*

---

### **Classificação das Vulnerabilidades e Hotspots em A02:2021 Falhas Criptográficas**
- **1 Vulnerabilidade (SonarCloud):**
  - **Descrição:** "Make sure these Redis credentials get revoked, changed, and removed from the code."
  - **Observação:** Classificado anteriormente como **A3:2017-Sensitive Data Exposure**; agora se enquadra em **A02:2021 Falhas Criptográficas**.
  
- **2 Hotspots de Weak Cryptography:**
  - **Descrição:** Uso de algoritmos criptográficos fracos, que podem comprometer a proteção de dados sensíveis.

- **4 Hotspots de Encryption of Sensitive Data:**
  - **Descrição:** Criptografia inadequada ou insuficiente de dados sensíveis, como informações pessoais ou chaves de acesso.

---

### **Sem Categoria no OWASP Top 10 (2021)**
#### **Ataques DoS (Denial of Service):**
- **4 Hotspots de DoS:**  
  - **Descrição:** Hotspots relacionados à negação de serviço, como ausência de rate-limiting ou manipulação de recursos que sobrecarregam o sistema.  
  - **Observação:** Não há uma categoria direta no OWASP Top 10 (2021) para DoS, mas pode ser analisado no contexto de **A05: Security Misconfiguration** ou conforme o vetor de ataque.

#### **Hotspots Não Classificados:**
- **3 Hotspots Genéricos:**
  - **Descrição:** Três hotspots reportados que não possuem associação direta com categorias do OWASP.

---

## **Resumo de Classificação**
- **A02:2021 Falhas Criptográficas:** 7 itens  
  - **1 vulnerabilidade de credenciais Redis**  
  - **2 hotspots de weak cryptography**  
  - **4 hotspots de encryption of sensitive data**

- **Sem Categoria no OWASP:** 7 itens  
  - **4 hotspots de DoS**  
  - **3 hotspots não classificados**

---

## **Sobre SonarCloud e Classificação**
- **Filtragem por Categorias OWASP e Outros Frameworks:**  
  SonarCloud permite a separação por frameworks de segurança, como:
  - **OWASP Top 10**
  - **SANS Top 25**
  - **CWE (Common Weakness Enumeration)**

- **Atualização de Classificação (A3 → A02):**  
  O **A3:2017-Sensitive Data Exposure** foi **renomeado e consolidado** no **A02:2021 Falhas Criptográficas**. A nova abordagem foca na causa raiz, **falhas criptográficas**, em vez de tratar apenas os sintomas de exposição de dados sensíveis.
