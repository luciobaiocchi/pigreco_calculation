# 🌧️ Raining Pi! (Monte Carlo Simulation) 🎯

An interactive **Streamlit** application designed to explain the Monte Carlo method and the importance of Big Data to elementary and middle school students. 
Created by the Machine Learning student team at **Politecnico di Torino (PoliTo)** for **Pi Day**.

## 🚀 What is this project?

The app estimates the value of Pi ($\pi$) by simulating the random dropping of "paint drops" (points) inside a square that contains an inscribed circle. 
It is a highly visual and fun way to introduce two key Data Science concepts to younger audiences:
1. **The Law of Large Numbers**: with few data points (few drops), the error margin is huge; as the amount of data increases, the approximation becomes incredibly precise.
2. **Statistical Sampling**: how randomness can be used to solve complex mathematical problems.

## 🛠️ Requirements and Installation

This project uses [uv](https://github.com/astral-sh/uv) for lightning-fast Python package and virtual environment management.

1. Clone the repository or download the project folder.
2. Make sure you have `uv` installed on your system.
3. Create the virtual environment and install the dependencies:

```bash
uv venv
uv pip install streamlit numpy matplotlib
