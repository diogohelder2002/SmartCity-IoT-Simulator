# SmartCity IoT Simulator

## Project Overview
**SmartCity-IoT-Simulator** is a Python-based engineering tool designed to emulate a network of distributed traffic sensors in a Smart City environment.

The application generates stochastic traffic data (simulating real-world variability) across multiple geographic nodes and **persists** this information into a relational database (**SQLite**) in real-time. This project serves as a foundational architecture for Data Engineering pipelines and IoT data collection systems.

## Key Features
* **Multi-Node Simulation:** Simulates simultaneous data streams from specific urban locations (e.g., *Rua da Boavista*, *Aliados*).
* **Data Persistence:** Implements a robust **SQLite** backend to ensure data durability and structured storage (`dados_cidade.db`).
* **Stochastic Modeling:** Uses randomized algorithms combined with temporal logic to mimic vehicle flow variability.
* **Modular Architecture:** Codebase structured with **Separation of Concerns (SoC)**, isolating database logic from data generation.
* **Fault Tolerance:** Graceful handling of interruptions (`KeyboardInterrupt`) to ensure database integrity upon exit.

## Tech Stack
* **Language:** Python 3.x
* **Database:** SQLite3 (Embedded)
* **Libraries:** `datetime`, `random`, `time` (Standard Library)

## Project Structure
```text
SmartCity-IoT-Simulator/
├── main.py             # Entry point of the simulation
├── dados_cidade.db     # Database file (generated automatically)
└── README.md           # Project documentation

## How to Run

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/SEU_USERNAME_AQUI/SmartCity-IoT-Simulator.git](https://github.com/SEU_USERNAME_AQUI/SmartCity-IoT-Simulator.git)
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd SmartCity-IoT-Simulator
    ```

3.  **Run the simulation:**
    ```bash
    python main.py
    ```

4.  **Verify the Output:**
    The script will start logging data to the console and automatically generate/update the `dados_cidade.db` file in the root folder.

    *Example Console Output:*
    ```text
    [LOG] Guardado: Rua da Boavista - 12 carros
    [LOG] Guardado: Aliados - 4 carros
    ...
    ```

## 🔮 Future Roadmap
To further enhance this project, the following features are planned:
- [ ] **Data Visualization:** Integrate `Matplotlib` or `Pandas` to generate traffic heatmaps.
- [ ] **API Integration:** Expose data via a REST API using `Flask`.
- [ ] **Dockerization:** Containerize the application for cloud deployment.

---

**Author:** [O TEU NOME]
*Student of Technology and Information Systems Programming (CTeSP)*