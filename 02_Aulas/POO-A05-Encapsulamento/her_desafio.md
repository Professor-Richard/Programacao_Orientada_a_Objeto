# Desafio

## Controle de Acesso em um Sistema Hospitalar

Você precisa desenvolver um sistema para um hospital que gerencie o acesso a prontuários médicos com base em:

- **Cargo do usuário** (médico, enfermeiro, administrador).
- **Horário de acesso** (enfermeiros só podem acessar prontuários entre 7h e 19h).
- **Nível de sensibilidade dos dados** (apenas médicos podem modificar diagnósticos).

## Requisitos Técnicos:

### Encapsulamento:

- Dados sensíveis do prontuário (como diagnóstico) devem ser privados, acessíveis apenas via métodos controlados.

### Herança:

- Crie uma hierarquia de classes para usuários (`Usuario`, `Medico`, `Enfermeiro`, `Administrador`).

### Polimorfismo:

- Implemente métodos `pode_visualizar_prontuario()` e `pode_alterar_diagnostico()` com comportamentos diferentes para cada cargo.

### Tratamento de Exceções:

- Crie exceções personalizadas como `AcessoNegadoError` e `HorarioInvalidoError`.

## Tarefa:

### Classe `Prontuario`:

- **Atributos encapsulados**: `_paciente` (str), `_diagnostico` (str), `_sensivel` (bool).
- **Métodos públicos**:
  - `visualizar(usuario)` → Valida acesso e registra auditoria.
  - `alterar_diagnostico(usuario, novo_diagnostico)` → Só permite se o usuário for médico.

### Classe `Usuario` (Abstrata):

- **Atributos**: `nome` (str), `cargo` (str).
- **Métodos abstratos**:
  - `verificar_horario_acesso(horario)` → Retorna `True`/`False` baseado no cargo.

### Classes Especializadas:

- **Medico**: Pode alterar diagnósticos a qualquer horário.
- **Enfermeiro**: Só visualiza prontuários entre 7h e 19h.
- **Administrador**: Acesso total, mas não pode modificar diagnósticos.

## Regras de Negócio:

- Se um enfermeiro tentar acessar fora do horário permitido, lance `HorarioInvalidoError`.
- Se um não médico tentar alterar um diagnóstico, lance `AcessoNegadoError`.
