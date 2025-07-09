# 🌿 Strange Garden Simulator

> A Python simulation that models the generational evolution of two fictional plant types — **Plant A** and **Plant B** — based on logical growth rules. Great for exploring cellular automata concepts in a fun and interactive way!

---

## 📸 Demo

<img src="https://user-images.githubusercontent.com/yourusername/plant-sim-demo.gif" alt="Simulation Demo" width="600">

---

## 📦 Features

- Simulates growth of two types of plants over multiple generations
- Plant A: Simple binary (alive/dormant) growth based on adjacent neighbors
- Plant B: Multi-state (big/small/dormant) growth based on a customizable neighborhood
- Interactive command-line interface
- Real-time visualization of garden state and statistics per generation

---
## 🧪 Usage

Run the simulation from the command line:

```bash
python TheStrangeGarden.py
```

### You'll be prompted to:

1. Choose plant type: `A` or `B`
2. Enter the starting garden (e.g., `.^*.^.*.`)
3. Input number of dormant plants to add on each side
4. Choose the number of generations to simulate
5. (For Plant B) Set neighborhood size

💡 You can re-run simulations as many times as you'd like without restarting the script.

---

## 🧬 Plant Rules

### 🌱 Plant A

* States: `*` = alive, `.` = dormant
* Neighborhood: immediate left/right
* Far-left and far-right are always dormant

### 🌿 Plant B

* States: `^` = big, `*` = small, `.` = dormant
* Neighborhood: customizable size
* Growth determined by whether number of alive plants (`^` or `*`) in neighborhood is even or odd

---