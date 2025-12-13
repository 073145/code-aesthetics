## 🎨 CODE-AESTHETICS: Transdução Algorítmica Híbrida

> "O código é o meio. O grafo é a estrutura. A tela é a retina."

### Visão Geral

CODE-AESTHETICS é o laboratório de **Transdução Algorítmica** do ecossistema 073145. Atua como o "Córtex Visual" e Auditivo, traduzindo estados matemáticos abstratos (vetores, entropia, fluxos de dados) em Artefatos Visuais e Sonoros perceptíveis.

Esta iteração do laboratório foca na **Hibridização de Ambientes**: uma ponte entre a portabilidade da Web (WASM/React) e a força bruta do Desktop (TouchDesigner/Isadora), explorando a **Semiótica Generativa** através de sistemas baseados em nós e processamento de sinal distribuído.

### Princípios Orientadores

* **Atomicidade Modular:** Decomposição da arte em nós funcionais reutilizáveis (Granular, FM, SDFs), permitindo a construção de grafos complexos a partir de primitivas simples.
* **Imediatez Reativa:** Uso de *Transient Updates* e arquiteturas orientadas a eventos para garantir latência zero entre o gesto (interação) e o resultado (som/imagem).
* **Simbiose Web-Desktop:** O navegador não é mais um visualizador passivo, mas um motor de DSP ativo (via WebAssembly) que dialoga com motores de renderização pesada via sockets.
* **Estética do Processo:** Visualização da lógica interna; o "patch" não é apenas o código fonte, é a própria obra de arte exposta.

---

## 🗺️ Estrutura do Repositório: Mapeamento Conceitual e Operacional

O repositório está organizado em três domínios funcionais principais, categorizados por ambiente de execução e nível de abstração.

### I. 0_ABSTRACTION_LOGIC (Lógica Pura e Agnóstica)

Contém a lógica agnóstica e as bases algorítmicas, independentes do motor de renderização.

| Conceito | Pasta Operacional | Descrição |
| :--- | :--- | :--- |
| **Generative-Grammars** | `generative_grammars` | L-Systems e Autômatos Celulares para geração de estrutura. |
| **DSP-Mathematics** | `dsp_math` | Fórmulas de processamento de sinal e provas de conceito matemáticas. |
| **Chaos-Theory** | `chaos_theory` | Equações de atratores estranhos e fractais agnósticos. |

### II. 1_LOCAL_DESKTOP_AV (TouchDesigner / Isadora / Sonic Pi)

Ambiente focado em alta performance, acesso a GPU dedicada e controle de palco.

| Categoria Conceitual | Pasta Operacional | Projetos Mapeados (Exemplos) |
| :--- | :--- | :--- |
| **Generative-Engine** | `_generative_engine` | **TouchDesigner**: SDFs via RayTK, Sistemas de Partículas GPU e Shaders GLSL. |
| **Performance-Host** | `_performance_host` | **Isadora**: Orquestração de cenas, Projection Mapping e Timeline linear. |
| **Auditory-Synthesis** | `sonic_pi` | Live Coding de áudio em Ruby (Algorave sets). |
| **Hybrid-Bridge** | `_bridge_server` | Relay Server (Node.js) para comunicação OSC/WebSocket bidirecional. |

### III. 2_WEB_BROWSER_PLATFORM (React / WASM / Elementary)

Ambiente focado em portabilidade, arquitetura de nós e DSP via WebAssembly.

| Categoria Conceitual | Pasta Operacional | Projetos Mapeados (Exemplos) |
| :--- | :--- | :--- |
| **Platform-Core** | `src/core` | Engine baseada em **React Flow** e gerenciamento de estado via **Zustand**. |
| **Visual-Synthesis** | `src/engine/visual` | **React Three Fiber** (Cena 3D), **Hydra** (Feedback Textures), **MediaPipe** (CV). |
| **Auditory-Synthesis** | `src/engine/audio` | **Elementary Audio** (Grafo DSP) e **Faust** (Compilação WASM nativa). |
| **Modules-Library** | `src/nodes-library` | Definições de nós: `synth_granular`, `loveletter_bomb`, `fx_greenscreen`. |

---

## 🛠️ Tech Stack

* **Linguagens:** TypeScript, GLSL, Ruby (Sonic Pi), Python (TD), Faust (.dsp).
* **Frameworks Web:** React Three Fiber, Elementary Audio, Hydra Synth, React Flow.
* **Frameworks Desktop:** TouchDesigner (RayTK), Isadora Core.
* **Protocolos:** WebAssembly (WASM), OSC (Open Sound Control), WebSocket, MIDI.

---

## ⚖️ Licença

BSD-2-Clause.

---

## ⚙️ Contribuição

Este repositório é um espaço aberto para pesquisa estética.

1.  Fork do repositório.
2.  Crie um *branch* para o seu experimento (`git checkout -b feature/nova-estetica`).
3.  Se criar um novo Nó Web, adicione a definição em `src/nodes-library`.
4.  Submeta um Pull Request.
